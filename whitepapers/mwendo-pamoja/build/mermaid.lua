local system = require "pandoc.system"

local cache_dir = ".mermaid_cache"
os.execute('if not exist "' .. cache_dir .. '" mkdir "' .. cache_dir .. '"')

local function file_exists(path)
  local handle = io.open(path, "rb")
  if handle then
    handle:close()
    return true
  end
  return false
end

local function render_mermaid(source, output_path)
  local temp_dir = os.getenv("TEMP") or os.getenv("TMP") or "."
  local hash = pandoc.sha1(source):sub(1, 12)
  local source_path = temp_dir .. "\\mwendo_mermaid_" .. hash .. ".mmd"
  local config_path = temp_dir .. "\\mwendo_puppeteer_config.json"

  local source_file = assert(io.open(source_path, "wb"))
  source_file:write(source)
  source_file:close()

  local config_file = assert(io.open(config_path, "wb"))
  config_file:write('{\n  "args": ["--no-sandbox", "--disable-setuid-sandbox"]\n}\n')
  config_file:close()

  local executable = "mmdc"
  if system.os == "mingw32" or system.os == "windows" then
    executable = "mmdc.cmd"
  end

  local command = string.format(
    '%s -p "%s" -i "%s" -o "%s" -b transparent -s 3',
    executable,
    config_path,
    source_path,
    output_path
  )

  local success = os.execute(command)
  os.remove(source_path)
  if not success or not file_exists(output_path) then
    error("Mermaid rendering failed for diagram " .. hash)
  end
end

function CodeBlock(block)
  if not block.classes:includes("mermaid") then
    return nil
  end

  local layout = block.attributes["layout"] or "standard"
  if layout ~= "standard" and layout ~= "fullpage" and layout ~= "landscape" then
    error("Unsupported Mermaid layout: " .. layout)
  end

  local hash = pandoc.sha1(block.text):sub(1, 12)
  local image_path = cache_dir .. "/mermaid_" .. hash .. ".png"
  if not file_exists(image_path) then
    render_mermaid(block.text, image_path)
  end

  if FORMAT:match("latex") then
    local width = "0.97\\linewidth"
    local height = "0.72\\textheight"
    if layout == "fullpage" then
      width = "0.98\\linewidth"
      height = "0.83\\textheight"
    elseif layout == "landscape" then
      width = "0.96\\linewidth"
      height = "0.76\\textheight"
    end

    local latex = table.concat({
      "% MWENDO_LAYOUT:" .. layout,
      "\\begin{center}",
      "\\vspace{0.35em}",
      "\\includegraphics[width=" .. width .. ",height=" .. height .. ",keepaspectratio]{" .. image_path .. "}",
      "\\vspace{0.35em}",
      "\\end{center}"
    }, "\n")
    return pandoc.RawBlock("latex", latex)
  end

  local image_width = "97%"
  if layout == "fullpage" or layout == "landscape" then
    image_width = "100%"
  end
  local image = pandoc.Image({}, image_path, "", pandoc.Attr("", {}, {width = image_width}))
  return pandoc.Para({image})
end

function BlockQuote(block)
  if not FORMAT:match("latex") then
    return nil
  end

  local first = block.content[1]
  if not first or (first.t ~= "Para" and first.t ~= "Plain") then
    return nil
  end

  local marker = pandoc.utils.stringify(first):match("^%[!([A-Z]+)%]")
  if marker ~= "NOTE" and marker ~= "IMPORTANT" then
    return nil
  end

  if first.content[1] and first.content[1].t == "Str"
      and first.content[1].text == "[!" .. marker .. "]" then
    table.remove(first.content, 1)
  else
    return nil
  end

  while first.content[1]
      and (first.content[1].t == "Space"
        or first.content[1].t == "SoftBreak"
        or first.content[1].t == "LineBreak") do
    table.remove(first.content, 1)
  end

  if #first.content == 0 then
    table.remove(block.content, 1)
  end

  local environment = marker == "NOTE" and "MwendoNote" or "MwendoImportant"
  local body = pandoc.write(pandoc.Pandoc(block.content), "latex")
  return pandoc.RawBlock(
    "latex",
    "\\begin{" .. environment .. "}\n" .. body .. "\\end{" .. environment .. "}"
  )
end

function Link(link)
  if not FORMAT:match("latex") then
    return nil
  end

  local visible = pandoc.utils.stringify(link.content)
  if visible:match("^https?://") then
    return pandoc.RawInline("latex", "\\url{" .. link.target .. "}")
  end

  return nil
end

local function latex_escape(text)
  local replacements = {
    ["\\"] = "\\textbackslash{}",
    ["{"] = "\\{",
    ["}"] = "\\}",
    ["%"] = "\\%",
    ["#"] = "\\#",
    ["&"] = "\\&",
    ["_"] = "\\_",
    ["$"] = "\\$",
    ["~"] = "\\textasciitilde{}",
    ["^"] = "\\textasciicircum{}"
  }
  return (text:gsub(".", function(character)
    return replacements[character] or character
  end))
end

function Pandoc(document)
  if not FORMAT:match("latex") then
    return document
  end

  local rebuilt = pandoc.List()
  local index = 1
  while index <= #document.blocks do
    local current = document.blocks[index]
    local following = document.blocks[index + 1]
    local caption = nil

    if current and current.t == "Para" then
      local text = pandoc.utils.stringify(current)
      if text:match("^Figure%s+%d+[a-zA-Z]?:") then
        caption = text
      end
    end

    if caption and following and following.t == "RawBlock"
        and following.format == "latex"
        and following.text:match("\\includegraphics") then
      local layout = following.text:match("MWENDO_LAYOUT:([%w_%-]+)") or "standard"
      local image_latex = following.text
        :gsub("%% MWENDO_LAYOUT:[^\n]+\n?", "")
        :gsub("\\begin{center}%s*", "")
        :gsub("%s*\\end{center}", "")
      local figure_latex

      if layout == "landscape" then
        figure_latex = table.concat({
          "\\clearpage",
          "\\begin{landscape}",
          "\\thispagestyle{fancy}",
          "\\begin{center}",
          "\\captionsetup{type=figure}",
          "\\caption*{\\textbf{" .. latex_escape(caption) .. "}}",
          image_latex,
          "\\end{center}",
          "\\end{landscape}",
          "\\clearpage"
        }, "\n")
      elseif layout == "fullpage" then
        figure_latex = table.concat({
          "\\clearpage",
          "\\thispagestyle{fancy}",
          "\\begin{center}",
          "\\captionsetup{type=figure}",
          "\\caption*{\\textbf{" .. latex_escape(caption) .. "}}",
          image_latex,
          "\\end{center}",
          "\\clearpage"
        }, "\n")
      else
        figure_latex = table.concat({
          "\\begin{figure}[!htbp]",
          "\\centering",
          "\\caption*{\\textbf{" .. latex_escape(caption) .. "}}",
          image_latex,
          "\\end{figure}"
        }, "\n")
      end

      rebuilt:insert(pandoc.RawBlock("latex", figure_latex))
      index = index + 2
    else
      rebuilt:insert(current)
      index = index + 1
    end
  end

  document.blocks = rebuilt
  return document
end
