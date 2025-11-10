$Env:CONDA_EXE = "C:/Users/vjvan/OneDrive/Desktop/GitHub/Text-Extraction-Model/miniconda\Scripts\conda.exe"
$Env:_CONDA_EXE = "C:/Users/vjvan/OneDrive/Desktop/GitHub/Text-Extraction-Model/miniconda\Scripts\conda.exe"
$Env:_CE_M = $null
$Env:_CE_CONDA = $null
$Env:CONDA_PYTHON_EXE = "C:/Users/vjvan/OneDrive/Desktop/GitHub/Text-Extraction-Model/miniconda\python.exe"
$Env:_CONDA_ROOT = "C:/Users/vjvan/OneDrive/Desktop/GitHub/Text-Extraction-Model/miniconda"
$CondaModuleArgs = @{ChangePs1 = $True}

Import-Module "$Env:_CONDA_ROOT\shell\condabin\Conda.psm1" -ArgumentList $CondaModuleArgs

Remove-Variable CondaModuleArgs