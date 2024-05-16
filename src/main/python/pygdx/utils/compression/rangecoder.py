from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.compression.rangecoder.Encoder as __Encoder
__Encoder = __Encoder
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Encoder():
    """com.badlogic.gdx.utils.compression.rangecoder.Encoder"""
 
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
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def GetPrice(arg0: int, arg1: int) -> int:
        """public static int com.badlogic.gdx.utils.compression.rangecoder.Encoder.GetPrice(int,int)"""
        return int.__wrap(__Encoder.GetPrice(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def ReleaseStream(self):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.ReleaseStream()"""
        super(Encoder, self).ReleaseStream()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.compression.rangecoder.Encoder()"""
        val = __Encoder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def GetPrice0(arg0: int) -> int:
        """public static int com.badlogic.gdx.utils.compression.rangecoder.Encoder.GetPrice0(int)"""
        return int.__wrap(__Encoder.GetPrice0(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def GetPrice1(arg0: int) -> int:
        """public static int com.badlogic.gdx.utils.compression.rangecoder.Encoder.GetPrice1(int)"""
        return int.__wrap(__Encoder.GetPrice1(__int.valueOf(arg0)))

    @overload
    def GetProcessedSizeAdd(self) -> int:
        """public long com.badlogic.gdx.utils.compression.rangecoder.Encoder.GetProcessedSizeAdd()"""
        return int.__wrap(super(Encoder, self).GetProcessedSizeAdd())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.compression.rangecoder.Encoder()"""
        val = __Encoder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def FlushStream(self):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.FlushStream() throws java.io.IOException"""
        super(Encoder, self).FlushStream()

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
    def Init(self):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.Init()"""
        super(Encoder, self).Init()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def Encode(self, arg0: 'short', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.Encode(short[],int,int) throws java.io.IOException"""
        super(__Encoder, self).Encode(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def SetStream(self, arg0: 'OutputStream'):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.SetStream(java.io.OutputStream)"""
        super(__Encoder, self).SetStream(arg0)

    @staticmethod
    @overload
    def InitBitModels(arg0: 'short'):
        """public static void com.badlogic.gdx.utils.compression.rangecoder.Encoder.InitBitModels(short[])"""
        __Encoder.InitBitModels(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def FlushData(self):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.FlushData() throws java.io.IOException"""
        super(Encoder, self).FlushData()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def ShiftLow(self):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.ShiftLow() throws java.io.IOException"""
        super(Encoder, self).ShiftLow()

    @overload
    def EncodeDirectBits(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.EncodeDirectBits(int,int) throws java.io.IOException"""
        super(__Encoder, self).EncodeDirectBits(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.utils.compression.rangecoder.Encoder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.compression.rangecoder.Encoder as __Encoder
__Encoder = __Encoder
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Encoder():
    """com.badlogic.gdx.utils.compression.rangecoder.Encoder"""
 
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
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def GetPrice(arg0: int, arg1: int) -> int:
        """public static int com.badlogic.gdx.utils.compression.rangecoder.Encoder.GetPrice(int,int)"""
        return int.__wrap(__Encoder.GetPrice(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def ReleaseStream(self):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.ReleaseStream()"""
        super(Encoder, self).ReleaseStream()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.compression.rangecoder.Encoder()"""
        val = __Encoder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def GetPrice0(arg0: int) -> int:
        """public static int com.badlogic.gdx.utils.compression.rangecoder.Encoder.GetPrice0(int)"""
        return int.__wrap(__Encoder.GetPrice0(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def GetPrice1(arg0: int) -> int:
        """public static int com.badlogic.gdx.utils.compression.rangecoder.Encoder.GetPrice1(int)"""
        return int.__wrap(__Encoder.GetPrice1(__int.valueOf(arg0)))

    @overload
    def GetProcessedSizeAdd(self) -> int:
        """public long com.badlogic.gdx.utils.compression.rangecoder.Encoder.GetProcessedSizeAdd()"""
        return int.__wrap(super(Encoder, self).GetProcessedSizeAdd())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.compression.rangecoder.Encoder()"""
        val = __Encoder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def FlushStream(self):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.FlushStream() throws java.io.IOException"""
        super(Encoder, self).FlushStream()

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
    def Init(self):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.Init()"""
        super(Encoder, self).Init()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def Encode(self, arg0: 'short', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.Encode(short[],int,int) throws java.io.IOException"""
        super(__Encoder, self).Encode(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def SetStream(self, arg0: 'OutputStream'):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.SetStream(java.io.OutputStream)"""
        super(__Encoder, self).SetStream(arg0)

    @staticmethod
    @overload
    def InitBitModels(arg0: 'short'):
        """public static void com.badlogic.gdx.utils.compression.rangecoder.Encoder.InitBitModels(short[])"""
        __Encoder.InitBitModels(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def FlushData(self):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.FlushData() throws java.io.IOException"""
        super(Encoder, self).FlushData()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def ShiftLow(self):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.ShiftLow() throws java.io.IOException"""
        super(Encoder, self).ShiftLow()

    @overload
    def EncodeDirectBits(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.EncodeDirectBits(int,int) throws java.io.IOException"""
        super(__Encoder, self).EncodeDirectBits(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.utils.compression.rangecoder.Encoder 
 
 
# CLASS: com.badlogic.gdx.utils.compression.rangecoder.Decoder
import com.badlogic.gdx.utils.compression.rangecoder.Decoder as __Decoder
__Decoder = __Decoder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Decoder():
    """com.badlogic.gdx.utils.compression.rangecoder.Decoder"""
 
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
    def DecodeDirectBits(self, arg0: int) -> int:
        """public final int com.badlogic.gdx.utils.compression.rangecoder.Decoder.DecodeDirectBits(int) throws java.io.IOException"""
        return int.__wrap(super(__Decoder, self).DecodeDirectBits(__int.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.compression.rangecoder.Decoder()"""
        val = __Decoder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def Init(self):
        """public final void com.badlogic.gdx.utils.compression.rangecoder.Decoder.Init() throws java.io.IOException"""
        super(Decoder, self).Init()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.compression.rangecoder.Decoder()"""
        val = __Decoder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def DecodeBit(self, arg0: 'short', arg1: int) -> int:
        """public int com.badlogic.gdx.utils.compression.rangecoder.Decoder.DecodeBit(short[],int) throws java.io.IOException"""
        return int.__wrap(super(__Decoder, self).DecodeBit(arg0, __int.valueOf(arg1)))

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
    def ReleaseStream(self):
        """public final void com.badlogic.gdx.utils.compression.rangecoder.Decoder.ReleaseStream()"""
        super(Decoder, self).ReleaseStream()

    @overload
    def SetStream(self, arg0: 'InputStream'):
        """public final void com.badlogic.gdx.utils.compression.rangecoder.Decoder.SetStream(java.io.InputStream)"""
        super(__Decoder, self).SetStream(arg0)

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
    def InitBitModels(arg0: 'short'):
        """public static void com.badlogic.gdx.utils.compression.rangecoder.Decoder.InitBitModels(short[])"""
        __Decoder.InitBitModels(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.compression.rangecoder.BitTreeEncoder
from builtins import str
import com.badlogic.gdx.utils.compression.rangecoder.BitTreeEncoder as __BitTreeEncoder
__BitTreeEncoder = __BitTreeEncoder
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
 
class BitTreeEncoder():
    """com.badlogic.gdx.utils.compression.rangecoder.BitTreeEncoder"""
 
    @staticmethod
    def __wrap(java_value: __BitTreeEncoder) -> 'BitTreeEncoder':
        return BitTreeEncoder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BitTreeEncoder):
        """
        Dynamic initializer for BitTreeEncoder.
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
    def ReverseGetPrice(self, arg0: int) -> int:
        """public int com.badlogic.gdx.utils.compression.rangecoder.BitTreeEncoder.ReverseGetPrice(int)"""
        return int.__wrap(super(__BitTreeEncoder, self).ReverseGetPrice(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def Encode(self, arg0: 'Encoder', arg1: int):
        """public void com.badlogic.gdx.utils.compression.rangecoder.BitTreeEncoder.Encode(com.badlogic.gdx.utils.compression.rangecoder.Encoder,int) throws java.io.IOException"""
        super(__BitTreeEncoder, self).Encode(arg0, __int.valueOf(arg1))

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
    def GetPrice(self, arg0: int) -> int:
        """public int com.badlogic.gdx.utils.compression.rangecoder.BitTreeEncoder.GetPrice(int)"""
        return int.__wrap(super(__BitTreeEncoder, self).GetPrice(__int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def ReverseEncode(arg0: 'short', arg1: int, arg2: 'Encoder', arg3: int, arg4: int):
        """public static void com.badlogic.gdx.utils.compression.rangecoder.BitTreeEncoder.ReverseEncode(short[],int,com.badlogic.gdx.utils.compression.rangecoder.Encoder,int,int) throws java.io.IOException"""
        __BitTreeEncoder.ReverseEncode(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4))

    @overload
    def Init(self):
        """public void com.badlogic.gdx.utils.compression.rangecoder.BitTreeEncoder.Init()"""
        super(BitTreeEncoder, self).Init()

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.compression.rangecoder.BitTreeEncoder(int)"""
        val = __BitTreeEncoder(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def ReverseGetPrice(arg0: 'short', arg1: int, arg2: int, arg3: int) -> int:
        """public static int com.badlogic.gdx.utils.compression.rangecoder.BitTreeEncoder.ReverseGetPrice(short[],int,int,int)"""
        return int.__wrap(__BitTreeEncoder.ReverseGetPrice(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

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
    def ReverseEncode(self, arg0: 'Encoder', arg1: int):
        """public void com.badlogic.gdx.utils.compression.rangecoder.BitTreeEncoder.ReverseEncode(com.badlogic.gdx.utils.compression.rangecoder.Encoder,int) throws java.io.IOException"""
        super(__BitTreeEncoder, self).ReverseEncode(arg0, __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.compression.rangecoder.BitTreeDecoder
from builtins import str
import com.badlogic.gdx.utils.compression.rangecoder.BitTreeDecoder as __BitTreeDecoder
__BitTreeDecoder = __BitTreeDecoder
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
 
class BitTreeDecoder():
    """com.badlogic.gdx.utils.compression.rangecoder.BitTreeDecoder"""
 
    @staticmethod
    def __wrap(java_value: __BitTreeDecoder) -> 'BitTreeDecoder':
        return BitTreeDecoder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BitTreeDecoder):
        """
        Dynamic initializer for BitTreeDecoder.
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

    @staticmethod
    @overload
    def ReverseDecode(arg0: 'short', arg1: int, arg2: 'Decoder', arg3: int) -> int:
        """public static int com.badlogic.gdx.utils.compression.rangecoder.BitTreeDecoder.ReverseDecode(short[],int,com.badlogic.gdx.utils.compression.rangecoder.Decoder,int) throws java.io.IOException"""
        return int.__wrap(__BitTreeDecoder.ReverseDecode(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3)))

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
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.compression.rangecoder.BitTreeDecoder(int)"""
        val = __BitTreeDecoder(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def Init(self):
        """public void com.badlogic.gdx.utils.compression.rangecoder.BitTreeDecoder.Init()"""
        super(BitTreeDecoder, self).Init()

    @overload
    def Decode(self, arg0: 'Decoder') -> int:
        """public int com.badlogic.gdx.utils.compression.rangecoder.BitTreeDecoder.Decode(com.badlogic.gdx.utils.compression.rangecoder.Decoder) throws java.io.IOException"""
        return int.__wrap(super(__BitTreeDecoder, self).Decode(arg0))

    @overload
    def ReverseDecode(self, arg0: 'Decoder') -> int:
        """public int com.badlogic.gdx.utils.compression.rangecoder.BitTreeDecoder.ReverseDecode(com.badlogic.gdx.utils.compression.rangecoder.Decoder) throws java.io.IOException"""
        return int.__wrap(super(__BitTreeDecoder, self).ReverseDecode(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))