from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.ai.GdxAI as __GdxAI
__GdxAI = __GdxAI
import com.badlogic.gdx.ai.Logger as __Logger
__Logger = __Logger
import com.badlogic.gdx.ai.Timepiece as __Timepiece
__Timepiece = __Timepiece
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.ai.FileSystem as __FileSystem
__FileSystem = __FileSystem
from builtins import int
 
class GdxAI():
    """com.badlogic.gdx.ai.GdxAI"""
 
    @staticmethod
    def __wrap(java_value: __GdxAI) -> 'GdxAI':
        return GdxAI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GdxAI):
        """
        Dynamic initializer for GdxAI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def setTimepiece(arg0: 'Timepiece'):
        """public static void com.badlogic.gdx.ai.GdxAI.setTimepiece(com.badlogic.gdx.ai.Timepiece)"""
        __GdxAI.setTimepiece(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getLogger() -> 'Logger':
        """public static com.badlogic.gdx.ai.Logger com.badlogic.gdx.ai.GdxAI.getLogger()"""
        return Logger.__wrap(__GdxAI.getLogger())

    @staticmethod
    @overload
    def getFileSystem() -> 'FileSystem':
        """public static com.badlogic.gdx.ai.FileSystem com.badlogic.gdx.ai.GdxAI.getFileSystem()"""
        return FileSystem.__wrap(__GdxAI.getFileSystem())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def setLogger(arg0: 'Logger'):
        """public static void com.badlogic.gdx.ai.GdxAI.setLogger(com.badlogic.gdx.ai.Logger)"""
        __GdxAI.setLogger(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def setFileSystem(arg0: 'FileSystem'):
        """public static void com.badlogic.gdx.ai.GdxAI.setFileSystem(com.badlogic.gdx.ai.FileSystem)"""
        __GdxAI.setFileSystem(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getTimepiece() -> 'Timepiece':
        """public static com.badlogic.gdx.ai.Timepiece com.badlogic.gdx.ai.GdxAI.getTimepiece()"""
        return Timepiece.__wrap(__GdxAI.getTimepiece())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.ai.GdxAI
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.ai.GdxAI as __GdxAI
__GdxAI = __GdxAI
import com.badlogic.gdx.ai.Logger as __Logger
__Logger = __Logger
import com.badlogic.gdx.ai.Timepiece as __Timepiece
__Timepiece = __Timepiece
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.ai.FileSystem as __FileSystem
__FileSystem = __FileSystem
from builtins import int
 
class GdxAI():
    """com.badlogic.gdx.ai.GdxAI"""
 
    @staticmethod
    def __wrap(java_value: __GdxAI) -> 'GdxAI':
        return GdxAI(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GdxAI):
        """
        Dynamic initializer for GdxAI.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def setTimepiece(arg0: 'Timepiece'):
        """public static void com.badlogic.gdx.ai.GdxAI.setTimepiece(com.badlogic.gdx.ai.Timepiece)"""
        __GdxAI.setTimepiece(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getLogger() -> 'Logger':
        """public static com.badlogic.gdx.ai.Logger com.badlogic.gdx.ai.GdxAI.getLogger()"""
        return Logger.__wrap(__GdxAI.getLogger())

    @staticmethod
    @overload
    def getFileSystem() -> 'FileSystem':
        """public static com.badlogic.gdx.ai.FileSystem com.badlogic.gdx.ai.GdxAI.getFileSystem()"""
        return FileSystem.__wrap(__GdxAI.getFileSystem())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def setLogger(arg0: 'Logger'):
        """public static void com.badlogic.gdx.ai.GdxAI.setLogger(com.badlogic.gdx.ai.Logger)"""
        __GdxAI.setLogger(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def setFileSystem(arg0: 'FileSystem'):
        """public static void com.badlogic.gdx.ai.GdxAI.setFileSystem(com.badlogic.gdx.ai.FileSystem)"""
        __GdxAI.setFileSystem(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getTimepiece() -> 'Timepiece':
        """public static com.badlogic.gdx.ai.Timepiece com.badlogic.gdx.ai.GdxAI.getTimepiece()"""
        return Timepiece.__wrap(__GdxAI.getTimepiece())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.ai.GdxAI 
 
 
# CLASS: com.badlogic.gdx.ai.FileSystem
from pyquantum_helper import import_once as __import_once__
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

import java.io.File as File
from abc import abstractmethod, ABC
import com.badlogic.gdx.ai.FileSystem as __FileSystem
__FileSystem = __FileSystem
 
class FileSystem(ABC):
    """com.badlogic.gdx.ai.FileSystem"""
 
    @staticmethod
    def __wrap(java_value: __FileSystem) -> 'FileSystem':
        return FileSystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FileSystem):
        """
        Dynamic initializer for FileSystem.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.ai.DefaultTimepiece
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.ai.DefaultTimepiece as __DefaultTimepiece
__DefaultTimepiece = __DefaultTimepiece
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DefaultTimepiece():
    """com.badlogic.gdx.ai.DefaultTimepiece"""
 
    @staticmethod
    def __wrap(java_value: __DefaultTimepiece) -> 'DefaultTimepiece':
        return DefaultTimepiece(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DefaultTimepiece):
        """
        Dynamic initializer for DefaultTimepiece.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.DefaultTimepiece()"""
        val = __DefaultTimepiece()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.DefaultTimepiece()"""
        val = __DefaultTimepiece()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getTime(self) -> float:
        """public float com.badlogic.gdx.ai.DefaultTimepiece.getTime()"""
        return float.__wrap(super(DefaultTimepiece, self).getTime())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getDeltaTime(self) -> float:
        """public float com.badlogic.gdx.ai.DefaultTimepiece.getDeltaTime()"""
        return float.__wrap(super(DefaultTimepiece, self).getDeltaTime())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def update(self, arg0: float):
        """public void com.badlogic.gdx.ai.DefaultTimepiece.update(float)"""
        super(__DefaultTimepiece, self).update(__float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: float):
        """public com.badlogic.gdx.ai.DefaultTimepiece(float)"""
        val = __DefaultTimepiece(__float.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.ai.NullLogger
import com.badlogic.gdx.ai.NullLogger as __NullLogger
__NullLogger = __NullLogger
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NullLogger():
    """com.badlogic.gdx.ai.NullLogger"""
 
    @staticmethod
    def __wrap(java_value: __NullLogger) -> 'NullLogger':
        return NullLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NullLogger):
        """
        Dynamic initializer for NullLogger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def debug(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.ai.NullLogger.debug(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(__NullLogger, self).debug(arg0, arg1, arg2)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.NullLogger()"""
        val = __NullLogger()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def error(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.ai.NullLogger.error(java.lang.String,java.lang.String)"""
        super(__NullLogger, self).error(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def info(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.ai.NullLogger.info(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(__NullLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def info(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.ai.NullLogger.info(java.lang.String,java.lang.String)"""
        super(__NullLogger, self).info(arg0, arg1)

    @override
    @overload
    def debug(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.ai.NullLogger.debug(java.lang.String,java.lang.String)"""
        super(__NullLogger, self).debug(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.NullLogger()"""
        val = __NullLogger()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def error(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.ai.NullLogger.error(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(__NullLogger, self).error(arg0, arg1, arg2) 
 
 
# CLASS: com.badlogic.gdx.ai.StdoutLogger
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.ai.StdoutLogger as __StdoutLogger
__StdoutLogger = __StdoutLogger
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class StdoutLogger():
    """com.badlogic.gdx.ai.StdoutLogger"""
 
    @staticmethod
    def __wrap(java_value: __StdoutLogger) -> 'StdoutLogger':
        return StdoutLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StdoutLogger):
        """
        Dynamic initializer for StdoutLogger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def debug(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.ai.StdoutLogger.debug(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(__StdoutLogger, self).debug(arg0, arg1, arg2)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def error(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.ai.StdoutLogger.error(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(__StdoutLogger, self).error(arg0, arg1, arg2)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.StdoutLogger()"""
        val = __StdoutLogger()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def info(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.ai.StdoutLogger.info(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(__StdoutLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def info(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.ai.StdoutLogger.info(java.lang.String,java.lang.String)"""
        super(__StdoutLogger, self).info(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def debug(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.ai.StdoutLogger.debug(java.lang.String,java.lang.String)"""
        super(__StdoutLogger, self).debug(arg0, arg1)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.StdoutLogger()"""
        val = __StdoutLogger()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def error(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.ai.StdoutLogger.error(java.lang.String,java.lang.String)"""
        super(__StdoutLogger, self).error(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.Logger
import com.badlogic.gdx.ai.Logger as __Logger
__Logger = __Logger
import java.lang.Throwable as Throwable
from abc import abstractmethod, ABC
 
class Logger(ABC):
    """com.badlogic.gdx.ai.Logger"""
 
    @staticmethod
    def __wrap(java_value: __Logger) -> 'Logger':
        return Logger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Logger):
        """
        Dynamic initializer for Logger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.ai.GdxFileSystem
from pyquantum_helper import import_once as __import_once__
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

import com.badlogic.gdx.files.FileHandle as __FileHandle
__FileHandle = __FileHandle
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.File as File
try:
    from pygdx.assets import loaders
except ImportError:
    loaders = __import_once__("pygdx.assets.loaders")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.ai.GdxFileSystem as __GdxFileSystem
__GdxFileSystem = __GdxFileSystem
import com.badlogic.gdx.assets.loaders.FileHandleResolver as __FileHandleResolver
__FileHandleResolver = __FileHandleResolver
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GdxFileSystem():
    """com.badlogic.gdx.ai.GdxFileSystem"""
 
    @staticmethod
    def __wrap(java_value: __GdxFileSystem) -> 'GdxFileSystem':
        return GdxFileSystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GdxFileSystem):
        """
        Dynamic initializer for GdxFileSystem.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def newFileHandle(self, arg0: 'File') -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.GdxFileSystem.newFileHandle(java.io.File)"""
        return 'files.FileHandle'.__wrap(super(__GdxFileSystem, self).newFileHandle(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.GdxFileSystem()"""
        val = __GdxFileSystem()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def newFileHandle(self, arg0: 'File', arg1: 'FileType') -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.GdxFileSystem.newFileHandle(java.io.File,com.badlogic.gdx.Files$FileType)"""
        return 'files.FileHandle'.__wrap(super(__GdxFileSystem, self).newFileHandle(arg0, arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.GdxFileSystem()"""
        val = __GdxFileSystem()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def newFileHandle(self, arg0: str, arg1: 'FileType') -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.GdxFileSystem.newFileHandle(java.lang.String,com.badlogic.gdx.Files$FileType)"""
        return 'files.FileHandle'.__wrap(super(__GdxFileSystem, self).newFileHandle(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def newFileHandle(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.GdxFileSystem.newFileHandle(java.lang.String)"""
        return 'files.FileHandle'.__wrap(super(__GdxFileSystem, self).newFileHandle(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def newResolver(self, arg0: 'FileType') -> 'loaders.FileHandleResolver':
        """public com.badlogic.gdx.assets.loaders.FileHandleResolver com.badlogic.gdx.ai.GdxFileSystem.newResolver(com.badlogic.gdx.Files$FileType)"""
        return 'loaders.FileHandleResolver'.__wrap(super(__GdxFileSystem, self).newResolver(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.StandaloneFileSystem$DesktopFileHandle
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
import java.io.Writer as __Writer
__Writer = __Writer
from builtins import type
import java.io.File as File
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import java.io.BufferedReader as __BufferedReader
__BufferedReader = __BufferedReader
import com.badlogic.gdx.ai.StandaloneFileSystem as __StandaloneFileSystem_DesktopFileHandle
__DesktopFileHandle = __StandaloneFileSystem_DesktopFileHandle.DesktopFileHandle
import java.lang.Class as __Class
__Class = __Class
import java.io.File as __File
__File = __File
import java.io.OutputStream as OutputStream
import java.lang.String as __string
import java.io.FilenameFilter as FilenameFilter
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

from builtins import bool
import java.io.BufferedInputStream as __BufferedInputStream
__BufferedInputStream = __BufferedInputStream
import com.badlogic.gdx.files.FileHandle as __FileHandle
__FileHandle = __FileHandle
from builtins import str
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

import java.nio.channels.FileChannel.MapMode as MapMode
import java.io.OutputStream as __OutputStream
__OutputStream = __OutputStream
from pyquantum_helper import override
import java.lang.Object as __object
import java.io.FileFilter as FileFilter
import com.badlogic.gdx.Files as __Files_FileType
__FileType = __Files_FileType.FileType
import java.io.InputStream as __InputStream
__InputStream = __InputStream
from typing import List
import java.io.Reader as __Reader
__Reader = __Reader
import java.io.BufferedReader as BufferedReader
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.io.BufferedInputStream as BufferedInputStream
import java.io.Reader as Reader
import java.io.Writer as Writer
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.nio.ByteBuffer as ByteBuffer
import java.lang.Integer as __int
from builtins import int
 
class DesktopFileHandle():
    """com.badlogic.gdx.ai.StandaloneFileSystem.DesktopFileHandle"""
 
    @staticmethod
    def __wrap(java_value: __DesktopFileHandle) -> 'DesktopFileHandle':
        return DesktopFileHandle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DesktopFileHandle):
        """
        Dynamic initializer for DesktopFileHandle.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def writer(self, arg0: bool) -> 'Writer':
        """public java.io.Writer com.badlogic.gdx.files.FileHandle.writer(boolean)"""
        return 'Writer'.__wrap(super(__files.FileHandle, self).writer(__boolean.valueOf(arg0)))

    @overload
    def read(self, arg0: int) -> 'BufferedInputStream':
        """public java.io.BufferedInputStream com.badlogic.gdx.files.FileHandle.read(int)"""
        return 'BufferedInputStream'.__wrap(super(__files.FileHandle, self).read(__int.valueOf(arg0)))

    @override
    @overload
    def read(self) -> 'InputStream':
        """public java.io.InputStream com.badlogic.gdx.files.FileHandle.read()"""
        return 'InputStream'.__wrap(super(files.FileHandle, self).read())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isDirectory(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.isDirectory()"""
        return bool.__wrap(super(files.FileHandle, self).isDirectory())

    @override
    @overload
    def deleteDirectory(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.deleteDirectory()"""
        return bool.__wrap(super(files.FileHandle, self).deleteDirectory())

    @override
    @overload
    def moveTo(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.files.FileHandle.moveTo(com.badlogic.gdx.files.FileHandle)"""
        super(__files.FileHandle, self).moveTo(arg0)

    @override
    @overload
    def readString(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.readString()"""
        return str.__wrap(super(files.FileHandle, self).readString())

    @override
    @overload
    def type(self) -> 'pygdx.Files$FileType':
        """public com.badlogic.gdx.Files$FileType com.badlogic.gdx.files.FileHandle.type()"""
        return 'pygdx.Files$FileType'.__wrap(super(files.FileHandle, self).type())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def writeString(self, arg0: str, arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeString(java.lang.String,boolean)"""
        super(__files.FileHandle, self).writeString(arg0, __boolean.valueOf(arg1))

    @override
    @overload
    def file(self) -> 'File':
        """public java.io.File com.badlogic.gdx.ai.StandaloneFileSystem$DesktopFileHandle.file()"""
        return 'File'.__wrap(super(DesktopFileHandle, self).file())

    @overload
    def map(self, arg0: 'MapMode') -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.files.FileHandle.map(java.nio.channels.FileChannel$MapMode)"""
        return 'ByteBuffer'.__wrap(super(__files.FileHandle, self).map(arg0))

    @overload
    def reader(self, arg0: str) -> 'Reader':
        """public java.io.Reader com.badlogic.gdx.files.FileHandle.reader(java.lang.String)"""
        return 'Reader'.__wrap(super(__files.FileHandle, self).reader(arg0))

    @override
    @overload
    def extension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.extension()"""
        return str.__wrap(super(files.FileHandle, self).extension())

    @overload
    def write(self, arg0: bool) -> 'OutputStream':
        """public java.io.OutputStream com.badlogic.gdx.files.FileHandle.write(boolean)"""
        return 'OutputStream'.__wrap(super(__files.FileHandle, self).write(__boolean.valueOf(arg0)))

    @overload
    def reader(self, arg0: int) -> 'BufferedReader':
        """public java.io.BufferedReader com.badlogic.gdx.files.FileHandle.reader(int)"""
        return 'BufferedReader'.__wrap(super(__files.FileHandle, self).reader(__int.valueOf(arg0)))

    @overload
    def list(self, arg0: str) -> List['files.FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.lang.String)"""
        return List['files.FileHandle'].__wrap(super(__files.FileHandle, self).list(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.files.FileHandle.hashCode()"""
        return int.__wrap(super(files.FileHandle, self).hashCode())

    @override
    @overload
    def writeString(self, arg0: str, arg1: bool, arg2: str):
        """public void com.badlogic.gdx.files.FileHandle.writeString(java.lang.String,boolean,java.lang.String)"""
        super(__files.FileHandle, self).writeString(arg0, __boolean.valueOf(arg1), arg2)

    @overload
    def child(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.StandaloneFileSystem$DesktopFileHandle.child(java.lang.String)"""
        return 'files.FileHandle'.__wrap(super(__DesktopFileHandle, self).child(arg0))

    @override
    @overload
    def emptyDirectory(self, arg0: bool):
        """public void com.badlogic.gdx.files.FileHandle.emptyDirectory(boolean)"""
        super(__files.FileHandle, self).emptyDirectory(__boolean.valueOf(arg0))

    @overload
    def writer(self, arg0: bool, arg1: str) -> 'Writer':
        """public java.io.Writer com.badlogic.gdx.files.FileHandle.writer(boolean,java.lang.String)"""
        return 'Writer'.__wrap(super(__files.FileHandle, self).writer(__boolean.valueOf(arg0), arg1))

    @override
    @overload
    def parent(self) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.StandaloneFileSystem$DesktopFileHandle.parent()"""
        return 'files.FileHandle'.__wrap(super(DesktopFileHandle, self).parent())

    @overload
    def readBytes(self, arg0: bytes, arg1: int, arg2: int) -> int:
        """public int com.badlogic.gdx.files.FileHandle.readBytes(byte[],int,int)"""
        return int.__wrap(super(__files.FileHandle, self).readBytes(bytes, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def reader(self, arg0: int, arg1: str) -> 'BufferedReader':
        """public java.io.BufferedReader com.badlogic.gdx.files.FileHandle.reader(int,java.lang.String)"""
        return 'BufferedReader'.__wrap(super(__files.FileHandle, self).reader(__int.valueOf(arg0), arg1))

    @staticmethod
    @overload
    def tempFile(arg0: str) -> 'files.FileHandle':
        """public static com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.tempFile(java.lang.String)"""
        return files.FileHandle.__wrap(__FileHandle.tempFile(arg0))

    @override
    @overload
    def pathWithoutExtension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.pathWithoutExtension()"""
        return str.__wrap(super(files.FileHandle, self).pathWithoutExtension())

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
    def write(self, arg0: 'InputStream', arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.write(java.io.InputStream,boolean)"""
        super(__files.FileHandle, self).write(arg0, __boolean.valueOf(arg1))

    @override
    @overload
    def lastModified(self) -> int:
        """public long com.badlogic.gdx.files.FileHandle.lastModified()"""
        return int.__wrap(super(files.FileHandle, self).lastModified())

    @override
    @overload
    def name(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.name()"""
        return str.__wrap(super(files.FileHandle, self).name())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def sibling(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.StandaloneFileSystem$DesktopFileHandle.sibling(java.lang.String)"""
        return 'files.FileHandle'.__wrap(super(__DesktopFileHandle, self).sibling(arg0))

    @override
    @overload
    def writeBytes(self, arg0: bytes, arg1: int, arg2: int, arg3: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeBytes(byte[],int,int,boolean)"""
        super(__files.FileHandle, self).writeBytes(bytes, __int.valueOf(arg1), __int.valueOf(arg2), __boolean.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def nameWithoutExtension(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.nameWithoutExtension()"""
        return str.__wrap(super(files.FileHandle, self).nameWithoutExtension())

    @override
    @overload
    def delete(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.delete()"""
        return bool.__wrap(super(files.FileHandle, self).delete())

    @overload
    def readString(self, arg0: str) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.readString(java.lang.String)"""
        return str.__wrap(super(__files.FileHandle, self).readString(arg0))

    @override
    @overload
    def readBytes(self) -> List[int]:
        """public byte[] com.badlogic.gdx.files.FileHandle.readBytes()"""
        return List[int].__wrap(super(files.FileHandle, self).readBytes())

    @overload
    def __init__(self, arg0: 'File', arg1: 'FileType'):
        """public com.badlogic.gdx.ai.StandaloneFileSystem$DesktopFileHandle(java.io.File,com.badlogic.gdx.Files$FileType)"""
        val = __DesktopFileHandle(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: 'FileType'):
        """public com.badlogic.gdx.ai.StandaloneFileSystem$DesktopFileHandle(java.lang.String,com.badlogic.gdx.Files$FileType)"""
        val = __DesktopFileHandle(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def tempDirectory(arg0: str) -> 'files.FileHandle':
        """public static com.badlogic.gdx.files.FileHandle com.badlogic.gdx.files.FileHandle.tempDirectory(java.lang.String)"""
        return files.FileHandle.__wrap(__FileHandle.tempDirectory(arg0))

    @override
    @overload
    def map(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.files.FileHandle.map()"""
        return 'ByteBuffer'.__wrap(super(files.FileHandle, self).map())

    @override
    @overload
    def length(self) -> int:
        """public long com.badlogic.gdx.files.FileHandle.length()"""
        return int.__wrap(super(files.FileHandle, self).length())

    @overload
    def list(self, arg0: 'FileFilter') -> List['files.FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.io.FileFilter)"""
        return List['files.FileHandle'].__wrap(super(__files.FileHandle, self).list(arg0))

    @overload
    def write(self, arg0: bool, arg1: int) -> 'OutputStream':
        """public java.io.OutputStream com.badlogic.gdx.files.FileHandle.write(boolean,int)"""
        return 'OutputStream'.__wrap(super(__files.FileHandle, self).write(__boolean.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def list(self) -> List['files.FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list()"""
        return List['files.FileHandle'].__wrap(super(files.FileHandle, self).list())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.toString()"""
        return str.__wrap(super(files.FileHandle, self).toString())

    @overload
    def list(self, arg0: 'FilenameFilter') -> List['files.FileHandle']:
        """public com.badlogic.gdx.files.FileHandle[] com.badlogic.gdx.files.FileHandle.list(java.io.FilenameFilter)"""
        return List['files.FileHandle'].__wrap(super(__files.FileHandle, self).list(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.equals(java.lang.Object)"""
        return bool.__wrap(super(__files.FileHandle, self).equals(arg0))

    @override
    @overload
    def writeBytes(self, arg0: bytes, arg1: bool):
        """public void com.badlogic.gdx.files.FileHandle.writeBytes(byte[],boolean)"""
        super(__files.FileHandle, self).writeBytes(bytes, __boolean.valueOf(arg1))

    @override
    @overload
    def reader(self) -> 'Reader':
        """public java.io.Reader com.badlogic.gdx.files.FileHandle.reader()"""
        return 'Reader'.__wrap(super(files.FileHandle, self).reader())

    @override
    @overload
    def path(self) -> str:
        """public java.lang.String com.badlogic.gdx.files.FileHandle.path()"""
        return str.__wrap(super(files.FileHandle, self).path())

    @override
    @overload
    def exists(self) -> bool:
        """public boolean com.badlogic.gdx.files.FileHandle.exists()"""
        return bool.__wrap(super(files.FileHandle, self).exists())

    @override
    @overload
    def copyTo(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.files.FileHandle.copyTo(com.badlogic.gdx.files.FileHandle)"""
        super(__files.FileHandle, self).copyTo(arg0) 
 
 
# CLASS: com.badlogic.gdx.ai.GdxLogger
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.ai.GdxLogger as __GdxLogger
__GdxLogger = __GdxLogger
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GdxLogger():
    """com.badlogic.gdx.ai.GdxLogger"""
 
    @staticmethod
    def __wrap(java_value: __GdxLogger) -> 'GdxLogger':
        return GdxLogger(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GdxLogger):
        """
        Dynamic initializer for GdxLogger.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def error(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.ai.GdxLogger.error(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(__GdxLogger, self).error(arg0, arg1, arg2)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def info(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.ai.GdxLogger.info(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(__GdxLogger, self).info(arg0, arg1, arg2)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def debug(self, arg0: str, arg1: str, arg2: 'Throwable'):
        """public void com.badlogic.gdx.ai.GdxLogger.debug(java.lang.String,java.lang.String,java.lang.Throwable)"""
        super(__GdxLogger, self).debug(arg0, arg1, arg2)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.GdxLogger()"""
        val = __GdxLogger()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def debug(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.ai.GdxLogger.debug(java.lang.String,java.lang.String)"""
        super(__GdxLogger, self).debug(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.GdxLogger()"""
        val = __GdxLogger()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def info(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.ai.GdxLogger.info(java.lang.String,java.lang.String)"""
        super(__GdxLogger, self).info(arg0, arg1)

    @override
    @overload
    def error(self, arg0: str, arg1: str):
        """public void com.badlogic.gdx.ai.GdxLogger.error(java.lang.String,java.lang.String)"""
        super(__GdxLogger, self).error(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.ai.Timepiece
import com.badlogic.gdx.ai.Timepiece as __Timepiece
__Timepiece = __Timepiece
from abc import abstractmethod, ABC
 
class Timepiece(ABC):
    """com.badlogic.gdx.ai.Timepiece"""
 
    @staticmethod
    def __wrap(java_value: __Timepiece) -> 'Timepiece':
        return Timepiece(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Timepiece):
        """
        Dynamic initializer for Timepiece.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.ai.StandaloneFileSystem
from pyquantum_helper import import_once as __import_once__
try:
    import pygdx
except ImportError:
    pygdx = __import_once__("pygdx")

import com.badlogic.gdx.files.FileHandle as __FileHandle
__FileHandle = __FileHandle
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.File as File
try:
    from pygdx.assets import loaders
except ImportError:
    loaders = __import_once__("pygdx.assets.loaders")

import com.badlogic.gdx.ai.StandaloneFileSystem as __StandaloneFileSystem
__StandaloneFileSystem = __StandaloneFileSystem
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.assets.loaders.FileHandleResolver as __FileHandleResolver
__FileHandleResolver = __FileHandleResolver
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class StandaloneFileSystem():
    """com.badlogic.gdx.ai.StandaloneFileSystem"""
 
    @staticmethod
    def __wrap(java_value: __StandaloneFileSystem) -> 'StandaloneFileSystem':
        return StandaloneFileSystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __StandaloneFileSystem):
        """
        Dynamic initializer for StandaloneFileSystem.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def newFileHandle(self, arg0: str, arg1: 'FileType') -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.StandaloneFileSystem.newFileHandle(java.lang.String,com.badlogic.gdx.Files$FileType)"""
        return 'files.FileHandle'.__wrap(super(__StandaloneFileSystem, self).newFileHandle(arg0, arg1))

    @overload
    def newFileHandle(self, arg0: 'File') -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.StandaloneFileSystem.newFileHandle(java.io.File)"""
        return 'files.FileHandle'.__wrap(super(__StandaloneFileSystem, self).newFileHandle(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.ai.StandaloneFileSystem()"""
        val = __StandaloneFileSystem()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def newFileHandle(self, arg0: 'File', arg1: 'FileType') -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.StandaloneFileSystem.newFileHandle(java.io.File,com.badlogic.gdx.Files$FileType)"""
        return 'files.FileHandle'.__wrap(super(__StandaloneFileSystem, self).newFileHandle(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def newResolver(self, arg0: 'FileType') -> 'loaders.FileHandleResolver':
        """public com.badlogic.gdx.assets.loaders.FileHandleResolver com.badlogic.gdx.ai.StandaloneFileSystem.newResolver(com.badlogic.gdx.Files$FileType)"""
        return 'loaders.FileHandleResolver'.__wrap(super(__StandaloneFileSystem, self).newResolver(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.ai.StandaloneFileSystem()"""
        val = __StandaloneFileSystem()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def newFileHandle(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.ai.StandaloneFileSystem.newFileHandle(java.lang.String)"""
        return 'files.FileHandle'.__wrap(super(__StandaloneFileSystem, self).newFileHandle(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))