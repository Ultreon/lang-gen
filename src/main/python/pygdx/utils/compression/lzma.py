from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.compression.lzma.Base as _Base
_Base = _Base
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Base():
    """com.badlogic.gdx.utils.compression.lzma.Base"""
 
    @staticmethod
    def _wrap(java_value: _Base) -> 'Base':
        return Base(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Base):
        """
        Dynamic initializer for Base.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Base__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Base__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def StateUpdateShortRep(arg0: int) -> int:
        """public static final int com.badlogic.gdx.utils.compression.lzma.Base.StateUpdateShortRep(int)"""
        return int._wrap(_Base.StateUpdateShortRep(_int.valueOf(arg0)))

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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def StateUpdateMatch(arg0: int) -> int:
        """public static final int com.badlogic.gdx.utils.compression.lzma.Base.StateUpdateMatch(int)"""
        return int._wrap(_Base.StateUpdateMatch(_int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.compression.lzma.Base()"""
        val = _Base()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def StateIsCharState(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.utils.compression.lzma.Base.StateIsCharState(int)"""
        return bool._wrap(_Base.StateIsCharState(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def StateInit() -> int:
        """public static final int com.badlogic.gdx.utils.compression.lzma.Base.StateInit()"""
        return int._wrap(_Base.StateInit())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def StateUpdateRep(arg0: int) -> int:
        """public static final int com.badlogic.gdx.utils.compression.lzma.Base.StateUpdateRep(int)"""
        return int._wrap(_Base.StateUpdateRep(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def GetLenToPosState(arg0: int) -> int:
        """public static final int com.badlogic.gdx.utils.compression.lzma.Base.GetLenToPosState(int)"""
        return int._wrap(_Base.GetLenToPosState(_int.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.compression.lzma.Base()"""
        val = _Base()
        self.__wrapper = val

    @staticmethod
    @overload
    def StateUpdateChar(arg0: int) -> int:
        """public static final int com.badlogic.gdx.utils.compression.lzma.Base.StateUpdateChar(int)"""
        return int._wrap(_Base.StateUpdateChar(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.utils.compression.lzma.Base
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.compression.lzma.Base as _Base
_Base = _Base
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Base():
    """com.badlogic.gdx.utils.compression.lzma.Base"""
 
    @staticmethod
    def _wrap(java_value: _Base) -> 'Base':
        return Base(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Base):
        """
        Dynamic initializer for Base.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Base__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Base__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def StateUpdateShortRep(arg0: int) -> int:
        """public static final int com.badlogic.gdx.utils.compression.lzma.Base.StateUpdateShortRep(int)"""
        return int._wrap(_Base.StateUpdateShortRep(_int.valueOf(arg0)))

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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def StateUpdateMatch(arg0: int) -> int:
        """public static final int com.badlogic.gdx.utils.compression.lzma.Base.StateUpdateMatch(int)"""
        return int._wrap(_Base.StateUpdateMatch(_int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.compression.lzma.Base()"""
        val = _Base()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def StateIsCharState(arg0: int) -> bool:
        """public static final boolean com.badlogic.gdx.utils.compression.lzma.Base.StateIsCharState(int)"""
        return bool._wrap(_Base.StateIsCharState(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def StateInit() -> int:
        """public static final int com.badlogic.gdx.utils.compression.lzma.Base.StateInit()"""
        return int._wrap(_Base.StateInit())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def StateUpdateRep(arg0: int) -> int:
        """public static final int com.badlogic.gdx.utils.compression.lzma.Base.StateUpdateRep(int)"""
        return int._wrap(_Base.StateUpdateRep(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def GetLenToPosState(arg0: int) -> int:
        """public static final int com.badlogic.gdx.utils.compression.lzma.Base.GetLenToPosState(int)"""
        return int._wrap(_Base.GetLenToPosState(_int.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.compression.lzma.Base()"""
        val = _Base()
        self.__wrapper = val

    @staticmethod
    @overload
    def StateUpdateChar(arg0: int) -> int:
        """public static final int com.badlogic.gdx.utils.compression.lzma.Base.StateUpdateChar(int)"""
        return int._wrap(_Base.StateUpdateChar(_int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.utils.compression.lzma.Base 
 
 
# CLASS: com.badlogic.gdx.utils.compression.lzma.Decoder
from builtins import str
import com.badlogic.gdx.utils.compression.lzma.Decoder as _Decoder
_Decoder = _Decoder
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.io.OutputStream as OutputStream
import java.lang.Integer as _int
import java.io.InputStream as InputStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Decoder():
    """com.badlogic.gdx.utils.compression.lzma.Decoder"""
 
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
    def Code(self, arg0: 'InputStream', arg1: 'OutputStream', arg2: int) -> bool:
        """public boolean com.badlogic.gdx.utils.compression.lzma.Decoder.Code(java.io.InputStream,java.io.OutputStream,long) throws java.io.IOException"""
        return bool._wrap(super(_Decoder, self).Code(arg0, arg1, _long.valueOf(arg2)))

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
    def SetDecoderProperties(self, arg0: bytes) -> bool:
        """public boolean com.badlogic.gdx.utils.compression.lzma.Decoder.SetDecoderProperties(byte[])"""
        return bool._wrap(super(_Decoder, self).SetDecoderProperties(bytes))

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
    def __init__(self, ):
        """public com.badlogic.gdx.utils.compression.lzma.Decoder()"""
        val = _Decoder()
        self.__wrapper = val

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
        """public com.badlogic.gdx.utils.compression.lzma.Decoder()"""
        val = _Decoder()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.utils.compression.lzma.Encoder
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.utils.compression.lzma.Encoder as _Encoder
_Encoder = _Encoder
import java.lang.String as _String
_String = _String
try:
    from pygdx.utils import compression
except ImportError:
    compression = _import_once("pygdx.utils.compression")

import java.lang.Boolean as _boolean
import java.io.OutputStream as OutputStream
import java.lang.Integer as _int
import java.io.InputStream as InputStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Encoder():
    """com.badlogic.gdx.utils.compression.lzma.Encoder"""
 
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
 
    @overload
    def SetEndMarkerMode(self, arg0: bool):
        """public void com.badlogic.gdx.utils.compression.lzma.Encoder.SetEndMarkerMode(boolean)"""
        super(_Encoder, self).SetEndMarkerMode(_boolean.valueOf(arg0))

    @overload
    def SetMatchFinder(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.compression.lzma.Encoder.SetMatchFinder(int)"""
        return bool._wrap(super(_Encoder, self).SetMatchFinder(_int.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.compression.lzma.Encoder()"""
        val = _Encoder()
        self.__wrapper = val

    @overload
    def SetDictionarySize(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.compression.lzma.Encoder.SetDictionarySize(int)"""
        return bool._wrap(super(_Encoder, self).SetDictionarySize(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def Code(self, arg0: 'InputStream', arg1: 'OutputStream', arg2: int, arg3: int, arg4: 'ICodeProgress'):
        """public void com.badlogic.gdx.utils.compression.lzma.Encoder.Code(java.io.InputStream,java.io.OutputStream,long,long,com.badlogic.gdx.utils.compression.ICodeProgress) throws java.io.IOException"""
        super(_Encoder, self).Code(arg0, arg1, _long.valueOf(arg2), _long.valueOf(arg3), arg4)

    @overload
    def CodeOneBlock(self, arg0: 'long', arg1: 'long', arg2: 'boolean'):
        """public void com.badlogic.gdx.utils.compression.lzma.Encoder.CodeOneBlock(long[],long[],boolean[]) throws java.io.IOException"""
        super(_Encoder, self).CodeOneBlock(arg0, arg1, arg2)

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
        """public com.badlogic.gdx.utils.compression.lzma.Encoder()"""
        val = _Encoder()
        self.__wrapper = val

    @overload
    def SetLcLpPb(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public boolean com.badlogic.gdx.utils.compression.lzma.Encoder.SetLcLpPb(int,int,int)"""
        return bool._wrap(super(_Encoder, self).SetLcLpPb(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def SetNumFastBytes(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.compression.lzma.Encoder.SetNumFastBytes(int)"""
        return bool._wrap(super(_Encoder, self).SetNumFastBytes(_int.valueOf(arg0)))

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
    def WriteCoderProperties(self, arg0: 'OutputStream'):
        """public void com.badlogic.gdx.utils.compression.lzma.Encoder.WriteCoderProperties(java.io.OutputStream) throws java.io.IOException"""
        super(_Encoder, self).WriteCoderProperties(arg0)

    @overload
    def SetAlgorithm(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.utils.compression.lzma.Encoder.SetAlgorithm(int)"""
        return bool._wrap(super(_Encoder, self).SetAlgorithm(_int.valueOf(arg0)))

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