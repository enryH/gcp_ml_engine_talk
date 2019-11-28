def chdir_(subfolders = ['notebook', 'src', 'talks']):
    """
    Change directory to parent if program runs in subfolder.
    
    subfolder: list
        List of subfolders in project.
    """
    import os
    WORKINGDIR = os.path.normpath(os.getcwd())
    print("Current Working direcotory:\t{}".format(WORKINGDIR))
    folders = WORKINGDIR.split(os.sep)
    if folders.pop() in subfolders:
      WORKINGDIR = os.sep.join(folders)
      print("Changed to New working directory:\t{dir}".format(dir=WORKINGDIR))
      os.chdir(WORKINGDIR)
    return WORKINGDIR