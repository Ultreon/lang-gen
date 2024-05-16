from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ApplicationAdapter as __ApplicationAdapter
__ApplicationAdapter = __ApplicationAdapter
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.tools.ktx.KTXProcessor as __KTXProcessor_KTXProcessorListener
__KTXProcessorListener = __KTXProcessor_KTXProcessorListener.KTXProcessorListener
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class KTXProcessorListener():
    """com.badlogic.gdx.tools.ktx.KTXProcessor.KTXProcessorListener"""
 
    @staticmethod
    def __wrap(java_value: __KTXProcessorListener) -> 'KTXProcessorListener':
        return KTXProcessorListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __KTXProcessorListener):
        """
        Dynamic initializer for KTXProcessorListener.
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

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.ApplicationAdapter.dispose()"""
        super(pygdx.ApplicationAdapter, self).dispose()

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
    def render(self):
        """public void com.badlogic.gdx.ApplicationAdapter.render()"""
        super(pygdx.ApplicationAdapter, self).render()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.ApplicationAdapter.resize(int,int)"""
        super(__pygdx.ApplicationAdapter, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

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
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.tools.ktx.KTXProcessor$KTXProcessorListener
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.ApplicationAdapter as __ApplicationAdapter
__ApplicationAdapter = __ApplicationAdapter
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.tools.ktx.KTXProcessor as __KTXProcessor_KTXProcessorListener
__KTXProcessorListener = __KTXProcessor_KTXProcessorListener.KTXProcessorListener
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class KTXProcessorListener():
    """com.badlogic.gdx.tools.ktx.KTXProcessor.KTXProcessorListener"""
 
    @staticmethod
    def __wrap(java_value: __KTXProcessorListener) -> 'KTXProcessorListener':
        return KTXProcessorListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __KTXProcessorListener):
        """
        Dynamic initializer for KTXProcessorListener.
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

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.ApplicationAdapter.dispose()"""
        super(pygdx.ApplicationAdapter, self).dispose()

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
    def render(self):
        """public void com.badlogic.gdx.ApplicationAdapter.render()"""
        super(pygdx.ApplicationAdapter, self).render()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.ApplicationAdapter.resize(int,int)"""
        super(__pygdx.ApplicationAdapter, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

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
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.tools.ktx.KTXProcessor$KTXProcessorListener 
 
 
# CLASS: com.badlogic.gdx.tools.ktx.KTXProcessor
from builtins import str
import java.lang.Boolean as __boolean
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
import com.badlogic.gdx.tools.ktx.KTXProcessor as __KTXProcessor
__KTXProcessor = __KTXProcessor
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class KTXProcessor():
    """com.badlogic.gdx.tools.ktx.KTXProcessor"""
 
    @staticmethod
    def __wrap(java_value: __KTXProcessor) -> 'KTXProcessor':
        return KTXProcessor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __KTXProcessor):
        """
        Dynamic initializer for KTXProcessor.
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
    def __init__(self, ):
        """public com.badlogic.gdx.tools.ktx.KTXProcessor()"""
        val = __KTXProcessor()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.ktx.KTXProcessor()"""
        val = __KTXProcessor()
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

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void com.badlogic.gdx.tools.ktx.KTXProcessor.main(java.lang.String[])"""
        __KTXProcessor.main(arg0)

    @staticmethod
    @overload
    def convert(arg0: str, arg1: str, arg2: bool, arg3: bool, arg4: bool):
        """public static void com.badlogic.gdx.tools.ktx.KTXProcessor.convert(java.lang.String,java.lang.String,boolean,boolean,boolean) throws java.lang.Exception"""
        __KTXProcessor.convert(arg0, arg1, __boolean.valueOf(arg2), __boolean.valueOf(arg3), __boolean.valueOf(arg4))

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

    @staticmethod
    @overload
    def convert(arg0: str, arg1: str, arg2: str, arg3: str, arg4: str, arg5: str, arg6: str, arg7: bool, arg8: bool, arg9: bool):
        """public static void com.badlogic.gdx.tools.ktx.KTXProcessor.convert(java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,java.lang.String,boolean,boolean,boolean) throws java.lang.Exception"""
        __KTXProcessor.convert(arg0, arg1, arg2, arg3, arg4, arg5, arg6, __boolean.valueOf(arg7), __boolean.valueOf(arg8), __boolean.valueOf(arg9))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))