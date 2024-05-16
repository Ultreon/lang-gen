from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.client.platform.GdxPlatform as __GdxPlatform
__GdxPlatform = __GdxPlatform
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class GdxPlatform():
    """dev.ultreon.quantum.client.platform.GdxPlatform"""
 
    @staticmethod
    def __wrap(java_value: __GdxPlatform) -> 'GdxPlatform':
        return GdxPlatform(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GdxPlatform):
        """
        Dynamic initializer for GdxPlatform.
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
 
    # public static final dev.ultreon.quantum.client.platform.GdxPlatform dev.ultreon.quantum.client.platform.GdxPlatform.ANDROID
    ANDROID: 'GdxPlatform' = __wrap(__GdxPlatform.ANDROID)

    # public static final dev.ultreon.quantum.client.platform.GdxPlatform dev.ultreon.quantum.client.platform.GdxPlatform.DESKTOP
    DESKTOP: 'GdxPlatform' = __wrap(__GdxPlatform.DESKTOP)

    # public static final dev.ultreon.quantum.client.platform.GdxPlatform dev.ultreon.quantum.client.platform.GdxPlatform.WEB
    WEB: 'GdxPlatform' = __wrap(__GdxPlatform.WEB)

    # public static final dev.ultreon.quantum.client.platform.GdxPlatform dev.ultreon.quantum.client.platform.GdxPlatform.IOS
    IOS: 'GdxPlatform' = __wrap(__GdxPlatform.IOS)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'GdxPlatform':
        """public static dev.ultreon.quantum.client.platform.GdxPlatform dev.ultreon.quantum.client.platform.GdxPlatform.valueOf(java.lang.String)"""
        return GdxPlatform.__wrap(__GdxPlatform.valueOf(arg0))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @overload
    def getDisplayName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.platform.GdxPlatform.getDisplayName()"""
        return str.__wrap(super(GdxPlatform, self).getDisplayName())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

    @staticmethod
    @overload
    def values() -> List['GdxPlatform']:
        """public static dev.ultreon.quantum.client.platform.GdxPlatform[] dev.ultreon.quantum.client.platform.GdxPlatform.values()"""
        return List[GdxPlatform].__wrap(__GdxPlatform.values())

 
 
 
# CLASS: dev.ultreon.quantum.client.platform.GdxPlatform
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.client.platform.GdxPlatform as __GdxPlatform
__GdxPlatform = __GdxPlatform
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class GdxPlatform():
    """dev.ultreon.quantum.client.platform.GdxPlatform"""
 
    @staticmethod
    def __wrap(java_value: __GdxPlatform) -> 'GdxPlatform':
        return GdxPlatform(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GdxPlatform):
        """
        Dynamic initializer for GdxPlatform.
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
 
    # public static final dev.ultreon.quantum.client.platform.GdxPlatform dev.ultreon.quantum.client.platform.GdxPlatform.ANDROID
    ANDROID: 'GdxPlatform' = __wrap(__GdxPlatform.ANDROID)

    # public static final dev.ultreon.quantum.client.platform.GdxPlatform dev.ultreon.quantum.client.platform.GdxPlatform.DESKTOP
    DESKTOP: 'GdxPlatform' = __wrap(__GdxPlatform.DESKTOP)

    # public static final dev.ultreon.quantum.client.platform.GdxPlatform dev.ultreon.quantum.client.platform.GdxPlatform.WEB
    WEB: 'GdxPlatform' = __wrap(__GdxPlatform.WEB)

    # public static final dev.ultreon.quantum.client.platform.GdxPlatform dev.ultreon.quantum.client.platform.GdxPlatform.IOS
    IOS: 'GdxPlatform' = __wrap(__GdxPlatform.IOS)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'GdxPlatform':
        """public static dev.ultreon.quantum.client.platform.GdxPlatform dev.ultreon.quantum.client.platform.GdxPlatform.valueOf(java.lang.String)"""
        return GdxPlatform.__wrap(__GdxPlatform.valueOf(arg0))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @overload
    def getDisplayName(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.platform.GdxPlatform.getDisplayName()"""
        return str.__wrap(super(GdxPlatform, self).getDisplayName())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

    @staticmethod
    @overload
    def values() -> List['GdxPlatform']:
        """public static dev.ultreon.quantum.client.platform.GdxPlatform[] dev.ultreon.quantum.client.platform.GdxPlatform.values()"""
        return List[GdxPlatform].__wrap(__GdxPlatform.values())

 
 
 
# CLASS: dev.ultreon.quantum.client.platform.GdxPlatform 
 
 
# CLASS: dev.ultreon.quantum.client.platform.PlatformType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import dev.ultreon.quantum.client.platform.PlatformType as __PlatformType
__PlatformType = __PlatformType
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class PlatformType():
    """dev.ultreon.quantum.client.platform.PlatformType"""
 
    @staticmethod
    def __wrap(java_value: __PlatformType) -> 'PlatformType':
        return PlatformType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PlatformType):
        """
        Dynamic initializer for PlatformType.
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
 
    # public static final dev.ultreon.quantum.client.platform.PlatformType dev.ultreon.quantum.client.platform.PlatformType.DESKTOP
    DESKTOP: 'PlatformType' = __wrap(__PlatformType.DESKTOP)

    # public static final dev.ultreon.quantum.client.platform.PlatformType dev.ultreon.quantum.client.platform.PlatformType.MOBILE
    MOBILE: 'PlatformType' = __wrap(__PlatformType.MOBILE)

    # public static final dev.ultreon.quantum.client.platform.PlatformType dev.ultreon.quantum.client.platform.PlatformType.WEB
    WEB: 'PlatformType' = __wrap(__PlatformType.WEB)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def values() -> List['PlatformType']:
        """public static dev.ultreon.quantum.client.platform.PlatformType[] dev.ultreon.quantum.client.platform.PlatformType.values()"""
        return List[PlatformType].__wrap(__PlatformType.values())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'PlatformType':
        """public static dev.ultreon.quantum.client.platform.PlatformType dev.ultreon.quantum.client.platform.PlatformType.valueOf(java.lang.String)"""
        return PlatformType.__wrap(__PlatformType.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: dev.ultreon.quantum.client.platform.OperatingSystem
from builtins import str
from pyquantum_helper import override
import dev.ultreon.quantum.client.platform.GdxPlatform as __GdxPlatform
__GdxPlatform = __GdxPlatform
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import dev.ultreon.quantum.client.platform.OperatingSystem as __OperatingSystem
__OperatingSystem = __OperatingSystem
import dev.ultreon.quantum.client.platform.PlatformType as __PlatformType
__PlatformType = __PlatformType
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class OperatingSystem():
    """dev.ultreon.quantum.client.platform.OperatingSystem"""
 
    @staticmethod
    def __wrap(java_value: __OperatingSystem) -> 'OperatingSystem':
        return OperatingSystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OperatingSystem):
        """
        Dynamic initializer for OperatingSystem.
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
 
    # public static final dev.ultreon.quantum.client.platform.OperatingSystem dev.ultreon.quantum.client.platform.OperatingSystem.LINUX
    LINUX: 'OperatingSystem' = __wrap(__OperatingSystem.LINUX)

    # public static final dev.ultreon.quantum.client.platform.OperatingSystem dev.ultreon.quantum.client.platform.OperatingSystem.ANDROID
    ANDROID: 'OperatingSystem' = __wrap(__OperatingSystem.ANDROID)

    # public static final dev.ultreon.quantum.client.platform.OperatingSystem dev.ultreon.quantum.client.platform.OperatingSystem.MAC_OS
    MAC_OS: 'OperatingSystem' = __wrap(__OperatingSystem.MAC_OS)

    # public static final dev.ultreon.quantum.client.platform.OperatingSystem dev.ultreon.quantum.client.platform.OperatingSystem.IOS
    IOS: 'OperatingSystem' = __wrap(__OperatingSystem.IOS)

    # public static final dev.ultreon.quantum.client.platform.OperatingSystem dev.ultreon.quantum.client.platform.OperatingSystem.WEB
    WEB: 'OperatingSystem' = __wrap(__OperatingSystem.WEB)

    # public static final dev.ultreon.quantum.client.platform.OperatingSystem dev.ultreon.quantum.client.platform.OperatingSystem.WINDOWS
    WINDOWS: 'OperatingSystem' = __wrap(__OperatingSystem.WINDOWS)

    # public static final dev.ultreon.quantum.client.platform.OperatingSystem dev.ultreon.quantum.client.platform.OperatingSystem.OS2
    OS2: 'OperatingSystem' = __wrap(__OperatingSystem.OS2)

    # public static final dev.ultreon.quantum.client.platform.OperatingSystem dev.ultreon.quantum.client.platform.OperatingSystem.SOLARIS
    SOLARIS: 'OperatingSystem' = __wrap(__OperatingSystem.SOLARIS)

    # public static final dev.ultreon.quantum.client.platform.OperatingSystem dev.ultreon.quantum.client.platform.OperatingSystem.UNIX
    UNIX: 'OperatingSystem' = __wrap(__OperatingSystem.UNIX)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def values() -> List['OperatingSystem']:
        """public static dev.ultreon.quantum.client.platform.OperatingSystem[] dev.ultreon.quantum.client.platform.OperatingSystem.values()"""
        return List[OperatingSystem].__wrap(__OperatingSystem.values())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @overload
    def getGdxPlatform(self) -> 'GdxPlatform':
        """public dev.ultreon.quantum.client.platform.GdxPlatform dev.ultreon.quantum.client.platform.OperatingSystem.getGdxPlatform()"""
        return 'GdxPlatform'.__wrap(super(OperatingSystem, self).getGdxPlatform())

    @overload
    def getType(self) -> 'PlatformType':
        """public dev.ultreon.quantum.client.platform.PlatformType dev.ultreon.quantum.client.platform.OperatingSystem.getType()"""
        return 'PlatformType'.__wrap(super(OperatingSystem, self).getType())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'OperatingSystem':
        """public static dev.ultreon.quantum.client.platform.OperatingSystem dev.ultreon.quantum.client.platform.OperatingSystem.valueOf(java.lang.String)"""
        return OperatingSystem.__wrap(__OperatingSystem.valueOf(arg0))