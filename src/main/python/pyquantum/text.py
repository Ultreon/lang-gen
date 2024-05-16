from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.text.TextDecoration as __TextDecoration
__TextDecoration = __TextDecoration
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
 
class TextDecoration(__Enum, Enum):
    """dev.ultreon.quantum.text.TextDecoration"""
 
    @staticmethod
    def __wrap(java_value: __TextDecoration) -> 'TextDecoration':
        return TextDecoration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextDecoration):
        """
        Dynamic initializer for TextDecoration.
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
 
    # public static final dev.ultreon.quantum.text.TextDecoration dev.ultreon.quantum.text.TextDecoration.ITALIC
    ITALIC: 'TextDecoration' = __wrap(__TextDecoration.ITALIC)

    # public static final dev.ultreon.quantum.text.TextDecoration dev.ultreon.quantum.text.TextDecoration.BOLD
    BOLD: 'TextDecoration' = __wrap(__TextDecoration.BOLD)

    # public static final dev.ultreon.quantum.text.TextDecoration dev.ultreon.quantum.text.TextDecoration.UNDERLINED
    UNDERLINED: 'TextDecoration' = __wrap(__TextDecoration.UNDERLINED)

    # public static final dev.ultreon.quantum.text.TextDecoration dev.ultreon.quantum.text.TextDecoration.STRIKETHROUGH
    STRIKETHROUGH: 'TextDecoration' = __wrap(__TextDecoration.STRIKETHROUGH)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def values() -> List['TextDecoration']:
        """public static dev.ultreon.quantum.text.TextDecoration[] dev.ultreon.quantum.text.TextDecoration.values()"""
        return List[TextDecoration].__wrap(__TextDecoration.values())

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
    def valueOf(arg0: str) -> 'TextDecoration':
        """public static dev.ultreon.quantum.text.TextDecoration dev.ultreon.quantum.text.TextDecoration.valueOf(java.lang.String)"""
        return TextDecoration.__wrap(__TextDecoration.valueOf(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.text.TextDecoration
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.text.TextDecoration as __TextDecoration
__TextDecoration = __TextDecoration
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
 
class TextDecoration(__Enum, Enum):
    """dev.ultreon.quantum.text.TextDecoration"""
 
    @staticmethod
    def __wrap(java_value: __TextDecoration) -> 'TextDecoration':
        return TextDecoration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextDecoration):
        """
        Dynamic initializer for TextDecoration.
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
 
    # public static final dev.ultreon.quantum.text.TextDecoration dev.ultreon.quantum.text.TextDecoration.ITALIC
    ITALIC: 'TextDecoration' = __wrap(__TextDecoration.ITALIC)

    # public static final dev.ultreon.quantum.text.TextDecoration dev.ultreon.quantum.text.TextDecoration.BOLD
    BOLD: 'TextDecoration' = __wrap(__TextDecoration.BOLD)

    # public static final dev.ultreon.quantum.text.TextDecoration dev.ultreon.quantum.text.TextDecoration.UNDERLINED
    UNDERLINED: 'TextDecoration' = __wrap(__TextDecoration.UNDERLINED)

    # public static final dev.ultreon.quantum.text.TextDecoration dev.ultreon.quantum.text.TextDecoration.STRIKETHROUGH
    STRIKETHROUGH: 'TextDecoration' = __wrap(__TextDecoration.STRIKETHROUGH)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def values() -> List['TextDecoration']:
        """public static dev.ultreon.quantum.text.TextDecoration[] dev.ultreon.quantum.text.TextDecoration.values()"""
        return List[TextDecoration].__wrap(__TextDecoration.values())

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
    def valueOf(arg0: str) -> 'TextDecoration':
        """public static dev.ultreon.quantum.text.TextDecoration dev.ultreon.quantum.text.TextDecoration.valueOf(java.lang.String)"""
        return TextDecoration.__wrap(__TextDecoration.valueOf(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.text.TextDecoration 
 
 
# CLASS: dev.ultreon.quantum.text.ColorCode
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from pyquantum_helper import transform as __transform
import java.lang.Character as __char
from builtins import type
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
from builtins import bool
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Optional as __Optional
__Optional = __Optional
import dev.ultreon.quantum.text.ColorCode as __ColorCode
__ColorCode = __ColorCode
from typing import List
import java.lang.Enum as Enum
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import dev.ultreon.quantum.util.Color as __Color
__Color = __Color
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.Integer as Integer
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class ColorCode(__Enum, Enum, pyquantum.__Color, util.Color):
    """dev.ultreon.quantum.text.ColorCode"""
 
    @staticmethod
    def __wrap(java_value: __ColorCode) -> 'ColorCode':
        return ColorCode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ColorCode):
        """
        Dynamic initializer for ColorCode.
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
 
    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.DARK_GREEN
    DARK_GREEN: 'ColorCode' = __wrap(__ColorCode.DARK_GREEN)

    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.ORANGE
    ORANGE: 'ColorCode' = __wrap(__ColorCode.ORANGE)

    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.DARK_RED
    DARK_RED: 'ColorCode' = __wrap(__ColorCode.DARK_RED)

    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.DARK_PURPLE
    DARK_PURPLE: 'ColorCode' = __wrap(__ColorCode.DARK_PURPLE)

    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.AQUA
    AQUA: 'ColorCode' = __wrap(__ColorCode.AQUA)

    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.UNDERLINE
    UNDERLINE: 'ColorCode' = __wrap(__ColorCode.UNDERLINE)

    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.AZURE
    AZURE: 'ColorCode' = __wrap(__ColorCode.AZURE)

    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.DARK_AQUA
    DARK_AQUA: 'ColorCode' = __wrap(__ColorCode.DARK_AQUA)

    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.GOLD
    GOLD: 'ColorCode' = __wrap(__ColorCode.GOLD)

    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.MAGIC
    MAGIC: 'ColorCode' = __wrap(__ColorCode.MAGIC)

    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.BLUE
    BLUE: 'ColorCode' = __wrap(__ColorCode.BLUE)

    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.GRAY
    GRAY: 'ColorCode' = __wrap(__ColorCode.GRAY)

    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.LIGHT_PURPLE
    LIGHT_PURPLE: 'ColorCode' = __wrap(__ColorCode.LIGHT_PURPLE)

    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.WHITE
    WHITE: 'ColorCode' = __wrap(__ColorCode.WHITE)

    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.MAGENTA
    MAGENTA: 'ColorCode' = __wrap(__ColorCode.MAGENTA)

    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.ITALIC
    ITALIC: 'ColorCode' = __wrap(__ColorCode.ITALIC)

    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.DARK_BLUE
    DARK_BLUE: 'ColorCode' = __wrap(__ColorCode.DARK_BLUE)

    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.STRIKETHROUGH
    STRIKETHROUGH: 'ColorCode' = __wrap(__ColorCode.STRIKETHROUGH)

    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.RED
    RED: 'ColorCode' = __wrap(__ColorCode.RED)

    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.BOLD
    BOLD: 'ColorCode' = __wrap(__ColorCode.BOLD)

    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.BLACK
    BLACK: 'ColorCode' = __wrap(__ColorCode.BLACK)

    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.DARK_GRAY
    DARK_GRAY: 'ColorCode' = __wrap(__ColorCode.DARK_GRAY)

    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.RESET
    RESET: 'ColorCode' = __wrap(__ColorCode.RESET)

    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.GREEN
    GREEN: 'ColorCode' = __wrap(__ColorCode.GREEN)

    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.LIME
    LIME: 'ColorCode' = __wrap(__ColorCode.LIME)

    # public static final dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.YELLOW
    YELLOW: 'ColorCode' = __wrap(__ColorCode.YELLOW)


    @overload
    def isFormat(self) -> bool:
        """public boolean dev.ultreon.quantum.text.ColorCode.isFormat()"""
        return bool.__wrap(super(ColorCode, self).isFormat())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def withGreen(self, arg0: int) -> 'util.Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.withGreen(int)"""
        return 'util.Color'.__wrap(super(__util.Color, self).withGreen(__int.valueOf(arg0)))

    @overload
    def getColor(self) -> 'Integer':
        """public java.lang.Integer dev.ultreon.quantum.text.ColorCode.getColor()"""
        return __transform(super(ColorCode, self).getColor()).'Integer'Value()

    @staticmethod
    @overload
    def values() -> List['ColorCode']:
        """public static dev.ultreon.quantum.text.ColorCode[] dev.ultreon.quantum.text.ColorCode.values()"""
        return List[ColorCode].__wrap(__ColorCode.values())

    @overload
    def getCode(self) -> str:
        """public char dev.ultreon.quantum.text.ColorCode.getCode()"""
        return str.__wrap(super(ColorCode, self).getCode())

    @override
    @overload
    def getBlue(self) -> int:
        """public int dev.ultreon.quantum.text.ColorCode.getBlue()"""
        return int.__wrap(super(ColorCode, self).getBlue())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def lighter(self) -> 'util.Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.lighter()"""
        return 'util.Color'.__wrap(super(util.Color, self).lighter())

    @overload
    def isColor(self) -> bool:
        """public boolean dev.ultreon.quantum.text.ColorCode.isColor()"""
        return bool.__wrap(super(ColorCode, self).isColor())

    @override
    @overload
    def toGdx(self) -> 'graphics.Color':
        """public default com.badlogic.gdx.graphics.Color dev.ultreon.quantum.util.Color.toGdx()"""
        return 'graphics.Color'.__wrap(super(util.Color, self).toGdx())

    @staticmethod
    @overload
    def getByChar(arg0: str) -> 'ColorCode':
        """public static dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.getByChar(char)"""
        return ColorCode.__wrap(__ColorCode.getByChar(__char.valueOf(arg0)))

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @overload
    def concat(self, arg0: 'ColorCode') -> str:
        """public java.lang.String dev.ultreon.quantum.text.ColorCode.concat(dev.ultreon.quantum.text.ColorCode)"""
        return str.__wrap(super(__ColorCode, self).concat(arg0))

    @staticmethod
    @overload
    def getByChar(arg0: str) -> 'ColorCode':
        """public static dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.getByChar(java.lang.String)"""
        return ColorCode.__wrap(__ColorCode.getByChar(arg0))

    @override
    @overload
    def toHex(self) -> str:
        """public default java.lang.String dev.ultreon.quantum.util.Color.toHex()"""
        return str.__wrap(super(util.Color, self).toHex())

    @override
    @overload
    def darker(self) -> 'util.Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.darker()"""
        return 'util.Color'.__wrap(super(util.Color, self).darker())

    @staticmethod
    @overload
    def stripColor(arg0: str) -> str:
        """public static java.lang.String dev.ultreon.quantum.text.ColorCode.stripColor(java.lang.String)"""
        return str.__wrap(__ColorCode.stripColor(arg0))

    @override
    @overload
    def getRed(self) -> int:
        """public int dev.ultreon.quantum.text.ColorCode.getRed()"""
        return int.__wrap(super(ColorCode, self).getRed())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @overload
    def withBlue(self, arg0: int) -> 'util.Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.withBlue(int)"""
        return 'util.Color'.__wrap(super(__util.Color, self).withBlue(__int.valueOf(arg0)))

    @overload
    def withAlpha(self, arg0: int) -> 'util.Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.withAlpha(int)"""
        return 'util.Color'.__wrap(super(__util.Color, self).withAlpha(__int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def getLastColors(arg0: str) -> 'ColorCode':
        """public static dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.getLastColors(java.lang.String)"""
        return ColorCode.__wrap(__ColorCode.getLastColors(arg0))

    @overload
    def getIntCode(self) -> int:
        """public int dev.ultreon.quantum.text.ColorCode.getIntCode()"""
        return int.__wrap(super(ColorCode, self).getIntCode())

    @override
    @overload
    def getGreen(self) -> int:
        """public int dev.ultreon.quantum.text.ColorCode.getGreen()"""
        return int.__wrap(super(ColorCode, self).getGreen())

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

    @staticmethod
    @overload
    def getById(arg0: int) -> 'ColorCode':
        """public static dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.getById(int)"""
        return ColorCode.__wrap(__ColorCode.getById(__int.valueOf(arg0)))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def asBungee(self) -> 'ColorCode':
        """public dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.asBungee()"""
        return 'ColorCode'.__wrap(super(ColorCode, self).asBungee())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.text.ColorCode.toString()"""
        return str.__wrap(super(ColorCode, self).toString())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ColorCode':
        """public static dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.valueOf(java.lang.String)"""
        return ColorCode.__wrap(__ColorCode.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getAlpha(self) -> int:
        """public int dev.ultreon.quantum.text.ColorCode.getAlpha()"""
        return int.__wrap(super(ColorCode, self).getAlpha())

    @overload
    def withRed(self, arg0: int) -> 'util.Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.withRed(int)"""
        return 'util.Color'.__wrap(super(__util.Color, self).withRed(__int.valueOf(arg0)))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def concat(self, arg0: str) -> str:
        """public java.lang.String dev.ultreon.quantum.text.ColorCode.concat(java.lang.String)"""
        return str.__wrap(super(__ColorCode, self).concat(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.text.TextObject
from pyquantum_helper import import_once as __import_once__
from builtins import type
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.quantum.text.LiteralText as __LiteralText
__LiteralText = __LiteralText
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Iterator as __Iterator
__Iterator = __Iterator
import java.lang.Object as __object
from builtins import object
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.text.TranslationText as __TranslationText
__TranslationText = __TranslationText
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.text.TextStyle as __TextStyle
__TextStyle = __TextStyle
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class TextObject(ABC, __Iterable, Iterable):
    """dev.ultreon.quantum.text.TextObject"""
 
    @staticmethod
    def __wrap(java_value: __TextObject) -> 'TextObject':
        return TextObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextObject):
        """
        Dynamic initializer for TextObject.
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

    @abstractmethod
    def copy(self, ):
        """public abstract dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.TextObject.copy()"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getText(self) -> str:
        """public java.lang.String dev.ultreon.quantum.text.TextObject.getText()"""
        return str.__wrap(super(TextObject, self).getText())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.text.TextObject.iterator()"""
        return 'Iterator'.__wrap(super(TextObject, self).iterator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @abstractmethod
    def createString(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.text.TextObject.createString()"""
        pass

    @staticmethod
    @overload
    def translation(arg0: str, *arg1: object) -> 'TranslationText':
        """public static dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.text.TextObject.translation(java.lang.String,java.lang.Object...)"""
        return TranslationText.__wrap(__TextObject.translation(arg0, arg1))

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
    def nullToEmpty(arg0: 'TextObject') -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.nullToEmpty(dev.ultreon.quantum.text.TextObject)"""
        return TextObject.__wrap(__TextObject.nullToEmpty(arg0))

    @staticmethod
    @overload
    def deserialize(arg0: 'MapType') -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.deserialize(dev.ultreon.ubo.types.MapType)"""
        return TextObject.__wrap(__TextObject.deserialize(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getStyle(self) -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextObject.getStyle()"""
        return 'TextStyle'.__wrap(super(TextObject, self).getStyle())

    @abstractmethod
    def serialize(self, ):
        """public abstract dev.ultreon.ubo.types.MapType dev.ultreon.quantum.text.TextObject.serialize()"""
        pass

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @staticmethod
    @overload
    def empty() -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.empty()"""
        return TextObject.__wrap(__TextObject.empty())

    @staticmethod
    @overload
    def literal(arg0: str) -> 'LiteralText':
        """public static dev.ultreon.quantum.text.LiteralText dev.ultreon.quantum.text.TextObject.literal(java.lang.String)"""
        return LiteralText.__wrap(__TextObject.literal(arg0))

    @staticmethod
    @overload
    def nullToEmpty(arg0: str) -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.nullToEmpty(java.lang.String)"""
        return TextObject.__wrap(__TextObject.nullToEmpty(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.text.LiteralText
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
from builtins import type
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.text.LiteralText as __LiteralText
__LiteralText = __LiteralText
import java.lang.String as __string
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
from builtins import bool
import dev.ultreon.quantum.text.MutableText as __MutableText
__MutableText = __MutableText
from builtins import str
import dev.ultreon.quantum.util.RgbColor as __RgbColor
__RgbColor = __RgbColor
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import object
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.text.TranslationText as __TranslationText
__TranslationText = __TranslationText
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.text.TextStyle as __TextStyle
__TextStyle = __TextStyle
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class LiteralText(__MutableText, MutableText):
    """dev.ultreon.quantum.text.LiteralText"""
 
    @staticmethod
    def __wrap(java_value: __LiteralText) -> 'LiteralText':
        return LiteralText(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LiteralText):
        """
        Dynamic initializer for LiteralText.
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
    def setColor(self, arg0: 'RgbColor') -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setColor(dev.ultreon.quantum.util.RgbColor)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setColor(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def translation(arg0: str, *arg1: object) -> 'TranslationText':
        """public static dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.text.TextObject.translation(java.lang.String,java.lang.Object...)"""
        return TranslationText.__wrap(__TextObject.translation(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isBold(self) -> bool:
        """public boolean dev.ultreon.quantum.text.MutableText.isBold()"""
        return bool.__wrap(super(MutableText, self).isBold())

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'TextObject') -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.nullToEmpty(dev.ultreon.quantum.text.TextObject)"""
        return TextObject.__wrap(__TextObject.nullToEmpty(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def getSize(self) -> int:
        """public int dev.ultreon.quantum.text.MutableText.getSize()"""
        return int.__wrap(super(MutableText, self).getSize())

    @overload
    def setBold(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setBold(boolean)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setBold(__boolean.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def serialize(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.text.LiteralText.serialize()"""
        return 'types.MapType'.__wrap(super(LiteralText, self).serialize())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def copy(self) -> 'LiteralText':
        """public dev.ultreon.quantum.text.LiteralText dev.ultreon.quantum.text.LiteralText.copy()"""
        return 'LiteralText'.__wrap(super(LiteralText, self).copy())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.text.TextObject.iterator()"""
        return 'Iterator'.__wrap(super(TextObject, self).iterator())

    @staticmethod
    @overload
    def deserialize(arg0: 'MapType') -> 'LiteralText':
        """public static dev.ultreon.quantum.text.LiteralText dev.ultreon.quantum.text.LiteralText.deserialize(dev.ultreon.ubo.types.MapType)"""
        return LiteralText.__wrap(__LiteralText.deserialize(arg0))

    @overload
    def setStrikethrough(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setStrikethrough(boolean)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setStrikethrough(__boolean.valueOf(arg0)))

    @override
    @overload
    def createString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.text.LiteralText.createString()"""
        return str.__wrap(super(LiteralText, self).createString())

    @override
    @overload
    def getColor(self) -> 'util.RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.text.MutableText.getColor()"""
        return 'util.RgbColor'.__wrap(super(MutableText, self).getColor())

    @override
    @overload
    def isUnderlined(self) -> bool:
        """public boolean dev.ultreon.quantum.text.MutableText.isUnderlined()"""
        return bool.__wrap(super(MutableText, self).isUnderlined())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setColor(self, arg0: 'ColorCode') -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.LiteralText.setColor(dev.ultreon.quantum.text.ColorCode)"""
        return 'MutableText'.__wrap(super(__LiteralText, self).setColor(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getStyle(self) -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextObject.getStyle()"""
        return 'TextStyle'.__wrap(super(TextObject, self).getStyle())

    @override
    @overload
    def isStrikethrough(self) -> bool:
        """public boolean dev.ultreon.quantum.text.MutableText.isStrikethrough()"""
        return bool.__wrap(super(MutableText, self).isStrikethrough())

    @override
    @overload
    def setSize(self, arg0: int):
        """public void dev.ultreon.quantum.text.MutableText.setSize(int)"""
        super(__MutableText, self).setSize(__int.valueOf(arg0))

    @override
    @overload
    def isItalic(self) -> bool:
        """public boolean dev.ultreon.quantum.text.MutableText.isItalic()"""
        return bool.__wrap(super(MutableText, self).isItalic())

    @staticmethod
    @overload
    def deserialize(arg0: 'MapType') -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.deserialize(dev.ultreon.ubo.types.MapType)"""
        return TextObject.__wrap(__TextObject.deserialize(arg0))

    @overload
    def setItalic(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setItalic(boolean)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setItalic(__boolean.valueOf(arg0)))

    @overload
    def append(self, arg0: object) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.append(java.lang.Object)"""
        return 'MutableText'.__wrap(super(__MutableText, self).append(arg0))

    @override
    @overload
    def getText(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.text.MutableText.getText()"""
        return str.__wrap(super(MutableText, self).getText())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def setUnderlined(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setUnderlined(boolean)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setUnderlined(__boolean.valueOf(arg0)))

    @staticmethod
    @overload
    def empty() -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.empty()"""
        return TextObject.__wrap(__TextObject.empty())

    @staticmethod
    @overload
    def literal(arg0: str) -> 'LiteralText':
        """public static dev.ultreon.quantum.text.LiteralText dev.ultreon.quantum.text.TextObject.literal(java.lang.String)"""
        return LiteralText.__wrap(__TextObject.literal(arg0))

    @staticmethod
    @overload
    def nullToEmpty(arg0: str) -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.nullToEmpty(java.lang.String)"""
        return TextObject.__wrap(__TextObject.nullToEmpty(arg0))

    @overload
    def style(self, arg0: 'Consumer') -> 'LiteralText':
        """public dev.ultreon.quantum.text.LiteralText dev.ultreon.quantum.text.LiteralText.style(java.util.function.Consumer<dev.ultreon.quantum.text.TextStyle>)"""
        return 'LiteralText'.__wrap(super(__LiteralText, self).style(arg0))

    @overload
    def append(self, arg0: 'TextObject') -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.append(dev.ultreon.quantum.text.TextObject)"""
        return 'MutableText'.__wrap(super(__MutableText, self).append(arg0))

    @overload
    def append(self, arg0: str) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.append(java.lang.String)"""
        return 'MutableText'.__wrap(super(__MutableText, self).append(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.text.Formatter
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.text.Formatter as __Formatter
__Formatter = __Formatter
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.text.ParseResult as __ParseResult
__ParseResult = __ParseResult
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Formatter():
    """dev.ultreon.quantum.text.Formatter"""
 
    @staticmethod
    def __wrap(java_value: __Formatter) -> 'Formatter':
        return Formatter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Formatter):
        """
        Dynamic initializer for Formatter.
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
    def format(arg0: str) -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.Formatter.format(java.lang.String)"""
        return TextObject.__wrap(__Formatter.format(arg0))

    @overload
    def c(self) -> str:
        """public char dev.ultreon.quantum.text.Formatter.c()"""
        return str.__wrap(super(Formatter, self).c())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def parseColor(self):
        """public void dev.ultreon.quantum.text.Formatter.parseColor()"""
        super(Formatter, self).parseColor()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def parseId(self):
        """public void dev.ultreon.quantum.text.Formatter.parseId()"""
        super(Formatter, self).parseId()

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
    def format(arg0: str, arg1: bool) -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.Formatter.format(java.lang.String,boolean)"""
        return TextObject.__wrap(__Formatter.format(arg0, __boolean.valueOf(arg1)))

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
    def getCurrentFont(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.text.Formatter.getCurrentFont()"""
        return 'util.Identifier'.__wrap(super(Formatter, self).getCurrentFont())

    @overload
    def parse(self) -> 'ParseResult':
        """public dev.ultreon.quantum.text.ParseResult dev.ultreon.quantum.text.Formatter.parse()"""
        return 'ParseResult'.__wrap(super(Formatter, self).parse())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: bool, arg1: bool, arg2: str, arg3: 'TextObject', arg4: 'TextObject', arg5: 'Player', arg6: 'RgbColor'):
        """public dev.ultreon.quantum.text.Formatter(boolean,boolean,java.lang.String,dev.ultreon.quantum.text.TextObject,dev.ultreon.quantum.text.TextObject,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.util.RgbColor)"""
        val = __Formatter(__boolean.valueOf(arg0), __boolean.valueOf(arg1), arg2, arg3, arg4, arg5, arg6)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.text.FormatSequence
import java.util.Spliterator as Spliterator
from abc import abstractmethod, ABC
import dev.ultreon.quantum.text.FormatSequence as __FormatSequence
__FormatSequence = __FormatSequence
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
import java.util.function.Consumer as Consumer
 
class FormatSequence(ABC, __Iterable, Iterable):
    """dev.ultreon.quantum.text.FormatSequence"""
 
    @staticmethod
    def __wrap(java_value: __FormatSequence) -> 'FormatSequence':
        return FormatSequence(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FormatSequence):
        """
        Dynamic initializer for FormatSequence.
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
    def isBoldAt(self, arg0: int):
        """public abstract boolean dev.ultreon.quantum.text.FormatSequence.isBoldAt(int)"""
        pass

    @abstractmethod
    def getHoverEventAt(self, arg0: int):
        """public abstract dev.ultreon.quantum.text.HoverEvent<?> dev.ultreon.quantum.text.FormatSequence.getHoverEventAt(int)"""
        pass

    @abstractmethod
    def getFontAt(self, arg0: int):
        """public abstract dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.text.FormatSequence.getFontAt(int)"""
        pass

    @abstractmethod
    def getColorAt(self, arg0: int):
        """public abstract dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.text.FormatSequence.getColorAt(int)"""
        pass

    @abstractmethod
    def iterator(self, ):
        """public abstract java.util.Iterator<T> java.lang.Iterable.iterator()"""
        pass

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @abstractmethod
    def isItalicAt(self, arg0: int):
        """public abstract boolean dev.ultreon.quantum.text.FormatSequence.isItalicAt(int)"""
        pass

    @abstractmethod
    def getClickEventAt(self, arg0: int):
        """public abstract dev.ultreon.quantum.text.ClickEvent dev.ultreon.quantum.text.FormatSequence.getClickEventAt(int)"""
        pass

    @abstractmethod
    def getTextAt(self, arg0: int):
        """public abstract dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.FormatSequence.getTextAt(int)"""
        pass

    @abstractmethod
    def isUnderlinedAt(self, arg0: int):
        """public abstract boolean dev.ultreon.quantum.text.FormatSequence.isUnderlinedAt(int)"""
        pass

    @abstractmethod
    def isStrikethroughAt(self, arg0: int):
        """public abstract boolean dev.ultreon.quantum.text.FormatSequence.isStrikethroughAt(int)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.text.TextStyle
from pyquantum_helper import import_once as __import_once__
import dev.ultreon.quantum.util.RgbColor as __RgbColor
__RgbColor = __RgbColor
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.text.HoverEvent as __HoverEvent
__HoverEvent = __HoverEvent
import dev.ultreon.quantum.text.ClickEvent as __ClickEvent
__ClickEvent = __ClickEvent
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.text.TextStyle as __TextStyle
__TextStyle = __TextStyle
from builtins import int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

 
class TextStyle():
    """dev.ultreon.quantum.text.TextStyle"""
 
    @staticmethod
    def __wrap(java_value: __TextStyle) -> 'TextStyle':
        return TextStyle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextStyle):
        """
        Dynamic initializer for TextStyle.
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
    def getHoverEvent(self) -> 'HoverEvent':
        """public dev.ultreon.quantum.text.HoverEvent<?> dev.ultreon.quantum.text.TextStyle.getHoverEvent()"""
        return 'HoverEvent'.__wrap(super(TextStyle, self).getHoverEvent())

    @overload
    def getColor(self) -> 'util.RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.text.TextStyle.getColor()"""
        return 'util.RgbColor'.__wrap(super(TextStyle, self).getColor())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def color(self, arg0: 'RgbColor') -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextStyle.color(dev.ultreon.quantum.util.RgbColor)"""
        return 'TextStyle'.__wrap(super(__TextStyle, self).color(arg0))

    @overload
    def isUnderline(self) -> bool:
        """public boolean dev.ultreon.quantum.text.TextStyle.isUnderline()"""
        return bool.__wrap(super(TextStyle, self).isUnderline())

    @overload
    def isItalic(self) -> bool:
        """public boolean dev.ultreon.quantum.text.TextStyle.isItalic()"""
        return bool.__wrap(super(TextStyle, self).isItalic())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def isStrikethrough(self) -> bool:
        """public boolean dev.ultreon.quantum.text.TextStyle.isStrikethrough()"""
        return bool.__wrap(super(TextStyle, self).isStrikethrough())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def underline(self, arg0: bool) -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextStyle.underline(boolean)"""
        return 'TextStyle'.__wrap(super(__TextStyle, self).underline(__boolean.valueOf(arg0)))

    @overload
    def bold(self, arg0: bool) -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextStyle.bold(boolean)"""
        return 'TextStyle'.__wrap(super(__TextStyle, self).bold(__boolean.valueOf(arg0)))

    @overload
    def getClickEvent(self) -> 'ClickEvent':
        """public dev.ultreon.quantum.text.ClickEvent dev.ultreon.quantum.text.TextStyle.getClickEvent()"""
        return 'ClickEvent'.__wrap(super(TextStyle, self).getClickEvent())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def strikethrough(self, arg0: bool) -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextStyle.strikethrough(boolean)"""
        return 'TextStyle'.__wrap(super(__TextStyle, self).strikethrough(__boolean.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getSize(self) -> int:
        """public int dev.ultreon.quantum.text.TextStyle.getSize()"""
        return int.__wrap(super(TextStyle, self).getSize())

    @overload
    def getFont(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.text.TextStyle.getFont()"""
        return 'util.Identifier'.__wrap(super(TextStyle, self).getFont())

    @overload
    def serialize(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.text.TextStyle.serialize()"""
        return 'types.MapType'.__wrap(super(TextStyle, self).serialize())

    @overload
    def hoverEvent(self, arg0: 'HoverEvent') -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextStyle.hoverEvent(dev.ultreon.quantum.text.HoverEvent<?>)"""
        return 'TextStyle'.__wrap(super(__TextStyle, self).hoverEvent(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.text.TextStyle()"""
        val = __TextStyle()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def italic(self, arg0: bool) -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextStyle.italic(boolean)"""
        return 'TextStyle'.__wrap(super(__TextStyle, self).italic(__boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def copy(self) -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextStyle.copy()"""
        return 'TextStyle'.__wrap(super(TextStyle, self).copy())

    @overload
    def clickEvent(self, arg0: 'ClickEvent') -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextStyle.clickEvent(dev.ultreon.quantum.text.ClickEvent)"""
        return 'TextStyle'.__wrap(super(__TextStyle, self).clickEvent(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.text.TextStyle()"""
        val = __TextStyle()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def deserialize(arg0: 'MapType') -> 'TextStyle':
        """public static dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextStyle.deserialize(dev.ultreon.ubo.types.MapType)"""
        return TextStyle.__wrap(__TextStyle.deserialize(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def size(self, arg0: int) -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextStyle.size(int)"""
        return 'TextStyle'.__wrap(super(__TextStyle, self).size(__int.valueOf(arg0)))

    @overload
    def font(self, arg0: 'Identifier') -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextStyle.font(dev.ultreon.quantum.util.Identifier)"""
        return 'TextStyle'.__wrap(super(__TextStyle, self).font(arg0))

    @staticmethod
    @overload
    def defaultStyle() -> 'TextStyle':
        """public static dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextStyle.defaultStyle()"""
        return TextStyle.__wrap(__TextStyle.defaultStyle())

    @overload
    def color(self, arg0: 'ColorCode'):
        """public void dev.ultreon.quantum.text.TextStyle.color(dev.ultreon.quantum.text.ColorCode)"""
        super(__TextStyle, self).color(arg0)

    @overload
    def isBold(self) -> bool:
        """public boolean dev.ultreon.quantum.text.TextStyle.isBold()"""
        return bool.__wrap(super(TextStyle, self).isBold()) 
 
 
# CLASS: dev.ultreon.quantum.text.TextKey
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.api import commands
except ImportError:
    commands = __import_once__("pyquantum.api.commands")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.text.TextKey as __TextKey
__TextKey = __TextKey
 
class TextKey(ABC):
    """dev.ultreon.quantum.text.TextKey"""
 
    @staticmethod
    def __wrap(java_value: __TextKey) -> 'TextKey':
        return TextKey(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextKey):
        """
        Dynamic initializer for TextKey.
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
    def get(self, arg0: 'CommandSender'):
        """public abstract java.lang.String dev.ultreon.quantum.text.TextKey.get(dev.ultreon.quantum.api.commands.CommandSender)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.text.TranslationText
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
import dev.ultreon.ubo.types.MapType as __MapType
__MapType = __MapType
from builtins import type
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.quantum.text.LiteralText as __LiteralText
__LiteralText = __LiteralText
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
from builtins import bool
import dev.ultreon.quantum.text.MutableText as __MutableText
__MutableText = __MutableText
from builtins import str
import dev.ultreon.quantum.util.RgbColor as __RgbColor
__RgbColor = __RgbColor
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import object
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import dev.ultreon.quantum.text.TranslationText as __TranslationText
__TranslationText = __TranslationText
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.text.TextStyle as __TextStyle
__TextStyle = __TextStyle
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

from builtins import int
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class TranslationText(__MutableText, MutableText):
    """dev.ultreon.quantum.text.TranslationText"""
 
    @staticmethod
    def __wrap(java_value: __TranslationText) -> 'TranslationText':
        return TranslationText(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TranslationText):
        """
        Dynamic initializer for TranslationText.
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
    def style(self, arg0: 'Consumer') -> 'TranslationText':
        """public dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.text.TranslationText.style(java.util.function.Consumer<dev.ultreon.quantum.text.TextStyle>)"""
        return 'TranslationText'.__wrap(super(__TranslationText, self).style(arg0))

    @overload
    def setColor(self, arg0: 'RgbColor') -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setColor(dev.ultreon.quantum.util.RgbColor)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setColor(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def translation(arg0: str, *arg1: object) -> 'TranslationText':
        """public static dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.text.TextObject.translation(java.lang.String,java.lang.Object...)"""
        return TranslationText.__wrap(__TextObject.translation(arg0, arg1))

    @override
    @overload
    def copy(self) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.TranslationText.copy()"""
        return 'MutableText'.__wrap(super(TranslationText, self).copy())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isBold(self) -> bool:
        """public boolean dev.ultreon.quantum.text.MutableText.isBold()"""
        return bool.__wrap(super(MutableText, self).isBold())

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'TextObject') -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.nullToEmpty(dev.ultreon.quantum.text.TextObject)"""
        return TextObject.__wrap(__TextObject.nullToEmpty(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def deserialize(arg0: 'MapType') -> 'TranslationText':
        """public static dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.text.TranslationText.deserialize(dev.ultreon.ubo.types.MapType)"""
        return TranslationText.__wrap(__TranslationText.deserialize(arg0))

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @override
    @overload
    def getSize(self) -> int:
        """public int dev.ultreon.quantum.text.MutableText.getSize()"""
        return int.__wrap(super(MutableText, self).getSize())

    @overload
    def setBold(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setBold(boolean)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setBold(__boolean.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def serialize(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.text.TranslationText.serialize()"""
        return 'types.MapType'.__wrap(super(TranslationText, self).serialize())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.text.TextObject.iterator()"""
        return 'Iterator'.__wrap(super(TextObject, self).iterator())

    @overload
    def setStrikethrough(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setStrikethrough(boolean)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setStrikethrough(__boolean.valueOf(arg0)))

    @override
    @overload
    def createString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.text.TranslationText.createString()"""
        return str.__wrap(super(TranslationText, self).createString())

    @override
    @overload
    def getColor(self) -> 'util.RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.text.MutableText.getColor()"""
        return 'util.RgbColor'.__wrap(super(MutableText, self).getColor())

    @override
    @overload
    def isUnderlined(self) -> bool:
        """public boolean dev.ultreon.quantum.text.MutableText.isUnderlined()"""
        return bool.__wrap(super(MutableText, self).isUnderlined())

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
    def getStyle(self) -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextObject.getStyle()"""
        return 'TextStyle'.__wrap(super(TextObject, self).getStyle())

    @override
    @overload
    def isStrikethrough(self) -> bool:
        """public boolean dev.ultreon.quantum.text.MutableText.isStrikethrough()"""
        return bool.__wrap(super(MutableText, self).isStrikethrough())

    @override
    @overload
    def setSize(self, arg0: int):
        """public void dev.ultreon.quantum.text.MutableText.setSize(int)"""
        super(__MutableText, self).setSize(__int.valueOf(arg0))

    @override
    @overload
    def isItalic(self) -> bool:
        """public boolean dev.ultreon.quantum.text.MutableText.isItalic()"""
        return bool.__wrap(super(MutableText, self).isItalic())

    @staticmethod
    @overload
    def deserialize(arg0: 'MapType') -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.deserialize(dev.ultreon.ubo.types.MapType)"""
        return TextObject.__wrap(__TextObject.deserialize(arg0))

    @overload
    def setItalic(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setItalic(boolean)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setItalic(__boolean.valueOf(arg0)))

    @overload
    def append(self, arg0: object) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.append(java.lang.Object)"""
        return 'MutableText'.__wrap(super(__MutableText, self).append(arg0))

    @override
    @overload
    def getText(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.text.MutableText.getText()"""
        return str.__wrap(super(MutableText, self).getText())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def setUnderlined(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setUnderlined(boolean)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setUnderlined(__boolean.valueOf(arg0)))

    @staticmethod
    @overload
    def empty() -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.empty()"""
        return TextObject.__wrap(__TextObject.empty())

    @staticmethod
    @overload
    def literal(arg0: str) -> 'LiteralText':
        """public static dev.ultreon.quantum.text.LiteralText dev.ultreon.quantum.text.TextObject.literal(java.lang.String)"""
        return LiteralText.__wrap(__TextObject.literal(arg0))

    @staticmethod
    @overload
    def nullToEmpty(arg0: str) -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.nullToEmpty(java.lang.String)"""
        return TextObject.__wrap(__TextObject.nullToEmpty(arg0))

    @overload
    def append(self, arg0: 'TextObject') -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.append(dev.ultreon.quantum.text.TextObject)"""
        return 'MutableText'.__wrap(super(__MutableText, self).append(arg0))

    @overload
    def append(self, arg0: str) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.append(java.lang.String)"""
        return 'MutableText'.__wrap(super(__MutableText, self).append(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.text.Translations
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
import dev.ultreon.quantum.text.Translations as __Translations
__Translations = __Translations
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Translations():
    """dev.ultreon.quantum.text.Translations"""
 
    @staticmethod
    def __wrap(java_value: __Translations) -> 'Translations':
        return Translations(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Translations):
        """
        Dynamic initializer for Translations.
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
 
    # public static final dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.Translations.NULL_OBJECT
    NULL_OBJECT: 'TextObject' = __wrap(__TextObject.NULL_OBJECT)


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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.text.Translations()"""
        val = __Translations()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self):
        """public dev.ultreon.quantum.text.Translations()"""
        val = __Translations()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.text.FontTexture
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.quantum.text.FontTexture as __FontTexture
__FontTexture = __FontTexture
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FontTexture():
    """dev.ultreon.quantum.text.FontTexture"""
 
    @staticmethod
    def __wrap(java_value: __FontTexture) -> 'FontTexture':
        return FontTexture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FontTexture):
        """
        Dynamic initializer for FontTexture.
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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.text.FontTexture.equals(java.lang.Object)"""
        return bool.__wrap(super(__FontTexture, self).equals(arg0))

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
    def __init__(self, arg0: str, arg1: 'Identifier'):
        """public dev.ultreon.quantum.text.FontTexture(char,dev.ultreon.quantum.util.Identifier)"""
        val = __FontTexture(__char.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int, arg1: 'Identifier'):
        """public dev.ultreon.quantum.text.FontTexture(int,dev.ultreon.quantum.util.Identifier)"""
        val = __FontTexture(__int.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.text.FontTexture.hashCode()"""
        return int.__wrap(super(FontTexture, self).hashCode())

    @overload
    def getFont(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.text.FontTexture.getFont()"""
        return 'util.Identifier'.__wrap(super(FontTexture, self).getFont())

    @overload
    def getChar(self) -> str:
        """public char dev.ultreon.quantum.text.FontTexture.getChar()"""
        return str.__wrap(super(FontTexture, self).getChar()) 
 
 
# CLASS: dev.ultreon.quantum.text.HoverEvent$Action
import dev.ultreon.quantum.text.HoverEvent as __HoverEvent_Action
__Action = __HoverEvent_Action.Action
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
from builtins import int
 
class Action(__Enum, Enum):
    """dev.ultreon.quantum.text.HoverEvent.Action"""
 
    @staticmethod
    def __wrap(java_value: __Action) -> 'Action':
        return Action(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Action):
        """
        Dynamic initializer for Action.
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
 
    # public static final dev.ultreon.quantum.text.HoverEvent$Action dev.ultreon.quantum.text.HoverEvent$Action.ENTITY
    ENTITY: 'Action' = __wrap(__Action.ENTITY)

    # public static final dev.ultreon.quantum.text.HoverEvent$Action dev.ultreon.quantum.text.HoverEvent$Action.PLAYER
    PLAYER: 'Action' = __wrap(__Action.PLAYER)

    # public static final dev.ultreon.quantum.text.HoverEvent$Action dev.ultreon.quantum.text.HoverEvent$Action.TEXT
    TEXT: 'Action' = __wrap(__Action.TEXT)

    # public static final dev.ultreon.quantum.text.HoverEvent$Action dev.ultreon.quantum.text.HoverEvent$Action.ITEM
    ITEM: 'Action' = __wrap(__Action.ITEM)

    # public static final dev.ultreon.quantum.text.HoverEvent$Action dev.ultreon.quantum.text.HoverEvent$Action.LOCATION
    LOCATION: 'Action' = __wrap(__Action.LOCATION)


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
    def valueOf(arg0: str) -> 'Action':
        """public static dev.ultreon.quantum.text.HoverEvent$Action dev.ultreon.quantum.text.HoverEvent$Action.valueOf(java.lang.String)"""
        return Action.__wrap(__Action.valueOf(arg0))

    @staticmethod
    @overload
    def values() -> List['Action']:
        """public static dev.ultreon.quantum.text.HoverEvent$Action[] dev.ultreon.quantum.text.HoverEvent$Action.values()"""
        return List[Action].__wrap(__Action.values())

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
 
 
# CLASS: dev.ultreon.quantum.text.ClickEvent
from builtins import str
from pyquantum_helper import override
import java.net.URI as URI
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.text.ClickEvent as __ClickEvent
__ClickEvent = __ClickEvent
import dev.ultreon.quantum.text.ClickEvent as __ClickEvent_Action
__Action = __ClickEvent_Action.Action
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
 
class ClickEvent(__Serializable, Serializable):
    """dev.ultreon.quantum.text.ClickEvent"""
 
    @staticmethod
    def __wrap(java_value: __ClickEvent) -> 'ClickEvent':
        return ClickEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClickEvent):
        """
        Dynamic initializer for ClickEvent.
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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.text.ClickEvent.equals(java.lang.Object)"""
        return bool.__wrap(super(__ClickEvent, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.text.ClickEvent.hashCode()"""
        return int.__wrap(super(ClickEvent, self).hashCode())

    @staticmethod
    @overload
    def suggestMessage(arg0: str) -> 'ClickEvent':
        """public static dev.ultreon.quantum.text.ClickEvent dev.ultreon.quantum.text.ClickEvent.suggestMessage(java.lang.String)"""
        return ClickEvent.__wrap(__ClickEvent.suggestMessage(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def copyToClipboard(arg0: str) -> 'ClickEvent':
        """public static dev.ultreon.quantum.text.ClickEvent dev.ultreon.quantum.text.ClickEvent.copyToClipboard(java.lang.String)"""
        return ClickEvent.__wrap(__ClickEvent.copyToClipboard(arg0))

    @staticmethod
    @overload
    def openUri(arg0: 'URI') -> 'ClickEvent':
        """public static dev.ultreon.quantum.text.ClickEvent dev.ultreon.quantum.text.ClickEvent.openUri(java.net.URI)"""
        return ClickEvent.__wrap(__ClickEvent.openUri(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def value(self) -> str:
        """public java.lang.String dev.ultreon.quantum.text.ClickEvent.value()"""
        return str.__wrap(super(ClickEvent, self).value())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.text.ClickEvent.toString()"""
        return str.__wrap(super(ClickEvent, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def runCommand(arg0: str) -> 'ClickEvent':
        """public static dev.ultreon.quantum.text.ClickEvent dev.ultreon.quantum.text.ClickEvent.runCommand(java.lang.String)"""
        return ClickEvent.__wrap(__ClickEvent.runCommand(arg0))

    @overload
    def __init__(self, arg0: 'Action', arg1: str):
        """public dev.ultreon.quantum.text.ClickEvent(dev.ultreon.quantum.text.ClickEvent$Action,java.lang.String)"""
        val = __ClickEvent(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def action(self) -> 'Action':
        """public dev.ultreon.quantum.text.ClickEvent$Action dev.ultreon.quantum.text.ClickEvent.action()"""
        return 'Action'.__wrap(super(ClickEvent, self).action()) 
 
 
# CLASS: dev.ultreon.quantum.text.FormattedText
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Iterable as Iterable
import dev.ultreon.quantum.text.FormattedText as __FormattedText
__FormattedText = __FormattedText
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.text.FormattedText as __FormattedText_TextFormatElement
__TextFormatElement = __FormattedText_TextFormatElement.TextFormatElement
from builtins import bool
from builtins import int
import java.util.List as List
import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class FormattedText():
    """dev.ultreon.quantum.text.FormattedText"""
 
    @staticmethod
    def __wrap(java_value: __FormattedText) -> 'FormattedText':
        return FormattedText(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FormattedText):
        """
        Dynamic initializer for FormattedText.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getElementsFrom(self, arg0: int) -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.text.FormattedText$TextFormatElement> dev.ultreon.quantum.text.FormattedText.getElementsFrom(int)"""
        return 'Iterable'.__wrap(super(__FormattedText, self).getElementsFrom(__int.valueOf(arg0)))

    @overload
    def indexOf(self, arg0: str, arg1: int) -> int:
        """public int dev.ultreon.quantum.text.FormattedText.indexOf(java.lang.String,int)"""
        return int.__wrap(super(__FormattedText, self).indexOf(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def from(arg0: str) -> 'FormattedText':
        """public static dev.ultreon.quantum.text.FormattedText dev.ultreon.quantum.text.FormattedText.from(java.lang.String)"""
        return FormattedText.__wrap(__FormattedText.from(arg0))

    @overload
    def getElementsWithin(self, arg0: int, arg1: int) -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.text.FormattedText$TextFormatElement> dev.ultreon.quantum.text.FormattedText.getElementsWithin(int,int)"""
        return 'Iterable'.__wrap(super(__FormattedText, self).getElementsWithin(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def lastIndexOf(self, arg0: str, arg1: int) -> int:
        """public int dev.ultreon.quantum.text.FormattedText.lastIndexOf(java.lang.String,int)"""
        return int.__wrap(super(__FormattedText, self).lastIndexOf(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def from(arg0: 'MutableText') -> 'FormattedText':
        """public static dev.ultreon.quantum.text.FormattedText dev.ultreon.quantum.text.FormattedText.from(dev.ultreon.quantum.text.MutableText)"""
        return FormattedText.__wrap(__FormattedText.from(arg0))

    @overload
    def getText(self) -> str:
        """public java.lang.String dev.ultreon.quantum.text.FormattedText.getText()"""
        return str.__wrap(super(FormattedText, self).getText())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.text.FormattedText.toString()"""
        return str.__wrap(super(FormattedText, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def length(self) -> int:
        """public int dev.ultreon.quantum.text.FormattedText.length()"""
        return int.__wrap(super(FormattedText, self).length())

    @overload
    def getNextElement(self, arg0: int) -> 'TextFormatElement':
        """public dev.ultreon.quantum.text.FormattedText$TextFormatElement dev.ultreon.quantum.text.FormattedText.getNextElement(int)"""
        return 'TextFormatElement'.__wrap(super(__FormattedText, self).getNextElement(__int.valueOf(arg0)))

    @overload
    def indexOf(self, arg0: str) -> int:
        """public int dev.ultreon.quantum.text.FormattedText.indexOf(java.lang.String)"""
        return int.__wrap(super(__FormattedText, self).indexOf(arg0))

    @overload
    def copy(self) -> 'FormattedText':
        """public dev.ultreon.quantum.text.FormattedText dev.ultreon.quantum.text.FormattedText.copy()"""
        return 'FormattedText'.__wrap(super(FormattedText, self).copy())

    @overload
    def getPreviousElement(self, arg0: int) -> 'TextFormatElement':
        """public dev.ultreon.quantum.text.FormattedText$TextFormatElement dev.ultreon.quantum.text.FormattedText.getPreviousElement(int)"""
        return 'TextFormatElement'.__wrap(super(__FormattedText, self).getPreviousElement(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'List'):
        """public dev.ultreon.quantum.text.FormattedText(java.util.List<dev.ultreon.quantum.text.FormattedText$TextFormatElement>)"""
        val = __FormattedText(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def indexOf(self, arg0: str, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.text.FormattedText.indexOf(java.lang.String,int,int)"""
        return int.__wrap(super(__FormattedText, self).indexOf(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getElements(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.FormattedText$TextFormatElement> dev.ultreon.quantum.text.FormattedText.getElements()"""
        return 'List'.__wrap(super(FormattedText, self).getElements())

    @overload
    def getElementsFromTo(self, arg0: int, arg1: int) -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.text.FormattedText$TextFormatElement> dev.ultreon.quantum.text.FormattedText.getElementsFromTo(int,int)"""
        return 'Iterable'.__wrap(super(__FormattedText, self).getElementsFromTo(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def indexOf(self, arg0: 'TextFormatElement') -> int:
        """public int dev.ultreon.quantum.text.FormattedText.indexOf(dev.ultreon.quantum.text.FormattedText$TextFormatElement)"""
        return int.__wrap(super(__FormattedText, self).indexOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def from(arg0: 'TextObject') -> 'FormattedText':
        """public static dev.ultreon.quantum.text.FormattedText dev.ultreon.quantum.text.FormattedText.from(dev.ultreon.quantum.text.TextObject)"""
        return FormattedText.__wrap(__FormattedText.from(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def lastIndexOf(self, arg0: str) -> int:
        """public int dev.ultreon.quantum.text.FormattedText.lastIndexOf(java.lang.String)"""
        return int.__wrap(super(__FormattedText, self).lastIndexOf(arg0))

    @overload
    def lastIndexOf(self, arg0: str, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.text.FormattedText.lastIndexOf(java.lang.String,int,int)"""
        return int.__wrap(super(__FormattedText, self).lastIndexOf(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.text.IconMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.text.IconMap as __IconMap
__IconMap = __IconMap
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.quantum.text.FontTexture as __FontTexture
__FontTexture = __FontTexture
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class IconMap():
    """dev.ultreon.quantum.text.IconMap"""
 
    @staticmethod
    def __wrap(java_value: __IconMap) -> 'IconMap':
        return IconMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IconMap):
        """
        Dynamic initializer for IconMap.
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
    def set(arg0: str, arg1: 'FontTexture'):
        """public static void dev.ultreon.quantum.text.IconMap.set(java.lang.String,dev.ultreon.quantum.text.FontTexture)"""
        __IconMap.set(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.text.IconMap()"""
        val = __IconMap()
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
    def get(arg0: str) -> 'FontTexture':
        """public static dev.ultreon.quantum.text.FontTexture dev.ultreon.quantum.text.IconMap.get(java.lang.String)"""
        return FontTexture.__wrap(__IconMap.get(arg0))

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
        def register():
            """public static void dev.ultreon.quantum.text.IconMap.register()"""
            __IconMap.register()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.text.IconMap()"""
        val = __IconMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.text.ServerLanguage
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.util.Locale as Locale
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import dev.ultreon.quantum.text.ServerLanguage as __ServerLanguage
__ServerLanguage = __ServerLanguage
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Locale as __Locale
__Locale = __Locale
from builtins import bool
import java.util.Map as Map
from builtins import int
 
class ServerLanguage():
    """dev.ultreon.quantum.text.ServerLanguage"""
 
    @staticmethod
    def __wrap(java_value: __ServerLanguage) -> 'ServerLanguage':
        return ServerLanguage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ServerLanguage):
        """
        Dynamic initializer for ServerLanguage.
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
    def get(self, arg0: str, *arg1: object) -> str:
        """public java.lang.String dev.ultreon.quantum.text.ServerLanguage.get(java.lang.String,java.lang.Object...)"""
        return str.__wrap(super(__ServerLanguage, self).get(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Locale', arg1: 'Map', arg2: 'Identifier'):
        """public dev.ultreon.quantum.text.ServerLanguage(java.util.Locale,java.util.Map<java.lang.String, java.lang.String>,dev.ultreon.quantum.util.Identifier)"""
        val = __ServerLanguage(arg0, arg1, arg2)
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

    @overload
    def getLocale(self) -> 'Locale':
        """public java.util.Locale dev.ultreon.quantum.text.ServerLanguage.getLocale()"""
        return 'Locale'.__wrap(super(ServerLanguage, self).getLocale())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.text.ServerLanguage.getId()"""
        return 'util.Identifier'.__wrap(super(ServerLanguage, self).getId())

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
 
 
# CLASS: dev.ultreon.quantum.text.HoverEvent
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
import dev.ultreon.quantum.text.HoverEvent as __HoverEvent_Action
__Action = __HoverEvent_Action.Action
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = __import_once__("pyquantum.entity.player")

import java.lang.Object as __object
try:
    from pyquantum import entity
except ImportError:
    entity = __import_once__("pyquantum.entity")

from builtins import type
import dev.ultreon.quantum.text.HoverEvent as __HoverEvent
__HoverEvent = __HoverEvent
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

from builtins import object
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
 
class HoverEvent(__Serializable, Serializable):
    """dev.ultreon.quantum.text.HoverEvent"""
 
    @staticmethod
    def __wrap(java_value: __HoverEvent) -> 'HoverEvent':
        return HoverEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HoverEvent):
        """
        Dynamic initializer for HoverEvent.
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
        """public java.lang.String dev.ultreon.quantum.text.HoverEvent.toString()"""
        return str.__wrap(super(HoverEvent, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Action', arg1: object):
        """public dev.ultreon.quantum.text.HoverEvent(dev.ultreon.quantum.text.HoverEvent$Action,T)"""
        val = __HoverEvent(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def location(arg0: 'Player') -> 'HoverEvent':
        """public static dev.ultreon.quantum.text.HoverEvent<dev.ultreon.quantum.entity.player.Player> dev.ultreon.quantum.text.HoverEvent.location(dev.ultreon.quantum.entity.player.Player)"""
        return HoverEvent.__wrap(__HoverEvent.location(arg0))

    @staticmethod
    @overload
    def location(arg0: 'Location') -> 'HoverEvent':
        """public static dev.ultreon.quantum.text.HoverEvent<dev.ultreon.quantum.world.Location> dev.ultreon.quantum.text.HoverEvent.location(dev.ultreon.quantum.world.Location)"""
        return HoverEvent.__wrap(__HoverEvent.location(arg0))

    @overload
    def action(self) -> 'Action':
        """public dev.ultreon.quantum.text.HoverEvent$Action dev.ultreon.quantum.text.HoverEvent.action()"""
        return 'Action'.__wrap(super(HoverEvent, self).action())

    @overload
    def value(self) -> object:
        """public T dev.ultreon.quantum.text.HoverEvent.value()"""
        return object.__wrap(super(HoverEvent, self).value())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def item(arg0: 'ItemStack') -> 'HoverEvent':
        """public static dev.ultreon.quantum.text.HoverEvent<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.text.HoverEvent.item(dev.ultreon.quantum.item.ItemStack)"""
        return HoverEvent.__wrap(__HoverEvent.item(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.text.HoverEvent.equals(java.lang.Object)"""
        return bool.__wrap(super(__HoverEvent, self).equals(arg0))

    @staticmethod
    @overload
    def location(arg0: 'Entity') -> 'HoverEvent':
        """public static dev.ultreon.quantum.text.HoverEvent<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.text.HoverEvent.location(dev.ultreon.quantum.entity.Entity)"""
        return HoverEvent.__wrap(__HoverEvent.location(arg0))

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
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.text.HoverEvent.hashCode()"""
        return int.__wrap(super(HoverEvent, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def text(arg0: str) -> 'HoverEvent':
        """public static dev.ultreon.quantum.text.HoverEvent<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.text.HoverEvent.text(java.lang.String)"""
        return HoverEvent.__wrap(__HoverEvent.text(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def text(arg0: 'TextObject') -> 'HoverEvent':
        """public static dev.ultreon.quantum.text.HoverEvent<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.text.HoverEvent.text(dev.ultreon.quantum.text.TextObject)"""
        return HoverEvent.__wrap(__HoverEvent.text(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.text.TextElement
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.text.TextElement as __TextElement
__TextElement = __TextElement
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import dev.ultreon.quantum.text.TextStyle as __TextStyle
__TextStyle = __TextStyle
from builtins import int
 
class TextElement():
    """dev.ultreon.quantum.text.TextElement"""
 
    @staticmethod
    def __wrap(java_value: __TextElement) -> 'TextElement':
        return TextElement(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextElement):
        """
        Dynamic initializer for TextElement.
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

    @overload
    def text(self) -> 'TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextElement.text()"""
        return 'TextObject'.__wrap(super(TextElement, self).text())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def style(self) -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextElement.style()"""
        return 'TextStyle'.__wrap(super(TextElement, self).style())

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
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.text.TextElement.hashCode()"""
        return int.__wrap(super(TextElement, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.text.TextElement.equals(java.lang.Object)"""
        return bool.__wrap(super(__TextElement, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.text.TextElement.toString()"""
        return str.__wrap(super(TextElement, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'TextObject', arg1: 'TextStyle'):
        """public dev.ultreon.quantum.text.TextElement(dev.ultreon.quantum.text.TextObject,dev.ultreon.quantum.text.TextStyle)"""
        val = __TextElement(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.text.Translatable
import dev.ultreon.quantum.text.MutableText as __MutableText
__MutableText = __MutableText
from builtins import str
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.text.Translatable as __Translatable
__Translatable = __Translatable
from abc import abstractmethod, ABC
 
class Translatable(ABC):
    """dev.ultreon.quantum.text.Translatable"""
 
    @staticmethod
    def __wrap(java_value: __Translatable) -> 'Translatable':
        return Translatable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Translatable):
        """
        Dynamic initializer for Translatable.
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
    def getTranslation(self) -> 'MutableText':
        """public default dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.Translatable.getTranslation()"""
        return 'MutableText'.__wrap(super(Translatable, self).getTranslation())

    @overload
    def getTranslationText(self) -> str:
        """public default java.lang.String dev.ultreon.quantum.text.Translatable.getTranslationText()"""
        return str.__wrap(super(Translatable, self).getTranslationText())

    @abstractmethod
    def getTranslationId(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.text.Translatable.getTranslationId()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.text.ClickEvent$Action
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import dev.ultreon.quantum.text.ClickEvent as __ClickEvent_Action
__Action = __ClickEvent_Action.Action
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
 
class Action(__Enum, Enum):
    """dev.ultreon.quantum.text.ClickEvent.Action"""
 
    @staticmethod
    def __wrap(java_value: __Action) -> 'Action':
        return Action(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Action):
        """
        Dynamic initializer for Action.
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
 
    # public static final dev.ultreon.quantum.text.ClickEvent$Action dev.ultreon.quantum.text.ClickEvent$Action.RUN_COMMAND
    RUN_COMMAND: 'Action' = __wrap(__Action.RUN_COMMAND)

    # public static final dev.ultreon.quantum.text.ClickEvent$Action dev.ultreon.quantum.text.ClickEvent$Action.COPY_TO_CLIPBOARD
    COPY_TO_CLIPBOARD: 'Action' = __wrap(__Action.COPY_TO_CLIPBOARD)

    # public static final dev.ultreon.quantum.text.ClickEvent$Action dev.ultreon.quantum.text.ClickEvent$Action.SUGGEST_MESSAGE
    SUGGEST_MESSAGE: 'Action' = __wrap(__Action.SUGGEST_MESSAGE)

    # public static final dev.ultreon.quantum.text.ClickEvent$Action dev.ultreon.quantum.text.ClickEvent$Action.OPEN_URL
    OPEN_URL: 'Action' = __wrap(__Action.OPEN_URL)


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
    def values() -> List['Action']:
        """public static dev.ultreon.quantum.text.ClickEvent$Action[] dev.ultreon.quantum.text.ClickEvent$Action.values()"""
        return List[Action].__wrap(__Action.values())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Action':
        """public static dev.ultreon.quantum.text.ClickEvent$Action dev.ultreon.quantum.text.ClickEvent$Action.valueOf(java.lang.String)"""
        return Action.__wrap(__Action.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.text.FormattedText$TextFormatElement
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.text.FormattedText as __FormattedText_TextFormatElement
__TextFormatElement = __FormattedText_TextFormatElement.TextFormatElement
from builtins import bool
import dev.ultreon.quantum.text.TextStyle as __TextStyle
__TextStyle = __TextStyle
from builtins import int
 
class TextFormatElement():
    """dev.ultreon.quantum.text.FormattedText.TextFormatElement"""
 
    @staticmethod
    def __wrap(java_value: __TextFormatElement) -> 'TextFormatElement':
        return TextFormatElement(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextFormatElement):
        """
        Dynamic initializer for TextFormatElement.
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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.text.FormattedText$TextFormatElement.equals(java.lang.Object)"""
        return bool.__wrap(super(__TextFormatElement, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def indexOf(self, arg0: str) -> int:
        """public int dev.ultreon.quantum.text.FormattedText$TextFormatElement.indexOf(java.lang.String)"""
        return int.__wrap(super(__TextFormatElement, self).indexOf(arg0))

    @overload
    def style(self) -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.FormattedText$TextFormatElement.style()"""
        return 'TextStyle'.__wrap(super(TextFormatElement, self).style())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.text.FormattedText$TextFormatElement.toString()"""
        return str.__wrap(super(TextFormatElement, self).toString())

    @overload
    def length(self) -> int:
        """public int dev.ultreon.quantum.text.FormattedText$TextFormatElement.length()"""
        return int.__wrap(super(TextFormatElement, self).length())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def text(self) -> str:
        """public java.lang.String dev.ultreon.quantum.text.FormattedText$TextFormatElement.text()"""
        return str.__wrap(super(TextFormatElement, self).text())

    @overload
    def __init__(self, arg0: 'TextStyle', arg1: str, arg2: int):
        """public dev.ultreon.quantum.text.FormattedText$TextFormatElement(dev.ultreon.quantum.text.TextStyle,java.lang.String,int)"""
        val = __TextFormatElement(arg0, arg1, __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def index(self) -> int:
        """public int dev.ultreon.quantum.text.FormattedText$TextFormatElement.index()"""
        return int.__wrap(super(TextFormatElement, self).index())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.text.FormattedText$TextFormatElement.hashCode()"""
        return int.__wrap(super(TextFormatElement, self).hashCode())

    @overload
    def split(self, arg0: int) -> List['TextFormatElement']:
        """public dev.ultreon.quantum.text.FormattedText$TextFormatElement[] dev.ultreon.quantum.text.FormattedText$TextFormatElement.split(int)"""
        return List['TextFormatElement'].__wrap(super(__TextFormatElement, self).split(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def copy(self) -> 'TextFormatElement':
        """public dev.ultreon.quantum.text.FormattedText$TextFormatElement dev.ultreon.quantum.text.FormattedText$TextFormatElement.copy()"""
        return 'TextFormatElement'.__wrap(super(TextFormatElement, self).copy()) 
 
 
# CLASS: dev.ultreon.quantum.text.ParseResult
import dev.ultreon.quantum.text.MutableText as __MutableText
__MutableText = __MutableText
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.text.ParseResult as __ParseResult
__ParseResult = __ParseResult
from typing import List
import java.lang.Exception as Exception
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
import java.util.List as List
 
class ParseResult():
    """dev.ultreon.quantum.text.ParseResult"""
 
    @staticmethod
    def __wrap(java_value: __ParseResult) -> 'ParseResult':
        return ParseResult(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParseResult):
        """
        Dynamic initializer for ParseResult.
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
    def error(arg0: 'Exception') -> 'ParseResult':
        """public static dev.ultreon.quantum.text.ParseResult dev.ultreon.quantum.text.ParseResult.error(java.lang.Exception)"""
        return ParseResult.__wrap(__ParseResult.error(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getTextResult(self) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.ParseResult.getTextResult()"""
        return 'MutableText'.__wrap(super(ParseResult, self).getTextResult())

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

    @overload
    def getResult(self) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.ParseResult.getResult()"""
        return 'MutableText'.__wrap(super(ParseResult, self).getResult())

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
    def getMutableTexts(self) -> List['TextObject']:
        """public dev.ultreon.quantum.text.TextObject[] dev.ultreon.quantum.text.ParseResult.getMutableTexts()"""
        return List['TextObject'].__wrap(super(ParseResult, self).getMutableTexts())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'List', arg1: 'TextObject', arg2: 'TextObject', arg3: 'MutableText'):
        """public dev.ultreon.quantum.text.ParseResult(java.util.List<dev.ultreon.quantum.entity.player.Player>,dev.ultreon.quantum.text.TextObject,dev.ultreon.quantum.text.TextObject,dev.ultreon.quantum.text.MutableText)"""
        val = __ParseResult(arg0, arg1, arg2, arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.text.MutableText
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
from builtins import type
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.quantum.text.LiteralText as __LiteralText
__LiteralText = __LiteralText
import dev.ultreon.quantum.text.TextObject as __TextObject
__TextObject = __TextObject
from builtins import bool
import dev.ultreon.quantum.text.MutableText as __MutableText
__MutableText = __MutableText
from builtins import str
import dev.ultreon.quantum.util.RgbColor as __RgbColor
__RgbColor = __RgbColor
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Iterator as __Iterator
__Iterator = __Iterator
from builtins import object
import java.util.Iterator as Iterator
import java.util.Spliterator as __Spliterator
__Spliterator = __Spliterator
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.text.TranslationText as __TranslationText
__TranslationText = __TranslationText
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.quantum.text.TextStyle as __TextStyle
__TextStyle = __TextStyle
from builtins import int
try:
    from pyubo import types
except ImportError:
    types = __import_once__("pyubo.types")

import java.lang.Iterable as __Iterable
__Iterable = __Iterable
 
class MutableText(ABC, __TextObject, TextObject):
    """dev.ultreon.quantum.text.MutableText"""
 
    @staticmethod
    def __wrap(java_value: __MutableText) -> 'MutableText':
        return MutableText(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MutableText):
        """
        Dynamic initializer for MutableText.
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

    @abstractmethod
    def copy(self, ):
        """public abstract dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.copy()"""
        pass

    @overload
    def setColor(self, arg0: 'RgbColor') -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setColor(dev.ultreon.quantum.util.RgbColor)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setColor(arg0))

    @overload
    def style(self, arg0: 'Consumer') -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.style(java.util.function.Consumer<dev.ultreon.quantum.text.TextStyle>)"""
        return 'MutableText'.__wrap(super(__MutableText, self).style(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def translation(arg0: str, *arg1: object) -> 'TranslationText':
        """public static dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.text.TextObject.translation(java.lang.String,java.lang.Object...)"""
        return TranslationText.__wrap(__TextObject.translation(arg0, arg1))

    @overload
    def getSize(self) -> int:
        """public int dev.ultreon.quantum.text.MutableText.getSize()"""
        return int.__wrap(super(MutableText, self).getSize())

    @overload
    def setSize(self, arg0: int):
        """public void dev.ultreon.quantum.text.MutableText.setSize(int)"""
        super(__MutableText, self).setSize(__int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'TextObject') -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.nullToEmpty(dev.ultreon.quantum.text.TextObject)"""
        return TextObject.__wrap(__TextObject.nullToEmpty(arg0))

    @overload
    def isItalic(self) -> bool:
        """public boolean dev.ultreon.quantum.text.MutableText.isItalic()"""
        return bool.__wrap(super(MutableText, self).isItalic())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(__Iterable, self).forEach(arg0)

    @overload
    def setBold(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setBold(boolean)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setBold(__boolean.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def isStrikethrough(self) -> bool:
        """public boolean dev.ultreon.quantum.text.MutableText.isStrikethrough()"""
        return bool.__wrap(super(MutableText, self).isStrikethrough())

    @overload
    def getColor(self) -> 'util.RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.text.MutableText.getColor()"""
        return 'util.RgbColor'.__wrap(super(MutableText, self).getColor())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.text.TextObject.iterator()"""
        return 'Iterator'.__wrap(super(TextObject, self).iterator())

    @overload
    def setStrikethrough(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setStrikethrough(boolean)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setStrikethrough(__boolean.valueOf(arg0)))

    @abstractmethod
    def createString(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.text.TextObject.createString()"""
        pass

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
    def getStyle(self) -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextObject.getStyle()"""
        return 'TextStyle'.__wrap(super(TextObject, self).getStyle())

    @overload
    def setItalic(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setItalic(boolean)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setItalic(__boolean.valueOf(arg0)))

    @staticmethod
    @overload
    def deserialize(arg0: 'MapType') -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.deserialize(dev.ultreon.ubo.types.MapType)"""
        return TextObject.__wrap(__TextObject.deserialize(arg0))

    @overload
    def isBold(self) -> bool:
        """public boolean dev.ultreon.quantum.text.MutableText.isBold()"""
        return bool.__wrap(super(MutableText, self).isBold())

    @abstractmethod
    def serialize(self, ):
        """public abstract dev.ultreon.ubo.types.MapType dev.ultreon.quantum.text.TextObject.serialize()"""
        pass

    @overload
    def append(self, arg0: object) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.append(java.lang.Object)"""
        return 'MutableText'.__wrap(super(__MutableText, self).append(arg0))

    @override
    @overload
    def getText(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.text.MutableText.getText()"""
        return str.__wrap(super(MutableText, self).getText())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'.__wrap(super(Iterable, self).spliterator())

    @overload
    def isUnderlined(self) -> bool:
        """public boolean dev.ultreon.quantum.text.MutableText.isUnderlined()"""
        return bool.__wrap(super(MutableText, self).isUnderlined())

    @overload
    def setUnderlined(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setUnderlined(boolean)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setUnderlined(__boolean.valueOf(arg0)))

    @staticmethod
    @overload
    def empty() -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.empty()"""
        return TextObject.__wrap(__TextObject.empty())

    @staticmethod
    @overload
    def literal(arg0: str) -> 'LiteralText':
        """public static dev.ultreon.quantum.text.LiteralText dev.ultreon.quantum.text.TextObject.literal(java.lang.String)"""
        return LiteralText.__wrap(__TextObject.literal(arg0))

    @staticmethod
    @overload
    def nullToEmpty(arg0: str) -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.nullToEmpty(java.lang.String)"""
        return TextObject.__wrap(__TextObject.nullToEmpty(arg0))

    @overload
    def append(self, arg0: 'TextObject') -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.append(dev.ultreon.quantum.text.TextObject)"""
        return 'MutableText'.__wrap(super(__MutableText, self).append(arg0))

    @overload
    def append(self, arg0: str) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.append(java.lang.String)"""
        return 'MutableText'.__wrap(super(__MutableText, self).append(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.text.LanguageBootstrap
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

from builtins import str
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.text.LanguageBootstrap as __LanguageBootstrap
__LanguageBootstrap = __LanguageBootstrap
from builtins import object
from abc import abstractmethod, ABC
 
class LanguageBootstrap(ABC):
    """dev.ultreon.quantum.text.LanguageBootstrap"""
 
    @staticmethod
    def __wrap(java_value: __LanguageBootstrap) -> 'LanguageBootstrap':
        return LanguageBootstrap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LanguageBootstrap):
        """
        Dynamic initializer for LanguageBootstrap.
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
 
    # public static final dev.ultreon.quantum.util.LazyValue<dev.ultreon.quantum.text.LanguageBootstrap> dev.ultreon.quantum.text.LanguageBootstrap.bootstrap
    bootstrap: 'util.LazyValue' = __wrap(__util.LazyValue.bootstrap)


    @abstractmethod
    def handleTranslation(self, arg0: str, *arg1: object):
        """public abstract java.lang.String dev.ultreon.quantum.text.LanguageBootstrap.handleTranslation(java.lang.String,java.lang.Object...)"""
        pass

    @staticmethod
    @overload
    def translate(arg0: str, *arg1: object) -> str:
        """public static java.lang.String dev.ultreon.quantum.text.LanguageBootstrap.translate(java.lang.String,java.lang.Object...)"""
        return str.__wrap(__LanguageBootstrap.translate(arg0, arg1)) 
 
 
# CLASS: dev.ultreon.quantum.text.EmoteMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.quantum.text.FontTexture as __FontTexture
__FontTexture = __FontTexture
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.text.EmoteMap as __EmoteMap
__EmoteMap = __EmoteMap
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EmoteMap():
    """dev.ultreon.quantum.text.EmoteMap"""
 
    @staticmethod
    def __wrap(java_value: __EmoteMap) -> 'EmoteMap':
        return EmoteMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EmoteMap):
        """
        Dynamic initializer for EmoteMap.
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
    def get(arg0: str) -> 'FontTexture':
        """public static dev.ultreon.quantum.text.FontTexture dev.ultreon.quantum.text.EmoteMap.get(java.lang.String)"""
        return FontTexture.__wrap(__EmoteMap.get(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def set(arg0: str, arg1: 'FontTexture'):
        """public static void dev.ultreon.quantum.text.EmoteMap.set(java.lang.String,dev.ultreon.quantum.text.FontTexture)"""
        __EmoteMap.set(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.text.EmoteMap()"""
        val = __EmoteMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
        def register():
            """public static void dev.ultreon.quantum.text.EmoteMap.register()"""
            __EmoteMap.register()

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
    def __init__(self, ):
        """public dev.ultreon.quantum.text.EmoteMap()"""
        val = __EmoteMap()
        self.__dict__ = val.__dict__
        self.__wrapper = val