from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.compression.lzma.Decoder as __Decoder
__Decoder = __Decoder
import java.io.OutputStream as OutputStream
import java.lang.String as __String
__String = __String
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Decoder():
    """com.badlogic.gdx.utils.compression.lzma.Decoder"""
 
    @staticmethod
    def __wrap(java_value: __Decoder) -> 'Decoder':
        return Decoder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Decoder):
        """
        Dynamic initializer for Decoder.
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
    def __init__(self):
        """public com.badlogic.gdx.utils.compression.lzma.Decoder()"""
        val = __Decoder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def SetDecoderProperties(self, arg0: bytes) -> bool:
        """public boolean com.badlogic.gdx.utils.compression.lzma.Decoder.SetDecoderProperties(byte[])"""
        return bool.__wrap(super(__Decoder, self).SetDecoderProperties(bytes))

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def Code(self, arg0: 'InputStream', arg1: 'OutputStream', arg2: int) -> bool:
        """public boolean com.badlogic.gdx.utils.compression.lzma.Decoder.Code(java.io.InputStream,java.io.OutputStream,long) throws java.io.IOException"""
        return bool.__wrap(super(__Decoder, self).Code(arg0, arg1, __long.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.compression.lzma.Decoder()"""
        val = __Decoder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.utils.compression.lzma.Decoder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.compression.lzma.Decoder as __Decoder
__Decoder = __Decoder
import java.io.OutputStream as OutputStream
import java.lang.String as __String
__String = __String
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Decoder():
    """com.badlogic.gdx.utils.compression.lzma.Decoder"""
 
    @staticmethod
    def __wrap(java_value: __Decoder) -> 'Decoder':
        return Decoder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Decoder):
        """
        Dynamic initializer for Decoder.
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
    def __init__(self):
        """public com.badlogic.gdx.utils.compression.lzma.Decoder()"""
        val = __Decoder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def SetDecoderProperties(self, arg0: bytes) -> bool:
        """public boolean com.badlogic.gdx.utils.compression.lzma.Decoder.SetDecoderProperties(byte[])"""
        return bool.__wrap(super(__Decoder, self).SetDecoderProperties(bytes))

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def Code(self, arg0: 'InputStream', arg1: 'OutputStream', arg2: int) -> bool:
        """public boolean com.badlogic.gdx.utils.compression.lzma.Decoder.Code(java.io.InputStream,java.io.OutputStream,long) throws java.io.IOException"""
        return bool.__wrap(super(__Decoder, self).Code(arg0, arg1, __long.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.compression.lzma.Decoder()"""
        val = __Decoder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.utils.compression.lzma.Decoder 
 
 
# CLASS: com.badlogic.gdx.utils.compression.lzma.Encoder
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pygdx.utils import compression
except ImportError:
    compression = __import_once__("pygdx.utils.compression")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __String
__String = __String
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.compression.lzma.Encoder as __Encoder
__Encoder = __Encoder
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Encoder():
    """com.badlogic.gdx.utils.compression.lzma.Encoder"""
 
    @staticmethod
    def __wrap(java_value: __Encoder) -> 'Encoder':
        return Encoder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Encoder):
        """
        Dynamic initializer for Encoder.
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
    def WriteCoderProperties(self, arg0: 'OutputStream'):
        """public void com.badlogic.gdx.utils.compression.lzma.Encoder.WriteCoderProperties(java.io.OutputStream) throws java.io.IOException"""
        super(__Encoder, self).WriteCoderProperties(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.compression.lzma.Encoder()"""
        val = __Encoder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def Code(self, arg0: 'InputStream', arg1: 'OutputStream', arg2: int, arg3: int, arg4: 'ICodeProgress'):
        """public void com.badlogic.gdx.utils.compression.lzma.Encoder.Code(java.io.InputStream,java.io.OutputStream,long,long,com.badlogic.gdx.utils.compression.ICodeProgress) throws java.io.IOException"""
        super(__Encoder, self).Code(arg0, arg1, __long.valueOf(arg2), __long.valueOf(arg3), arg4)

    @overload
    def SetAlgorithm(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.compression.lzma.Encoder.SetAlgorithm(int)"""
        return bool.__wrap(super(__Encoder, self).SetAlgorithm(__int.valueOf(arg0)))

    @overload
    def SetLcLpPb(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.utils.compression.lzma.Encoder.SetLcLpPb(int,int,int)"""
        return bool.__wrap(super(__Encoder, self).SetLcLpPb(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def CodeOneBlock(self, arg0: 'long', arg1: 'long', arg2: 'boolean'):
        """public void com.badlogic.gdx.utils.compression.lzma.Encoder.CodeOneBlock(long[],long[],boolean[]) throws java.io.IOException"""
        super(__Encoder, self).CodeOneBlock(arg0, arg1, arg2)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def SetNumFastBytes(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.compression.lzma.Encoder.SetNumFastBytes(int)"""
        return bool.__wrap(super(__Encoder, self).SetNumFastBytes(__int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def SetDictionarySize(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.compression.lzma.Encoder.SetDictionarySize(int)"""
        return bool.__wrap(super(__Encoder, self).SetDictionarySize(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def SetMatchFinder(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.compression.lzma.Encoder.SetMatchFinder(int)"""
        return bool.__wrap(super(__Encoder, self).SetMatchFinder(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.compression.lzma.Encoder()"""
        val = __Encoder()
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

    @overload
    def SetEndMarkerMode(self, arg0: bool):
        """public void com.badlogic.gdx.utils.compression.lzma.Encoder.SetEndMarkerMode(boolean)"""
        super(__Encoder, self).SetEndMarkerMode(__boolean.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.compression.lzma.Base
import com.badlogic.gdx.utils.compression.lzma.Base as __Base
__Base = __Base
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Base():
    """com.badlogic.gdx.utils.compression.lzma.Base"""
 
    @staticmethod
    def __wrap(java_value: __Base) -> 'Base':
        return Base(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Base):
        """
        Dynamic initializer for Base.
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
    def StateUpdateMatch(arg0: int) -> int:
        """public static final int com.badlogic.gdx.utils.compression.lzma.Base.StateUpdateMatch(int)"""
        return int.__wrap(__Base.StateUpdateMatch(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def StateInit() -> int:
        """public static final int com.badlogic.gdx.utils.compression.lzma.Base.StateInit()"""
        return int.__wrap(__Base.StateInit())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def GetLenToPosState(arg0: int) -> int:
        """public static final int com.badlogic.gdx.utils.compression.lzma.Base.GetLenToPosState(int)"""
        return int.__wrap(__Base.GetLenToPosState(__int.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.compression.lzma.Base()"""
        val = __Base()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def StateIsCharState(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.utils.compression.lzma.Base.StateIsCharState(int)"""
        return bool.__wrap(__Base.StateIsCharState(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def StateUpdateShortRep(arg0: int) -> int:
        """public static final int com.badlogic.gdx.utils.compression.lzma.Base.StateUpdateShortRep(int)"""
        return int.__wrap(__Base.StateUpdateShortRep(__int.valueOf(arg0)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.compression.lzma.Base()"""
        val = __Base()
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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def StateUpdateChar(arg0: int) -> int:
        """public static final int com.badlogic.gdx.utils.compression.lzma.Base.StateUpdateChar(int)"""
        return int.__wrap(__Base.StateUpdateChar(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def StateUpdateRep(arg0: int) -> int:
        """public static final int com.badlogic.gdx.utils.compression.lzma.Base.StateUpdateRep(int)"""
        return int.__wrap(__Base.StateUpdateRep(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))