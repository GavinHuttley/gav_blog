.. post:: Mar 1, 2022
   :tags: education, development, research, tips
   :category: computational science


***************************************************
Setting up your computer for computational research
***************************************************

How much impact can a computer setup possibly have? It turns out some choices can make your daily life as a computational scientist a lot happier. Conversely, other choices can make you curse yourself. If it sounds like I'm talking from experience, you're correct -- 20+ years worth.

Be systematic
=============

There are many reasons why adopting a systematic approach to organising your research activities on your computer is important. If you adopt a naming scheme and always organise your project files in the same way, you increase the *clarity and predictability* of your work. Putting all research work under a single directory facilitates *portability*, meaning it can easily be mirrored on different computers and code working on one system works on another. Predictability and portability improve the *reproducibility* of your work since you will not have to write custom code to handle execution on different systems.

Designing your work with reproducibility in mind benefits you and your colleagues and contributes to your long-term reputation. It also reduces the chance you'll go |:zany_face:|.

Take account of the resources you will use
==========================================

Computers
---------

Consider the following computational setup:

- *laptop, running macOS or Windows*: most development and prototyping will be done here
- *lab server, running Ubuntu 20*: data sampling against databases is done here
- *supercomputer, running "Rocky Linux release 8.5"*: large scale analysis is done here

In this scenario, data sampling code and data are synchronised between the laptop and the lab server. Large scale analyses are first prototyped on the laptop, and a selected data subset, code, and computational environment are synchronised with the supercomputer. Results are brought back to the laptop.

*How can you simplify keeping the different computational environments in sync?*

Adopt a directed relationship (click the tabs below to see illustrations for our example). For example, designate your laptop as the canonical machine for any source code. That means only editing code on that machine. Communicate those edits to the other computers in one direction only (use git for this). If you don't adhere to this, your code will quickly devolve to an inconsistent state, making you |:cry:|.

.. tabbed:: Code flow
    :name: code_flow

    .. digraph:: code_flow

        node [shape="rectangle"];

        GitHub [color="darkgray" style=filled];
        Laptop [color="skyblue" style=filled];
        "Lab Server" [fontcolor="white" color="blue" style=filled];
        Supercomputer [fontcolor="white" color="darkblue" style=filled];
        Laptop -> GitHub;
        Laptop -> "Lab Server";
        Laptop -> Supercomputer;
        GitHub -> "Lab Server" [style=dotted];
        GitHub -> "Supercomputer" [style=dotted];

    Arrows direction indicates direction of flow. If you authorise all computers (via ssh keys) with GitHub, you enable moving all code between computers via git [#]_.

.. tabbed:: Data flow
    :name: data_flow

    .. digraph:: data_flow

        node [shape="rectangle"];

        External [color="darkgray" style=filled];
        Laptop [color="skyblue" style=filled];
        "Lab Server" [fontcolor="white" color="blue" style=filled];
        Supercomputer [fontcolor="white" color="darkblue" style=filled];
        External -> Laptop;
        "Lab Server" -> Laptop;
        Laptop -> Supercomputer;

    Arrows direction indicates direction of flow. The Lab Server is where data sampling is taking place (remember, we're assuming it hosts databases), and the laptop specifies what is moved to the Supercomputer.

.. tabbed:: Results flow
    :name: results_flow

    .. digraph:: results_flow

        node [shape="rectangle"];

        Laptop [color="skyblue" style=filled];
        Supercomputer [fontcolor="white" color="darkblue" style=filled];
        Laptop -> Laptop
        Supercomputer -> Laptop;

    Arrows direction indicates direction of flow. Results are either generated on the Laptop or the Supercomputer.

.. note::

    Homogeneity in operating systems is key to the portability of your work. While macOS and Linux have substantial differences, they are both POSIX operating systems. So the effort to develop code on a macOS laptop and get it running on a Linux machine is, in my experience, quite small.
    
    Windows, on the other hand, is more of a challenge. Because most machines used in the computational sciences are running a POSIX OS (i.e. Linux), I strongly advise you to do your development work using WSL_ on a Windows laptop.

Major software tools
--------------------

Package manager
^^^^^^^^^^^^^^^

If your laptop is running macOS, you already have a unix based system |:sunglasses:|. However, you will almost certainly need to install a unix-style package manager. I recommend Homebrew_. This can be used to install non-python tools, such as the ``openmpi`` library [#]_.

If your laptop is running Windows, install the latest WSL_ (Windows subsystem for Linux, which installs Ubuntu). You will then get the ``apt`` package manager.

Terminal app
^^^^^^^^^^^^

The Terminal application is your gateway to the command line on all the computers you will access. The terminal is just an interface to your shell environment. At present, ``zsh`` is the default shell on macOS, while ``bash`` is the default on Linux distributions. Configuration files are located in your home directory and named ``.zshrc`` and ``.bashrc`` respectively. You will be editing them.

As this same application is employed to interact with all the computers you will use, it's worth looking into making your shell environments on different computers as similar as possible, albeit you need to make sure it's clear which computer you're on. The latter can be achieved by customising the terminal prompt.

If you use ``zsh``, consider installing `ohmyzsh <https://ohmyz.sh/>`_. Some other command line tools I find super useful are:

- `autojump <https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/autojump>`_, jump to commonly used directories
- `starship <https://github.com/starship/starship>`_, customised prompts
- ``mcfly``, control+r magic for getting back to past commands
- ``fd``, super fast find
- ``ripgrep``, a better, easier to use, grep

See the `modern unix tools <https://github.com/ibraheemdev/modern-unix>`_ page.

Text editor
^^^^^^^^^^^

No matter what OS your laptop is running, I encourage you to install `VS Code`_ . The reasons are simple, it provides an excellent experience for editing files on remote machines along with a fully-featured terminal experience. Be sure and research useful extensions. On my system, I have:

- `autodocstring <https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring>`_
- `Python extensions <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_
- `Jupyter <https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter>`_
- `Python Test Explorer UI <https://marketplace.visualstudio.com/items?itemName=hbenl.vscode-test-explorer>`_
- `Remote SSH <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh>`_ [#]_

Install the ``code`` command-line tool for invoking VS Code from the terminal. Open the command palette (macOS command+shift+p) and type "install code" at the prompt. This will show a single listing with "Shell Command: Install 'code' in PATH". Click on that and follow any prompts.

Configure ssh
^^^^^^^^^^^^^

``ssh`` stands for secure shell which provides a mechanism for accessing remote computers either for interactive terminal sessions or for copying files to / from. On your laptop, you should create a private / public key pair.

.. code::

    $ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

Follow the prompts, and set a good password. The public copy of this key (which you can find under ``~/.ssh/id_rsa.pub``) will be copied to your other computer accounts, enabling simplified steps to authorise your access.

But wait, you're not done with ssh yet! Using your newly configured VS Code, enter the following command in the terminal

.. code::

    $ code ~/.ssh/config

This will open an empty file. You can include a shortcut in this file for every remote machine you need to access. Here's an example

::

    Host qik
    UseKeychain yes
    HostName super.annoying.domain.com
    User ini777

Save the file. Instead of logging into ``super.annoying.domain.com`` as

.. code::

    $ ssh ini777@super.annoying.domain.com

You can do

.. code::

    $ ssh qik

|:tada:|

Login into each computer and repeat the ssh keygen step there (this will facilitate code sharing, see below). Copy your **public** ssh key into your clip board on each computer.

.. code::

    $ cat ~/.ssh/id_rsa.pub | pbcopy

Add the result to your ``authorized_keys`` on each of your remote computers by logging into each remote machine and doing the following

.. code::

    $ ssh qik
    $ nano ~/.ssh/authorized_keys # or your favourite editor

paste the key on a new line [#]_ and exit ``nano`` [#]_.

Using ``git`` and GitHub for version control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The version control tool ``git`` should already be installed on your computer. To use ``git`` you need to configure it.

.. code::

    $ git config --global user.name "Firstname Lastname"
    $ git config --global user.email "username@myEmail.com"

These will be used by ``git`` to sign any commits you make. I recommend you do this on all the computers you will be using.

If you don't already have an account on GitHub, create one. At this point, you should copy the public ssh keys you created on each machine and add them to your GitHub account. Follow the `instructions at GitHub <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account>`_.

.. tip:: When you add a key, give it the computer's name. Doing this means it's easy to delete a key if you lose access to that computer (e.g. you buy a new laptop).

Reproducible computational environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There is no single answer to this challenge that applies to all cases. Some will argue that conda_ provides the most general solution to this problem. My own experience is that if your computations include a supercomputer, you may find conda troublesome. Supercomputers are often administered via a granting system whereby some quantity of resources is allocated. Those resources include CPU hours and storage. If you exceed your allocation, you can no longer use the computer.

``conda`` does not work well in the supercomputer context. Shared facilities may penalise user accounts with many files [#]_ due to the significant overhead they can impose on performance of the file sustem. I have witnessed this effect with naive ``conda`` installs. In addition, supercomputer facilities often provide custom builds of core tools. For instance, higher performance builds of Python than what you will obtain from ``conda-forge``.

If ``conda`` seems to be the only way to solve your case, make sure you only install the minimal dependency set. You can specify that set using a `conda environment yaml file <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually>`_, remembering to "pin" [#]_ your versions.

If you are lucky enough to have a Python-only project [#]_, then use the `built-in capability <https://realpython.com/python-virtual-environments-a-primer/>`_ to create virtual environments. These can be made portable by creating a ``requirements.txt`` file, which you share between your different accounts. If this is the approach you take, be sure and `pin your dependency versions <https://pip.pypa.io/en/latest/reference/requirements-file-format/>`_.

.. tip:: You can reconstruct your computing environment by just the yaml or requirements file. As plaint text file formats, they should be version controlled too.

Structuring your projects
=========================

.. tip:: Put them all into a single directory, call it ``repos`` [#]_.

Having a single directory makes moving your research projects between computers easier. I advise you also to include repositories for any dependency that is being actively developed in this directory. This way, you preserve the entire compute state.

.. tip:: Since you will be versioning everything, the first action you take to start a new project is create a repository on GitHub_. Then clone it into your ``~/repos`` directory.

Typically, I have two repositories if I'm engaged in research to develop a software tool. The first is for the tool to be distributed to the target audience. The second is for the analyses to be undertaken to establish the tool is worth using. Below I give sample structures for a "software project" and a "research project".

Directory structure for a software methods project
--------------------------------------------------

::

    .
    └── software_project/
        ├── project config files
        ├── docs/
        │   ├── data/
        │   │   └── small sample data files
        │   └── doc files
        ├── src/
        │   └── lib_name/
        │   └── source code files
        └── tests/
            ├── data/
            │   └── small sample data files
            └── test files

Software development projects have input data necessary for your test suite and documentation, which should be tracked in version control. They should be minimal, sufficient for their testing and / or demonstration purposes.

Directory structure for a research project
------------------------------------------

::

    .
    └── research_project/
        ├── README describing usage
        ├── data/
        │   ├── processed/
        │   └── raw/
        ├── results/
        │   ├── figures/
        │   └── tables/
        ├── src
        │   ├── analysis scripts
        │   ├── data sampling scripts
        │   └── notebook files
        └── tests/
            ├── data/
            └── test files

Research projects have input data that may be local to your institute or external, e.g. resources such as Zenodo_, GenBank_, or Ensembl_. Wherever your data comes from, store it under the ``data/`` directory with a name that reflects its origin.

For a research project, these data files can be massive! As such, you are advised not to add data files to your research project's ``git`` repository. An alternate way to version those files is by uploading them to Zenodo_ (for instance) and adding a script that does the download. Users seeking to replicate your work then run that script to reconstitute the state of your project directory.

.. note:: Putting Jupyter notebook files in version control can be problematic. There are multiple reasons for this, e.g. embedded images can make these files very large. This has led to tools like `nbstripout <https://github.com/kynan/nbstripout>`_. My advice is only to include notebooks if they're small.

.. rubric:: Footnotes

.. [#] Yo do not actually have to use GitHub_ for this. But if GitHub_ is how you will share your work with other |:scientist:|, you may as well.
.. [#] This is necessary for prototyping your code runs in parallel using MPI library (Message Passing Interface). MPI is the most likely protocol for parallel computation supported on the supercomputer.
.. [#] On windows, install the `Remote WSL <https://code.visualstudio.com/docs/remote/wsl-tutorial>`_ extension.
.. [#] The public key must be on a single line.
.. [#] It is up to you be sure you know how to use the ``nano`` editor. When in doubt, google.
.. [#] measured via `inodes <https://en.wikipedia.org/wiki/Inode>`_
.. [#] Pinning here means to state a specific version number of the tool.
.. [#] "Lucky" in the sense that there is less complexity in the project, simplifying your development process and reducing the storage footprint of your project.
.. [#] ``repos`` because it is short for repositories, and **every** project will be version controlled ... right?

.. _Ensembl: https://ensembl.org
.. _GenBank: https://www.ncbi.nlm.nih.gov/genbank/
.. _Zenodo: https://zenodo.org
.. _conda: https://docs.conda.io/en/latest/miniconda.html
.. _VS Code: https://code.visualstudio.com
.. _GitHub: https://github.com
.. _Homebrew: https://brew.sh/
.. _WSL: https://docs.microsoft.com/en-us/windows/wsl/install
