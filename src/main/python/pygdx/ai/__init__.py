from __future__ import annotations
from overload import overload


 
import com.badlogic.gdx.ai.Timepiece as _Timepiece
_Timepiece = _Timepiece
from abc import abstractmethod, ABC
 
class Timepiece():
    """com.badlogic.gdx.ai.Timepiece"""
 
    @staticmethod
    def _wrap(java_value: _Timepiece) -> 'Timepiece':
        return Timepiece(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Timepiece):
        """
        Dynamic initializer for Timepiece.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Timepiece__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Timepiece__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def update(self, arg0: float):
        """public abstract void com.badlogic.gdx.ai.Timepiece.update(float)"""
        pass

    @abstractmethod
    def getTime(self, ):
        """public abstract float com.badlogic.gdx.ai.Timepiece.getTime()"""
        pass

    @abstractmethod
    def getDeltaTime(self, ):
        """public abstract float com.badlogic.gdx.ai.Timepiece.getDeltaTime()"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.ai.Timepiece
import com.badlogic.gdx.ai.Timepiece as _Timepiece
_Timepiece = _Timepiece
from abc import abstractmethod, ABC
 
class Timepiece():
    """com.badlogic.gdx.ai.Timepiece"""
 
    @staticmethod
    def _wrap(java_value: _Timepiece) -> 'Timepiece':
        return Timepiece(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Timepiece):
        """
        Dynamic initializer for Timepiece.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Timepiece__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Timepiece__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def update(self, arg0: float):
        """public abstract void com.badlogic.gdx.ai.Timepiece.update(float)"""
        pass

    @abstractmethod
    def getTime(self, ):
        """public abstract float com.badlogic.gdx.ai.Timepiece.getTime()"""
        pass

    @abstractmethod
    def getDeltaTime(self, ):
        """public abstract float com.badlogic.gdx.ai.Timepiece.getDeltaTime()"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.ai.Timepiece 
 
 
# CLASS: com.badlogic.gdx.ai.Logger
import com.badlogic.gdx.ai.Logger as _Logger
_Logger = _Logger
import java.lang.Throwable as Throwable
from abc import abstractmethod, ABC
 
class Logger():
    """com.badlogic.gdx.ai.Logger"""
 
    @staticmethod
    def _wrap(java_value: _Logger) -> 'Logger':
        return Logger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Logger):
        """
        Dynamic initializer for Logger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Logger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Logger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def debug(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public abstract void com.badlogic.gdx.ai.Logger.debug(java.lang.String,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public abstract void com.badlogic.gdx.ai.Logger.info(java.lang.String,java.lang.String,java.lang.Throwable)"""
        pass

    @abstractmethod
    def info(self, arg0: str, arg1: str):
        """public abstract void com.badlogic.gdx.ai.Logger.info(java.lang.String,java.lang.String)"""
        pass

    @abstractmethod
    def error(self, arg0: str, arg1: str):
        """public abstract void com.badlogic.gdx.ai.Logger.error(java.lang.String,java.lang.String)"""
        pass

    @abstractmethod
    def debug(self, arg0: str, arg1: str):
        """public abstract void com.badlogic.gdx.ai.Logger.debug(java.lang.String,java.lang.String)"""
        pass

    @abstractmethod
    def error(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public abstract void com.badlogic.gdx.ai.Logger.error(java.lang.String,java.lang.String,java.lang.Throwable)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.GdxAI
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.ai.Timepiece as _Timepiece
_Timepiece = _Timepiece
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.Logger as _Logger
_Logger = _Logger
import java.lang.Integer as _int
import com.badlogic.gdx.ai.GdxAI as _GdxAI
_GdxAI = _GdxAI
from builtins import bool
import com.badlogic.gdx.ai.FileSystem as _FileSystem
_FileSystem = _FileSystem
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GdxAI():
    """com.badlogic.gdx.ai.GdxAI"""
 
    @staticmethod
    def _wrap(java_value: _GdxAI) -> 'GdxAI':
        return GdxAI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GdxAI):
        """
        Dynamic initializer for GdxAI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GdxAI__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GdxAI__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def setFileSystem(arg0: 'FileSystem'):
        """public static void com.badlogic.gdx.ai.GdxAI.setFileSystem(com.badlogic.gdx.ai.FileSystem)"""
        _GdxAI.setFileSystem(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def setTimepiece(arg0: 'Timepiece'):
        """public static void com.badlogic.gdx.ai.GdxAI.setTimepiece(com.badlogic.gdx.ai.Timepiece)"""
        _GdxAI.setTimepiece(arg0)

    @staticmethod
    @overload
    def getFileSystem() -> 'FileSystem':
        """public static com.badlogic.gdx.ai.FileSystem com.badlogic.gdx.ai.GdxAI.getFileSystem()"""
        return FileSystem._wrap(_GdxAI.getFileSystem())

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

    @staticmethod
    @overload
    def getTimepiece() -> 'Timepiece':
        """public static com.badlogic.gdx.ai.Timepiece com.badlogic.gdx.ai.GdxAI.getTimepiece()"""
        return Timepiece._wrap(_GdxAI.getTimepiece())

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

    @staticmethod
    @overload
    def getLogger() -> 'Logger':
        """public static com.badlogic.gdx.ai.Logger com.badlogic.gdx.ai.GdxAI.getLogger()"""
        return Logger._wrap(_GdxAI.getLogger())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def setLogger(arg0: 'Logger'):
        """public static void com.badlogic.gdx.ai.GdxAI.setLogger(com.badlogic.gdx.ai.Logger)"""
        _GdxAI.setLogger(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.DefaultTimepiece
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.ai.DefaultTimepiece as _DefaultTimepiece
_DefaultTimepiece = _DefaultTimepiece
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DefaultTimepiece():
    """com.badlogic.gdx.ai.DefaultTimepiece"""
 
    @staticmethod
    def _wrap(java_value: _DefaultTimepiece) -> 'DefaultTimepiece':
        return DefaultTimepiece(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefaultTimepiece):
        """
        Dynamic initializer for DefaultTimepiece.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefaultTimepiece__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefaultTimepiece__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.ai.DefaultTimepiece.getTime()"""
        return float._wrap(super(DefaultTimepiece, self).getTime())

    @override
    @overload
    def getDeltaTime(self) -> float:
        """public float com.badlogic.gdx.ai.DefaultTimepiece.getDeltaTime()"""
        return float._wrap(super(DefaultTimepiece, self).getDeltaTime())

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
    def __init__(self):
        """public com.badlogic.gdx.ai.DefaultTimepiece()"""
        val = _DefaultTimepiece()
        self.__wrapper = val

    @override
    @overload
    def update(self, arg0: float):
        """public void com.badlogic.gdx.ai.DefaultTimepiece.update(float)"""
        super(_DefaultTimepiece, self).update(_float.valueOf(arg0))

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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

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
        """public com.badlogic.gdx.ai.DefaultTimepiece()"""
        val = _DefaultTimepiece()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.DefaultTimepiece(float)"""
        val = _DefaultTimepiece(_float.valueOf(arg0))
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.ai.GdxLogger
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.ai.GdxLogger as _GdxLogger
_GdxLogger = _GdxLogger
import java.lang.String as _string
import java.lang.Integer as _int
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GdxLogger():
    """com.badlogic.gdx.ai.GdxLogger"""
 
    @staticmethod
    def _wrap(java_value: _GdxLogger) -> 'GdxLogger':
        return GdxLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GdxLogger):
        """
        Dynamic initializer for GdxLogger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GdxLogger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GdxLogger__wrapper":
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

    @override
    @overload
    def info(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.ai.GdxLogger.info(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(_GdxLogger, self).info(arg0, arg1, arg2)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.GdxLogger()"""
        val = _GdxLogger()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def debug(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.ai.GdxLogger.debug(java.lang.String,java.lang.String)"""
        super(_GdxLogger, self).debug(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.ai.GdxLogger.debug(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(_GdxLogger, self).debug(arg0, arg1, arg2)

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
    def error(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.ai.GdxLogger.error(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(_GdxLogger, self).error(arg0, arg1, arg2)

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
    def __init__(self):
        """public com.badlogic.gdx.ai.GdxLogger()"""
        val = _GdxLogger()
        self.__wrapper = val

    @override
    @overload
    def error(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.ai.GdxLogger.error(java.lang.String,java.lang.String)"""
        super(_GdxLogger, self).error(arg0, arg1)

    @override
    @overload
    def info(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.ai.GdxLogger.info(java.lang.String,java.lang.String)"""
        super(_GdxLogger, self).info(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.GdxFileSystem
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
import java.io.File as File
import java.lang.String as _String
_String = _String
try:
    from pygdx.assets import loaders
except ImportError:
    loaders = _import_once("pygdx.assets.loaders")

import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import java.lang.String as _string
import com.badlogic.gdx.ai.GdxFileSystem as _GdxFileSystem
_GdxFileSystem = _GdxFileSystem
import com.badlogic.gdx.assets.loaders.FileHandleResolver as _FileHandleResolver
_FileHandleResolver = _FileHandleResolver
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
 
class GdxFileSystem():
    """com.badlogic.gdx.ai.GdxFileSystem"""
 
    @staticmethod
    def _wrap(java_value: _GdxFileSystem) -> 'GdxFileSystem':
        return GdxFileSystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GdxFileSystem):
        """
        Dynamic initializer for GdxFileSystem.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GdxFileSystem__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GdxFileSystem__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def newFileHandle(self, arg0: str, arg1: 'FileType') -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.GdxFileSystem.newFileHandle(java.lang.String,com.badlogic.gdx.Files$FileType)"""
        return 'files.FileHandle'._wrap(super(_GdxFileSystem, self).newFileHandle(arg0, arg1))

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.GdxFileSystem()"""
        val = _GdxFileSystem()
        self.__wrapper = val

    @overload
    def newResolver(self, arg0: 'FileType') -> 'loaders.FileHandleResolver':
        """public com.badlogic.gdx.assets.loaders.FileHandleResolver com.badlogic.gdx.ai.GdxFileSystem.newResolver(com.badlogic.gdx.Files$FileType)"""
        return 'loaders.FileHandleResolver'._wrap(super(_GdxFileSystem, self).newResolver(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.GdxFileSystem()"""
        val = _GdxFileSystem()
        self.__wrapper = val

    @overload
    def newFileHandle(self, arg0: 'File') -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.GdxFileSystem.newFileHandle(java.io.File)"""
        return 'files.FileHandle'._wrap(super(_GdxFileSystem, self).newFileHandle(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def newFileHandle(self, arg0: 'File', arg1: 'FileType') -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.GdxFileSystem.newFileHandle(java.io.File,com.badlogic.gdx.Files$FileType)"""
        return 'files.FileHandle'._wrap(super(_GdxFileSystem, self).newFileHandle(arg0, arg1))

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
    def newFileHandle(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.GdxFileSystem.newFileHandle(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_GdxFileSystem, self).newFileHandle(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.NullLogger
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.ai.NullLogger as _NullLogger
_NullLogger = _NullLogger
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NullLogger():
    """com.badlogic.gdx.ai.NullLogger"""
 
    @staticmethod
    def _wrap(java_value: _NullLogger) -> 'NullLogger':
        return NullLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NullLogger):
        """
        Dynamic initializer for NullLogger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NullLogger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NullLogger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def debug(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.ai.NullLogger.debug(java.lang.String,java.lang.String)"""
        super(_NullLogger, self).debug(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.ai.NullLogger.error(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(_NullLogger, self).error(arg0, arg1, arg2)

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
        """public com.badlogic.gdx.ai.NullLogger()"""
        val = _NullLogger()
        self.__wrapper = val

    @override
    @overload
    def info(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.ai.NullLogger.info(java.lang.String,java.lang.String)"""
        super(_NullLogger, self).info(arg0, arg1)

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
    def error(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.ai.NullLogger.error(java.lang.String,java.lang.String)"""
        super(_NullLogger, self).error(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def debug(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.ai.NullLogger.debug(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(_NullLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def info(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.ai.NullLogger.info(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(_NullLogger, self).info(arg0, arg1, arg2)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.NullLogger()"""
        val = _NullLogger()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.FileSystem
from pyquantum_helper import import_once as _import_once
try:
    import pygdx
except ImportError:
    pygdx = _import_once("pygdx")

import java.io.File as File
from abc import abstractmethod, ABC
import com.badlogic.gdx.ai.FileSystem as _FileSystem
_FileSystem = _FileSystem
 
class FileSystem():
    """com.badlogic.gdx.ai.FileSystem"""
 
    @staticmethod
    def _wrap(java_value: _FileSystem) -> 'FileSystem':
        return FileSystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FileSystem):
        """
        Dynamic initializer for FileSystem.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FileSystem__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FileSystem__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def newFileHandle(self, arg0: str):
        """public abstract com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.FileSystem.newFileHandle(java.lang.String)"""
        pass

    @abstractmethod
    def newResolver(self, arg0: 'FileType'):
        """public abstract com.badlogic.gdx.assets.loaders.FileHandleResolver com.badlogic.gdx.ai.FileSystem.newResolver(com.badlogic.gdx.Files$FileType)"""
        pass

    @abstractmethod
    def newFileHandle(self, arg0: str, arg1: 'FileType'):
        """public abstract com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.FileSystem.newFileHandle(java.lang.String,com.badlogic.gdx.Files$FileType)"""
        pass

    @abstractmethod
    def newFileHandle(self, arg0: 'File', arg1: 'FileType'):
        """public abstract com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.FileSystem.newFileHandle(java.io.File,com.badlogic.gdx.Files$FileType)"""
        pass

    @abstractmethod
    def newFileHandle(self, arg0: 'File'):
        """public abstract com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.FileSystem.newFileHandle(java.io.File)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.ai.StdoutLogger
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.ai.StdoutLogger as _StdoutLogger
_StdoutLogger = _StdoutLogger
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StdoutLogger():
    """com.badlogic.gdx.ai.StdoutLogger"""
 
    @staticmethod
    def _wrap(java_value: _StdoutLogger) -> 'StdoutLogger':
        return StdoutLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StdoutLogger):
        """
        Dynamic initializer for StdoutLogger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StdoutLogger__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StdoutLogger__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def info(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.ai.StdoutLogger.info(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(_StdoutLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def error(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.ai.StdoutLogger.error(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(_StdoutLogger, self).error(arg0, arg1, arg2)

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
    def error(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.ai.StdoutLogger.error(java.lang.String,java.lang.String)"""
        super(_StdoutLogger, self).error(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def debug(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.ai.StdoutLogger.debug(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(_StdoutLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def debug(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.ai.StdoutLogger.debug(java.lang.String,java.lang.String)"""
        super(_StdoutLogger, self).debug(arg0, arg1)

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
        """public com.badlogic.gdx.ai.StdoutLogger()"""
        val = _StdoutLogger()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.StdoutLogger()"""
        val = _StdoutLogger()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def info(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.ai.StdoutLogger.info(java.lang.String,java.lang.String)"""
        super(_StdoutLogger, self).info(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.ai.StandaloneFileSystem$DesktopFileHandle
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
import com.badlogic.gdx.ai.StandaloneFileSystem as _StandaloneFileSystem_DesktopFileHandle
_DesktopFileHandle = _StandaloneFileSystem_DesktopFileHandle.DesktopFileHandle
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
 
class DesktopFileHandle():
    """com.badlogic.gdx.ai.StandaloneFileSystem.DesktopFileHandle"""
 
    @staticmethod
    def _wrap(java_value: _DesktopFileHandle) -> 'DesktopFileHandle':
        return DesktopFileHandle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DesktopFileHandle):
        """
        Dynamic initializer for DesktopFileHandle.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DesktopFileHandle__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DesktopFileHandle__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def reader(self, arg0: str) -> 'Reader':
        """public java.io.Reader com.badlogic.gdx.files.FileHandle.reader(java.lang.String)"""
        return 'Reader'._wrap(super(_files.FileHandle, self).reader(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: str, arg1: 'FileType'):
        """public com.badlogic.gdx.ai.StandaloneFileSystem$DesktopFileHandle(java.lang.String,com.badlogic.gdx.Files$FileType)"""
        val = _DesktopFileHandle(arg0, arg1)
        self.__wrapper = val

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
    def child(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.StandaloneFileSystem$DesktopFileHandle.child(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_DesktopFileHandle, self).child(arg0))

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def file(self) -> 'File':
        """public java.io.File com.badlogic.gdx.ai.StandaloneFileSystem$DesktopFileHandle.file()"""
        return 'File'._wrap(super(DesktopFileHandle, self).file())

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
    def sibling(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.StandaloneFileSystem$DesktopFileHandle.sibling(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_DesktopFileHandle, self).sibling(arg0))

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

    @override
    @overload
    def parent(self) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.StandaloneFileSystem$DesktopFileHandle.parent()"""
        return 'files.FileHandle'._wrap(super(DesktopFileHandle, self).parent())

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

    @overload
    def __init__(self, arg0: 'File', arg1: 'FileType'):
        """public com.badlogic.gdx.ai.StandaloneFileSystem$DesktopFileHandle(java.io.File,com.badlogic.gdx.Files$FileType)"""
        val = _DesktopFileHandle(arg0, arg1)
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.ai.StandaloneFileSystem
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
import java.io.File as File
import java.lang.String as _String
_String = _String
try:
    from pygdx.assets import loaders
except ImportError:
    loaders = _import_once("pygdx.assets.loaders")

import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
import java.lang.String as _string
import com.badlogic.gdx.assets.loaders.FileHandleResolver as _FileHandleResolver
_FileHandleResolver = _FileHandleResolver
import java.lang.Integer as _int
import com.badlogic.gdx.ai.StandaloneFileSystem as _StandaloneFileSystem
_StandaloneFileSystem = _StandaloneFileSystem
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StandaloneFileSystem():
    """com.badlogic.gdx.ai.StandaloneFileSystem"""
 
    @staticmethod
    def _wrap(java_value: _StandaloneFileSystem) -> 'StandaloneFileSystem':
        return StandaloneFileSystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StandaloneFileSystem):
        """
        Dynamic initializer for StandaloneFileSystem.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StandaloneFileSystem__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StandaloneFileSystem__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def newResolver(self, arg0: 'FileType') -> 'loaders.FileHandleResolver':
        """public com.badlogic.gdx.assets.loaders.FileHandleResolver com.badlogic.gdx.ai.StandaloneFileSystem.newResolver(com.badlogic.gdx.Files$FileType)"""
        return 'loaders.FileHandleResolver'._wrap(super(_StandaloneFileSystem, self).newResolver(arg0))

    @overload
    def newFileHandle(self, arg0: 'File', arg1: 'FileType') -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.StandaloneFileSystem.newFileHandle(java.io.File,com.badlogic.gdx.Files$FileType)"""
        return 'files.FileHandle'._wrap(super(_StandaloneFileSystem, self).newFileHandle(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.StandaloneFileSystem()"""
        val = _StandaloneFileSystem()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def newFileHandle(self, arg0: str, arg1: 'FileType') -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.StandaloneFileSystem.newFileHandle(java.lang.String,com.badlogic.gdx.Files$FileType)"""
        return 'files.FileHandle'._wrap(super(_StandaloneFileSystem, self).newFileHandle(arg0, arg1))

    @overload
    def newFileHandle(self, arg0: 'File') -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.StandaloneFileSystem.newFileHandle(java.io.File)"""
        return 'files.FileHandle'._wrap(super(_StandaloneFileSystem, self).newFileHandle(arg0))

    @overload
    def newFileHandle(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.StandaloneFileSystem.newFileHandle(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_StandaloneFileSystem, self).newFileHandle(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.StandaloneFileSystem()"""
        val = _StandaloneFileSystem()
        self.__wrapper = val

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())