from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.backends.headless.HeadlessFiles as _HeadlessFiles
_HeadlessFiles = _HeadlessFiles
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import java.lang.String as _string
import java.lang.Integer as _int
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HeadlessFiles():
    """com.badlogic.gdx.backends.headless.HeadlessFiles"""
 
    @staticmethod
    def _wrap(java_value: _HeadlessFiles) -> 'HeadlessFiles':
        return HeadlessFiles(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HeadlessFiles):
        """
        Dynamic initializer for HeadlessFiles.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HeadlessFiles__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HeadlessFiles__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.HeadlessFiles()"""
        val = _HeadlessFiles()
        self.__wrapper = val

    @overload
    def internal(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.backends.headless.HeadlessFiles.internal(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_HeadlessFiles, self).internal(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getFileHandle(self, arg0: str, arg1: 'FileType') -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.backends.headless.HeadlessFiles.getFileHandle(java.lang.String,com.badlogic.gdx.Files$FileType)"""
        return 'files.FileHandle'._wrap(super(_HeadlessFiles, self).getFileHandle(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getExternalStoragePath(self) -> str:
        """public java.lang.String com.badlogic.gdx.backends.headless.HeadlessFiles.getExternalStoragePath()"""
        return str._wrap(super(HeadlessFiles, self).getExternalStoragePath())

    @overload
    def local(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.backends.headless.HeadlessFiles.local(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_HeadlessFiles, self).local(arg0))

    @override
    @overload
    def isExternalStorageAvailable(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.HeadlessFiles.isExternalStorageAvailable()"""
        return bool._wrap(super(HeadlessFiles, self).isExternalStorageAvailable())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.HeadlessFiles()"""
        val = _HeadlessFiles()
        self.__wrapper = val

    @overload
    def classpath(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.backends.headless.HeadlessFiles.classpath(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_HeadlessFiles, self).classpath(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalStoragePath(self) -> str:
        """public java.lang.String com.badlogic.gdx.backends.headless.HeadlessFiles.getLocalStoragePath()"""
        return str._wrap(super(HeadlessFiles, self).getLocalStoragePath())

    @overload
    def external(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.backends.headless.HeadlessFiles.external(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_HeadlessFiles, self).external(arg0))

    @override
    @overload
    def isLocalStorageAvailable(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.HeadlessFiles.isLocalStorageAvailable()"""
        return bool._wrap(super(HeadlessFiles, self).isLocalStorageAvailable())

    @overload
    def absolute(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.backends.headless.HeadlessFiles.absolute(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_HeadlessFiles, self).absolute(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.backends.headless.HeadlessFiles
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.backends.headless.HeadlessFiles as _HeadlessFiles
_HeadlessFiles = _HeadlessFiles
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import java.lang.String as _string
import java.lang.Integer as _int
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HeadlessFiles():
    """com.badlogic.gdx.backends.headless.HeadlessFiles"""
 
    @staticmethod
    def _wrap(java_value: _HeadlessFiles) -> 'HeadlessFiles':
        return HeadlessFiles(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HeadlessFiles):
        """
        Dynamic initializer for HeadlessFiles.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HeadlessFiles__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HeadlessFiles__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.HeadlessFiles()"""
        val = _HeadlessFiles()
        self.__wrapper = val

    @overload
    def internal(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.backends.headless.HeadlessFiles.internal(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_HeadlessFiles, self).internal(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getFileHandle(self, arg0: str, arg1: 'FileType') -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.backends.headless.HeadlessFiles.getFileHandle(java.lang.String,com.badlogic.gdx.Files$FileType)"""
        return 'files.FileHandle'._wrap(super(_HeadlessFiles, self).getFileHandle(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getExternalStoragePath(self) -> str:
        """public java.lang.String com.badlogic.gdx.backends.headless.HeadlessFiles.getExternalStoragePath()"""
        return str._wrap(super(HeadlessFiles, self).getExternalStoragePath())

    @overload
    def local(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.backends.headless.HeadlessFiles.local(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_HeadlessFiles, self).local(arg0))

    @override
    @overload
    def isExternalStorageAvailable(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.HeadlessFiles.isExternalStorageAvailable()"""
        return bool._wrap(super(HeadlessFiles, self).isExternalStorageAvailable())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.HeadlessFiles()"""
        val = _HeadlessFiles()
        self.__wrapper = val

    @overload
    def classpath(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.backends.headless.HeadlessFiles.classpath(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_HeadlessFiles, self).classpath(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalStoragePath(self) -> str:
        """public java.lang.String com.badlogic.gdx.backends.headless.HeadlessFiles.getLocalStoragePath()"""
        return str._wrap(super(HeadlessFiles, self).getLocalStoragePath())

    @overload
    def external(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.backends.headless.HeadlessFiles.external(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_HeadlessFiles, self).external(arg0))

    @override
    @overload
    def isLocalStorageAvailable(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.HeadlessFiles.isLocalStorageAvailable()"""
        return bool._wrap(super(HeadlessFiles, self).isLocalStorageAvailable())

    @overload
    def absolute(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.backends.headless.HeadlessFiles.absolute(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_HeadlessFiles, self).absolute(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.backends.headless.HeadlessFiles 
 
 
# CLASS: com.badlogic.gdx.backends.headless.HeadlessApplication
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.Preferences as _Preferences
_Preferences = _Preferences
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.Application as _Application_ApplicationType
_ApplicationType = _Application_ApplicationType.ApplicationType
from builtins import type
import com.badlogic.gdx.Graphics as _Graphics
_Graphics = _Graphics
import java.lang.String as _string
from builtins import bool
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

import com.badlogic.gdx.Input as _Input
_Input = _Input
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _object
import com.badlogic.gdx.utils.Clipboard as _Clipboard
_Clipboard = _Clipboard
import java.lang.Runnable as Runnable
import com.badlogic.gdx.ApplicationListener as _ApplicationListener
_ApplicationListener = _ApplicationListener
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.Net as _Net
_Net = _Net
import java.lang.Throwable as Throwable
import com.badlogic.gdx.Audio as _Audio
_Audio = _Audio
import com.badlogic.gdx.Files as _Files
_Files = _Files
import com.badlogic.gdx.ApplicationLogger as _ApplicationLogger
_ApplicationLogger = _ApplicationLogger
import com.badlogic.gdx.backends.headless.HeadlessApplication as _HeadlessApplication
_HeadlessApplication = _HeadlessApplication
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HeadlessApplication():
    """com.badlogic.gdx.backends.headless.HeadlessApplication"""
 
    @staticmethod
    def _wrap(java_value: _HeadlessApplication) -> 'HeadlessApplication':
        return HeadlessApplication(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HeadlessApplication):
        """
        Dynamic initializer for HeadlessApplication.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HeadlessApplication__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HeadlessApplication__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getNet(self) -> 'pygdx.Net':
        """public com.badlogic.gdx.Net com.badlogic.gdx.backends.headless.HeadlessApplication.getNet()"""
        return 'pygdx.Net'._wrap(super(HeadlessApplication, self).getNet())

    @override
    @overload
    def debug(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplication.debug(java.lang.String,java.lang.String)"""
        super(_HeadlessApplication, self).debug(arg0, arg1)

    @overload
    def __init__(self, arg0: 'ApplicationListener'):
        """public com.badlogic.gdx.backends.headless.HeadlessApplication(com.badlogic.gdx.ApplicationListener)"""
        val = _HeadlessApplication(arg0)
        self.__wrapper = val

    @override
    @overload
    def getAudio(self) -> 'pygdx.Audio':
        """public com.badlogic.gdx.Audio com.badlogic.gdx.backends.headless.HeadlessApplication.getAudio()"""
        return 'pygdx.Audio'._wrap(super(HeadlessApplication, self).getAudio())

    @override
    @overload
    def getNativeHeap(self) -> int:
        """public long com.badlogic.gdx.backends.headless.HeadlessApplication.getNativeHeap()"""
        return int._wrap(super(HeadlessApplication, self).getNativeHeap())

    @overload
    def getPreferences(self, arg0: str) -> 'pygdx.Preferences':
        """public com.badlogic.gdx.Preferences com.badlogic.gdx.backends.headless.HeadlessApplication.getPreferences(java.lang.String)"""
        return 'pygdx.Preferences'._wrap(super(_HeadlessApplication, self).getPreferences(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def debug(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplication.debug(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(_HeadlessApplication, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def postRunnable(self, arg0: 'Runnable'):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplication.postRunnable(java.lang.Runnable)"""
        super(_HeadlessApplication, self).postRunnable(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getGraphics(self) -> 'pygdx.Graphics':
        """public com.badlogic.gdx.Graphics com.badlogic.gdx.backends.headless.HeadlessApplication.getGraphics()"""
        return 'pygdx.Graphics'._wrap(super(HeadlessApplication, self).getGraphics())

    @override
    @overload
    def getVersion(self) -> int:
        """public int com.badlogic.gdx.backends.headless.HeadlessApplication.getVersion()"""
        return int._wrap(super(HeadlessApplication, self).getVersion())

    @override
    @overload
    def error(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplication.error(java.lang.String,java.lang.String)"""
        super(_HeadlessApplication, self).error(arg0, arg1)

    @override
    @overload
    def removeLifecycleListener(self, arg0: 'LifecycleListener'):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplication.removeLifecycleListener(com.badlogic.gdx.LifecycleListener)"""
        super(_HeadlessApplication, self).removeLifecycleListener(arg0)

    @override
    @overload
    def setLogLevel(self, arg0: int):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplication.setLogLevel(int)"""
        super(_HeadlessApplication, self).setLogLevel(_int.valueOf(arg0))

    @override
    @overload
    def error(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplication.error(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(_HeadlessApplication, self).error(arg0, arg1, arg2)

    @override
    @overload
    def getClipboard(self) -> 'utils.Clipboard':
        """public com.badlogic.gdx.utils.Clipboard com.badlogic.gdx.backends.headless.HeadlessApplication.getClipboard()"""
        return 'utils.Clipboard'._wrap(super(HeadlessApplication, self).getClipboard())

    @override
    @overload
    def getJavaHeap(self) -> int:
        """public long com.badlogic.gdx.backends.headless.HeadlessApplication.getJavaHeap()"""
        return int._wrap(super(HeadlessApplication, self).getJavaHeap())

    @override
    @overload
    def getFiles(self) -> 'pygdx.Files':
        """public com.badlogic.gdx.Files com.badlogic.gdx.backends.headless.HeadlessApplication.getFiles()"""
        return 'pygdx.Files'._wrap(super(HeadlessApplication, self).getFiles())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def setApplicationLogger(self, arg0: 'ApplicationLogger'):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplication.setApplicationLogger(com.badlogic.gdx.ApplicationLogger)"""
        super(_HeadlessApplication, self).setApplicationLogger(arg0)

    @override
    @overload
    def getLogLevel(self) -> int:
        """public int com.badlogic.gdx.backends.headless.HeadlessApplication.getLogLevel()"""
        return int._wrap(super(HeadlessApplication, self).getLogLevel())

    @override
    @overload
    def log(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplication.log(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(_HeadlessApplication, self).log(arg0, arg1, arg2)

    @override
    @overload
    def getInput(self) -> 'pygdx.Input':
        """public com.badlogic.gdx.Input com.badlogic.gdx.backends.headless.HeadlessApplication.getInput()"""
        return 'pygdx.Input'._wrap(super(HeadlessApplication, self).getInput())

    @override
    @overload
    def exit(self):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplication.exit()"""
        super(HeadlessApplication, self).exit()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getType(self) -> 'pygdx.Application$ApplicationType':
        """public com.badlogic.gdx.Application$ApplicationType com.badlogic.gdx.backends.headless.HeadlessApplication.getType()"""
        return 'pygdx.Application$ApplicationType'._wrap(super(HeadlessApplication, self).getType())

    @override
    @overload
    def getApplicationLogger(self) -> 'pygdx.ApplicationLogger':
        """public com.badlogic.gdx.ApplicationLogger com.badlogic.gdx.backends.headless.HeadlessApplication.getApplicationLogger()"""
        return 'pygdx.ApplicationLogger'._wrap(super(HeadlessApplication, self).getApplicationLogger())

    @overload
    def executeRunnables(self) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.HeadlessApplication.executeRunnables()"""
        return bool._wrap(super(HeadlessApplication, self).executeRunnables())

    @overload
    def __init__(self, arg0: 'ApplicationListener', arg1: 'HeadlessApplicationConfiguration'):
        """public com.badlogic.gdx.backends.headless.HeadlessApplication(com.badlogic.gdx.ApplicationListener,com.badlogic.gdx.backends.headless.HeadlessApplicationConfiguration)"""
        val = _HeadlessApplication(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def log(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplication.log(java.lang.String,java.lang.String)"""
        super(_HeadlessApplication, self).log(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def addLifecycleListener(self, arg0: 'LifecycleListener'):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplication.addLifecycleListener(com.badlogic.gdx.LifecycleListener)"""
        super(_HeadlessApplication, self).addLifecycleListener(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getApplicationListener(self) -> 'pygdx.ApplicationListener':
        """public com.badlogic.gdx.ApplicationListener com.badlogic.gdx.backends.headless.HeadlessApplication.getApplicationListener()"""
        return 'pygdx.ApplicationListener'._wrap(super(HeadlessApplication, self).getApplicationListener())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.backends.headless.HeadlessNet
from pyquantum_helper import import_once as _import_once
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.net.Socket as _Socket
_Socket = _Socket
try:
    from pygdx import net
except ImportError:
    net = _import_once("pygdx.net")

import java.lang.String as _String
_String = _String
import com.badlogic.gdx.net.ServerSocket as _ServerSocket
_ServerSocket = _ServerSocket
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.backends.headless.HeadlessNet as _HeadlessNet
_HeadlessNet = _HeadlessNet
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HeadlessNet():
    """com.badlogic.gdx.backends.headless.HeadlessNet"""
 
    @staticmethod
    def _wrap(java_value: _HeadlessNet) -> 'HeadlessNet':
        return HeadlessNet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HeadlessNet):
        """
        Dynamic initializer for HeadlessNet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HeadlessNet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HeadlessNet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def newClientSocket(self, arg0: 'Protocol', arg1: str, arg2: int, arg3: 'SocketHints') -> 'net.Socket':
        """public com.badlogic.gdx.net.Socket com.badlogic.gdx.backends.headless.HeadlessNet.newClientSocket(com.badlogic.gdx.Net$Protocol,java.lang.String,int,com.badlogic.gdx.net.SocketHints)"""
        return 'net.Socket'._wrap(super(_HeadlessNet, self).newClientSocket(arg0, arg1, _int.valueOf(arg2), arg3))

    @overload
    def __init__(self, arg0: 'HeadlessApplicationConfiguration'):
        """public com.badlogic.gdx.backends.headless.HeadlessNet(com.badlogic.gdx.backends.headless.HeadlessApplicationConfiguration)"""
        val = _HeadlessNet(arg0)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def openURI(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.HeadlessNet.openURI(java.lang.String)"""
        return bool._wrap(super(_HeadlessNet, self).openURI(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def newServerSocket(self, arg0: 'Protocol', arg1: str, arg2: int, arg3: 'ServerSocketHints') -> 'net.ServerSocket':
        """public com.badlogic.gdx.net.ServerSocket com.badlogic.gdx.backends.headless.HeadlessNet.newServerSocket(com.badlogic.gdx.Net$Protocol,java.lang.String,int,com.badlogic.gdx.net.ServerSocketHints)"""
        return 'net.ServerSocket'._wrap(super(_HeadlessNet, self).newServerSocket(arg0, arg1, _int.valueOf(arg2), arg3))

    @override
    @overload
    def cancelHttpRequest(self, arg0: 'HttpRequest'):
        """public void com.badlogic.gdx.backends.headless.HeadlessNet.cancelHttpRequest(com.badlogic.gdx.Net$HttpRequest)"""
        super(_HeadlessNet, self).cancelHttpRequest(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def sendHttpRequest(self, arg0: 'HttpRequest', arg1: 'HttpResponseListener'):
        """public void com.badlogic.gdx.backends.headless.HeadlessNet.sendHttpRequest(com.badlogic.gdx.Net$HttpRequest,com.badlogic.gdx.Net$HttpResponseListener)"""
        super(_HeadlessNet, self).sendHttpRequest(arg0, arg1)

    @overload
    def newServerSocket(self, arg0: 'Protocol', arg1: int, arg2: 'ServerSocketHints') -> 'net.ServerSocket':
        """public com.badlogic.gdx.net.ServerSocket com.badlogic.gdx.backends.headless.HeadlessNet.newServerSocket(com.badlogic.gdx.Net$Protocol,int,com.badlogic.gdx.net.ServerSocketHints)"""
        return 'net.ServerSocket'._wrap(super(_HeadlessNet, self).newServerSocket(arg0, _int.valueOf(arg1), arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.backends.headless.HeadlessFileHandle
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
import java.io.Writer as _Writer
_Writer = _Writer
from builtins import type
import java.io.File as File
import com.badlogic.gdx.Files as _Files_FileType
_FileType = _Files_FileType.FileType
import java.io.BufferedReader as _BufferedReader
_BufferedReader = _BufferedReader
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.io.OutputStream as OutputStream
import java.io.FilenameFilter as FilenameFilter
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

import java.nio.channels.FileChannel.MapMode as MapMode
import java.io.Reader as _Reader
_Reader = _Reader
import com.badlogic.gdx.backends.headless.HeadlessFileHandle as _HeadlessFileHandle
_HeadlessFileHandle = _HeadlessFileHandle
from pyquantum_helper import override
import java.io.OutputStream as _OutputStream
_OutputStream = _OutputStream
import java.lang.Object as _object
import java.io.FileFilter as FileFilter
import java.nio.ByteBuffer as _ByteBuffer
_ByteBuffer = _ByteBuffer
import java.io.BufferedInputStream as _BufferedInputStream
_BufferedInputStream = _BufferedInputStream
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
from typing import List
import java.io.InputStream as _InputStream
_InputStream = _InputStream
import java.io.BufferedReader as BufferedReader
import java.io.File as _File
_File = _File
import java.lang.Integer as _int
import java.io.BufferedInputStream as BufferedInputStream
import java.io.Reader as Reader
import java.io.Writer as Writer
import java.io.InputStream as InputStream
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HeadlessFileHandle():
    """com.badlogic.gdx.backends.headless.HeadlessFileHandle"""
 
    @staticmethod
    def _wrap(java_value: _HeadlessFileHandle) -> 'HeadlessFileHandle':
        return HeadlessFileHandle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HeadlessFileHandle):
        """
        Dynamic initializer for HeadlessFileHandle.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HeadlessFileHandle__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HeadlessFileHandle__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def parent(self) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.backends.headless.HeadlessFileHandle.parent()"""
        return 'files.FileHandle'._wrap(super(HeadlessFileHandle, self).parent())

    @overload
    def reader(self, arg0: str) -> 'Reader':
        """public java.io.Reader com.badlogic.gdx.files.FileHandle.reader(java.lang.String)"""
        return 'Reader'._wrap(super(_files.FileHandle, self).reader(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def readBytes(self) -> List[int]:
        """public byte[] com.badlogic.gdx.files.FileHandle.readBytes()"""
        return List[int]._wrap(super(files.FileHandle, self).readBytes())

    @override
    @overload
    def emptyDirectory(self, arg0: bool):
        """public void com.badlogic.gdx.files.FileHandle.emptyDirectory(boolean)"""
        super(_files.FileHandle, self).emptyDirectory(_boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.equals(java.lang.Object)"""
        return bool._wrap(super(_files.FileHandle, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def map(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.files.FileHandle.map()"""
        return 'ByteBuffer'._wrap(super(files.FileHandle, self).map())

    @overload
    def list(self, arg0: 'FilenameFilter') -> List['files.FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.io.FilenameFilter)"""
        return List['files.FileHandle']._wrap(super(_files.FileHandle, self).list(arg0))

    @override
    @overload
    def deleteDirectory(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.deleteDirectory()"""
        return bool._wrap(super(files.FileHandle, self).deleteDirectory())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.files.FileHandle.hashCode()"""
        return int._wrap(super(files.FileHandle, self).hashCode())

    @override
    @overload
    def mkdirs(self):
        """public void com.badlogic.gdx.files.FileHandle.mkdirs()"""
        super(files.FileHandle, self).mkdirs()

    @override
    @overload
    def emptyDirectory(self):
        """public void com.badlogic.gdx.files.FileHandle.emptyDirectory()"""
        super(files.FileHandle, self).emptyDirectory()

    @override
    @overload
    def length(self) -> int:
        """public long com.badlogic.gdx.files.FileHandle.length()"""
        return int._wrap(super(files.FileHandle, self).length())

    @override
    @overload
    def pathWithoutExtension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.pathWithoutExtension()"""
        return str._wrap(super(files.FileHandle, self).pathWithoutExtension())

    @override
    @overload
    def copyTo(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.files.FileHandle.copyTo(com.badlogic.gdx.files.FileHandle)"""
        super(_files.FileHandle, self).copyTo(arg0)

    @overload
    def read(self, arg0: int) -> 'BufferedInputStream':
        """public java.io.BufferedInputStream com.badlogic.gdx.files.FileHandle.read(int)"""
        return 'BufferedInputStream'._wrap(super(_files.FileHandle, self).read(_int.valueOf(arg0)))

    @override
    @overload
    def writeBytes(self, arg0: bytes, arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeBytes(byte[],boolean)"""
        super(_files.FileHandle, self).writeBytes(bytes, _boolean.valueOf(arg1))

    @overload
    def writer(self, arg0: bool) -> 'Writer':
        """public java.io.Writer com.badlogic.gdx.files.FileHandle.writer(boolean)"""
        return 'Writer'._wrap(super(_files.FileHandle, self).writer(_boolean.valueOf(arg0)))

    @override
    @overload
    def lastModified(self) -> int:
        """public long com.badlogic.gdx.files.FileHandle.lastModified()"""
        return int._wrap(super(files.FileHandle, self).lastModified())

    @override
    @overload
    def file(self) -> 'File':
        """public java.io.File com.badlogic.gdx.backends.headless.HeadlessFileHandle.file()"""
        return 'File'._wrap(super(HeadlessFileHandle, self).file())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def extension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.extension()"""
        return str._wrap(super(files.FileHandle, self).extension())

    @staticmethod
    @overload
    def tempFile(arg0: str) -> 'files.FileHandle':
        """public static com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.tempFile(java.lang.String)"""
        return files.FileHandle._wrap(_FileHandle.tempFile(arg0))

    @overload
    def __init__(self, arg0: str, arg1: 'FileType'):
        """public com.badlogic.gdx.backends.headless.HeadlessFileHandle(java.lang.String,com.badlogic.gdx.Files$FileType)"""
        val = _HeadlessFileHandle(arg0, arg1)
        self.__wrapper = val

    @overload
    def sibling(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.backends.headless.HeadlessFileHandle.sibling(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_HeadlessFileHandle, self).sibling(arg0))

    @override
    @overload
    def readString(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.readString()"""
        return str._wrap(super(files.FileHandle, self).readString())

    @override
    @overload
    def write(self, arg0: 'InputStream', arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.write(java.io.InputStream,boolean)"""
        super(_files.FileHandle, self).write(arg0, _boolean.valueOf(arg1))

    @overload
    def readString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.readString(java.lang.String)"""
        return str._wrap(super(_files.FileHandle, self).readString(arg0))

    @overload
    def map(self, arg0: 'MapMode') -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.files.FileHandle.map(java.nio.channels.FileChannel$MapMode)"""
        return 'ByteBuffer'._wrap(super(_files.FileHandle, self).map(arg0))

    @overload
    def list(self, arg0: str) -> List['files.FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.lang.String)"""
        return List['files.FileHandle']._wrap(super(_files.FileHandle, self).list(arg0))

    @override
    @overload
    def read(self) -> 'InputStream':
        """public java.io.InputStream com.badlogic.gdx.files.FileHandle.read()"""
        return 'InputStream'._wrap(super(files.FileHandle, self).read())

    @overload
    def writer(self, arg0: bool, arg1: str) -> 'Writer':
        """public java.io.Writer com.badlogic.gdx.files.FileHandle.writer(boolean,java.lang.String)"""
        return 'Writer'._wrap(super(_files.FileHandle, self).writer(_boolean.valueOf(arg0), arg1))

    @override
    @overload
    def name(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.name()"""
        return str._wrap(super(files.FileHandle, self).name())

    @override
    @overload
    def writeString(self, arg0: str, arg1: bool, arg2: str):
        """public void com.badlogic.gdx.files.FileHandle.writeString(java.lang.String,boolean,java.lang.String)"""
        super(_files.FileHandle, self).writeString(arg0, _boolean.valueOf(arg1), arg2)

    @override
    @overload
    def delete(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.delete()"""
        return bool._wrap(super(files.FileHandle, self).delete())

    @staticmethod
    @overload
    def tempDirectory(arg0: str) -> 'files.FileHandle':
        """public static com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.tempDirectory(java.lang.String)"""
        return files.FileHandle._wrap(_FileHandle.tempDirectory(arg0))

    @overload
    def child(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.backends.headless.HeadlessFileHandle.child(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_HeadlessFileHandle, self).child(arg0))

    @overload
    def write(self, arg0: bool) -> 'OutputStream':
        """public java.io.OutputStream com.badlogic.gdx.files.FileHandle.write(boolean)"""
        return 'OutputStream'._wrap(super(_files.FileHandle, self).write(_boolean.valueOf(arg0)))

    @overload
    def readBytes(self, arg0: bytes, arg1: int, arg2: int) -> int:
        """public int com.badlogic.gdx.files.FileHandle.readBytes(byte[],int,int)"""
        return int._wrap(super(_files.FileHandle, self).readBytes(bytes, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def nameWithoutExtension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.nameWithoutExtension()"""
        return str._wrap(super(files.FileHandle, self).nameWithoutExtension())

    @override
    @overload
    def type(self) -> 'pygdx.Files$FileType':
        """public com.badlogic.gdx.Files$FileType com.badlogic.gdx.files.FileHandle.type()"""
        return 'pygdx.Files$FileType'._wrap(super(files.FileHandle, self).type())

    @override
    @overload
    def reader(self) -> 'Reader':
        """public java.io.Reader com.badlogic.gdx.files.FileHandle.reader()"""
        return 'Reader'._wrap(super(files.FileHandle, self).reader())

    @overload
    def reader(self, arg0: int, arg1: str) -> 'BufferedReader':
        """public java.io.BufferedReader com.badlogic.gdx.files.FileHandle.reader(int,java.lang.String)"""
        return 'BufferedReader'._wrap(super(_files.FileHandle, self).reader(_int.valueOf(arg0), arg1))

    @override
    @overload
    def writeBytes(self, arg0: bytes, arg1: int, arg2: int, arg3: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeBytes(byte[],int,int,boolean)"""
        super(_files.FileHandle, self).writeBytes(bytes, _int.valueOf(arg1), _int.valueOf(arg2), _boolean.valueOf(arg3))

    @override
    @overload
    def exists(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.exists()"""
        return bool._wrap(super(files.FileHandle, self).exists())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def write(self, arg0: bool, arg1: int) -> 'OutputStream':
        """public java.io.OutputStream com.badlogic.gdx.files.FileHandle.write(boolean,int)"""
        return 'OutputStream'._wrap(super(_files.FileHandle, self).write(_boolean.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def list(self, arg0: 'FileFilter') -> List['files.FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.io.FileFilter)"""
        return List['files.FileHandle']._wrap(super(_files.FileHandle, self).list(arg0))

    @override
    @overload
    def path(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.path()"""
        return str._wrap(super(files.FileHandle, self).path())

    @overload
    def reader(self, arg0: int) -> 'BufferedReader':
        """public java.io.BufferedReader com.badlogic.gdx.files.FileHandle.reader(int)"""
        return 'BufferedReader'._wrap(super(_files.FileHandle, self).reader(_int.valueOf(arg0)))

    @override
    @overload
    def writeString(self, arg0: str, arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeString(java.lang.String,boolean)"""
        super(_files.FileHandle, self).writeString(arg0, _boolean.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.toString()"""
        return str._wrap(super(files.FileHandle, self).toString())

    @overload
    def __init__(self, arg0: 'File', arg1: 'FileType'):
        """public com.badlogic.gdx.backends.headless.HeadlessFileHandle(java.io.File,com.badlogic.gdx.Files$FileType)"""
        val = _HeadlessFileHandle(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def isDirectory(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.isDirectory()"""
        return bool._wrap(super(files.FileHandle, self).isDirectory())

    @override
    @overload
    def moveTo(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.files.FileHandle.moveTo(com.badlogic.gdx.files.FileHandle)"""
        super(_files.FileHandle, self).moveTo(arg0)

    @override
    @overload
    def list(self) -> List['files.FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list()"""
        return List['files.FileHandle']._wrap(super(files.FileHandle, self).list()) 
 
 
# CLASS: com.badlogic.gdx.backends.headless.HeadlessNativesLoader
import com.badlogic.gdx.backends.headless.HeadlessNativesLoader as _HeadlessNativesLoader
_HeadlessNativesLoader = _HeadlessNativesLoader
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HeadlessNativesLoader():
    """com.badlogic.gdx.backends.headless.HeadlessNativesLoader"""
 
    @staticmethod
    def _wrap(java_value: _HeadlessNativesLoader) -> 'HeadlessNativesLoader':
        return HeadlessNativesLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HeadlessNativesLoader):
        """
        Dynamic initializer for HeadlessNativesLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HeadlessNativesLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HeadlessNativesLoader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

        @staticmethod
        @overload
        def load():
            """public static void com.badlogic.gdx.backends.headless.HeadlessNativesLoader.load()"""
            _HeadlessNativesLoader.load()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.HeadlessNativesLoader()"""
        val = _HeadlessNativesLoader()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.HeadlessNativesLoader()"""
        val = _HeadlessNativesLoader()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.backends.headless.HeadlessPreferences
from pyquantum_helper import import_once as _import_once
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

import com.badlogic.gdx.Preferences as _Preferences
_Preferences = _Preferences
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.backends.headless.HeadlessPreferences as _HeadlessPreferences
_HeadlessPreferences = _HeadlessPreferences
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HeadlessPreferences():
    """com.badlogic.gdx.backends.headless.HeadlessPreferences"""
 
    @staticmethod
    def _wrap(java_value: _HeadlessPreferences) -> 'HeadlessPreferences':
        return HeadlessPreferences(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HeadlessPreferences):
        """
        Dynamic initializer for HeadlessPreferences.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HeadlessPreferences__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HeadlessPreferences__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def putLong(self, arg0: str, arg1: int) -> 'pygdx.Preferences':
        """public com.badlogic.gdx.Preferences com.badlogic.gdx.backends.headless.HeadlessPreferences.putLong(java.lang.String,long)"""
        return 'pygdx.Preferences'._wrap(super(_HeadlessPreferences, self).putLong(arg0, _long.valueOf(arg1)))

    @overload
    def getString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.backends.headless.HeadlessPreferences.getString(java.lang.String)"""
        return str._wrap(super(_HeadlessPreferences, self).getString(arg0))

    @overload
    def put(self, arg0: 'Map') -> 'pygdx.Preferences':
        """public com.badlogic.gdx.Preferences com.badlogic.gdx.backends.headless.HeadlessPreferences.put(java.util.Map<java.lang.String, ?>)"""
        return 'pygdx.Preferences'._wrap(super(_HeadlessPreferences, self).put(arg0))

    @overload
    def getBoolean(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.HeadlessPreferences.getBoolean(java.lang.String)"""
        return bool._wrap(super(_HeadlessPreferences, self).getBoolean(arg0))

    @overload
    def getLong(self, arg0: str) -> int:
        """public long com.badlogic.gdx.backends.headless.HeadlessPreferences.getLong(java.lang.String)"""
        return int._wrap(super(_HeadlessPreferences, self).getLong(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def putBoolean(self, arg0: str, arg1: bool) -> 'pygdx.Preferences':
        """public com.badlogic.gdx.Preferences com.badlogic.gdx.backends.headless.HeadlessPreferences.putBoolean(java.lang.String,boolean)"""
        return 'pygdx.Preferences'._wrap(super(_HeadlessPreferences, self).putBoolean(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def putFloat(self, arg0: str, arg1: float) -> 'pygdx.Preferences':
        """public com.badlogic.gdx.Preferences com.badlogic.gdx.backends.headless.HeadlessPreferences.putFloat(java.lang.String,float)"""
        return 'pygdx.Preferences'._wrap(super(_HeadlessPreferences, self).putFloat(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def remove(self, arg0: str):
        """public void com.badlogic.gdx.backends.headless.HeadlessPreferences.remove(java.lang.String)"""
        super(_HeadlessPreferences, self).remove(arg0)

    @overload
    def getString(self, arg0: str, arg1: str) -> str:
        """public java.lang.String com.badlogic.gdx.backends.headless.HeadlessPreferences.getString(java.lang.String,java.lang.String)"""
        return str._wrap(super(_HeadlessPreferences, self).getString(arg0, arg1))

    @override
    @overload
    def flush(self):
        """public void com.badlogic.gdx.backends.headless.HeadlessPreferences.flush()"""
        super(HeadlessPreferences, self).flush()

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public com.badlogic.gdx.backends.headless.HeadlessPreferences(java.lang.String,java.lang.String)"""
        val = _HeadlessPreferences(arg0, arg1)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getFloat(self, arg0: str) -> float:
        """public float com.badlogic.gdx.backends.headless.HeadlessPreferences.getFloat(java.lang.String)"""
        return float._wrap(super(_HeadlessPreferences, self).getFloat(arg0))

    @overload
    def getLong(self, arg0: str, arg1: int) -> int:
        """public long com.badlogic.gdx.backends.headless.HeadlessPreferences.getLong(java.lang.String,long)"""
        return int._wrap(super(_HeadlessPreferences, self).getLong(arg0, _long.valueOf(arg1)))

    @overload
    def getFloat(self, arg0: str, arg1: float) -> float:
        """public float com.badlogic.gdx.backends.headless.HeadlessPreferences.getFloat(java.lang.String,float)"""
        return float._wrap(super(_HeadlessPreferences, self).getFloat(arg0, _float.valueOf(arg1)))

    @overload
    def getBoolean(self, arg0: str, arg1: bool) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.HeadlessPreferences.getBoolean(java.lang.String,boolean)"""
        return bool._wrap(super(_HeadlessPreferences, self).getBoolean(arg0, _boolean.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def get(self) -> 'Map':
        """public java.util.Map<java.lang.String, ?> com.badlogic.gdx.backends.headless.HeadlessPreferences.get()"""
        return 'Map'._wrap(super(HeadlessPreferences, self).get())

    @overload
    def getInteger(self, arg0: str, arg1: int) -> int:
        """public int com.badlogic.gdx.backends.headless.HeadlessPreferences.getInteger(java.lang.String,int)"""
        return int._wrap(super(_HeadlessPreferences, self).getInteger(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def putInteger(self, arg0: str, arg1: int) -> 'pygdx.Preferences':
        """public com.badlogic.gdx.Preferences com.badlogic.gdx.backends.headless.HeadlessPreferences.putInteger(java.lang.String,int)"""
        return 'pygdx.Preferences'._wrap(super(_HeadlessPreferences, self).putInteger(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.backends.headless.HeadlessPreferences.clear()"""
        super(HeadlessPreferences, self).clear()

    @overload
    def putString(self, arg0: str, arg1: str) -> 'pygdx.Preferences':
        """public com.badlogic.gdx.Preferences com.badlogic.gdx.backends.headless.HeadlessPreferences.putString(java.lang.String,java.lang.String)"""
        return 'pygdx.Preferences'._wrap(super(_HeadlessPreferences, self).putString(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'FileHandle'):
        """public com.badlogic.gdx.backends.headless.HeadlessPreferences(com.badlogic.gdx.files.FileHandle)"""
        val = _HeadlessPreferences(arg0)
        self.__wrapper = val

    @overload
    def contains(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.backends.headless.HeadlessPreferences.contains(java.lang.String)"""
        return bool._wrap(super(_HeadlessPreferences, self).contains(arg0))

    @overload
    def getInteger(self, arg0: str) -> int:
        """public int com.badlogic.gdx.backends.headless.HeadlessPreferences.getInteger(java.lang.String)"""
        return int._wrap(super(_HeadlessPreferences, self).getInteger(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.backends.headless.HeadlessApplicationConfiguration
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.backends.headless.HeadlessApplicationConfiguration as _HeadlessApplicationConfiguration
_HeadlessApplicationConfiguration = _HeadlessApplicationConfiguration
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HeadlessApplicationConfiguration():
    """com.badlogic.gdx.backends.headless.HeadlessApplicationConfiguration"""
 
    @staticmethod
    def _wrap(java_value: _HeadlessApplicationConfiguration) -> 'HeadlessApplicationConfiguration':
        return HeadlessApplicationConfiguration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HeadlessApplicationConfiguration):
        """
        Dynamic initializer for HeadlessApplicationConfiguration.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HeadlessApplicationConfiguration__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HeadlessApplicationConfiguration__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.HeadlessApplicationConfiguration()"""
        val = _HeadlessApplicationConfiguration()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.HeadlessApplicationConfiguration()"""
        val = _HeadlessApplicationConfiguration()
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.backends.headless.HeadlessApplicationLogger
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.backends.headless.HeadlessApplicationLogger as _HeadlessApplicationLogger
_HeadlessApplicationLogger = _HeadlessApplicationLogger
import java.lang.String as _string
import java.lang.Integer as _int
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HeadlessApplicationLogger():
    """com.badlogic.gdx.backends.headless.HeadlessApplicationLogger"""
 
    @staticmethod
    def _wrap(java_value: _HeadlessApplicationLogger) -> 'HeadlessApplicationLogger':
        return HeadlessApplicationLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HeadlessApplicationLogger):
        """
        Dynamic initializer for HeadlessApplicationLogger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HeadlessApplicationLogger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HeadlessApplicationLogger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.backends.headless.HeadlessApplicationLogger()"""
        val = _HeadlessApplicationLogger()
        self.__wrapper = val

    @override
    @overload
    def debug(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplicationLogger.debug(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(_HeadlessApplicationLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.backends.headless.HeadlessApplicationLogger()"""
        val = _HeadlessApplicationLogger()
        self.__wrapper = val

    @override
    @overload
    def error(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplicationLogger.error(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(_HeadlessApplicationLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def log(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplicationLogger.log(java.lang.String,java.lang.String)"""
        super(_HeadlessApplicationLogger, self).log(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def error(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplicationLogger.error(java.lang.String,java.lang.String)"""
        super(_HeadlessApplicationLogger, self).error(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplicationLogger.debug(java.lang.String,java.lang.String)"""
        super(_HeadlessApplicationLogger, self).debug(arg0, arg1)

    @override
    @overload
    def log(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.backends.headless.HeadlessApplicationLogger.log(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(_HeadlessApplicationLogger, self).log(arg0, arg1, arg2)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())