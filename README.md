# <p style="text-align: center;">BSA Python Workshop</p>
 
<p align="center"> <img src="PythonWorkshop.png" class="center"></p>

# Prerequisites

### Install Anaconda (or Miniconda if you're adventurous)

#### Windows

If you don't have anaconda installed, follow [this installation](https://www.datacamp.com/community/tutorials/installing-anaconda-windows) guide.
Remember to check "Add Anaconda to `PATH`"

If you already installed anaconda but forgot to check "Add Anaconda to `PATH`" box, then follow "Add Anaconda to Path (Optional)" section from the [above installation link](https://www.datacamp.com/community/tutorials/installing-anaconda-windows) link.

Now open a Powershell(prefer not to use cmd) prompt, and execute the following commands:

```powershell

conda init powershell
conda config --set auto_activate_base False

```

#### MacOSX

For MacOSX, follow [this link](https://docs.anaconda.com/anaconda/install/mac-os/) (easy installer) to install Anaconda.

If you prefer to use `brew` package manager use [this link](https://medium.com/ayuth/install-anaconda-on-macos-with-homebrew-c94437d63a37) to install Anaconda.

Open a new Terminal (Cmd+Space --> Type Terminal) and execute:

```bash

[[ -z $BASH_VERSION ]] && conda init zsh || conda init bash
conda config --set auto_activate_base False

```

#### Linux

*if you're crazy enough to use Linux you can surely install stupid Anaconda!*

###  Install `Visual Studio Code`

Simply download the installer (or portable zip) from this [link](https://code.visualstudio.com/download).

Install Visual Studio Code from the installer or extract from the Zip if you've chosen the portable version.

Open Visual Studio Code and install these extensions:
  - [ ] Microsoft Python
  - [ ] Visual Studio Intellicode
  - [ ] MagicPython
  - [ ] [Optional] Pylance
  - [ ] [Optional] Rainbow Indent
  - [ ] [Optional] Rainbow Brackets