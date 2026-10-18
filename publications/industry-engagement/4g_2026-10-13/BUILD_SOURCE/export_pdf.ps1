$ErrorActionPreference='Stop'
$deckBuild='C:\Users\Nevo\Downloads\insuretech & embedded finance\.build\four_g_2026-10-18\deck'
$powerpoint=$null
$presentation=$null
try {
 $powerpoint=New-Object -ComObject PowerPoint.Application
 $presentation=$powerpoint.Presentations.Open((Join-Path $deckBuild 'candidate.pptx'),-1,0,0)
 $presentation.SaveAs((Join-Path $deckBuild 'four_g_rebuilt.pdf'),32)
 $renderTarget=Join-Path $deckBuild 'powerpoint_renders'
 New-Item -ItemType Directory -Path $renderTarget -Force | Out-Null
 $presentation.Export($renderTarget,'PNG',1600,900)
 Write-Output ('PDF exported; slide count: '+$presentation.Slides.Count)
} finally {
 if($null -ne $presentation){$presentation.Close();[System.Runtime.InteropServices.Marshal]::ReleaseComObject($presentation)|Out-Null}
 if($null -ne $powerpoint){$powerpoint.Quit();[System.Runtime.InteropServices.Marshal]::ReleaseComObject($powerpoint)|Out-Null}
}
