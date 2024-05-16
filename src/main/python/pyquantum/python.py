from __future__ import annotations
from overload import overload


 
import org.graalvm.polyglot.Context as Context
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.graalvm.polyglot.Context as __Context
__Context = __Context
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.python.PyLang as __PyLang
__PyLang = __PyLang
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PyLang():
    """dev.ultreon.quantum.python.PyLang"""
 
    @staticmethod
    def __wrap(java_value: __PyLang) -> 'PyLang':
        return PyLang(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PyLang):
        """
        Dynamic initializer for PyLang.
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
    def __init__(self):
        """public dev.ultreon.quantum.python.PyLang()"""
        val = __PyLang()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.python.PyLang()"""
        val = __PyLang()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def getContext() -> 'Context':
        """public static org.graalvm.polyglot.Context dev.ultreon.quantum.python.PyLang.getContext()"""
        return Context.__wrap(__PyLang.getContext())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def init(self):
        """public void dev.ultreon.quantum.python.PyLang.init()"""
        super(PyLang, self).init()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.python.PyLang
import org.graalvm.polyglot.Context as Context
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.graalvm.polyglot.Context as __Context
__Context = __Context
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.python.PyLang as __PyLang
__PyLang = __PyLang
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PyLang():
    """dev.ultreon.quantum.python.PyLang"""
 
    @staticmethod
    def __wrap(java_value: __PyLang) -> 'PyLang':
        return PyLang(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PyLang):
        """
        Dynamic initializer for PyLang.
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
    def __init__(self):
        """public dev.ultreon.quantum.python.PyLang()"""
        val = __PyLang()
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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.python.PyLang()"""
        val = __PyLang()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def getContext() -> 'Context':
        """public static org.graalvm.polyglot.Context dev.ultreon.quantum.python.PyLang.getContext()"""
        return Context.__wrap(__PyLang.getContext())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def init(self):
        """public void dev.ultreon.quantum.python.PyLang.init()"""
        super(PyLang, self).init()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.python.PyLang 
 
 
# CLASS: dev.ultreon.quantum.python.PyAdditionalMixins
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import dev.ultreon.quantum.python.PyAdditionalMixins as __PyAdditionalMixins
__PyAdditionalMixins = __PyAdditionalMixins
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PyAdditionalMixins():
    """dev.ultreon.quantum.python.PyAdditionalMixins"""
 
    @staticmethod
    def __wrap(java_value: __PyAdditionalMixins) -> 'PyAdditionalMixins':
        return PyAdditionalMixins(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PyAdditionalMixins):
        """
        Dynamic initializer for PyAdditionalMixins.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.python.PyAdditionalMixins()"""
        val = __PyAdditionalMixins()
        self.__dict__ = val.__dict__
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
    def __init__(self):
        """public dev.ultreon.quantum.python.PyAdditionalMixins()"""
        val = __PyAdditionalMixins()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.python.PyLoader
import org.graalvm.polyglot.Context as Context
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Runnable as Runnable
import java.nio.file.Path as Path
import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.python.PyLoader as __PyLoader
__PyLoader = __PyLoader
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PyLoader():
    """dev.ultreon.quantum.python.PyLoader"""
 
    @staticmethod
    def __wrap(java_value: __PyLoader) -> 'PyLoader':
        return PyLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PyLoader):
        """
        Dynamic initializer for PyLoader.
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

    @overload
    def init(self, arg0: 'Path', arg1: 'Context'):
        """public void dev.ultreon.quantum.python.PyLoader.init(java.nio.file.Path,org.graalvm.polyglot.Context) throws java.io.IOException"""
        super(__PyLoader, self).init(arg0, arg1)

    @overload
    def close(self):
        """public void dev.ultreon.quantum.python.PyLoader.close()"""
        super(PyLoader, self).close()

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
    def __init__(self, ):
        """public dev.ultreon.quantum.python.PyLoader()"""
        val = __PyLoader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def initMods(self):
        """public void dev.ultreon.quantum.python.PyLoader.initMods()"""
        super(PyLoader, self).initMods()

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
    def register(self, arg0: str, arg1: 'Runnable'):
        """public void dev.ultreon.quantum.python.PyLoader.register(java.lang.String,java.lang.Runnable)"""
        super(__PyLoader, self).register(arg0, arg1)

    @staticmethod
    @overload
    def getInstance() -> 'PyLoader':
        """public static dev.ultreon.quantum.python.PyLoader dev.ultreon.quantum.python.PyLoader.getInstance()"""
        return PyLoader.__wrap(__PyLoader.getInstance())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getMods(self) -> 'Collection':
        """public java.util.Collection<dev.ultreon.quantum.python.PyMod> dev.ultreon.quantum.python.PyLoader.getMods()"""
        return 'Collection'.__wrap(super(PyLoader, self).getMods())

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
    def __init__(self):
        """public dev.ultreon.quantum.python.PyLoader()"""
        val = __PyLoader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.python.PyMod
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.nio.file.Path as __Path
__Path = __Path
from builtins import type
import java.nio.file.Path as Path
import dev.ultreon.quantum.python.PyMod as __PyMod
__PyMod = __PyMod
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PyMod():
    """dev.ultreon.quantum.python.PyMod"""
 
    @staticmethod
    def __wrap(java_value: __PyMod) -> 'PyMod':
        return PyMod(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PyMod):
        """
        Dynamic initializer for PyMod.
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

    @overload
    def name(self) -> str:
        """public java.lang.String dev.ultreon.quantum.python.PyMod.name()"""
        return str.__wrap(super(PyMod, self).name())

    @overload
    def setPath(self, arg0: 'Path'):
        """public void dev.ultreon.quantum.python.PyMod.setPath(java.nio.file.Path)"""
        super(__PyMod, self).setPath(arg0)

    @overload
    def author(self) -> str:
        """public java.lang.String dev.ultreon.quantum.python.PyMod.author()"""
        return str.__wrap(super(PyMod, self).author())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.python.PyMod.equals(java.lang.Object)"""
        return bool.__wrap(super(__PyMod, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def description(self) -> str:
        """public java.lang.String dev.ultreon.quantum.python.PyMod.description()"""
        return str.__wrap(super(PyMod, self).description())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.python.PyMod.toString()"""
        return str.__wrap(super(PyMod, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def version(self) -> str:
        """public java.lang.String dev.ultreon.quantum.python.PyMod.version()"""
        return str.__wrap(super(PyMod, self).version())

    @overload
    def id(self) -> str:
        """public java.lang.String dev.ultreon.quantum.python.PyMod.id()"""
        return str.__wrap(super(PyMod, self).id())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: str):
        """public dev.ultreon.quantum.python.PyMod(java.lang.String)"""
        val = __PyMod(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getPath(self) -> 'Path':
        """public java.nio.file.Path dev.ultreon.quantum.python.PyMod.getPath()"""
        return 'Path'.__wrap(super(PyMod, self).getPath())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.python.PyMod.hashCode()"""
        return int.__wrap(super(PyMod, self).hashCode())