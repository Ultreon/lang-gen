from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import org.apache.commons.lang3.text.translate.OctalUnescaper as __OctalUnescaper
__OctalUnescaper = __OctalUnescaper
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.lang3.text.translate.CharSequenceTranslator as __CharSequenceTranslator
__CharSequenceTranslator = __CharSequenceTranslator
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class OctalUnescaper(__CharSequenceTranslator, CharSequenceTranslator):
    """org.apache.commons.lang3.text.translate.OctalUnescaper"""
 
    @staticmethod
    def __wrap(java_value: __OctalUnescaper) -> 'OctalUnescaper':
        return OctalUnescaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OctalUnescaper):
        """
        Dynamic initializer for OctalUnescaper.
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
    def translate(self, arg0: 'CharSequence', arg1: 'Writer'):
        """public final void org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,java.io.Writer) throws java.io.IOException"""
        super(__CharSequenceTranslator, self).translate(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def translate(self, arg0: 'CharSequence', arg1: int, arg2: 'Writer') -> int:
        """public int org.apache.commons.lang3.text.translate.OctalUnescaper.translate(java.lang.CharSequence,int,java.io.Writer) throws java.io.IOException"""
        return int.__wrap(super(__OctalUnescaper, self).translate(arg0, __int.valueOf(arg1), arg2))

    @overload
    def with(self, *arg0: 'CharSequenceTranslator') -> 'CharSequenceTranslator':
        """public final org.apache.commons.lang3.text.translate.CharSequenceTranslator org.apache.commons.lang3.text.translate.CharSequenceTranslator.with(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        return 'CharSequenceTranslator'.__wrap(super(__CharSequenceTranslator, self).with(arg0))

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
    def __init__(self, ):
        """public org.apache.commons.lang3.text.translate.OctalUnescaper()"""
        val = __OctalUnescaper()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def hex(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.hex(int)"""
        return str.__wrap(__CharSequenceTranslator.hex(__int.valueOf(arg0)))

    @overload
    def translate(self, arg0: 'CharSequence') -> str:
        """public final java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence)"""
        return str.__wrap(super(__CharSequenceTranslator, self).translate(arg0))

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
    def __init__(self):
        """public org.apache.commons.lang3.text.translate.OctalUnescaper()"""
        val = __OctalUnescaper()
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

 
 
 
# CLASS: org.apache.commons.lang3.text.translate.OctalUnescaper
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import org.apache.commons.lang3.text.translate.OctalUnescaper as __OctalUnescaper
__OctalUnescaper = __OctalUnescaper
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.lang3.text.translate.CharSequenceTranslator as __CharSequenceTranslator
__CharSequenceTranslator = __CharSequenceTranslator
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class OctalUnescaper(__CharSequenceTranslator, CharSequenceTranslator):
    """org.apache.commons.lang3.text.translate.OctalUnescaper"""
 
    @staticmethod
    def __wrap(java_value: __OctalUnescaper) -> 'OctalUnescaper':
        return OctalUnescaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OctalUnescaper):
        """
        Dynamic initializer for OctalUnescaper.
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
    def translate(self, arg0: 'CharSequence', arg1: 'Writer'):
        """public final void org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,java.io.Writer) throws java.io.IOException"""
        super(__CharSequenceTranslator, self).translate(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def translate(self, arg0: 'CharSequence', arg1: int, arg2: 'Writer') -> int:
        """public int org.apache.commons.lang3.text.translate.OctalUnescaper.translate(java.lang.CharSequence,int,java.io.Writer) throws java.io.IOException"""
        return int.__wrap(super(__OctalUnescaper, self).translate(arg0, __int.valueOf(arg1), arg2))

    @overload
    def with(self, *arg0: 'CharSequenceTranslator') -> 'CharSequenceTranslator':
        """public final org.apache.commons.lang3.text.translate.CharSequenceTranslator org.apache.commons.lang3.text.translate.CharSequenceTranslator.with(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        return 'CharSequenceTranslator'.__wrap(super(__CharSequenceTranslator, self).with(arg0))

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
    def __init__(self, ):
        """public org.apache.commons.lang3.text.translate.OctalUnescaper()"""
        val = __OctalUnescaper()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def hex(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.hex(int)"""
        return str.__wrap(__CharSequenceTranslator.hex(__int.valueOf(arg0)))

    @overload
    def translate(self, arg0: 'CharSequence') -> str:
        """public final java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence)"""
        return str.__wrap(super(__CharSequenceTranslator, self).translate(arg0))

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
    def __init__(self):
        """public org.apache.commons.lang3.text.translate.OctalUnescaper()"""
        val = __OctalUnescaper()
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

 
 
 
# CLASS: org.apache.commons.lang3.text.translate.OctalUnescaper 
 
 
# CLASS: org.apache.commons.lang3.text.translate.NumericEntityUnescaper$OPTION
from builtins import str
from pyquantum_helper import override
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
import org.apache.commons.lang3.text.translate.NumericEntityUnescaper as __NumericEntityUnescaper_OPTION
__OPTION = __NumericEntityUnescaper_OPTION.OPTION
from builtins import int
 
class OPTION(__Enum, Enum):
    """org.apache.commons.lang3.text.translate.NumericEntityUnescaper.OPTION"""
 
    @staticmethod
    def __wrap(java_value: __OPTION) -> 'OPTION':
        return OPTION(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OPTION):
        """
        Dynamic initializer for OPTION.
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
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'OPTION':
        """public static org.apache.commons.lang3.text.translate.NumericEntityUnescaper$OPTION org.apache.commons.lang3.text.translate.NumericEntityUnescaper$OPTION.valueOf(java.lang.String)"""
        return OPTION.__wrap(__OPTION.valueOf(arg0))

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
    def values() -> List['OPTION']:
        """public static org.apache.commons.lang3.text.translate.NumericEntityUnescaper$OPTION[] org.apache.commons.lang3.text.translate.NumericEntityUnescaper$OPTION.values()"""
        return List[OPTION].__wrap(__OPTION.values())

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
 
 
# CLASS: org.apache.commons.lang3.text.translate.JavaUnicodeEscaper
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.text.translate.CodePointTranslator as __CodePointTranslator
__CodePointTranslator = __CodePointTranslator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.lang3.text.translate.CharSequenceTranslator as __CharSequenceTranslator
__CharSequenceTranslator = __CharSequenceTranslator
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.lang3.text.translate.JavaUnicodeEscaper as __JavaUnicodeEscaper
__JavaUnicodeEscaper = __JavaUnicodeEscaper
import java.lang.Integer as __int
import org.apache.commons.lang3.text.translate.UnicodeEscaper as __UnicodeEscaper
__UnicodeEscaper = __UnicodeEscaper
from builtins import bool
from builtins import int
 
class JavaUnicodeEscaper(__UnicodeEscaper, UnicodeEscaper):
    """org.apache.commons.lang3.text.translate.JavaUnicodeEscaper"""
 
    @staticmethod
    def __wrap(java_value: __JavaUnicodeEscaper) -> 'JavaUnicodeEscaper':
        return JavaUnicodeEscaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JavaUnicodeEscaper):
        """
        Dynamic initializer for JavaUnicodeEscaper.
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
    def below(arg0: int) -> 'JavaUnicodeEscaper':
        """public static org.apache.commons.lang3.text.translate.JavaUnicodeEscaper org.apache.commons.lang3.text.translate.JavaUnicodeEscaper.below(int)"""
        return JavaUnicodeEscaper.__wrap(__JavaUnicodeEscaper.below(__int.valueOf(arg0)))

    @overload
    def translate(self, arg0: 'CharSequence', arg1: int, arg2: 'Writer') -> int:
        """public final int org.apache.commons.lang3.text.translate.CodePointTranslator.translate(java.lang.CharSequence,int,java.io.Writer) throws java.io.IOException"""
        return int.__wrap(super(__CodePointTranslator, self).translate(arg0, __int.valueOf(arg1), arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def above(arg0: int) -> 'JavaUnicodeEscaper':
        """public static org.apache.commons.lang3.text.translate.JavaUnicodeEscaper org.apache.commons.lang3.text.translate.JavaUnicodeEscaper.above(int)"""
        return JavaUnicodeEscaper.__wrap(__JavaUnicodeEscaper.above(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def between(arg0: int, arg1: int) -> 'JavaUnicodeEscaper':
        """public static org.apache.commons.lang3.text.translate.JavaUnicodeEscaper org.apache.commons.lang3.text.translate.JavaUnicodeEscaper.between(int,int)"""
        return JavaUnicodeEscaper.__wrap(__JavaUnicodeEscaper.between(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def outsideOf(arg0: int, arg1: int) -> 'JavaUnicodeEscaper':
        """public static org.apache.commons.lang3.text.translate.JavaUnicodeEscaper org.apache.commons.lang3.text.translate.JavaUnicodeEscaper.outsideOf(int,int)"""
        return JavaUnicodeEscaper.__wrap(__JavaUnicodeEscaper.outsideOf(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def translate(self, arg0: 'CharSequence', arg1: 'Writer'):
        """public final void org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,java.io.Writer) throws java.io.IOException"""
        super(__CharSequenceTranslator, self).translate(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: bool):
        """public org.apache.commons.lang3.text.translate.JavaUnicodeEscaper(int,int,boolean)"""
        val = __JavaUnicodeEscaper(__int.valueOf(arg0), __int.valueOf(arg1), __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def between(arg0: int, arg1: int) -> 'UnicodeEscaper':
        """public static org.apache.commons.lang3.text.translate.UnicodeEscaper org.apache.commons.lang3.text.translate.UnicodeEscaper.between(int,int)"""
        return UnicodeEscaper.__wrap(__UnicodeEscaper.between(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def translate(self, arg0: int, arg1: 'Writer') -> bool:
        """public boolean org.apache.commons.lang3.text.translate.UnicodeEscaper.translate(int,java.io.Writer) throws java.io.IOException"""
        return bool.__wrap(super(__UnicodeEscaper, self).translate(__int.valueOf(arg0), arg1))

    @overload
    def with(self, *arg0: 'CharSequenceTranslator') -> 'CharSequenceTranslator':
        """public final org.apache.commons.lang3.text.translate.CharSequenceTranslator org.apache.commons.lang3.text.translate.CharSequenceTranslator.with(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        return 'CharSequenceTranslator'.__wrap(super(__CharSequenceTranslator, self).with(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def below(arg0: int) -> 'UnicodeEscaper':
        """public static org.apache.commons.lang3.text.translate.UnicodeEscaper org.apache.commons.lang3.text.translate.UnicodeEscaper.below(int)"""
        return UnicodeEscaper.__wrap(__UnicodeEscaper.below(__int.valueOf(arg0)))

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
    def hex(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.hex(int)"""
        return str.__wrap(__CharSequenceTranslator.hex(__int.valueOf(arg0)))

    @overload
    def translate(self, arg0: 'CharSequence') -> str:
        """public final java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence)"""
        return str.__wrap(super(__CharSequenceTranslator, self).translate(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def above(arg0: int) -> 'UnicodeEscaper':
        """public static org.apache.commons.lang3.text.translate.UnicodeEscaper org.apache.commons.lang3.text.translate.UnicodeEscaper.above(int)"""
        return UnicodeEscaper.__wrap(__UnicodeEscaper.above(__int.valueOf(arg0)))

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
    def outsideOf(arg0: int, arg1: int) -> 'UnicodeEscaper':
        """public static org.apache.commons.lang3.text.translate.UnicodeEscaper org.apache.commons.lang3.text.translate.UnicodeEscaper.outsideOf(int,int)"""
        return UnicodeEscaper.__wrap(__UnicodeEscaper.outsideOf(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.text.translate.NumericEntityEscaper
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.text.translate.CodePointTranslator as __CodePointTranslator
__CodePointTranslator = __CodePointTranslator
import org.apache.commons.lang3.text.translate.NumericEntityEscaper as __NumericEntityEscaper
__NumericEntityEscaper = __NumericEntityEscaper
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.lang3.text.translate.CharSequenceTranslator as __CharSequenceTranslator
__CharSequenceTranslator = __CharSequenceTranslator
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NumericEntityEscaper(__CodePointTranslator, CodePointTranslator):
    """org.apache.commons.lang3.text.translate.NumericEntityEscaper"""
 
    @staticmethod
    def __wrap(java_value: __NumericEntityEscaper) -> 'NumericEntityEscaper':
        return NumericEntityEscaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NumericEntityEscaper):
        """
        Dynamic initializer for NumericEntityEscaper.
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
    def translate(self, arg0: 'CharSequence', arg1: int, arg2: 'Writer') -> int:
        """public final int org.apache.commons.lang3.text.translate.CodePointTranslator.translate(java.lang.CharSequence,int,java.io.Writer) throws java.io.IOException"""
        return int.__wrap(super(__CodePointTranslator, self).translate(arg0, __int.valueOf(arg1), arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def translate(self, arg0: 'CharSequence', arg1: 'Writer'):
        """public final void org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,java.io.Writer) throws java.io.IOException"""
        super(__CharSequenceTranslator, self).translate(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def with(self, *arg0: 'CharSequenceTranslator') -> 'CharSequenceTranslator':
        """public final org.apache.commons.lang3.text.translate.CharSequenceTranslator org.apache.commons.lang3.text.translate.CharSequenceTranslator.with(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        return 'CharSequenceTranslator'.__wrap(super(__CharSequenceTranslator, self).with(arg0))

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
    def __init__(self, ):
        """public org.apache.commons.lang3.text.translate.NumericEntityEscaper()"""
        val = __NumericEntityEscaper()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def between(arg0: int, arg1: int) -> 'NumericEntityEscaper':
        """public static org.apache.commons.lang3.text.translate.NumericEntityEscaper org.apache.commons.lang3.text.translate.NumericEntityEscaper.between(int,int)"""
        return NumericEntityEscaper.__wrap(__NumericEntityEscaper.between(__int.valueOf(arg0), __int.valueOf(arg1)))

    @staticmethod
    @overload
    def hex(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.hex(int)"""
        return str.__wrap(__CharSequenceTranslator.hex(__int.valueOf(arg0)))

    @overload
    def translate(self, arg0: 'CharSequence') -> str:
        """public final java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence)"""
        return str.__wrap(super(__CharSequenceTranslator, self).translate(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.text.translate.NumericEntityEscaper()"""
        val = __NumericEntityEscaper()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def below(arg0: int) -> 'NumericEntityEscaper':
        """public static org.apache.commons.lang3.text.translate.NumericEntityEscaper org.apache.commons.lang3.text.translate.NumericEntityEscaper.below(int)"""
        return NumericEntityEscaper.__wrap(__NumericEntityEscaper.below(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def translate(self, arg0: int, arg1: 'Writer') -> bool:
        """public boolean org.apache.commons.lang3.text.translate.NumericEntityEscaper.translate(int,java.io.Writer) throws java.io.IOException"""
        return bool.__wrap(super(__NumericEntityEscaper, self).translate(__int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def above(arg0: int) -> 'NumericEntityEscaper':
        """public static org.apache.commons.lang3.text.translate.NumericEntityEscaper org.apache.commons.lang3.text.translate.NumericEntityEscaper.above(int)"""
        return NumericEntityEscaper.__wrap(__NumericEntityEscaper.above(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def outsideOf(arg0: int, arg1: int) -> 'NumericEntityEscaper':
        """public static org.apache.commons.lang3.text.translate.NumericEntityEscaper org.apache.commons.lang3.text.translate.NumericEntityEscaper.outsideOf(int,int)"""
        return NumericEntityEscaper.__wrap(__NumericEntityEscaper.outsideOf(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: org.apache.commons.lang3.text.translate.UnicodeEscaper
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.text.translate.CodePointTranslator as __CodePointTranslator
__CodePointTranslator = __CodePointTranslator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.lang3.text.translate.CharSequenceTranslator as __CharSequenceTranslator
__CharSequenceTranslator = __CharSequenceTranslator
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.lang3.text.translate.UnicodeEscaper as __UnicodeEscaper
__UnicodeEscaper = __UnicodeEscaper
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class UnicodeEscaper(__CodePointTranslator, CodePointTranslator):
    """org.apache.commons.lang3.text.translate.UnicodeEscaper"""
 
    @staticmethod
    def __wrap(java_value: __UnicodeEscaper) -> 'UnicodeEscaper':
        return UnicodeEscaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnicodeEscaper):
        """
        Dynamic initializer for UnicodeEscaper.
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
    def translate(self, arg0: 'CharSequence', arg1: int, arg2: 'Writer') -> int:
        """public final int org.apache.commons.lang3.text.translate.CodePointTranslator.translate(java.lang.CharSequence,int,java.io.Writer) throws java.io.IOException"""
        return int.__wrap(super(__CodePointTranslator, self).translate(arg0, __int.valueOf(arg1), arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def translate(self, arg0: 'CharSequence', arg1: 'Writer'):
        """public final void org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,java.io.Writer) throws java.io.IOException"""
        super(__CharSequenceTranslator, self).translate(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def between(arg0: int, arg1: int) -> 'UnicodeEscaper':
        """public static org.apache.commons.lang3.text.translate.UnicodeEscaper org.apache.commons.lang3.text.translate.UnicodeEscaper.between(int,int)"""
        return UnicodeEscaper.__wrap(__UnicodeEscaper.between(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def translate(self, arg0: int, arg1: 'Writer') -> bool:
        """public boolean org.apache.commons.lang3.text.translate.UnicodeEscaper.translate(int,java.io.Writer) throws java.io.IOException"""
        return bool.__wrap(super(__UnicodeEscaper, self).translate(__int.valueOf(arg0), arg1))

    @overload
    def with(self, *arg0: 'CharSequenceTranslator') -> 'CharSequenceTranslator':
        """public final org.apache.commons.lang3.text.translate.CharSequenceTranslator org.apache.commons.lang3.text.translate.CharSequenceTranslator.with(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        return 'CharSequenceTranslator'.__wrap(super(__CharSequenceTranslator, self).with(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def below(arg0: int) -> 'UnicodeEscaper':
        """public static org.apache.commons.lang3.text.translate.UnicodeEscaper org.apache.commons.lang3.text.translate.UnicodeEscaper.below(int)"""
        return UnicodeEscaper.__wrap(__UnicodeEscaper.below(__int.valueOf(arg0)))

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
        """public org.apache.commons.lang3.text.translate.UnicodeEscaper()"""
        val = __UnicodeEscaper()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def hex(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.hex(int)"""
        return str.__wrap(__CharSequenceTranslator.hex(__int.valueOf(arg0)))

    @overload
    def translate(self, arg0: 'CharSequence') -> str:
        """public final java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence)"""
        return str.__wrap(super(__CharSequenceTranslator, self).translate(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def above(arg0: int) -> 'UnicodeEscaper':
        """public static org.apache.commons.lang3.text.translate.UnicodeEscaper org.apache.commons.lang3.text.translate.UnicodeEscaper.above(int)"""
        return UnicodeEscaper.__wrap(__UnicodeEscaper.above(__int.valueOf(arg0)))

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
    def outsideOf(arg0: int, arg1: int) -> 'UnicodeEscaper':
        """public static org.apache.commons.lang3.text.translate.UnicodeEscaper org.apache.commons.lang3.text.translate.UnicodeEscaper.outsideOf(int,int)"""
        return UnicodeEscaper.__wrap(__UnicodeEscaper.outsideOf(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.translate.UnicodeEscaper()"""
        val = __UnicodeEscaper()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.lang3.text.translate.NumericEntityUnescaper
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.text.translate.NumericEntityUnescaper as __NumericEntityUnescaper
__NumericEntityUnescaper = __NumericEntityUnescaper
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.lang3.text.translate.CharSequenceTranslator as __CharSequenceTranslator
__CharSequenceTranslator = __CharSequenceTranslator
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NumericEntityUnescaper(__CharSequenceTranslator, CharSequenceTranslator):
    """org.apache.commons.lang3.text.translate.NumericEntityUnescaper"""
 
    @staticmethod
    def __wrap(java_value: __NumericEntityUnescaper) -> 'NumericEntityUnescaper':
        return NumericEntityUnescaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NumericEntityUnescaper):
        """
        Dynamic initializer for NumericEntityUnescaper.
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
    def translate(self, arg0: 'CharSequence', arg1: 'Writer'):
        """public final void org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,java.io.Writer) throws java.io.IOException"""
        super(__CharSequenceTranslator, self).translate(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def isSet(self, arg0: 'OPTION') -> bool:
        """public boolean org.apache.commons.lang3.text.translate.NumericEntityUnescaper.isSet(org.apache.commons.lang3.text.translate.NumericEntityUnescaper$OPTION)"""
        return bool.__wrap(super(__NumericEntityUnescaper, self).isSet(arg0))

    @overload
    def translate(self, arg0: 'CharSequence', arg1: int, arg2: 'Writer') -> int:
        """public int org.apache.commons.lang3.text.translate.NumericEntityUnescaper.translate(java.lang.CharSequence,int,java.io.Writer) throws java.io.IOException"""
        return int.__wrap(super(__NumericEntityUnescaper, self).translate(arg0, __int.valueOf(arg1), arg2))

    @overload
    def with(self, *arg0: 'CharSequenceTranslator') -> 'CharSequenceTranslator':
        """public final org.apache.commons.lang3.text.translate.CharSequenceTranslator org.apache.commons.lang3.text.translate.CharSequenceTranslator.with(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        return 'CharSequenceTranslator'.__wrap(super(__CharSequenceTranslator, self).with(arg0))

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

    @staticmethod
    @overload
    def hex(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.hex(int)"""
        return str.__wrap(__CharSequenceTranslator.hex(__int.valueOf(arg0)))

    @overload
    def translate(self, arg0: 'CharSequence') -> str:
        """public final java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence)"""
        return str.__wrap(super(__CharSequenceTranslator, self).translate(arg0))

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, *arg0: 'OPTION'):
        """public org.apache.commons.lang3.text.translate.NumericEntityUnescaper(org.apache.commons.lang3.text.translate.NumericEntityUnescaper$OPTION...)"""
        val = __NumericEntityUnescaper(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.text.translate.LookupTranslator
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.text.translate.LookupTranslator as __LookupTranslator
__LookupTranslator = __LookupTranslator
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.lang3.text.translate.CharSequenceTranslator as __CharSequenceTranslator
__CharSequenceTranslator = __CharSequenceTranslator
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LookupTranslator(__CharSequenceTranslator, CharSequenceTranslator):
    """org.apache.commons.lang3.text.translate.LookupTranslator"""
 
    @staticmethod
    def __wrap(java_value: __LookupTranslator) -> 'LookupTranslator':
        return LookupTranslator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LookupTranslator):
        """
        Dynamic initializer for LookupTranslator.
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
    def translate(self, arg0: 'CharSequence', arg1: 'Writer'):
        """public final void org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,java.io.Writer) throws java.io.IOException"""
        super(__CharSequenceTranslator, self).translate(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def translate(self, arg0: 'CharSequence', arg1: int, arg2: 'Writer') -> int:
        """public int org.apache.commons.lang3.text.translate.LookupTranslator.translate(java.lang.CharSequence,int,java.io.Writer) throws java.io.IOException"""
        return int.__wrap(super(__LookupTranslator, self).translate(arg0, __int.valueOf(arg1), arg2))

    @overload
    def with(self, *arg0: 'CharSequenceTranslator') -> 'CharSequenceTranslator':
        """public final org.apache.commons.lang3.text.translate.CharSequenceTranslator org.apache.commons.lang3.text.translate.CharSequenceTranslator.with(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        return 'CharSequenceTranslator'.__wrap(super(__CharSequenceTranslator, self).with(arg0))

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

    @staticmethod
    @overload
    def hex(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.hex(int)"""
        return str.__wrap(__CharSequenceTranslator.hex(__int.valueOf(arg0)))

    @overload
    def translate(self, arg0: 'CharSequence') -> str:
        """public final java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence)"""
        return str.__wrap(super(__CharSequenceTranslator, self).translate(arg0))

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, *arg0: List['CharSequence']):
        """public org.apache.commons.lang3.text.translate.LookupTranslator(java.lang.CharSequence[]...)"""
        val = __LookupTranslator(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.text.translate.UnicodeUnpairedSurrogateRemover
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.text.translate.CodePointTranslator as __CodePointTranslator
__CodePointTranslator = __CodePointTranslator
import org.apache.commons.lang3.text.translate.UnicodeUnpairedSurrogateRemover as __UnicodeUnpairedSurrogateRemover
__UnicodeUnpairedSurrogateRemover = __UnicodeUnpairedSurrogateRemover
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.lang3.text.translate.CharSequenceTranslator as __CharSequenceTranslator
__CharSequenceTranslator = __CharSequenceTranslator
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class UnicodeUnpairedSurrogateRemover(__CodePointTranslator, CodePointTranslator):
    """org.apache.commons.lang3.text.translate.UnicodeUnpairedSurrogateRemover"""
 
    @staticmethod
    def __wrap(java_value: __UnicodeUnpairedSurrogateRemover) -> 'UnicodeUnpairedSurrogateRemover':
        return UnicodeUnpairedSurrogateRemover(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnicodeUnpairedSurrogateRemover):
        """
        Dynamic initializer for UnicodeUnpairedSurrogateRemover.
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
    def translate(self, arg0: 'CharSequence', arg1: int, arg2: 'Writer') -> int:
        """public final int org.apache.commons.lang3.text.translate.CodePointTranslator.translate(java.lang.CharSequence,int,java.io.Writer) throws java.io.IOException"""
        return int.__wrap(super(__CodePointTranslator, self).translate(arg0, __int.valueOf(arg1), arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def translate(self, arg0: int, arg1: 'Writer') -> bool:
        """public boolean org.apache.commons.lang3.text.translate.UnicodeUnpairedSurrogateRemover.translate(int,java.io.Writer) throws java.io.IOException"""
        return bool.__wrap(super(__UnicodeUnpairedSurrogateRemover, self).translate(__int.valueOf(arg0), arg1))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.translate.UnicodeUnpairedSurrogateRemover()"""
        val = __UnicodeUnpairedSurrogateRemover()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def translate(self, arg0: 'CharSequence', arg1: 'Writer'):
        """public final void org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,java.io.Writer) throws java.io.IOException"""
        super(__CharSequenceTranslator, self).translate(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def with(self, *arg0: 'CharSequenceTranslator') -> 'CharSequenceTranslator':
        """public final org.apache.commons.lang3.text.translate.CharSequenceTranslator org.apache.commons.lang3.text.translate.CharSequenceTranslator.with(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        return 'CharSequenceTranslator'.__wrap(super(__CharSequenceTranslator, self).with(arg0))

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

    @staticmethod
    @overload
    def hex(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.hex(int)"""
        return str.__wrap(__CharSequenceTranslator.hex(__int.valueOf(arg0)))

    @overload
    def translate(self, arg0: 'CharSequence') -> str:
        """public final java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence)"""
        return str.__wrap(super(__CharSequenceTranslator, self).translate(arg0))

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
    def __init__(self):
        """public org.apache.commons.lang3.text.translate.UnicodeUnpairedSurrogateRemover()"""
        val = __UnicodeUnpairedSurrogateRemover()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: org.apache.commons.lang3.text.translate.UnicodeUnescaper
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.lang3.text.translate.CharSequenceTranslator as __CharSequenceTranslator
__CharSequenceTranslator = __CharSequenceTranslator
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import org.apache.commons.lang3.text.translate.UnicodeUnescaper as __UnicodeUnescaper
__UnicodeUnescaper = __UnicodeUnescaper
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class UnicodeUnescaper(__CharSequenceTranslator, CharSequenceTranslator):
    """org.apache.commons.lang3.text.translate.UnicodeUnescaper"""
 
    @staticmethod
    def __wrap(java_value: __UnicodeUnescaper) -> 'UnicodeUnescaper':
        return UnicodeUnescaper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnicodeUnescaper):
        """
        Dynamic initializer for UnicodeUnescaper.
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
    def translate(self, arg0: 'CharSequence', arg1: 'Writer'):
        """public final void org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,java.io.Writer) throws java.io.IOException"""
        super(__CharSequenceTranslator, self).translate(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def with(self, *arg0: 'CharSequenceTranslator') -> 'CharSequenceTranslator':
        """public final org.apache.commons.lang3.text.translate.CharSequenceTranslator org.apache.commons.lang3.text.translate.CharSequenceTranslator.with(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        return 'CharSequenceTranslator'.__wrap(super(__CharSequenceTranslator, self).with(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.text.translate.UnicodeUnescaper()"""
        val = __UnicodeUnescaper()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def translate(self, arg0: 'CharSequence', arg1: int, arg2: 'Writer') -> int:
        """public int org.apache.commons.lang3.text.translate.UnicodeUnescaper.translate(java.lang.CharSequence,int,java.io.Writer) throws java.io.IOException"""
        return int.__wrap(super(__UnicodeUnescaper, self).translate(arg0, __int.valueOf(arg1), arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def hex(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.hex(int)"""
        return str.__wrap(__CharSequenceTranslator.hex(__int.valueOf(arg0)))

    @overload
    def translate(self, arg0: 'CharSequence') -> str:
        """public final java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence)"""
        return str.__wrap(super(__CharSequenceTranslator, self).translate(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.translate.UnicodeUnescaper()"""
        val = __UnicodeUnescaper()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: org.apache.commons.lang3.text.translate.EntityArrays
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.text.translate.EntityArrays as __EntityArrays
__EntityArrays = __EntityArrays
from typing import List
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
 
class EntityArrays():
    """org.apache.commons.lang3.text.translate.EntityArrays"""
 
    @staticmethod
    def __wrap(java_value: __EntityArrays) -> 'EntityArrays':
        return EntityArrays(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntityArrays):
        """
        Dynamic initializer for EntityArrays.
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
    def invert(arg0: 'String') -> List[List[str]]:
        """public static java.lang.String[][] org.apache.commons.lang3.text.translate.EntityArrays.invert(java.lang.String[][])"""
        return List[List[str]].__wrap(__EntityArrays.invert(arg0))

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

    @staticmethod
    @overload
    def APOS_UNESCAPE() -> List[List[str]]:
        """public static java.lang.String[][] org.apache.commons.lang3.text.translate.EntityArrays.APOS_UNESCAPE()"""
        return List[List[str]].__wrap(__EntityArrays.APOS_UNESCAPE())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.translate.EntityArrays()"""
        val = __EntityArrays()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def ISO8859_1_ESCAPE() -> List[List[str]]:
        """public static java.lang.String[][] org.apache.commons.lang3.text.translate.EntityArrays.ISO8859_1_ESCAPE()"""
        return List[List[str]].__wrap(__EntityArrays.ISO8859_1_ESCAPE())

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
    def JAVA_CTRL_CHARS_ESCAPE() -> List[List[str]]:
        """public static java.lang.String[][] org.apache.commons.lang3.text.translate.EntityArrays.JAVA_CTRL_CHARS_ESCAPE()"""
        return List[List[str]].__wrap(__EntityArrays.JAVA_CTRL_CHARS_ESCAPE())

    @staticmethod
    @overload
    def HTML40_EXTENDED_UNESCAPE() -> List[List[str]]:
        """public static java.lang.String[][] org.apache.commons.lang3.text.translate.EntityArrays.HTML40_EXTENDED_UNESCAPE()"""
        return List[List[str]].__wrap(__EntityArrays.HTML40_EXTENDED_UNESCAPE())

    @staticmethod
    @overload
    def HTML40_EXTENDED_ESCAPE() -> List[List[str]]:
        """public static java.lang.String[][] org.apache.commons.lang3.text.translate.EntityArrays.HTML40_EXTENDED_ESCAPE()"""
        return List[List[str]].__wrap(__EntityArrays.HTML40_EXTENDED_ESCAPE())

    @staticmethod
    @overload
    def JAVA_CTRL_CHARS_UNESCAPE() -> List[List[str]]:
        """public static java.lang.String[][] org.apache.commons.lang3.text.translate.EntityArrays.JAVA_CTRL_CHARS_UNESCAPE()"""
        return List[List[str]].__wrap(__EntityArrays.JAVA_CTRL_CHARS_UNESCAPE())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.text.translate.EntityArrays()"""
        val = __EntityArrays()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def BASIC_ESCAPE() -> List[List[str]]:
        """public static java.lang.String[][] org.apache.commons.lang3.text.translate.EntityArrays.BASIC_ESCAPE()"""
        return List[List[str]].__wrap(__EntityArrays.BASIC_ESCAPE())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def BASIC_UNESCAPE() -> List[List[str]]:
        """public static java.lang.String[][] org.apache.commons.lang3.text.translate.EntityArrays.BASIC_UNESCAPE()"""
        return List[List[str]].__wrap(__EntityArrays.BASIC_UNESCAPE())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def APOS_ESCAPE() -> List[List[str]]:
        """public static java.lang.String[][] org.apache.commons.lang3.text.translate.EntityArrays.APOS_ESCAPE()"""
        return List[List[str]].__wrap(__EntityArrays.APOS_ESCAPE())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def ISO8859_1_UNESCAPE() -> List[List[str]]:
        """public static java.lang.String[][] org.apache.commons.lang3.text.translate.EntityArrays.ISO8859_1_UNESCAPE()"""
        return List[List[str]].__wrap(__EntityArrays.ISO8859_1_UNESCAPE())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.text.translate.CodePointTranslator
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.text.translate.CodePointTranslator as __CodePointTranslator
__CodePointTranslator = __CodePointTranslator
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.lang3.text.translate.CharSequenceTranslator as __CharSequenceTranslator
__CharSequenceTranslator = __CharSequenceTranslator
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CodePointTranslator(ABC, __CharSequenceTranslator, CharSequenceTranslator):
    """org.apache.commons.lang3.text.translate.CodePointTranslator"""
 
    @staticmethod
    def __wrap(java_value: __CodePointTranslator) -> 'CodePointTranslator':
        return CodePointTranslator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CodePointTranslator):
        """
        Dynamic initializer for CodePointTranslator.
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
    def translate(self, arg0: 'CharSequence', arg1: int, arg2: 'Writer') -> int:
        """public final int org.apache.commons.lang3.text.translate.CodePointTranslator.translate(java.lang.CharSequence,int,java.io.Writer) throws java.io.IOException"""
        return int.__wrap(super(__CodePointTranslator, self).translate(arg0, __int.valueOf(arg1), arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def translate(self, arg0: 'CharSequence', arg1: 'Writer'):
        """public final void org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,java.io.Writer) throws java.io.IOException"""
        super(__CharSequenceTranslator, self).translate(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @abstractmethod
    def translate(self, arg0: int, arg1: 'Writer'):
        """public abstract boolean org.apache.commons.lang3.text.translate.CodePointTranslator.translate(int,java.io.Writer) throws java.io.IOException"""
        pass

    @overload
    def with(self, *arg0: 'CharSequenceTranslator') -> 'CharSequenceTranslator':
        """public final org.apache.commons.lang3.text.translate.CharSequenceTranslator org.apache.commons.lang3.text.translate.CharSequenceTranslator.with(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        return 'CharSequenceTranslator'.__wrap(super(__CharSequenceTranslator, self).with(arg0))

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

    @staticmethod
    @overload
    def hex(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.hex(int)"""
        return str.__wrap(__CharSequenceTranslator.hex(__int.valueOf(arg0)))

    @overload
    def translate(self, arg0: 'CharSequence') -> str:
        """public final java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence)"""
        return str.__wrap(super(__CharSequenceTranslator, self).translate(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.text.translate.CodePointTranslator()"""
        val = __CodePointTranslator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, ):
        """public org.apache.commons.lang3.text.translate.CodePointTranslator()"""
        val = __CodePointTranslator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.text.translate.AggregateTranslator
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import org.apache.commons.lang3.text.translate.AggregateTranslator as __AggregateTranslator
__AggregateTranslator = __AggregateTranslator
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.lang3.text.translate.CharSequenceTranslator as __CharSequenceTranslator
__CharSequenceTranslator = __CharSequenceTranslator
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AggregateTranslator(__CharSequenceTranslator, CharSequenceTranslator):
    """org.apache.commons.lang3.text.translate.AggregateTranslator"""
 
    @staticmethod
    def __wrap(java_value: __AggregateTranslator) -> 'AggregateTranslator':
        return AggregateTranslator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AggregateTranslator):
        """
        Dynamic initializer for AggregateTranslator.
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
    def translate(self, arg0: 'CharSequence', arg1: 'Writer'):
        """public final void org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,java.io.Writer) throws java.io.IOException"""
        super(__CharSequenceTranslator, self).translate(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def with(self, *arg0: 'CharSequenceTranslator') -> 'CharSequenceTranslator':
        """public final org.apache.commons.lang3.text.translate.CharSequenceTranslator org.apache.commons.lang3.text.translate.CharSequenceTranslator.with(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        return 'CharSequenceTranslator'.__wrap(super(__CharSequenceTranslator, self).with(arg0))

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

    @staticmethod
    @overload
    def hex(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.hex(int)"""
        return str.__wrap(__CharSequenceTranslator.hex(__int.valueOf(arg0)))

    @overload
    def translate(self, arg0: 'CharSequence') -> str:
        """public final java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence)"""
        return str.__wrap(super(__CharSequenceTranslator, self).translate(arg0))

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
    def __init__(self, *arg0: 'CharSequenceTranslator'):
        """public org.apache.commons.lang3.text.translate.AggregateTranslator(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        val = __AggregateTranslator(arg0)
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
    def translate(self, arg0: 'CharSequence', arg1: int, arg2: 'Writer') -> int:
        """public int org.apache.commons.lang3.text.translate.AggregateTranslator.translate(java.lang.CharSequence,int,java.io.Writer) throws java.io.IOException"""
        return int.__wrap(super(__AggregateTranslator, self).translate(arg0, __int.valueOf(arg1), arg2)) 
 
 
# CLASS: org.apache.commons.lang3.text.translate.CharSequenceTranslator
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.lang3.text.translate.CharSequenceTranslator as __CharSequenceTranslator
__CharSequenceTranslator = __CharSequenceTranslator
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class CharSequenceTranslator(ABC):
    """org.apache.commons.lang3.text.translate.CharSequenceTranslator"""
 
    @staticmethod
    def __wrap(java_value: __CharSequenceTranslator) -> 'CharSequenceTranslator':
        return CharSequenceTranslator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CharSequenceTranslator):
        """
        Dynamic initializer for CharSequenceTranslator.
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
    def translate(self, arg0: 'CharSequence', arg1: 'Writer'):
        """public final void org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,java.io.Writer) throws java.io.IOException"""
        super(__CharSequenceTranslator, self).translate(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def with(self, *arg0: 'CharSequenceTranslator') -> 'CharSequenceTranslator':
        """public final org.apache.commons.lang3.text.translate.CharSequenceTranslator org.apache.commons.lang3.text.translate.CharSequenceTranslator.with(org.apache.commons.lang3.text.translate.CharSequenceTranslator...)"""
        return 'CharSequenceTranslator'.__wrap(super(__CharSequenceTranslator, self).with(arg0))

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

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.text.translate.CharSequenceTranslator()"""
        val = __CharSequenceTranslator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @abstractmethod
    def translate(self, arg0: 'CharSequence', arg1: int, arg2: 'Writer'):
        """public abstract int org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence,int,java.io.Writer) throws java.io.IOException"""
        pass

    @staticmethod
    @overload
    def hex(arg0: int) -> str:
        """public static java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.hex(int)"""
        return str.__wrap(__CharSequenceTranslator.hex(__int.valueOf(arg0)))

    @overload
    def translate(self, arg0: 'CharSequence') -> str:
        """public final java.lang.String org.apache.commons.lang3.text.translate.CharSequenceTranslator.translate(java.lang.CharSequence)"""
        return str.__wrap(super(__CharSequenceTranslator, self).translate(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.text.translate.CharSequenceTranslator()"""
        val = __CharSequenceTranslator()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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