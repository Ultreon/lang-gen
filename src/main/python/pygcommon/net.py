from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import com.google.common.net.PercentEscaper as _PercentEscaper
_PercentEscaper = _PercentEscaper
try:
    from pygcommon import base
except ImportError:
    base = _import_once("pygcommon.base")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import com.google.common.base.Function as _Function
_Function = _Function
import com.google.common.escape.Escaper as _Escaper
_Escaper = _Escaper
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PercentEscaper():
    """com.google.common.net.PercentEscaper"""
 
    @staticmethod
    def _wrap(java_value: _PercentEscaper) -> 'PercentEscaper':
        return PercentEscaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PercentEscaper):
        """
        Dynamic initializer for PercentEscaper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PercentEscaper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PercentEscaper__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def escape(self, s: str) -> str:
        """public java.lang.String com.google.common.net.PercentEscaper.escape(java.lang.String)"""
        return str._wrap(super(_PercentEscaper, self).escape(s))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, safeChars: str, plusForSpace: bool):
        """public com.google.common.net.PercentEscaper(java.lang.String,boolean)"""
        val = _PercentEscaper(safeChars, _boolean.valueOf(plusForSpace))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def asFunction(self) -> 'base.Function':
        """public final com.google.common.base.Function<java.lang.String, java.lang.String> com.google.common.escape.Escaper.asFunction()"""
        return 'base.Function'._wrap(super(escape.Escaper, self).asFunction())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.google.common.net.PercentEscaper
from pyquantum_helper import import_once as _import_once
import com.google.common.net.PercentEscaper as _PercentEscaper
_PercentEscaper = _PercentEscaper
try:
    from pygcommon import base
except ImportError:
    base = _import_once("pygcommon.base")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import com.google.common.base.Function as _Function
_Function = _Function
import com.google.common.escape.Escaper as _Escaper
_Escaper = _Escaper
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PercentEscaper():
    """com.google.common.net.PercentEscaper"""
 
    @staticmethod
    def _wrap(java_value: _PercentEscaper) -> 'PercentEscaper':
        return PercentEscaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PercentEscaper):
        """
        Dynamic initializer for PercentEscaper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PercentEscaper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PercentEscaper__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def escape(self, s: str) -> str:
        """public java.lang.String com.google.common.net.PercentEscaper.escape(java.lang.String)"""
        return str._wrap(super(_PercentEscaper, self).escape(s))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, safeChars: str, plusForSpace: bool):
        """public com.google.common.net.PercentEscaper(java.lang.String,boolean)"""
        val = _PercentEscaper(safeChars, _boolean.valueOf(plusForSpace))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def asFunction(self) -> 'base.Function':
        """public final com.google.common.base.Function<java.lang.String, java.lang.String> com.google.common.escape.Escaper.asFunction()"""
        return 'base.Function'._wrap(super(escape.Escaper, self).asFunction())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.google.common.net.PercentEscaper 
 
 
# CLASS: com.google.common.net.MediaType
from pyquantum_helper import import_once as _import_once
try:
    from pygcommon import base
except ImportError:
    base = _import_once("pygcommon.base")

from builtins import str
from pyquantum_helper import override
import java.nio.charset.Charset as Charset
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.base.Optional as _Optional
_Optional = _Optional
import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
import java.lang.String as _string
try:
    import pygcollect
except ImportError:
    pygcollect = _import_once("pygcollect")

import com.google.common.net.MediaType as _MediaType
_MediaType = _MediaType
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import com.google.common.collect.ImmutableListMultimap as _ImmutableListMultimap
_ImmutableListMultimap = _ImmutableListMultimap
import java.lang.Class as _Class
_Class = _Class
 
class MediaType():
    """com.google.common.net.MediaType"""
 
    @staticmethod
    def _wrap(java_value: _MediaType) -> 'MediaType':
        return MediaType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MediaType):
        """
        Dynamic initializer for MediaType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MediaType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MediaType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def charset(self) -> 'base.Optional':
        """public com.google.common.base.Optional<java.nio.charset.Charset> com.google.common.net.MediaType.charset()"""
        return 'base.Optional'._wrap(super(MediaType, self).charset())

    @overload
    def is(self, mediaTypeRange: 'MediaType') -> bool:
        """public boolean com.google.common.net.MediaType.is(com.google.common.net.MediaType)"""
        return bool._wrap(super(_MediaType, self).is(mediaTypeRange))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def create(type: str, subtype: str) -> 'MediaType':
        """public static com.google.common.net.MediaType com.google.common.net.MediaType.create(java.lang.String,java.lang.String)"""
        return MediaType._wrap(_MediaType.create(type, subtype))

    @overload
    def subtype(self) -> str:
        """public java.lang.String com.google.common.net.MediaType.subtype()"""
        return str._wrap(super(MediaType, self).subtype())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def type(self) -> str:
        """public java.lang.String com.google.common.net.MediaType.type()"""
        return str._wrap(super(MediaType, self).type())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.net.MediaType.toString()"""
        return str._wrap(super(MediaType, self).toString())

    @overload
    def withoutParameters(self) -> 'MediaType':
        """public com.google.common.net.MediaType com.google.common.net.MediaType.withoutParameters()"""
        return 'MediaType'._wrap(super(MediaType, self).withoutParameters())

    @overload
    def withCharset(self, charset: 'Charset') -> 'MediaType':
        """public com.google.common.net.MediaType com.google.common.net.MediaType.withCharset(java.nio.charset.Charset)"""
        return 'MediaType'._wrap(super(_MediaType, self).withCharset(charset))

    @overload
    def parameters(self) -> 'pygcollect.ImmutableListMultimap':
        """public com.google.common.collect.ImmutableListMultimap<java.lang.String, java.lang.String> com.google.common.net.MediaType.parameters()"""
        return 'pygcollect.ImmutableListMultimap'._wrap(super(MediaType, self).parameters())

    @overload
    def withParameters(self, attribute: str, values: 'Iterable') -> 'MediaType':
        """public com.google.common.net.MediaType com.google.common.net.MediaType.withParameters(java.lang.String,java.lang.Iterable<java.lang.String>)"""
        return 'MediaType'._wrap(super(_MediaType, self).withParameters(attribute, values))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.net.MediaType.hashCode()"""
        return int._wrap(super(MediaType, self).hashCode())

    @staticmethod
    @overload
    def parse(input: str) -> 'MediaType':
        """public static com.google.common.net.MediaType com.google.common.net.MediaType.parse(java.lang.String)"""
        return MediaType._wrap(_MediaType.parse(input))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.net.MediaType.equals(java.lang.Object)"""
        return bool._wrap(super(_MediaType, self).equals(obj))

    @overload
    def withParameter(self, attribute: str, value: str) -> 'MediaType':
        """public com.google.common.net.MediaType com.google.common.net.MediaType.withParameter(java.lang.String,java.lang.String)"""
        return 'MediaType'._wrap(super(_MediaType, self).withParameter(attribute, value))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def hasWildcard(self) -> bool:
        """public boolean com.google.common.net.MediaType.hasWildcard()"""
        return bool._wrap(super(MediaType, self).hasWildcard())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def withParameters(self, parameters: 'Multimap') -> 'MediaType':
        """public com.google.common.net.MediaType com.google.common.net.MediaType.withParameters(com.google.common.collect.Multimap<java.lang.String, java.lang.String>)"""
        return 'MediaType'._wrap(super(_MediaType, self).withParameters(parameters)) 
 
 
# CLASS: com.google.common.net.HttpHeaders$ReferrerPolicyValues
from builtins import str
import com.google.common.net.HttpHeaders as _HttpHeaders_ReferrerPolicyValues
_ReferrerPolicyValues = _HttpHeaders_ReferrerPolicyValues.ReferrerPolicyValues
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ReferrerPolicyValues():
    """com.google.common.net.HttpHeaders.ReferrerPolicyValues"""
 
    @staticmethod
    def _wrap(java_value: _ReferrerPolicyValues) -> 'ReferrerPolicyValues':
        return ReferrerPolicyValues(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReferrerPolicyValues):
        """
        Dynamic initializer for ReferrerPolicyValues.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReferrerPolicyValues__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReferrerPolicyValues__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.net.InetAddresses
import java.net.InetAddress as _InetAddress
_InetAddress = _InetAddress
from builtins import str
from pyquantum_helper import override
import java.net.InetAddress as InetAddress
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.net.InetAddresses as _InetAddresses
_InetAddresses = _InetAddresses
import java.lang.String as _String
_String = _String
import java.net.Inet6Address as _Inet6Address
_Inet6Address = _Inet6Address
import java.net.Inet4Address as Inet4Address
import java.lang.String as _string
import java.math.BigInteger as BigInteger
import java.lang.Integer as _int
import java.net.Inet6Address as Inet6Address
import com.google.common.net.InetAddresses as _InetAddresses_TeredoInfo
_TeredoInfo = _InetAddresses_TeredoInfo.TeredoInfo
from builtins import bool
import java.lang.Long as _long
import java.net.Inet4Address as _Inet4Address
_Inet4Address = _Inet4Address
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InetAddresses():
    """com.google.common.net.InetAddresses"""
 
    @staticmethod
    def _wrap(java_value: _InetAddresses) -> 'InetAddresses':
        return InetAddresses(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InetAddresses):
        """
        Dynamic initializer for InetAddresses.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InetAddresses__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InetAddresses__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def fromInteger(address: int) -> 'Inet4Address':
        """public static java.net.Inet4Address com.google.common.net.InetAddresses.fromInteger(int)"""
        return Inet4Address._wrap(_InetAddresses.fromInteger(_int.valueOf(address)))

    @staticmethod
    @overload
    def isMappedIPv4Address(ipString: str) -> bool:
        """public static boolean com.google.common.net.InetAddresses.isMappedIPv4Address(java.lang.String)"""
        return bool._wrap(_InetAddresses.isMappedIPv4Address(ipString))

    @staticmethod
    @overload
    def forUriString(hostAddr: str) -> 'InetAddress':
        """public static java.net.InetAddress com.google.common.net.InetAddresses.forUriString(java.lang.String)"""
        return InetAddress._wrap(_InetAddresses.forUriString(hostAddr))

    @staticmethod
    @overload
    def getIsatapIPv4Address(ip: 'Inet6Address') -> 'Inet4Address':
        """public static java.net.Inet4Address com.google.common.net.InetAddresses.getIsatapIPv4Address(java.net.Inet6Address)"""
        return Inet4Address._wrap(_InetAddresses.getIsatapIPv4Address(ip))

    @staticmethod
    @overload
    def toUriString(ip: 'InetAddress') -> str:
        """public static java.lang.String com.google.common.net.InetAddresses.toUriString(java.net.InetAddress)"""
        return str._wrap(_InetAddresses.toUriString(ip))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def is6to4Address(ip: 'Inet6Address') -> bool:
        """public static boolean com.google.common.net.InetAddresses.is6to4Address(java.net.Inet6Address)"""
        return bool._wrap(_InetAddresses.is6to4Address(ip))

    @staticmethod
    @overload
    def getEmbeddedIPv4ClientAddress(ip: 'Inet6Address') -> 'Inet4Address':
        """public static java.net.Inet4Address com.google.common.net.InetAddresses.getEmbeddedIPv4ClientAddress(java.net.Inet6Address)"""
        return Inet4Address._wrap(_InetAddresses.getEmbeddedIPv4ClientAddress(ip))

    @staticmethod
    @overload
    def fromLittleEndianByteArray(addr: bytes) -> 'InetAddress':
        """public static java.net.InetAddress com.google.common.net.InetAddresses.fromLittleEndianByteArray(byte[]) throws java.net.UnknownHostException"""
        return InetAddress._wrap(_InetAddresses.fromLittleEndianByteArray(bytes))

    @staticmethod
    @overload
    def isMaximum(address: 'InetAddress') -> bool:
        """public static boolean com.google.common.net.InetAddresses.isMaximum(java.net.InetAddress)"""
        return bool._wrap(_InetAddresses.isMaximum(address))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def decrement(address: 'InetAddress') -> 'InetAddress':
        """public static java.net.InetAddress com.google.common.net.InetAddresses.decrement(java.net.InetAddress)"""
        return InetAddress._wrap(_InetAddresses.decrement(address))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getTeredoInfo(ip: 'Inet6Address') -> 'TeredoInfo':
        """public static com.google.common.net.InetAddresses$TeredoInfo com.google.common.net.InetAddresses.getTeredoInfo(java.net.Inet6Address)"""
        return TeredoInfo._wrap(_InetAddresses.getTeredoInfo(ip))

    @staticmethod
    @overload
    def coerceToInteger(ip: 'InetAddress') -> int:
        """public static int com.google.common.net.InetAddresses.coerceToInteger(java.net.InetAddress)"""
        return int._wrap(_InetAddresses.coerceToInteger(ip))

    @staticmethod
    @overload
    def isInetAddress(ipString: str) -> bool:
        """public static boolean com.google.common.net.InetAddresses.isInetAddress(java.lang.String)"""
        return bool._wrap(_InetAddresses.isInetAddress(ipString))

    @staticmethod
    @overload
    def isTeredoAddress(ip: 'Inet6Address') -> bool:
        """public static boolean com.google.common.net.InetAddresses.isTeredoAddress(java.net.Inet6Address)"""
        return bool._wrap(_InetAddresses.isTeredoAddress(ip))

    @staticmethod
    @overload
    def fromIPv6BigInteger(address: 'BigInteger') -> 'Inet6Address':
        """public static java.net.Inet6Address com.google.common.net.InetAddresses.fromIPv6BigInteger(java.math.BigInteger)"""
        return Inet6Address._wrap(_InetAddresses.fromIPv6BigInteger(address))

    @staticmethod
    @overload
    def getCoercedIPv4Address(ip: 'InetAddress') -> 'Inet4Address':
        """public static java.net.Inet4Address com.google.common.net.InetAddresses.getCoercedIPv4Address(java.net.InetAddress)"""
        return Inet4Address._wrap(_InetAddresses.getCoercedIPv4Address(ip))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def toBigInteger(toBigInteger) -> 'BigInteger':
        """public static java.math.BigInteger com.google.common.net.InetAddresses.toBigInteger(java.net.InetAddress)"""
        return _transform(_address.InetAddresses(address: 'InetAddress')).'BigInteger'Value()

    @staticmethod
    @overload
    def toAddrString(ip: 'InetAddress') -> str:
        """public static java.lang.String com.google.common.net.InetAddresses.toAddrString(java.net.InetAddress)"""
        return str._wrap(_InetAddresses.toAddrString(ip))

    @staticmethod
    @overload
    def isCompatIPv4Address(ip: 'Inet6Address') -> bool:
        """public static boolean com.google.common.net.InetAddresses.isCompatIPv4Address(java.net.Inet6Address)"""
        return bool._wrap(_InetAddresses.isCompatIPv4Address(ip))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def get6to4IPv4Address(ip: 'Inet6Address') -> 'Inet4Address':
        """public static java.net.Inet4Address com.google.common.net.InetAddresses.get6to4IPv4Address(java.net.Inet6Address)"""
        return Inet4Address._wrap(_InetAddresses.get6to4IPv4Address(ip))

    @staticmethod
    @overload
    def fromIPv4BigInteger(address: 'BigInteger') -> 'Inet4Address':
        """public static java.net.Inet4Address com.google.common.net.InetAddresses.fromIPv4BigInteger(java.math.BigInteger)"""
        return Inet4Address._wrap(_InetAddresses.fromIPv4BigInteger(address))

    @staticmethod
    @overload
    def getCompatIPv4Address(ip: 'Inet6Address') -> 'Inet4Address':
        """public static java.net.Inet4Address com.google.common.net.InetAddresses.getCompatIPv4Address(java.net.Inet6Address)"""
        return Inet4Address._wrap(_InetAddresses.getCompatIPv4Address(ip))

    @staticmethod
    @overload
    def increment(address: 'InetAddress') -> 'InetAddress':
        """public static java.net.InetAddress com.google.common.net.InetAddresses.increment(java.net.InetAddress)"""
        return InetAddress._wrap(_InetAddresses.increment(address))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def isIsatapAddress(ip: 'Inet6Address') -> bool:
        """public static boolean com.google.common.net.InetAddresses.isIsatapAddress(java.net.Inet6Address)"""
        return bool._wrap(_InetAddresses.isIsatapAddress(ip))

    @staticmethod
    @overload
    def forString(ipString: str) -> 'InetAddress':
        """public static java.net.InetAddress com.google.common.net.InetAddresses.forString(java.lang.String)"""
        return InetAddress._wrap(_InetAddresses.forString(ipString))

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

    @staticmethod
    @overload
    def isUriInetAddress(ipString: str) -> bool:
        """public static boolean com.google.common.net.InetAddresses.isUriInetAddress(java.lang.String)"""
        return bool._wrap(_InetAddresses.isUriInetAddress(ipString))

    @staticmethod
    @overload
    def hasEmbeddedIPv4ClientAddress(ip: 'Inet6Address') -> bool:
        """public static boolean com.google.common.net.InetAddresses.hasEmbeddedIPv4ClientAddress(java.net.Inet6Address)"""
        return bool._wrap(_InetAddresses.hasEmbeddedIPv4ClientAddress(ip))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.net.HostAndPort
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.net.HostAndPort as _HostAndPort
_HostAndPort = _HostAndPort
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HostAndPort():
    """com.google.common.net.HostAndPort"""
 
    @staticmethod
    def _wrap(java_value: _HostAndPort) -> 'HostAndPort':
        return HostAndPort(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HostAndPort):
        """
        Dynamic initializer for HostAndPort.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HostAndPort__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HostAndPort__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def requireBracketsForIPv6(self) -> 'HostAndPort':
        """public com.google.common.net.HostAndPort com.google.common.net.HostAndPort.requireBracketsForIPv6()"""
        return 'HostAndPort'._wrap(super(HostAndPort, self).requireBracketsForIPv6())

    @staticmethod
    @overload
    def fromParts(host: str, port: int) -> 'HostAndPort':
        """public static com.google.common.net.HostAndPort com.google.common.net.HostAndPort.fromParts(java.lang.String,int)"""
        return HostAndPort._wrap(_HostAndPort.fromParts(host, _int.valueOf(port)))

    @overload
    def getPort(self) -> int:
        """public int com.google.common.net.HostAndPort.getPort()"""
        return int._wrap(super(HostAndPort, self).getPort())

    @overload
    def getPortOrDefault(self, defaultPort: int) -> int:
        """public int com.google.common.net.HostAndPort.getPortOrDefault(int)"""
        return int._wrap(super(_HostAndPort, self).getPortOrDefault(_int.valueOf(defaultPort)))

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
        """public java.lang.String com.google.common.net.HostAndPort.toString()"""
        return str._wrap(super(HostAndPort, self).toString())

    @staticmethod
    @overload
    def fromHost(host: str) -> 'HostAndPort':
        """public static com.google.common.net.HostAndPort com.google.common.net.HostAndPort.fromHost(java.lang.String)"""
        return HostAndPort._wrap(_HostAndPort.fromHost(host))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.net.HostAndPort.hashCode()"""
        return int._wrap(super(HostAndPort, self).hashCode())

    @overload
    def getHost(self) -> str:
        """public java.lang.String com.google.common.net.HostAndPort.getHost()"""
        return str._wrap(super(HostAndPort, self).getHost())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, other: object) -> bool:
        """public boolean com.google.common.net.HostAndPort.equals(java.lang.Object)"""
        return bool._wrap(super(_HostAndPort, self).equals(other))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def withDefaultPort(self, defaultPort: int) -> 'HostAndPort':
        """public com.google.common.net.HostAndPort com.google.common.net.HostAndPort.withDefaultPort(int)"""
        return 'HostAndPort'._wrap(super(_HostAndPort, self).withDefaultPort(_int.valueOf(defaultPort)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def hasPort(self) -> bool:
        """public boolean com.google.common.net.HostAndPort.hasPort()"""
        return bool._wrap(super(HostAndPort, self).hasPort())

    @staticmethod
    @overload
    def fromString(hostPortString: str) -> 'HostAndPort':
        """public static com.google.common.net.HostAndPort com.google.common.net.HostAndPort.fromString(java.lang.String)"""
        return HostAndPort._wrap(_HostAndPort.fromString(hostPortString))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.google.common.net.UrlEscapers
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.google.common.escape.Escaper as _Escaper
_Escaper = _Escaper
import java.lang.Integer as _int
try:
    from pygcommon import escape
except ImportError:
    escape = _import_once("pygcommon.escape")

import com.google.common.net.UrlEscapers as _UrlEscapers
_UrlEscapers = _UrlEscapers
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UrlEscapers():
    """com.google.common.net.UrlEscapers"""
 
    @staticmethod
    def _wrap(java_value: _UrlEscapers) -> 'UrlEscapers':
        return UrlEscapers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UrlEscapers):
        """
        Dynamic initializer for UrlEscapers.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UrlEscapers__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UrlEscapers__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def urlPathSegmentEscaper() -> 'escape.Escaper':
        """public static com.google.common.escape.Escaper com.google.common.net.UrlEscapers.urlPathSegmentEscaper()"""
        return escape.Escaper._wrap(_UrlEscapers.urlPathSegmentEscaper())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def urlFormParameterEscaper() -> 'escape.Escaper':
        """public static com.google.common.escape.Escaper com.google.common.net.UrlEscapers.urlFormParameterEscaper()"""
        return escape.Escaper._wrap(_UrlEscapers.urlFormParameterEscaper())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def urlFragmentEscaper() -> 'escape.Escaper':
        """public static com.google.common.escape.Escaper com.google.common.net.UrlEscapers.urlFragmentEscaper()"""
        return escape.Escaper._wrap(_UrlEscapers.urlFragmentEscaper())

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.net.HttpHeaders
import com.google.common.net.HttpHeaders as _HttpHeaders
_HttpHeaders = _HttpHeaders
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HttpHeaders():
    """com.google.common.net.HttpHeaders"""
 
    @staticmethod
    def _wrap(java_value: _HttpHeaders) -> 'HttpHeaders':
        return HttpHeaders(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HttpHeaders):
        """
        Dynamic initializer for HttpHeaders.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HttpHeaders__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HttpHeaders__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.net.InetAddresses$TeredoInfo
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.net.Inet4Address as Inet4Address
import java.lang.Integer as _int
import com.google.common.net.InetAddresses as _InetAddresses_TeredoInfo
_TeredoInfo = _InetAddresses_TeredoInfo.TeredoInfo
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.net.Inet4Address as _Inet4Address
_Inet4Address = _Inet4Address
import java.lang.Class as _Class
_Class = _Class
 
class TeredoInfo():
    """com.google.common.net.InetAddresses.TeredoInfo"""
 
    @staticmethod
    def _wrap(java_value: _TeredoInfo) -> 'TeredoInfo':
        return TeredoInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TeredoInfo):
        """
        Dynamic initializer for TeredoInfo.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TeredoInfo__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TeredoInfo__wrapper":
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

    @overload
    def getPort(self) -> int:
        """public int com.google.common.net.InetAddresses$TeredoInfo.getPort()"""
        return int._wrap(super(TeredoInfo, self).getPort())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getClient(self) -> 'Inet4Address':
        """public java.net.Inet4Address com.google.common.net.InetAddresses$TeredoInfo.getClient()"""
        return 'Inet4Address'._wrap(super(TeredoInfo, self).getClient())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, server: 'Inet4Address', client: 'Inet4Address', port: int, flags: int):
        """public com.google.common.net.InetAddresses$TeredoInfo(java.net.Inet4Address,java.net.Inet4Address,int,int)"""
        val = _TeredoInfo(server, client, _int.valueOf(port), _int.valueOf(flags))
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

    @overload
    def getServer(self) -> 'Inet4Address':
        """public java.net.Inet4Address com.google.common.net.InetAddresses$TeredoInfo.getServer()"""
        return 'Inet4Address'._wrap(super(TeredoInfo, self).getServer())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getFlags(self) -> int:
        """public int com.google.common.net.InetAddresses$TeredoInfo.getFlags()"""
        return int._wrap(super(TeredoInfo, self).getFlags())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.net.InternetDomainName
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.collect.ImmutableList as _ImmutableList
_ImmutableList = _ImmutableList
import java.lang.String as _String
_String = _String
import java.lang.String as _string
try:
    import pygcollect
except ImportError:
    pygcollect = _import_once("pygcollect")

import java.lang.Integer as _int
import com.google.common.net.InternetDomainName as _InternetDomainName
_InternetDomainName = _InternetDomainName
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InternetDomainName():
    """com.google.common.net.InternetDomainName"""
 
    @staticmethod
    def _wrap(java_value: _InternetDomainName) -> 'InternetDomainName':
        return InternetDomainName(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InternetDomainName):
        """
        Dynamic initializer for InternetDomainName.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InternetDomainName__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InternetDomainName__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def child(self, leftParts: str) -> 'InternetDomainName':
        """public com.google.common.net.InternetDomainName com.google.common.net.InternetDomainName.child(java.lang.String)"""
        return 'InternetDomainName'._wrap(super(_InternetDomainName, self).child(leftParts))

    @overload
    def isTopPrivateDomain(self) -> bool:
        """public boolean com.google.common.net.InternetDomainName.isTopPrivateDomain()"""
        return bool._wrap(super(InternetDomainName, self).isTopPrivateDomain())

    @overload
    def hasRegistrySuffix(self) -> bool:
        """public boolean com.google.common.net.InternetDomainName.hasRegistrySuffix()"""
        return bool._wrap(super(InternetDomainName, self).hasRegistrySuffix())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.net.InternetDomainName.toString()"""
        return str._wrap(super(InternetDomainName, self).toString())

    @overload
    def topPrivateDomain(self) -> 'InternetDomainName':
        """public com.google.common.net.InternetDomainName com.google.common.net.InternetDomainName.topPrivateDomain()"""
        return 'InternetDomainName'._wrap(super(InternetDomainName, self).topPrivateDomain())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def parent(self) -> 'InternetDomainName':
        """public com.google.common.net.InternetDomainName com.google.common.net.InternetDomainName.parent()"""
        return 'InternetDomainName'._wrap(super(InternetDomainName, self).parent())

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
    def isValid(name: str) -> bool:
        """public static boolean com.google.common.net.InternetDomainName.isValid(java.lang.String)"""
        return bool._wrap(_InternetDomainName.isValid(name))

    @overload
    def hasPublicSuffix(self) -> bool:
        """public boolean com.google.common.net.InternetDomainName.hasPublicSuffix()"""
        return bool._wrap(super(InternetDomainName, self).hasPublicSuffix())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.net.InternetDomainName.hashCode()"""
        return int._wrap(super(InternetDomainName, self).hashCode())

    @overload
    def registrySuffix(self) -> 'InternetDomainName':
        """public com.google.common.net.InternetDomainName com.google.common.net.InternetDomainName.registrySuffix()"""
        return 'InternetDomainName'._wrap(super(InternetDomainName, self).registrySuffix())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def isRegistrySuffix(self) -> bool:
        """public boolean com.google.common.net.InternetDomainName.isRegistrySuffix()"""
        return bool._wrap(super(InternetDomainName, self).isRegistrySuffix())

    @overload
    def topDomainUnderRegistrySuffix(self) -> 'InternetDomainName':
        """public com.google.common.net.InternetDomainName com.google.common.net.InternetDomainName.topDomainUnderRegistrySuffix()"""
        return 'InternetDomainName'._wrap(super(InternetDomainName, self).topDomainUnderRegistrySuffix())

    @overload
    def isUnderRegistrySuffix(self) -> bool:
        """public boolean com.google.common.net.InternetDomainName.isUnderRegistrySuffix()"""
        return bool._wrap(super(InternetDomainName, self).isUnderRegistrySuffix())

    @overload
    def equals(self, object: object) -> bool:
        """public boolean com.google.common.net.InternetDomainName.equals(java.lang.Object)"""
        return bool._wrap(super(_InternetDomainName, self).equals(object))

    @overload
    def hasParent(self) -> bool:
        """public boolean com.google.common.net.InternetDomainName.hasParent()"""
        return bool._wrap(super(InternetDomainName, self).hasParent())

    @overload
    def isUnderPublicSuffix(self) -> bool:
        """public boolean com.google.common.net.InternetDomainName.isUnderPublicSuffix()"""
        return bool._wrap(super(InternetDomainName, self).isUnderPublicSuffix())

    @staticmethod
    @overload
    def from(domain: str) -> 'InternetDomainName':
        """public static com.google.common.net.InternetDomainName com.google.common.net.InternetDomainName.from(java.lang.String)"""
        return InternetDomainName._wrap(_InternetDomainName.from(domain))

    @overload
    def parts(self) -> 'pygcollect.ImmutableList':
        """public com.google.common.collect.ImmutableList<java.lang.String> com.google.common.net.InternetDomainName.parts()"""
        return 'pygcollect.ImmutableList'._wrap(super(InternetDomainName, self).parts())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def isPublicSuffix(self) -> bool:
        """public boolean com.google.common.net.InternetDomainName.isPublicSuffix()"""
        return bool._wrap(super(InternetDomainName, self).isPublicSuffix())

    @overload
    def publicSuffix(self) -> 'InternetDomainName':
        """public com.google.common.net.InternetDomainName com.google.common.net.InternetDomainName.publicSuffix()"""
        return 'InternetDomainName'._wrap(super(InternetDomainName, self).publicSuffix())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isTopDomainUnderRegistrySuffix(self) -> bool:
        """public boolean com.google.common.net.InternetDomainName.isTopDomainUnderRegistrySuffix()"""
        return bool._wrap(super(InternetDomainName, self).isTopDomainUnderRegistrySuffix()) 
 
 
# CLASS: com.google.common.net.HostSpecifier
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
import com.google.common.net.HostSpecifier as _HostSpecifier
_HostSpecifier = _HostSpecifier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HostSpecifier():
    """com.google.common.net.HostSpecifier"""
 
    @staticmethod
    def _wrap(java_value: _HostSpecifier) -> 'HostSpecifier':
        return HostSpecifier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HostSpecifier):
        """
        Dynamic initializer for HostSpecifier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HostSpecifier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HostSpecifier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def isValid(specifier: str) -> bool:
        """public static boolean com.google.common.net.HostSpecifier.isValid(java.lang.String)"""
        return bool._wrap(_HostSpecifier.isValid(specifier))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.net.HostSpecifier.toString()"""
        return str._wrap(super(HostSpecifier, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.net.HostSpecifier.hashCode()"""
        return int._wrap(super(HostSpecifier, self).hashCode())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def fromValid(specifier: str) -> 'HostSpecifier':
        """public static com.google.common.net.HostSpecifier com.google.common.net.HostSpecifier.fromValid(java.lang.String)"""
        return HostSpecifier._wrap(_HostSpecifier.fromValid(specifier))

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, other: object) -> bool:
        """public boolean com.google.common.net.HostSpecifier.equals(java.lang.Object)"""
        return bool._wrap(super(_HostSpecifier, self).equals(other))

    @staticmethod
    @overload
    def from(specifier: str) -> 'HostSpecifier':
        """public static com.google.common.net.HostSpecifier com.google.common.net.HostSpecifier.from(java.lang.String) throws java.text.ParseException"""
        return HostSpecifier._wrap(_HostSpecifier.from(specifier))