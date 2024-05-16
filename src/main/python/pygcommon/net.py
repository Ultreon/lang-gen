from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.net.UrlEscapers as __UrlEscapers
__UrlEscapers = __UrlEscapers
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pygcommon import escape
except ImportError:
    escape = __import_once__("pygcommon.escape")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.google.common.escape.Escaper as __Escaper
__Escaper = __Escaper
from builtins import int
 
class UrlEscapers():
    """com.google.common.net.UrlEscapers"""
 
    @staticmethod
    def __wrap(java_value: __UrlEscapers) -> 'UrlEscapers':
        return UrlEscapers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UrlEscapers):
        """
        Dynamic initializer for UrlEscapers.
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
 
    @staticmethod
    @overload
    def urlFormParameterEscaper() -> 'escape.Escaper':
        """public static com.google.common.escape.Escaper com.google.common.net.UrlEscapers.urlFormParameterEscaper()"""
        return escape.Escaper.__wrap(__UrlEscapers.urlFormParameterEscaper())

    @staticmethod
    @overload
    def urlFragmentEscaper() -> 'escape.Escaper':
        """public static com.google.common.escape.Escaper com.google.common.net.UrlEscapers.urlFragmentEscaper()"""
        return escape.Escaper.__wrap(__UrlEscapers.urlFragmentEscaper())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def urlPathSegmentEscaper() -> 'escape.Escaper':
        """public static com.google.common.escape.Escaper com.google.common.net.UrlEscapers.urlPathSegmentEscaper()"""
        return escape.Escaper.__wrap(__UrlEscapers.urlPathSegmentEscaper())

 
 
 
# CLASS: com.google.common.net.UrlEscapers
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.net.UrlEscapers as __UrlEscapers
__UrlEscapers = __UrlEscapers
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pygcommon import escape
except ImportError:
    escape = __import_once__("pygcommon.escape")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.google.common.escape.Escaper as __Escaper
__Escaper = __Escaper
from builtins import int
 
class UrlEscapers():
    """com.google.common.net.UrlEscapers"""
 
    @staticmethod
    def __wrap(java_value: __UrlEscapers) -> 'UrlEscapers':
        return UrlEscapers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UrlEscapers):
        """
        Dynamic initializer for UrlEscapers.
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
 
    @staticmethod
    @overload
    def urlFormParameterEscaper() -> 'escape.Escaper':
        """public static com.google.common.escape.Escaper com.google.common.net.UrlEscapers.urlFormParameterEscaper()"""
        return escape.Escaper.__wrap(__UrlEscapers.urlFormParameterEscaper())

    @staticmethod
    @overload
    def urlFragmentEscaper() -> 'escape.Escaper':
        """public static com.google.common.escape.Escaper com.google.common.net.UrlEscapers.urlFragmentEscaper()"""
        return escape.Escaper.__wrap(__UrlEscapers.urlFragmentEscaper())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def urlPathSegmentEscaper() -> 'escape.Escaper':
        """public static com.google.common.escape.Escaper com.google.common.net.UrlEscapers.urlPathSegmentEscaper()"""
        return escape.Escaper.__wrap(__UrlEscapers.urlPathSegmentEscaper())

 
 
 
# CLASS: com.google.common.net.UrlEscapers 
 
 
# CLASS: com.google.common.net.InternetDomainName
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.net.InternetDomainName as __InternetDomainName
__InternetDomainName = __InternetDomainName
import com.google.common.collect.ImmutableList as __ImmutableList
__ImmutableList = __ImmutableList
try:
    import pygcollect
except ImportError:
    pygcollect = __import_once__("pygcollect")

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
 
class InternetDomainName():
    """com.google.common.net.InternetDomainName"""
 
    @staticmethod
    def __wrap(java_value: __InternetDomainName) -> 'InternetDomainName':
        return InternetDomainName(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InternetDomainName):
        """
        Dynamic initializer for InternetDomainName.
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
    def topPrivateDomain(self) -> 'InternetDomainName':
        """public com.google.common.net.InternetDomainName com.google.common.net.InternetDomainName.topPrivateDomain()"""
        return 'InternetDomainName'.__wrap(super(InternetDomainName, self).topPrivateDomain())

    @overload
    def hasParent(self) -> bool:
        """public boolean com.google.common.net.InternetDomainName.hasParent()"""
        return bool.__wrap(super(InternetDomainName, self).hasParent())

    @overload
    def isPublicSuffix(self) -> bool:
        """public boolean com.google.common.net.InternetDomainName.isPublicSuffix()"""
        return bool.__wrap(super(InternetDomainName, self).isPublicSuffix())

    @overload
    def topDomainUnderRegistrySuffix(self) -> 'InternetDomainName':
        """public com.google.common.net.InternetDomainName com.google.common.net.InternetDomainName.topDomainUnderRegistrySuffix()"""
        return 'InternetDomainName'.__wrap(super(InternetDomainName, self).topDomainUnderRegistrySuffix())

    @overload
    def equals(self, object: object) -> bool:
        """public boolean com.google.common.net.InternetDomainName.equals(java.lang.Object)"""
        return bool.__wrap(super(__InternetDomainName, self).equals(object))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.net.InternetDomainName.hashCode()"""
        return int.__wrap(super(InternetDomainName, self).hashCode())

    @overload
    def parts(self) -> 'pygcollect.ImmutableList':
        """public com.google.common.collect.ImmutableList<java.lang.String> com.google.common.net.InternetDomainName.parts()"""
        return 'pygcollect.ImmutableList'.__wrap(super(InternetDomainName, self).parts())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def isTopDomainUnderRegistrySuffix(self) -> bool:
        """public boolean com.google.common.net.InternetDomainName.isTopDomainUnderRegistrySuffix()"""
        return bool.__wrap(super(InternetDomainName, self).isTopDomainUnderRegistrySuffix())

    @staticmethod
    @overload
    def from(domain: str) -> 'InternetDomainName':
        """public static com.google.common.net.InternetDomainName com.google.common.net.InternetDomainName.from(java.lang.String)"""
        return InternetDomainName.__wrap(__InternetDomainName.from(domain))

    @overload
    def child(self, leftParts: str) -> 'InternetDomainName':
        """public com.google.common.net.InternetDomainName com.google.common.net.InternetDomainName.child(java.lang.String)"""
        return 'InternetDomainName'.__wrap(super(__InternetDomainName, self).child(leftParts))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.net.InternetDomainName.toString()"""
        return str.__wrap(super(InternetDomainName, self).toString())

    @overload
    def isUnderPublicSuffix(self) -> bool:
        """public boolean com.google.common.net.InternetDomainName.isUnderPublicSuffix()"""
        return bool.__wrap(super(InternetDomainName, self).isUnderPublicSuffix())

    @overload
    def hasRegistrySuffix(self) -> bool:
        """public boolean com.google.common.net.InternetDomainName.hasRegistrySuffix()"""
        return bool.__wrap(super(InternetDomainName, self).hasRegistrySuffix())

    @overload
    def isTopPrivateDomain(self) -> bool:
        """public boolean com.google.common.net.InternetDomainName.isTopPrivateDomain()"""
        return bool.__wrap(super(InternetDomainName, self).isTopPrivateDomain())

    @overload
    def isUnderRegistrySuffix(self) -> bool:
        """public boolean com.google.common.net.InternetDomainName.isUnderRegistrySuffix()"""
        return bool.__wrap(super(InternetDomainName, self).isUnderRegistrySuffix())

    @overload
    def publicSuffix(self) -> 'InternetDomainName':
        """public com.google.common.net.InternetDomainName com.google.common.net.InternetDomainName.publicSuffix()"""
        return 'InternetDomainName'.__wrap(super(InternetDomainName, self).publicSuffix())

    @overload
    def hasPublicSuffix(self) -> bool:
        """public boolean com.google.common.net.InternetDomainName.hasPublicSuffix()"""
        return bool.__wrap(super(InternetDomainName, self).hasPublicSuffix())

    @overload
    def registrySuffix(self) -> 'InternetDomainName':
        """public com.google.common.net.InternetDomainName com.google.common.net.InternetDomainName.registrySuffix()"""
        return 'InternetDomainName'.__wrap(super(InternetDomainName, self).registrySuffix())

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
    def isRegistrySuffix(self) -> bool:
        """public boolean com.google.common.net.InternetDomainName.isRegistrySuffix()"""
        return bool.__wrap(super(InternetDomainName, self).isRegistrySuffix())

    @staticmethod
    @overload
    def isValid(name: str) -> bool:
        """public static boolean com.google.common.net.InternetDomainName.isValid(java.lang.String)"""
        return bool.__wrap(__InternetDomainName.isValid(name))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def parent(self) -> 'InternetDomainName':
        """public com.google.common.net.InternetDomainName com.google.common.net.InternetDomainName.parent()"""
        return 'InternetDomainName'.__wrap(super(InternetDomainName, self).parent()) 
 
 
# CLASS: com.google.common.net.InetAddresses$TeredoInfo
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.net.Inet4Address as __Inet4Address
__Inet4Address = __Inet4Address
import java.net.Inet4Address as Inet4Address
import com.google.common.net.InetAddresses as __InetAddresses_TeredoInfo
__TeredoInfo = __InetAddresses_TeredoInfo.TeredoInfo
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TeredoInfo():
    """com.google.common.net.InetAddresses.TeredoInfo"""
 
    @staticmethod
    def __wrap(java_value: __TeredoInfo) -> 'TeredoInfo':
        return TeredoInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TeredoInfo):
        """
        Dynamic initializer for TeredoInfo.
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
    def __init__(self, server: 'Inet4Address', client: 'Inet4Address', port: int, flags: int):
        """public com.google.common.net.InetAddresses$TeredoInfo(java.net.Inet4Address,java.net.Inet4Address,int,int)"""
        val = __TeredoInfo(server, client, __int.valueOf(port), __int.valueOf(flags))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getClient(self) -> 'Inet4Address':
        """public java.net.Inet4Address com.google.common.net.InetAddresses$TeredoInfo.getClient()"""
        return 'Inet4Address'.__wrap(super(TeredoInfo, self).getClient())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getFlags(self) -> int:
        """public int com.google.common.net.InetAddresses$TeredoInfo.getFlags()"""
        return int.__wrap(super(TeredoInfo, self).getFlags())

    @overload
    def getServer(self) -> 'Inet4Address':
        """public java.net.Inet4Address com.google.common.net.InetAddresses$TeredoInfo.getServer()"""
        return 'Inet4Address'.__wrap(super(TeredoInfo, self).getServer())

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
    def getPort(self) -> int:
        """public int com.google.common.net.InetAddresses$TeredoInfo.getPort()"""
        return int.__wrap(super(TeredoInfo, self).getPort())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.google.common.net.HttpHeaders
from builtins import str
import com.google.common.net.HttpHeaders as __HttpHeaders
__HttpHeaders = __HttpHeaders
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
 
class HttpHeaders():
    """com.google.common.net.HttpHeaders"""
 
    @staticmethod
    def __wrap(java_value: __HttpHeaders) -> 'HttpHeaders':
        return HttpHeaders(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HttpHeaders):
        """
        Dynamic initializer for HttpHeaders.
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.net.InetAddresses
import java.net.InetAddress as __InetAddress
__InetAddress = __InetAddress
from builtins import str
from pyquantum_helper import override
import java.net.InetAddress as InetAddress
import java.lang.Object as __object
from builtins import type
import java.net.Inet4Address as __Inet4Address
__Inet4Address = __Inet4Address
import java.net.Inet4Address as Inet4Address
import java.math.BigInteger as BigInteger
import com.google.common.net.InetAddresses as __InetAddresses_TeredoInfo
__TeredoInfo = __InetAddresses_TeredoInfo.TeredoInfo
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.net.Inet6Address as __Inet6Address
__Inet6Address = __Inet6Address
import java.lang.Object as __Object
__Object = __Object
import java.net.Inet6Address as Inet6Address
import com.google.common.net.InetAddresses as __InetAddresses
__InetAddresses = __InetAddresses
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InetAddresses():
    """com.google.common.net.InetAddresses"""
 
    @staticmethod
    def __wrap(java_value: __InetAddresses) -> 'InetAddresses':
        return InetAddresses(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InetAddresses):
        """
        Dynamic initializer for InetAddresses.
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
    def toBigInteger(toBigInteger) -> 'BigInteger':
        """public static java.math.BigInteger com.google.common.net.InetAddresses.toBigInteger(java.net.InetAddress)"""
        return __transform(__address.InetAddresses(address: 'InetAddress')).'BigInteger'Value()

    @staticmethod
    @overload
    def fromLittleEndianByteArray(addr: bytes) -> 'InetAddress':
        """public static java.net.InetAddress com.google.common.net.InetAddresses.fromLittleEndianByteArray(byte[]) throws java.net.UnknownHostException"""
        return InetAddress.__wrap(__InetAddresses.fromLittleEndianByteArray(bytes))

    @staticmethod
    @overload
    def getEmbeddedIPv4ClientAddress(ip: 'Inet6Address') -> 'Inet4Address':
        """public static java.net.Inet4Address com.google.common.net.InetAddresses.getEmbeddedIPv4ClientAddress(java.net.Inet6Address)"""
        return Inet4Address.__wrap(__InetAddresses.getEmbeddedIPv4ClientAddress(ip))

    @staticmethod
    @overload
    def fromIPv4BigInteger(address: 'BigInteger') -> 'Inet4Address':
        """public static java.net.Inet4Address com.google.common.net.InetAddresses.fromIPv4BigInteger(java.math.BigInteger)"""
        return Inet4Address.__wrap(__InetAddresses.fromIPv4BigInteger(address))

    @staticmethod
    @overload
    def get6to4IPv4Address(ip: 'Inet6Address') -> 'Inet4Address':
        """public static java.net.Inet4Address com.google.common.net.InetAddresses.get6to4IPv4Address(java.net.Inet6Address)"""
        return Inet4Address.__wrap(__InetAddresses.get6to4IPv4Address(ip))

    @staticmethod
    @overload
    def decrement(address: 'InetAddress') -> 'InetAddress':
        """public static java.net.InetAddress com.google.common.net.InetAddresses.decrement(java.net.InetAddress)"""
        return InetAddress.__wrap(__InetAddresses.decrement(address))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getTeredoInfo(ip: 'Inet6Address') -> 'TeredoInfo':
        """public static com.google.common.net.InetAddresses$TeredoInfo com.google.common.net.InetAddresses.getTeredoInfo(java.net.Inet6Address)"""
        return TeredoInfo.__wrap(__InetAddresses.getTeredoInfo(ip))

    @staticmethod
    @overload
    def hasEmbeddedIPv4ClientAddress(ip: 'Inet6Address') -> bool:
        """public static boolean com.google.common.net.InetAddresses.hasEmbeddedIPv4ClientAddress(java.net.Inet6Address)"""
        return bool.__wrap(__InetAddresses.hasEmbeddedIPv4ClientAddress(ip))

    @staticmethod
    @overload
    def forString(ipString: str) -> 'InetAddress':
        """public static java.net.InetAddress com.google.common.net.InetAddresses.forString(java.lang.String)"""
        return InetAddress.__wrap(__InetAddresses.forString(ipString))

    @staticmethod
    @overload
    def toUriString(ip: 'InetAddress') -> str:
        """public static java.lang.String com.google.common.net.InetAddresses.toUriString(java.net.InetAddress)"""
        return str.__wrap(__InetAddresses.toUriString(ip))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def isMappedIPv4Address(ipString: str) -> bool:
        """public static boolean com.google.common.net.InetAddresses.isMappedIPv4Address(java.lang.String)"""
        return bool.__wrap(__InetAddresses.isMappedIPv4Address(ipString))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def isIsatapAddress(ip: 'Inet6Address') -> bool:
        """public static boolean com.google.common.net.InetAddresses.isIsatapAddress(java.net.Inet6Address)"""
        return bool.__wrap(__InetAddresses.isIsatapAddress(ip))

    @staticmethod
    @overload
    def getCoercedIPv4Address(ip: 'InetAddress') -> 'Inet4Address':
        """public static java.net.Inet4Address com.google.common.net.InetAddresses.getCoercedIPv4Address(java.net.InetAddress)"""
        return Inet4Address.__wrap(__InetAddresses.getCoercedIPv4Address(ip))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def toAddrString(ip: 'InetAddress') -> str:
        """public static java.lang.String com.google.common.net.InetAddresses.toAddrString(java.net.InetAddress)"""
        return str.__wrap(__InetAddresses.toAddrString(ip))

    @staticmethod
    @overload
    def coerceToInteger(ip: 'InetAddress') -> int:
        """public static int com.google.common.net.InetAddresses.coerceToInteger(java.net.InetAddress)"""
        return int.__wrap(__InetAddresses.coerceToInteger(ip))

    @staticmethod
    @overload
    def isUriInetAddress(ipString: str) -> bool:
        """public static boolean com.google.common.net.InetAddresses.isUriInetAddress(java.lang.String)"""
        return bool.__wrap(__InetAddresses.isUriInetAddress(ipString))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getCompatIPv4Address(ip: 'Inet6Address') -> 'Inet4Address':
        """public static java.net.Inet4Address com.google.common.net.InetAddresses.getCompatIPv4Address(java.net.Inet6Address)"""
        return Inet4Address.__wrap(__InetAddresses.getCompatIPv4Address(ip))

    @staticmethod
    @overload
    def increment(address: 'InetAddress') -> 'InetAddress':
        """public static java.net.InetAddress com.google.common.net.InetAddresses.increment(java.net.InetAddress)"""
        return InetAddress.__wrap(__InetAddresses.increment(address))

    @staticmethod
    @overload
    def isInetAddress(ipString: str) -> bool:
        """public static boolean com.google.common.net.InetAddresses.isInetAddress(java.lang.String)"""
        return bool.__wrap(__InetAddresses.isInetAddress(ipString))

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
    def fromIPv6BigInteger(address: 'BigInteger') -> 'Inet6Address':
        """public static java.net.Inet6Address com.google.common.net.InetAddresses.fromIPv6BigInteger(java.math.BigInteger)"""
        return Inet6Address.__wrap(__InetAddresses.fromIPv6BigInteger(address))

    @staticmethod
    @overload
    def isCompatIPv4Address(ip: 'Inet6Address') -> bool:
        """public static boolean com.google.common.net.InetAddresses.isCompatIPv4Address(java.net.Inet6Address)"""
        return bool.__wrap(__InetAddresses.isCompatIPv4Address(ip))

    @staticmethod
    @overload
    def getIsatapIPv4Address(ip: 'Inet6Address') -> 'Inet4Address':
        """public static java.net.Inet4Address com.google.common.net.InetAddresses.getIsatapIPv4Address(java.net.Inet6Address)"""
        return Inet4Address.__wrap(__InetAddresses.getIsatapIPv4Address(ip))

    @staticmethod
    @overload
    def forUriString(hostAddr: str) -> 'InetAddress':
        """public static java.net.InetAddress com.google.common.net.InetAddresses.forUriString(java.lang.String)"""
        return InetAddress.__wrap(__InetAddresses.forUriString(hostAddr))

    @staticmethod
    @overload
    def isTeredoAddress(ip: 'Inet6Address') -> bool:
        """public static boolean com.google.common.net.InetAddresses.isTeredoAddress(java.net.Inet6Address)"""
        return bool.__wrap(__InetAddresses.isTeredoAddress(ip))

    @staticmethod
    @overload
    def isMaximum(address: 'InetAddress') -> bool:
        """public static boolean com.google.common.net.InetAddresses.isMaximum(java.net.InetAddress)"""
        return bool.__wrap(__InetAddresses.isMaximum(address))

    @staticmethod
    @overload
    def is6to4Address(ip: 'Inet6Address') -> bool:
        """public static boolean com.google.common.net.InetAddresses.is6to4Address(java.net.Inet6Address)"""
        return bool.__wrap(__InetAddresses.is6to4Address(ip))

    @staticmethod
    @overload
    def fromInteger(address: int) -> 'Inet4Address':
        """public static java.net.Inet4Address com.google.common.net.InetAddresses.fromInteger(int)"""
        return Inet4Address.__wrap(__InetAddresses.fromInteger(__int.valueOf(address)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.google.common.net.HostAndPort
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.google.common.net.HostAndPort as __HostAndPort
__HostAndPort = __HostAndPort
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
 
class HostAndPort(__Serializable, Serializable):
    """com.google.common.net.HostAndPort"""
 
    @staticmethod
    def __wrap(java_value: __HostAndPort) -> 'HostAndPort':
        return HostAndPort(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HostAndPort):
        """
        Dynamic initializer for HostAndPort.
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
    def requireBracketsForIPv6(self) -> 'HostAndPort':
        """public com.google.common.net.HostAndPort com.google.common.net.HostAndPort.requireBracketsForIPv6()"""
        return 'HostAndPort'.__wrap(super(HostAndPort, self).requireBracketsForIPv6())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def fromString(hostPortString: str) -> 'HostAndPort':
        """public static com.google.common.net.HostAndPort com.google.common.net.HostAndPort.fromString(java.lang.String)"""
        return HostAndPort.__wrap(__HostAndPort.fromString(hostPortString))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getPortOrDefault(self, defaultPort: int) -> int:
        """public int com.google.common.net.HostAndPort.getPortOrDefault(int)"""
        return int.__wrap(super(__HostAndPort, self).getPortOrDefault(__int.valueOf(defaultPort)))

    @overload
    def equals(self, other: object) -> bool:
        """public boolean com.google.common.net.HostAndPort.equals(java.lang.Object)"""
        return bool.__wrap(super(__HostAndPort, self).equals(other))

    @overload
    def getPort(self) -> int:
        """public int com.google.common.net.HostAndPort.getPort()"""
        return int.__wrap(super(HostAndPort, self).getPort())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.net.HostAndPort.toString()"""
        return str.__wrap(super(HostAndPort, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def fromHost(host: str) -> 'HostAndPort':
        """public static com.google.common.net.HostAndPort com.google.common.net.HostAndPort.fromHost(java.lang.String)"""
        return HostAndPort.__wrap(__HostAndPort.fromHost(host))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def hasPort(self) -> bool:
        """public boolean com.google.common.net.HostAndPort.hasPort()"""
        return bool.__wrap(super(HostAndPort, self).hasPort())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.net.HostAndPort.hashCode()"""
        return int.__wrap(super(HostAndPort, self).hashCode())

    @overload
    def getHost(self) -> str:
        """public java.lang.String com.google.common.net.HostAndPort.getHost()"""
        return str.__wrap(super(HostAndPort, self).getHost())

    @staticmethod
    @overload
    def fromParts(host: str, port: int) -> 'HostAndPort':
        """public static com.google.common.net.HostAndPort com.google.common.net.HostAndPort.fromParts(java.lang.String,int)"""
        return HostAndPort.__wrap(__HostAndPort.fromParts(host, __int.valueOf(port)))

    @overload
    def withDefaultPort(self, defaultPort: int) -> 'HostAndPort':
        """public com.google.common.net.HostAndPort com.google.common.net.HostAndPort.withDefaultPort(int)"""
        return 'HostAndPort'.__wrap(super(__HostAndPort, self).withDefaultPort(__int.valueOf(defaultPort))) 
 
 
# CLASS: com.google.common.net.HostSpecifier
import com.google.common.net.HostSpecifier as __HostSpecifier
__HostSpecifier = __HostSpecifier
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
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
 
class HostSpecifier():
    """com.google.common.net.HostSpecifier"""
 
    @staticmethod
    def __wrap(java_value: __HostSpecifier) -> 'HostSpecifier':
        return HostSpecifier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HostSpecifier):
        """
        Dynamic initializer for HostSpecifier.
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
    def toString(self) -> str:
        """public java.lang.String com.google.common.net.HostSpecifier.toString()"""
        return str.__wrap(super(HostSpecifier, self).toString())

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
    def hashCode(self) -> int:
        """public int com.google.common.net.HostSpecifier.hashCode()"""
        return int.__wrap(super(HostSpecifier, self).hashCode())

    @overload
    def equals(self, other: object) -> bool:
        """public boolean com.google.common.net.HostSpecifier.equals(java.lang.Object)"""
        return bool.__wrap(super(__HostSpecifier, self).equals(other))

    @staticmethod
    @overload
    def isValid(specifier: str) -> bool:
        """public static boolean com.google.common.net.HostSpecifier.isValid(java.lang.String)"""
        return bool.__wrap(__HostSpecifier.isValid(specifier))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def from(specifier: str) -> 'HostSpecifier':
        """public static com.google.common.net.HostSpecifier com.google.common.net.HostSpecifier.from(java.lang.String) throws java.text.ParseException"""
        return HostSpecifier.__wrap(__HostSpecifier.from(specifier))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def fromValid(specifier: str) -> 'HostSpecifier':
        """public static com.google.common.net.HostSpecifier com.google.common.net.HostSpecifier.fromValid(java.lang.String)"""
        return HostSpecifier.__wrap(__HostSpecifier.fromValid(specifier))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.net.HttpHeaders$ReferrerPolicyValues
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
import com.google.common.net.HttpHeaders as __HttpHeaders_ReferrerPolicyValues
__ReferrerPolicyValues = __HttpHeaders_ReferrerPolicyValues.ReferrerPolicyValues
from builtins import int
 
class ReferrerPolicyValues():
    """com.google.common.net.HttpHeaders.ReferrerPolicyValues"""
 
    @staticmethod
    def __wrap(java_value: __ReferrerPolicyValues) -> 'ReferrerPolicyValues':
        return ReferrerPolicyValues(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReferrerPolicyValues):
        """
        Dynamic initializer for ReferrerPolicyValues.
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.google.common.net.MediaType
from pyquantum_helper import import_once as __import_once__
import com.google.common.net.MediaType as __MediaType
__MediaType = __MediaType
try:
    from pygcommon import base
except ImportError:
    base = __import_once__("pygcommon.base")

from builtins import str
from pyquantum_helper import override
import java.nio.charset.Charset as Charset
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
try:
    import pygcollect
except ImportError:
    pygcollect = __import_once__("pygcollect")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import com.google.common.collect.ImmutableListMultimap as __ImmutableListMultimap
__ImmutableListMultimap = __ImmutableListMultimap
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.google.common.base.Optional as __Optional
__Optional = __Optional
from builtins import int
 
class MediaType():
    """com.google.common.net.MediaType"""
 
    @staticmethod
    def __wrap(java_value: __MediaType) -> 'MediaType':
        return MediaType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MediaType):
        """
        Dynamic initializer for MediaType.
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
    def hasWildcard(self) -> bool:
        """public boolean com.google.common.net.MediaType.hasWildcard()"""
        return bool.__wrap(super(MediaType, self).hasWildcard())

    @overload
    def charset(self) -> 'base.Optional':
        """public com.google.common.base.Optional<java.nio.charset.Charset> com.google.common.net.MediaType.charset()"""
        return 'base.Optional'.__wrap(super(MediaType, self).charset())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def create(type: str, subtype: str) -> 'MediaType':
        """public static com.google.common.net.MediaType com.google.common.net.MediaType.create(java.lang.String,java.lang.String)"""
        return MediaType.__wrap(__MediaType.create(type, subtype))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def withoutParameters(self) -> 'MediaType':
        """public com.google.common.net.MediaType com.google.common.net.MediaType.withoutParameters()"""
        return 'MediaType'.__wrap(super(MediaType, self).withoutParameters())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.net.MediaType.equals(java.lang.Object)"""
        return bool.__wrap(super(__MediaType, self).equals(obj))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def parameters(self) -> 'pygcollect.ImmutableListMultimap':
        """public com.google.common.collect.ImmutableListMultimap<java.lang.String, java.lang.String> com.google.common.net.MediaType.parameters()"""
        return 'pygcollect.ImmutableListMultimap'.__wrap(super(MediaType, self).parameters())

    @overload
    def withParameters(self, parameters: 'Multimap') -> 'MediaType':
        """public com.google.common.net.MediaType com.google.common.net.MediaType.withParameters(com.google.common.collect.Multimap<java.lang.String, java.lang.String>)"""
        return 'MediaType'.__wrap(super(__MediaType, self).withParameters(parameters))

    @overload
    def is(self, mediaTypeRange: 'MediaType') -> bool:
        """public boolean com.google.common.net.MediaType.is(com.google.common.net.MediaType)"""
        return bool.__wrap(super(__MediaType, self).is(mediaTypeRange))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.net.MediaType.hashCode()"""
        return int.__wrap(super(MediaType, self).hashCode())

    @overload
    def withParameters(self, attribute: str, values: 'Iterable') -> 'MediaType':
        """public com.google.common.net.MediaType com.google.common.net.MediaType.withParameters(java.lang.String,java.lang.Iterable<java.lang.String>)"""
        return 'MediaType'.__wrap(super(__MediaType, self).withParameters(attribute, values))

    @overload
    def subtype(self) -> str:
        """public java.lang.String com.google.common.net.MediaType.subtype()"""
        return str.__wrap(super(MediaType, self).subtype())

    @overload
    def type(self) -> str:
        """public java.lang.String com.google.common.net.MediaType.type()"""
        return str.__wrap(super(MediaType, self).type())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def withCharset(self, charset: 'Charset') -> 'MediaType':
        """public com.google.common.net.MediaType com.google.common.net.MediaType.withCharset(java.nio.charset.Charset)"""
        return 'MediaType'.__wrap(super(__MediaType, self).withCharset(charset))

    @staticmethod
    @overload
    def parse(input: str) -> 'MediaType':
        """public static com.google.common.net.MediaType com.google.common.net.MediaType.parse(java.lang.String)"""
        return MediaType.__wrap(__MediaType.parse(input))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.net.MediaType.toString()"""
        return str.__wrap(super(MediaType, self).toString())

    @overload
    def withParameter(self, attribute: str, value: str) -> 'MediaType':
        """public com.google.common.net.MediaType com.google.common.net.MediaType.withParameter(java.lang.String,java.lang.String)"""
        return 'MediaType'.__wrap(super(__MediaType, self).withParameter(attribute, value)) 
 
 
# CLASS: com.google.common.net.PercentEscaper
from pyquantum_helper import import_once as __import_once__
try:
    from pygcommon import base
except ImportError:
    base = __import_once__("pygcommon.base")

from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.google.common.base.Function as __Function
__Function = __Function
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.google.common.net.PercentEscaper as __PercentEscaper
__PercentEscaper = __PercentEscaper
import java.lang.Integer as __int
from builtins import bool
import com.google.common.escape.Escaper as __Escaper
__Escaper = __Escaper
from builtins import int
 
class PercentEscaper(pygcommon.__UnicodeEscaper, escape.UnicodeEscaper):
    """com.google.common.net.PercentEscaper"""
 
    @staticmethod
    def __wrap(java_value: __PercentEscaper) -> 'PercentEscaper':
        return PercentEscaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PercentEscaper):
        """
        Dynamic initializer for PercentEscaper.
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
    def escape(self, s: str) -> str:
        """public java.lang.String com.google.common.net.PercentEscaper.escape(java.lang.String)"""
        return str.__wrap(super(__PercentEscaper, self).escape(s))

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
    def __init__(self, safeChars: str, plusForSpace: bool):
        """public com.google.common.net.PercentEscaper(java.lang.String,boolean)"""
        val = __PercentEscaper(safeChars, __boolean.valueOf(plusForSpace))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def asFunction(self) -> 'base.Function':
        """public final com.google.common.base.Function<java.lang.String, java.lang.String> com.google.common.escape.Escaper.asFunction()"""
        return 'base.Function'.__wrap(super(escape.Escaper, self).asFunction())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))