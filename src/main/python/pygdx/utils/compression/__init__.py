from __future__ import annotations
from overload import overload


 
import com.badlogic.gdx.utils.compression.ICodeProgress as __ICodeProgress
__ICodeProgress = __ICodeProgress
from abc import abstractmethod, ABC
 
class ICodeProgress(ABC):
    """com.badlogic.gdx.utils.compression.ICodeProgress"""
 
    @staticmethod
    def __wrap(java_value: __ICodeProgress) -> 'ICodeProgress':
        return ICodeProgress(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ICodeProgress):
        """
        Dynamic initializer for ICodeProgress.
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
    def SetProgress(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.utils.compression.ICodeProgress.SetProgress(long,long)"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.utils.compression.ICodeProgress
import com.badlogic.gdx.utils.compression.ICodeProgress as __ICodeProgress
__ICodeProgress = __ICodeProgress
from abc import abstractmethod, ABC
 
class ICodeProgress(ABC):
    """com.badlogic.gdx.utils.compression.ICodeProgress"""
 
    @staticmethod
    def __wrap(java_value: __ICodeProgress) -> 'ICodeProgress':
        return ICodeProgress(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ICodeProgress):
        """
        Dynamic initializer for ICodeProgress.
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
    def SetProgress(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.utils.compression.ICodeProgress.SetProgress(long,long)"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.utils.compression.ICodeProgress 
 
 
# CLASS: com.badlogic.gdx.utils.compression.Lzma
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.compression.Lzma as __Lzma
__Lzma = __Lzma
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __String
__String = __String
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Lzma():
    """com.badlogic.gdx.utils.compression.Lzma"""
 
    @staticmethod
    def __wrap(java_value: __Lzma) -> 'Lzma':
        return Lzma(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Lzma):
        """
        Dynamic initializer for Lzma.
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

    @staticmethod
    @overload
    def compress(arg0: 'InputStream', arg1: 'OutputStream'):
        """public static void com.badlogic.gdx.utils.compression.Lzma.compress(java.io.InputStream,java.io.OutputStream) throws java.io.IOException"""
        __Lzma.compress(arg0, arg1)

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.compression.Lzma()"""
        val = __Lzma()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.compression.Lzma()"""
        val = __Lzma()
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

    @staticmethod
    @overload
    def decompress(arg0: 'InputStream', arg1: 'OutputStream'):
        """public static void com.badlogic.gdx.utils.compression.Lzma.decompress(java.io.InputStream,java.io.OutputStream) throws java.io.IOException"""
        __Lzma.decompress(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.compression.CRC
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import com.badlogic.gdx.utils.compression.CRC as __CRC
__CRC = __CRC
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CRC():
    """com.badlogic.gdx.utils.compression.CRC"""
 
    @staticmethod
    def __wrap(java_value: __CRC) -> 'CRC':
        return CRC(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CRC):
        """
        Dynamic initializer for CRC.
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
    def GetDigest(self) -> int:
        """public int com.badlogic.gdx.utils.compression.CRC.GetDigest()"""
        return int.__wrap(super(CRC, self).GetDigest())

    @overload
    def Update(self, arg0: bytes, arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.compression.CRC.Update(byte[],int,int)"""
        super(__CRC, self).Update(bytes, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.compression.CRC()"""
        val = __CRC()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def UpdateByte(self, arg0: int):
        """public void com.badlogic.gdx.utils.compression.CRC.UpdateByte(int)"""
        super(__CRC, self).UpdateByte(__int.valueOf(arg0))

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
    def Init(self):
        """public void com.badlogic.gdx.utils.compression.CRC.Init()"""
        super(CRC, self).Init()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.compression.CRC()"""
        val = __CRC()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def Update(self, arg0: bytes):
        """public void com.badlogic.gdx.utils.compression.CRC.Update(byte[])"""
        super(__CRC, self).Update(bytes)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))