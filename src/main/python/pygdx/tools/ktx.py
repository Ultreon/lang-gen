from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.tools.ktx.KTXProcessor as _KTXProcessor_KTXProcessorListener
_KTXProcessorListener = _KTXProcessor_KTXProcessorListener.KTXProcessorListener
import com.badlogic.gdx.ApplicationAdapter as _ApplicationAdapter
_ApplicationAdapter = _ApplicationAdapter
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class KTXProcessorListener():
    """com.badlogic.gdx.tools.ktx.KTXProcessor.KTXProcessorListener"""
 
    @staticmethod
    def _wrap(java_value: _KTXProcessorListener) -> 'KTXProcessorListener':
        return KTXProcessorListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _KTXProcessorListener):
        """
        Dynamic initializer for KTXProcessorListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_KTXProcessorListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_KTXProcessorListener__wrapper":
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
    def resize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.ApplicationAdapter.resize(int,int)"""
        super(_pygdx.ApplicationAdapter, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.ApplicationAdapter.dispose()"""
        super(pygdx.ApplicationAdapter, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def create(self):
        """public void com.badlogic.gdx.tools.ktx.KTXProcessor$KTXProcessorListener.create()"""
        super(KTXProcessorListener, self).create()

    @override
    @overload
    def resume(self):
        """public void com.badlogic.gdx.ApplicationAdapter.resume()"""
        super(pygdx.ApplicationAdapter, self).resume()

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
    def render(self):
        """public void com.badlogic.gdx.ApplicationAdapter.render()"""
        super(pygdx.ApplicationAdapter, self).render()

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
    def pause(self):
        """public void com.badlogic.gdx.ApplicationAdapter.pause()"""
        super(pygdx.ApplicationAdapter, self).pause()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.tools.ktx.KTXProcessor$KTXProcessorListener
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.tools.ktx.KTXProcessor as _KTXProcessor_KTXProcessorListener
_KTXProcessorListener = _KTXProcessor_KTXProcessorListener.KTXProcessorListener
import com.badlogic.gdx.ApplicationAdapter as _ApplicationAdapter
_ApplicationAdapter = _ApplicationAdapter
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class KTXProcessorListener():
    """com.badlogic.gdx.tools.ktx.KTXProcessor.KTXProcessorListener"""
 
    @staticmethod
    def _wrap(java_value: _KTXProcessorListener) -> 'KTXProcessorListener':
        return KTXProcessorListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _KTXProcessorListener):
        """
        Dynamic initializer for KTXProcessorListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_KTXProcessorListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_KTXProcessorListener__wrapper":
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
    def resize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.ApplicationAdapter.resize(int,int)"""
        super(_pygdx.ApplicationAdapter, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.ApplicationAdapter.dispose()"""
        super(pygdx.ApplicationAdapter, self).dispose()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def create(self):
        """public void com.badlogic.gdx.tools.ktx.KTXProcessor$KTXProcessorListener.create()"""
        super(KTXProcessorListener, self).create()

    @override
    @overload
    def resume(self):
        """public void com.badlogic.gdx.ApplicationAdapter.resume()"""
        super(pygdx.ApplicationAdapter, self).resume()

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
    def render(self):
        """public void com.badlogic.gdx.ApplicationAdapter.render()"""
        super(pygdx.ApplicationAdapter, self).render()

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
    def pause(self):
        """public void com.badlogic.gdx.ApplicationAdapter.pause()"""
        super(pygdx.ApplicationAdapter, self).pause()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.tools.ktx.KTXProcessor$KTXProcessorListener 
 
 
# CLASS: com.badlogic.gdx.tools.ktx.KTXProcessor
from builtins import str
import com.badlogic.gdx.tools.ktx.KTXProcessor as _KTXProcessor
_KTXProcessor = _KTXProcessor
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class KTXProcessor():
    """com.badlogic.gdx.tools.ktx.KTXProcessor"""
 
    @staticmethod
    def _wrap(java_value: _KTXProcessor) -> 'KTXProcessor':
        return KTXProcessor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _KTXProcessor):
        """
        Dynamic initializer for KTXProcessor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_KTXProcessor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_KTXProcessor__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def convert(arg0: str, arg1: str, arg2: bool, arg3: bool, arg4: bool):
        """public static void com.badlogic.gdx.tools.ktx.KTXProcessor.convert(java.lang.String,java.lang.String,boolean,boolean,boolean) throws java.lang.Exception"""
        _KTXProcessor.convert(arg0, arg1, _boolean.valueOf(arg2), _boolean.valueOf(arg3), _boolean.valueOf(arg4))

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

    @staticmethod
    @overload
    def convert(arg0: str, arg1: str, arg2: str, arg3: str, arg4: str, arg5: str, arg6: str, arg7: bool, arg8: bool, arg9: bool):
        """public static void com.badlogic.gdx.tools.ktx.KTXProcessor.convert(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,boolean,boolean,boolean) throws java.lang.Exception"""
        _KTXProcessor.convert(arg0, arg1, arg2, arg3, arg4, arg5, arg6, _boolean.valueOf(arg7), _boolean.valueOf(arg8), _boolean.valueOf(arg9))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void com.badlogic.gdx.tools.ktx.KTXProcessor.main(java.lang.String[])"""
        _KTXProcessor.main(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.ktx.KTXProcessor()"""
        val = _KTXProcessor()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.ktx.KTXProcessor()"""
        val = _KTXProcessor()
        self.__wrapper = val

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