from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.io.OutputStream as OutputStream
import com.badlogic.gdx.utils.compression.rangecoder.Encoder as _Encoder
_Encoder = _Encoder
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Encoder():
    """com.badlogic.gdx.utils.compression.rangecoder.Encoder"""
 
    @staticmethod
    def _wrap(java_value: _Encoder) -> 'Encoder':
        return Encoder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Encoder):
        """
        Dynamic initializer for Encoder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Encoder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Encoder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def GetPrice0(arg0: int) -> int:
        """public static int com.badlogic.gdx.utils.compression.rangecoder.Encoder.GetPrice0(int)"""
        return int._wrap(_Encoder.GetPrice0(_int.valueOf(arg0)))

    @overload
    def ReleaseStream(self):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.ReleaseStream()"""
        super(Encoder, self).ReleaseStream()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def SetStream(self, arg0: 'OutputStream'):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.SetStream(java.io.OutputStream)"""
        super(_Encoder, self).SetStream(arg0)

    @staticmethod
    @overload
    def GetPrice1(arg0: int) -> int:
        """public static int com.badlogic.gdx.utils.compression.rangecoder.Encoder.GetPrice1(int)"""
        return int._wrap(_Encoder.GetPrice1(_int.valueOf(arg0)))

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
    def FlushStream(self):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.FlushStream() throws java.io.IOException"""
        super(Encoder, self).FlushStream()

    @overload
    def GetProcessedSizeAdd(self) -> int:
        """public long com.badlogic.gdx.utils.compression.rangecoder.Encoder.GetProcessedSizeAdd()"""
        return int._wrap(super(Encoder, self).GetProcessedSizeAdd())

    @overload
    def Init(self):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.Init()"""
        super(Encoder, self).Init()

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
        """public com.badlogic.gdx.utils.compression.rangecoder.Encoder()"""
        val = _Encoder()
        self.__wrapper = val

    @overload
    def Encode(self, arg0: 'short', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.Encode(short[],int,int) throws java.io.IOException"""
        super(_Encoder, self).Encode(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def GetPrice(arg0: int, arg1: int) -> int:
        """public static int com.badlogic.gdx.utils.compression.rangecoder.Encoder.GetPrice(int,int)"""
        return int._wrap(_Encoder.GetPrice(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.compression.rangecoder.Encoder()"""
        val = _Encoder()
        self.__wrapper = val

    @overload
    def FlushData(self):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.FlushData() throws java.io.IOException"""
        super(Encoder, self).FlushData()

    @staticmethod
    @overload
    def InitBitModels(arg0: 'short'):
        """public static void com.badlogic.gdx.utils.compression.rangecoder.Encoder.InitBitModels(short[])"""
        _Encoder.InitBitModels(arg0)

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
        super(_Encoder, self).EncodeDirectBits(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.utils.compression.rangecoder.Encoder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import java.io.OutputStream as OutputStream
import com.badlogic.gdx.utils.compression.rangecoder.Encoder as _Encoder
_Encoder = _Encoder
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Encoder():
    """com.badlogic.gdx.utils.compression.rangecoder.Encoder"""
 
    @staticmethod
    def _wrap(java_value: _Encoder) -> 'Encoder':
        return Encoder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Encoder):
        """
        Dynamic initializer for Encoder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Encoder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Encoder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def GetPrice0(arg0: int) -> int:
        """public static int com.badlogic.gdx.utils.compression.rangecoder.Encoder.GetPrice0(int)"""
        return int._wrap(_Encoder.GetPrice0(_int.valueOf(arg0)))

    @overload
    def ReleaseStream(self):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.ReleaseStream()"""
        super(Encoder, self).ReleaseStream()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def SetStream(self, arg0: 'OutputStream'):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.SetStream(java.io.OutputStream)"""
        super(_Encoder, self).SetStream(arg0)

    @staticmethod
    @overload
    def GetPrice1(arg0: int) -> int:
        """public static int com.badlogic.gdx.utils.compression.rangecoder.Encoder.GetPrice1(int)"""
        return int._wrap(_Encoder.GetPrice1(_int.valueOf(arg0)))

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
    def FlushStream(self):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.FlushStream() throws java.io.IOException"""
        super(Encoder, self).FlushStream()

    @overload
    def GetProcessedSizeAdd(self) -> int:
        """public long com.badlogic.gdx.utils.compression.rangecoder.Encoder.GetProcessedSizeAdd()"""
        return int._wrap(super(Encoder, self).GetProcessedSizeAdd())

    @overload
    def Init(self):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.Init()"""
        super(Encoder, self).Init()

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
        """public com.badlogic.gdx.utils.compression.rangecoder.Encoder()"""
        val = _Encoder()
        self.__wrapper = val

    @overload
    def Encode(self, arg0: 'short', arg1: int, arg2: int):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.Encode(short[],int,int) throws java.io.IOException"""
        super(_Encoder, self).Encode(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @staticmethod
    @overload
    def GetPrice(arg0: int, arg1: int) -> int:
        """public static int com.badlogic.gdx.utils.compression.rangecoder.Encoder.GetPrice(int,int)"""
        return int._wrap(_Encoder.GetPrice(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.compression.rangecoder.Encoder()"""
        val = _Encoder()
        self.__wrapper = val

    @overload
    def FlushData(self):
        """public void com.badlogic.gdx.utils.compression.rangecoder.Encoder.FlushData() throws java.io.IOException"""
        super(Encoder, self).FlushData()

    @staticmethod
    @overload
    def InitBitModels(arg0: 'short'):
        """public static void com.badlogic.gdx.utils.compression.rangecoder.Encoder.InitBitModels(short[])"""
        _Encoder.InitBitModels(arg0)

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
        super(_Encoder, self).EncodeDirectBits(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.utils.compression.rangecoder.Encoder 
 
 
# CLASS: com.badlogic.gdx.utils.compression.rangecoder.BitTreeDecoder
from builtins import str
import com.badlogic.gdx.utils.compression.rangecoder.BitTreeDecoder as _BitTreeDecoder
_BitTreeDecoder = _BitTreeDecoder
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BitTreeDecoder():
    """com.badlogic.gdx.utils.compression.rangecoder.BitTreeDecoder"""
 
    @staticmethod
    def _wrap(java_value: _BitTreeDecoder) -> 'BitTreeDecoder':
        return BitTreeDecoder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BitTreeDecoder):
        """
        Dynamic initializer for BitTreeDecoder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BitTreeDecoder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BitTreeDecoder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def ReverseDecode(arg0: 'short', arg1: int, arg2: 'Decoder', arg3: int) -> int:
        """public static int com.badlogic.gdx.utils.compression.rangecoder.BitTreeDecoder.ReverseDecode(short[],int,com.badlogic.gdx.utils.compression.rangecoder.Decoder,int) throws java.io.IOException"""
        return int._wrap(_BitTreeDecoder.ReverseDecode(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3)))

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
    def Decode(self, arg0: 'Decoder') -> int:
        """public int com.badlogic.gdx.utils.compression.rangecoder.BitTreeDecoder.Decode(com.badlogic.gdx.utils.compression.rangecoder.Decoder) throws java.io.IOException"""
        return int._wrap(super(_BitTreeDecoder, self).Decode(arg0))

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
    def Init(self):
        """public void com.badlogic.gdx.utils.compression.rangecoder.BitTreeDecoder.Init()"""
        super(BitTreeDecoder, self).Init()

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.compression.rangecoder.BitTreeDecoder(int)"""
        val = _BitTreeDecoder(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def ReverseDecode(self, arg0: 'Decoder') -> int:
        """public int com.badlogic.gdx.utils.compression.rangecoder.BitTreeDecoder.ReverseDecode(com.badlogic.gdx.utils.compression.rangecoder.Decoder) throws java.io.IOException"""
        return int._wrap(super(_BitTreeDecoder, self).ReverseDecode(arg0))

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
 
 
# CLASS: com.badlogic.gdx.utils.compression.rangecoder.Decoder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.compression.rangecoder.Decoder as _Decoder
_Decoder = _Decoder
import java.lang.Integer as _int
import java.io.InputStream as InputStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Decoder():
    """com.badlogic.gdx.utils.compression.rangecoder.Decoder"""
 
    @staticmethod
    def _wrap(java_value: _Decoder) -> 'Decoder':
        return Decoder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Decoder):
        """
        Dynamic initializer for Decoder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Decoder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Decoder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def DecodeDirectBits(self, arg0: int) -> int:
        """public final int com.badlogic.gdx.utils.compression.rangecoder.Decoder.DecodeDirectBits(int) throws java.io.IOException"""
        return int._wrap(super(_Decoder, self).DecodeDirectBits(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def InitBitModels(arg0: 'short'):
        """public static void com.badlogic.gdx.utils.compression.rangecoder.Decoder.InitBitModels(short[])"""
        _Decoder.InitBitModels(arg0)

    @overload
    def Init(self):
        """public final void com.badlogic.gdx.utils.compression.rangecoder.Decoder.Init() throws java.io.IOException"""
        super(Decoder, self).Init()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.compression.rangecoder.Decoder()"""
        val = _Decoder()
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.compression.rangecoder.Decoder()"""
        val = _Decoder()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def DecodeBit(self, arg0: 'short', arg1: int) -> int:
        """public int com.badlogic.gdx.utils.compression.rangecoder.Decoder.DecodeBit(short[],int) throws java.io.IOException"""
        return int._wrap(super(_Decoder, self).DecodeBit(arg0, _int.valueOf(arg1)))

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
    def ReleaseStream(self):
        """public final void com.badlogic.gdx.utils.compression.rangecoder.Decoder.ReleaseStream()"""
        super(Decoder, self).ReleaseStream()

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
    def SetStream(self, arg0: 'InputStream'):
        """public final void com.badlogic.gdx.utils.compression.rangecoder.Decoder.SetStream(java.io.InputStream)"""
        super(_Decoder, self).SetStream(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.utils.compression.rangecoder.BitTreeEncoder
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.utils.compression.rangecoder.BitTreeEncoder as _BitTreeEncoder
_BitTreeEncoder = _BitTreeEncoder
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BitTreeEncoder():
    """com.badlogic.gdx.utils.compression.rangecoder.BitTreeEncoder"""
 
    @staticmethod
    def _wrap(java_value: _BitTreeEncoder) -> 'BitTreeEncoder':
        return BitTreeEncoder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BitTreeEncoder):
        """
        Dynamic initializer for BitTreeEncoder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BitTreeEncoder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BitTreeEncoder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def ReverseEncode(self, arg0: 'Encoder', arg1: int):
        """public void com.badlogic.gdx.utils.compression.rangecoder.BitTreeEncoder.ReverseEncode(com.badlogic.gdx.utils.compression.rangecoder.Encoder,int) throws java.io.IOException"""
        super(_BitTreeEncoder, self).ReverseEncode(arg0, _int.valueOf(arg1))

    @staticmethod
    @overload
    def ReverseEncode(arg0: 'short', arg1: int, arg2: 'Encoder', arg3: int, arg4: int):
        """public static void com.badlogic.gdx.utils.compression.rangecoder.BitTreeEncoder.ReverseEncode(short[],int,com.badlogic.gdx.utils.compression.rangecoder.Encoder,int,int) throws java.io.IOException"""
        _BitTreeEncoder.ReverseEncode(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def Encode(self, arg0: 'Encoder', arg1: int):
        """public void com.badlogic.gdx.utils.compression.rangecoder.BitTreeEncoder.Encode(com.badlogic.gdx.utils.compression.rangecoder.Encoder,int) throws java.io.IOException"""
        super(_BitTreeEncoder, self).Encode(arg0, _int.valueOf(arg1))

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
    def ReverseGetPrice(arg0: 'short', arg1: int, arg2: int, arg3: int) -> int:
        """public static int com.badlogic.gdx.utils.compression.rangecoder.BitTreeEncoder.ReverseGetPrice(short[],int,int,int)"""
        return int._wrap(_BitTreeEncoder.ReverseGetPrice(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def Init(self):
        """public void com.badlogic.gdx.utils.compression.rangecoder.BitTreeEncoder.Init()"""
        super(BitTreeEncoder, self).Init()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def ReverseGetPrice(self, arg0: int) -> int:
        """public int com.badlogic.gdx.utils.compression.rangecoder.BitTreeEncoder.ReverseGetPrice(int)"""
        return int._wrap(super(_BitTreeEncoder, self).ReverseGetPrice(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def GetPrice(self, arg0: int) -> int:
        """public int com.badlogic.gdx.utils.compression.rangecoder.BitTreeEncoder.GetPrice(int)"""
        return int._wrap(super(_BitTreeEncoder, self).GetPrice(_int.valueOf(arg0)))

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
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.utils.compression.rangecoder.BitTreeEncoder(int)"""
        val = _BitTreeEncoder(_int.valueOf(arg0))
        self.__wrapper = val