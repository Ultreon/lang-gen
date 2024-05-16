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
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.text.TextDecoration as _TextDecoration
_TextDecoration = _TextDecoration
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextDecoration():
    """dev.ultreon.quantum.text.TextDecoration"""
 
    @staticmethod
    def _wrap(java_value: _TextDecoration) -> 'TextDecoration':
        return TextDecoration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextDecoration):
        """
        Dynamic initializer for TextDecoration.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextDecoration__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextDecoration__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def values() -> List['TextDecoration']:
        """public static dev.ultreon.quantum.text.TextDecoration[] dev.ultreon.quantum.text.TextDecoration.values()"""
        return List[TextDecoration]._wrap(_TextDecoration.values())

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'TextDecoration':
        """public static dev.ultreon.quantum.text.TextDecoration dev.ultreon.quantum.text.TextDecoration.valueOf(java.lang.String)"""
        return TextDecoration._wrap(_TextDecoration.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


TextDecoration.ITALIC = TextDecoration._wrap(_ITALIC.ITALIC)

TextDecoration.UNDERLINED = TextDecoration._wrap(_UNDERLINED.UNDERLINED)

TextDecoration.STRIKETHROUGH = TextDecoration._wrap(_STRIKETHROUGH.STRIKETHROUGH)

TextDecoration.BOLD = TextDecoration._wrap(_BOLD.BOLD)

 
 
 
# CLASS: dev.ultreon.quantum.text.TextDecoration
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.text.TextDecoration as _TextDecoration
_TextDecoration = _TextDecoration
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextDecoration():
    """dev.ultreon.quantum.text.TextDecoration"""
 
    @staticmethod
    def _wrap(java_value: _TextDecoration) -> 'TextDecoration':
        return TextDecoration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextDecoration):
        """
        Dynamic initializer for TextDecoration.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextDecoration__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextDecoration__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def values() -> List['TextDecoration']:
        """public static dev.ultreon.quantum.text.TextDecoration[] dev.ultreon.quantum.text.TextDecoration.values()"""
        return List[TextDecoration]._wrap(_TextDecoration.values())

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'TextDecoration':
        """public static dev.ultreon.quantum.text.TextDecoration dev.ultreon.quantum.text.TextDecoration.valueOf(java.lang.String)"""
        return TextDecoration._wrap(_TextDecoration.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


TextDecoration.ITALIC = TextDecoration._wrap(_ITALIC.ITALIC)

TextDecoration.UNDERLINED = TextDecoration._wrap(_UNDERLINED.UNDERLINED)

TextDecoration.STRIKETHROUGH = TextDecoration._wrap(_STRIKETHROUGH.STRIKETHROUGH)

TextDecoration.BOLD = TextDecoration._wrap(_BOLD.BOLD)

 
 
 
# CLASS: dev.ultreon.quantum.text.TextDecoration 
 
 
# CLASS: dev.ultreon.quantum.text.ColorCode
from pyquantum_helper import import_once as _import_once
import java.lang.Character as _char
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import dev.ultreon.quantum.text.ColorCode as _ColorCode
_ColorCode = _ColorCode
import java.lang.String as _string
import java.util.Optional as _Optional
_Optional = _Optional
from builtins import bool
from builtins import str
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Enum as _Enum
_Enum = _Enum
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import dev.ultreon.quantum.util.Color as _Color
_Color = _Color
import java.lang.Integer as _int
import java.lang.Integer as Integer
import java.util.Optional as Optional
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ColorCode():
    """dev.ultreon.quantum.text.ColorCode"""
 
    @staticmethod
    def _wrap(java_value: _ColorCode) -> 'ColorCode':
        return ColorCode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ColorCode):
        """
        Dynamic initializer for ColorCode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ColorCode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ColorCode__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getIntCode(self) -> int:
        """public int dev.ultreon.quantum.text.ColorCode.getIntCode()"""
        return int._wrap(super(ColorCode, self).getIntCode())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def getRed(self) -> int:
        """public int dev.ultreon.quantum.text.ColorCode.getRed()"""
        return int._wrap(super(ColorCode, self).getRed())

    @staticmethod
    @overload
    def values() -> List['ColorCode']:
        """public static dev.ultreon.quantum.text.ColorCode[] dev.ultreon.quantum.text.ColorCode.values()"""
        return List[ColorCode]._wrap(_ColorCode.values())

    @overload
    def concat(self, arg0: str) -> str:
        """public java.lang.String dev.ultreon.quantum.text.ColorCode.concat(java.lang.String)"""
        return str._wrap(super(_ColorCode, self).concat(arg0))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @overload
    def asBungee(self) -> 'ColorCode':
        """public dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.asBungee()"""
        return 'ColorCode'._wrap(super(ColorCode, self).asBungee())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toHex(self) -> str:
        """public default java.lang.String dev.ultreon.quantum.util.Color.toHex()"""
        return str._wrap(super(util.Color, self).toHex())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.text.ColorCode.toString()"""
        return str._wrap(super(ColorCode, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def getById(arg0: int) -> 'ColorCode':
        """public static dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.getById(int)"""
        return ColorCode._wrap(_ColorCode.getById(_int.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @overload
    def isFormat(self) -> bool:
        """public boolean dev.ultreon.quantum.text.ColorCode.isFormat()"""
        return bool._wrap(super(ColorCode, self).isFormat())

    @overload
    def getColor(self) -> 'Integer':
        """public java.lang.Integer dev.ultreon.quantum.text.ColorCode.getColor()"""
        return _transform(super(ColorCode, self).getColor()).'Integer'Value()

    @override
    @overload
    def lighter(self) -> 'util.Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.lighter()"""
        return 'util.Color'._wrap(super(util.Color, self).lighter())

    @staticmethod
    @overload
    def stripColor(arg0: str) -> str:
        """public static java.lang.String dev.ultreon.quantum.text.ColorCode.stripColor(java.lang.String)"""
        return str._wrap(_ColorCode.stripColor(arg0))

    @staticmethod
    @overload
    def getLastColors(arg0: str) -> 'ColorCode':
        """public static dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.getLastColors(java.lang.String)"""
        return ColorCode._wrap(_ColorCode.getLastColors(arg0))

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def withBlue(self, arg0: int) -> 'util.Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.withBlue(int)"""
        return 'util.Color'._wrap(super(_util.Color, self).withBlue(_int.valueOf(arg0)))

    @overload
    def withRed(self, arg0: int) -> 'util.Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.withRed(int)"""
        return 'util.Color'._wrap(super(_util.Color, self).withRed(_int.valueOf(arg0)))

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def toGdx(self) -> 'graphics.Color':
        """public default com.badlogic.gdx.graphics.Color dev.ultreon.quantum.util.Color.toGdx()"""
        return 'graphics.Color'._wrap(super(util.Color, self).toGdx())

    @overload
    def withAlpha(self, arg0: int) -> 'util.Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.withAlpha(int)"""
        return 'util.Color'._wrap(super(_util.Color, self).withAlpha(_int.valueOf(arg0)))

    @overload
    def concat(self, arg0: 'ColorCode') -> str:
        """public java.lang.String dev.ultreon.quantum.text.ColorCode.concat(dev.ultreon.quantum.text.ColorCode)"""
        return str._wrap(super(_ColorCode, self).concat(arg0))

    @staticmethod
    @overload
    def getByChar(arg0: str) -> 'ColorCode':
        """public static dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.getByChar(char)"""
        return ColorCode._wrap(_ColorCode.getByChar(_char.valueOf(arg0)))

    @override
    @overload
    def getBlue(self) -> int:
        """public int dev.ultreon.quantum.text.ColorCode.getBlue()"""
        return int._wrap(super(ColorCode, self).getBlue())

    @override
    @overload
    def getAlpha(self) -> int:
        """public int dev.ultreon.quantum.text.ColorCode.getAlpha()"""
        return int._wrap(super(ColorCode, self).getAlpha())

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @overload
    def isColor(self) -> bool:
        """public boolean dev.ultreon.quantum.text.ColorCode.isColor()"""
        return bool._wrap(super(ColorCode, self).isColor())

    @staticmethod
    @overload
    def getByChar(arg0: str) -> 'ColorCode':
        """public static dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.getByChar(java.lang.String)"""
        return ColorCode._wrap(_ColorCode.getByChar(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def withGreen(self, arg0: int) -> 'util.Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.withGreen(int)"""
        return 'util.Color'._wrap(super(_util.Color, self).withGreen(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ColorCode':
        """public static dev.ultreon.quantum.text.ColorCode dev.ultreon.quantum.text.ColorCode.valueOf(java.lang.String)"""
        return ColorCode._wrap(_ColorCode.valueOf(arg0))

    @overload
    def getCode(self) -> str:
        """public char dev.ultreon.quantum.text.ColorCode.getCode()"""
        return str._wrap(super(ColorCode, self).getCode())

    @override
    @overload
    def getGreen(self) -> int:
        """public int dev.ultreon.quantum.text.ColorCode.getGreen()"""
        return int._wrap(super(ColorCode, self).getGreen())

    @override
    @overload
    def darker(self) -> 'util.Color':
        """public default dev.ultreon.quantum.util.Color dev.ultreon.quantum.util.Color.darker()"""
        return 'util.Color'._wrap(super(util.Color, self).darker())


ColorCode.GRAY = ColorCode._wrap(_GRAY.GRAY)

ColorCode.DARK_GREEN = ColorCode._wrap(_DARK_GREEN.DARK_GREEN)

ColorCode.MAGIC = ColorCode._wrap(_MAGIC.MAGIC)

ColorCode.ITALIC = ColorCode._wrap(_ITALIC.ITALIC)

ColorCode.LIME = ColorCode._wrap(_LIME.LIME)

ColorCode.MAGENTA = ColorCode._wrap(_MAGENTA.MAGENTA)

ColorCode.ORANGE = ColorCode._wrap(_ORANGE.ORANGE)

ColorCode.UNDERLINE = ColorCode._wrap(_UNDERLINE.UNDERLINE)

ColorCode.BOLD = ColorCode._wrap(_BOLD.BOLD)

ColorCode.DARK_PURPLE = ColorCode._wrap(_DARK_PURPLE.DARK_PURPLE)

ColorCode.DARK_GRAY = ColorCode._wrap(_DARK_GRAY.DARK_GRAY)

ColorCode.WHITE = ColorCode._wrap(_WHITE.WHITE)

ColorCode.STRIKETHROUGH = ColorCode._wrap(_STRIKETHROUGH.STRIKETHROUGH)

ColorCode.DARK_RED = ColorCode._wrap(_DARK_RED.DARK_RED)

ColorCode.DARK_AQUA = ColorCode._wrap(_DARK_AQUA.DARK_AQUA)

ColorCode.GOLD = ColorCode._wrap(_GOLD.GOLD)

ColorCode.LIGHT_PURPLE = ColorCode._wrap(_LIGHT_PURPLE.LIGHT_PURPLE)

ColorCode.AZURE = ColorCode._wrap(_AZURE.AZURE)

ColorCode.YELLOW = ColorCode._wrap(_YELLOW.YELLOW)

ColorCode.AQUA = ColorCode._wrap(_AQUA.AQUA)

ColorCode.RED = ColorCode._wrap(_RED.RED)

ColorCode.RESET = ColorCode._wrap(_RESET.RESET)

ColorCode.DARK_BLUE = ColorCode._wrap(_DARK_BLUE.DARK_BLUE)

ColorCode.BLACK = ColorCode._wrap(_BLACK.BLACK)

ColorCode.GREEN = ColorCode._wrap(_GREEN.GREEN)

ColorCode.BLUE = ColorCode._wrap(_BLUE.BLUE) 
 
 
# CLASS: dev.ultreon.quantum.text.TextObject
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
import java.lang.String as _string
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.util.Spliterator as Spliterator
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import dev.ultreon.quantum.text.TranslationText as _TranslationText
_TranslationText = _TranslationText
import java.util.Iterator as Iterator
import dev.ultreon.quantum.text.LiteralText as _LiteralText
_LiteralText = _LiteralText
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

import dev.ultreon.quantum.text.TextStyle as _TextStyle
_TextStyle = _TextStyle
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextObject():
    """dev.ultreon.quantum.text.TextObject"""
 
    @staticmethod
    def _wrap(java_value: _TextObject) -> 'TextObject':
        return TextObject(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextObject):
        """
        Dynamic initializer for TextObject.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextObject__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextObject__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def literal(arg0: str) -> 'LiteralText':
        """public static dev.ultreon.quantum.text.LiteralText dev.ultreon.quantum.text.TextObject.literal(java.lang.String)"""
        return LiteralText._wrap(_TextObject.literal(arg0))

    @staticmethod
    @overload
    def empty() -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.empty()"""
        return TextObject._wrap(_TextObject.empty())

    @abstractmethod
    def copy(self, ):
        """public abstract dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.TextObject.copy()"""
        pass

    @overload
    def getText(self) -> str:
        """public java.lang.String dev.ultreon.quantum.text.TextObject.getText()"""
        return str._wrap(super(TextObject, self).getText())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def deserialize(arg0: 'MapType') -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.deserialize(dev.ultreon.ubo.types.MapType)"""
        return TextObject._wrap(_TextObject.deserialize(arg0))

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
    def nullToEmpty(arg0: 'TextObject') -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.nullToEmpty(dev.ultreon.quantum.text.TextObject)"""
        return TextObject._wrap(_TextObject.nullToEmpty(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getStyle(self) -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextObject.getStyle()"""
        return 'TextStyle'._wrap(super(TextObject, self).getStyle())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

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
    def translation(arg0: str, *arg1: object) -> 'TranslationText':
        """public static dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.text.TextObject.translation(java.lang.String,java.lang.Object...)"""
        return TranslationText._wrap(_TextObject.translation(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @abstractmethod
    def serialize(self, ):
        """public abstract dev.ultreon.ubo.types.MapType dev.ultreon.quantum.text.TextObject.serialize()"""
        pass

    @staticmethod
    @overload
    def nullToEmpty(arg0: str) -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.nullToEmpty(java.lang.String)"""
        return TextObject._wrap(_TextObject.nullToEmpty(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.text.TextObject.iterator()"""
        return 'Iterator'._wrap(super(TextObject, self).iterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.text.LiteralText
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import dev.ultreon.quantum.util.RgbColor as _RgbColor
_RgbColor = _RgbColor
import java.util.function.Consumer as Consumer
import java.lang.String as _string
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.util.Spliterator as Spliterator
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.text.MutableText as _MutableText
_MutableText = _MutableText
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import dev.ultreon.quantum.text.TranslationText as _TranslationText
_TranslationText = _TranslationText
import java.util.Iterator as Iterator
import dev.ultreon.quantum.text.LiteralText as _LiteralText
_LiteralText = _LiteralText
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import dev.ultreon.quantum.text.TextStyle as _TextStyle
_TextStyle = _TextStyle
import java.lang.Class as _Class
_Class = _Class
 
class LiteralText():
    """dev.ultreon.quantum.text.LiteralText"""
 
    @staticmethod
    def _wrap(java_value: _LiteralText) -> 'LiteralText':
        return LiteralText(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LiteralText):
        """
        Dynamic initializer for LiteralText.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LiteralText__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LiteralText__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def empty() -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.empty()"""
        return TextObject._wrap(_TextObject.empty())

    @staticmethod
    @overload
    def deserialize(arg0: 'MapType') -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.deserialize(dev.ultreon.ubo.types.MapType)"""
        return TextObject._wrap(_TextObject.deserialize(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setUnderlined(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setUnderlined(boolean)"""
        return 'MutableText'._wrap(super(_MutableText, self).setUnderlined(_boolean.valueOf(arg0)))

    @overload
    def setStrikethrough(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setStrikethrough(boolean)"""
        return 'MutableText'._wrap(super(_MutableText, self).setStrikethrough(_boolean.valueOf(arg0)))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

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
    def createString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.text.LiteralText.createString()"""
        return str._wrap(super(LiteralText, self).createString())

    @overload
    def style(self, arg0: 'Consumer') -> 'LiteralText':
        """public dev.ultreon.quantum.text.LiteralText dev.ultreon.quantum.text.LiteralText.style(java.util.function.Consumer<dev.ultreon.quantum.text.TextStyle>)"""
        return 'LiteralText'._wrap(super(_LiteralText, self).style(arg0))

    @overload
    def append(self, arg0: str) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.append(java.lang.String)"""
        return 'MutableText'._wrap(super(_MutableText, self).append(arg0))

    @override
    @overload
    def isItalic(self) -> bool:
        """public boolean dev.ultreon.quantum.text.MutableText.isItalic()"""
        return bool._wrap(super(MutableText, self).isItalic())

    @staticmethod
    @overload
    def nullToEmpty(arg0: str) -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.nullToEmpty(java.lang.String)"""
        return TextObject._wrap(_TextObject.nullToEmpty(arg0))

    @override
    @overload
    def getSize(self) -> int:
        """public int dev.ultreon.quantum.text.MutableText.getSize()"""
        return int._wrap(super(MutableText, self).getSize())

    @override
    @overload
    def isBold(self) -> bool:
        """public boolean dev.ultreon.quantum.text.MutableText.isBold()"""
        return bool._wrap(super(MutableText, self).isBold())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.text.TextObject.iterator()"""
        return 'Iterator'._wrap(super(TextObject, self).iterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def literal(arg0: str) -> 'LiteralText':
        """public static dev.ultreon.quantum.text.LiteralText dev.ultreon.quantum.text.TextObject.literal(java.lang.String)"""
        return LiteralText._wrap(_TextObject.literal(arg0))

    @override
    @overload
    def getText(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.text.MutableText.getText()"""
        return str._wrap(super(MutableText, self).getText())

    @overload
    def setColor(self, arg0: 'ColorCode') -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.LiteralText.setColor(dev.ultreon.quantum.text.ColorCode)"""
        return 'MutableText'._wrap(super(_LiteralText, self).setColor(arg0))

    @override
    @overload
    def isStrikethrough(self) -> bool:
        """public boolean dev.ultreon.quantum.text.MutableText.isStrikethrough()"""
        return bool._wrap(super(MutableText, self).isStrikethrough())

    @override
    @overload
    def copy(self) -> 'LiteralText':
        """public dev.ultreon.quantum.text.LiteralText dev.ultreon.quantum.text.LiteralText.copy()"""
        return 'LiteralText'._wrap(super(LiteralText, self).copy())

    @override
    @overload
    def setSize(self, arg0: int):
        """public void dev.ultreon.quantum.text.MutableText.setSize(int)"""
        super(_MutableText, self).setSize(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'TextObject') -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.nullToEmpty(dev.ultreon.quantum.text.TextObject)"""
        return TextObject._wrap(_TextObject.nullToEmpty(arg0))

    @overload
    def setItalic(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setItalic(boolean)"""
        return 'MutableText'._wrap(super(_MutableText, self).setItalic(_boolean.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def isUnderlined(self) -> bool:
        """public boolean dev.ultreon.quantum.text.MutableText.isUnderlined()"""
        return bool._wrap(super(MutableText, self).isUnderlined())

    @overload
    def setColor(self, arg0: 'RgbColor') -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setColor(dev.ultreon.quantum.util.RgbColor)"""
        return 'MutableText'._wrap(super(_MutableText, self).setColor(arg0))

    @override
    @overload
    def getColor(self) -> 'util.RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.text.MutableText.getColor()"""
        return 'util.RgbColor'._wrap(super(MutableText, self).getColor())

    @overload
    def append(self, arg0: object) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.append(java.lang.Object)"""
        return 'MutableText'._wrap(super(_MutableText, self).append(arg0))

    @overload
    def setBold(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setBold(boolean)"""
        return 'MutableText'._wrap(super(_MutableText, self).setBold(_boolean.valueOf(arg0)))

    @overload
    def append(self, arg0: 'TextObject') -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.append(dev.ultreon.quantum.text.TextObject)"""
        return 'MutableText'._wrap(super(_MutableText, self).append(arg0))

    @staticmethod
    @overload
    def translation(arg0: str, *arg1: object) -> 'TranslationText':
        """public static dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.text.TextObject.translation(java.lang.String,java.lang.Object...)"""
        return TranslationText._wrap(_TextObject.translation(arg0, arg1))

    @staticmethod
    @overload
    def deserialize(arg0: 'MapType') -> 'LiteralText':
        """public static dev.ultreon.quantum.text.LiteralText dev.ultreon.quantum.text.LiteralText.deserialize(dev.ultreon.ubo.types.MapType)"""
        return LiteralText._wrap(_LiteralText.deserialize(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def serialize(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.text.LiteralText.serialize()"""
        return 'types.MapType'._wrap(super(LiteralText, self).serialize())

    @override
    @overload
    def getStyle(self) -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextObject.getStyle()"""
        return 'TextStyle'._wrap(super(TextObject, self).getStyle())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.text.Formatter
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.text.Formatter as _Formatter
_Formatter = _Formatter
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.String as _string
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.text.ParseResult as _ParseResult
_ParseResult = _ParseResult
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Formatter():
    """dev.ultreon.quantum.text.Formatter"""
 
    @staticmethod
    def _wrap(java_value: _Formatter) -> 'Formatter':
        return Formatter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Formatter):
        """
        Dynamic initializer for Formatter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Formatter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Formatter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def parseColor(self):
        """public void dev.ultreon.quantum.text.Formatter.parseColor()"""
        super(Formatter, self).parseColor()

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

    @staticmethod
    @overload
    def format(arg0: str, arg1: bool) -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.Formatter.format(java.lang.String,boolean)"""
        return TextObject._wrap(_Formatter.format(arg0, _boolean.valueOf(arg1)))

    @overload
    def parseId(self):
        """public void dev.ultreon.quantum.text.Formatter.parseId()"""
        super(Formatter, self).parseId()

    @overload
    def getCurrentFont(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.text.Formatter.getCurrentFont()"""
        return 'util.Identifier'._wrap(super(Formatter, self).getCurrentFont())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def parse(self) -> 'ParseResult':
        """public dev.ultreon.quantum.text.ParseResult dev.ultreon.quantum.text.Formatter.parse()"""
        return 'ParseResult'._wrap(super(Formatter, self).parse())

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
    def __init__(self, arg0: bool, arg1: bool, arg2: str, arg3: 'TextObject', arg4: 'TextObject', arg5: 'Player', arg6: 'RgbColor'):
        """public dev.ultreon.quantum.text.Formatter(boolean,boolean,java.lang.String,dev.ultreon.quantum.text.TextObject,dev.ultreon.quantum.text.TextObject,dev.ultreon.quantum.entity.player.Player,dev.ultreon.quantum.util.RgbColor)"""
        val = _Formatter(_boolean.valueOf(arg0), _boolean.valueOf(arg1), arg2, arg3, arg4, arg5, arg6)
        self.__wrapper = val

    @staticmethod
    @overload
    def format(arg0: str) -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.Formatter.format(java.lang.String)"""
        return TextObject._wrap(_Formatter.format(arg0))

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
    def c(self) -> str:
        """public char dev.ultreon.quantum.text.Formatter.c()"""
        return str._wrap(super(Formatter, self).c())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.text.FormatSequence
import java.util.Spliterator as Spliterator
from pyquantum_helper import override
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import dev.ultreon.quantum.text.FormatSequence as _FormatSequence
_FormatSequence = _FormatSequence
from abc import abstractmethod, ABC
import java.util.function.Consumer as Consumer
 
class FormatSequence():
    """dev.ultreon.quantum.text.FormatSequence"""
 
    @staticmethod
    def _wrap(java_value: _FormatSequence) -> 'FormatSequence':
        return FormatSequence(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FormatSequence):
        """
        Dynamic initializer for FormatSequence.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FormatSequence__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FormatSequence__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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

    @abstractmethod
    def isItalicAt(self, arg0: int):
        """public abstract boolean dev.ultreon.quantum.text.FormatSequence.isItalicAt(int)"""
        pass

    @abstractmethod
    def getTextAt(self, arg0: int):
        """public abstract dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.FormatSequence.getTextAt(int)"""
        pass

    @abstractmethod
    def getClickEventAt(self, arg0: int):
        """public abstract dev.ultreon.quantum.text.ClickEvent dev.ultreon.quantum.text.FormatSequence.getClickEventAt(int)"""
        pass

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @abstractmethod
    def isUnderlinedAt(self, arg0: int):
        """public abstract boolean dev.ultreon.quantum.text.FormatSequence.isUnderlinedAt(int)"""
        pass

    @abstractmethod
    def isStrikethroughAt(self, arg0: int):
        """public abstract boolean dev.ultreon.quantum.text.FormatSequence.isStrikethroughAt(int)"""
        pass

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator()) 
 
 
# CLASS: dev.ultreon.quantum.text.TextStyle
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.util.RgbColor as _RgbColor
_RgbColor = _RgbColor
import dev.ultreon.quantum.text.HoverEvent as _HoverEvent
_HoverEvent = _HoverEvent
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
import dev.ultreon.quantum.text.ClickEvent as _ClickEvent
_ClickEvent = _ClickEvent
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.text.TextStyle as _TextStyle
_TextStyle = _TextStyle
from builtins import int
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

import java.lang.Class as _Class
_Class = _Class
 
class TextStyle():
    """dev.ultreon.quantum.text.TextStyle"""
 
    @staticmethod
    def _wrap(java_value: _TextStyle) -> 'TextStyle':
        return TextStyle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextStyle):
        """
        Dynamic initializer for TextStyle.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextStyle__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextStyle__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def underline(self, arg0: bool) -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextStyle.underline(boolean)"""
        return 'TextStyle'._wrap(super(_TextStyle, self).underline(_boolean.valueOf(arg0)))

    @overload
    def copy(self) -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextStyle.copy()"""
        return 'TextStyle'._wrap(super(TextStyle, self).copy())

    @overload
    def getColor(self) -> 'util.RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.text.TextStyle.getColor()"""
        return 'util.RgbColor'._wrap(super(TextStyle, self).getColor())

    @staticmethod
    @overload
    def defaultStyle() -> 'TextStyle':
        """public static dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextStyle.defaultStyle()"""
        return TextStyle._wrap(_TextStyle.defaultStyle())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isBold(self) -> bool:
        """public boolean dev.ultreon.quantum.text.TextStyle.isBold()"""
        return bool._wrap(super(TextStyle, self).isBold())

    @overload
    def getClickEvent(self) -> 'ClickEvent':
        """public dev.ultreon.quantum.text.ClickEvent dev.ultreon.quantum.text.TextStyle.getClickEvent()"""
        return 'ClickEvent'._wrap(super(TextStyle, self).getClickEvent())

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
    def color(self, arg0: 'RgbColor') -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextStyle.color(dev.ultreon.quantum.util.RgbColor)"""
        return 'TextStyle'._wrap(super(_TextStyle, self).color(arg0))

    @overload
    def color(self, arg0: 'ColorCode'):
        """public void dev.ultreon.quantum.text.TextStyle.color(dev.ultreon.quantum.text.ColorCode)"""
        super(_TextStyle, self).color(arg0)

    @overload
    def hoverEvent(self, arg0: 'HoverEvent') -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextStyle.hoverEvent(dev.ultreon.quantum.text.HoverEvent<?>)"""
        return 'TextStyle'._wrap(super(_TextStyle, self).hoverEvent(arg0))

    @overload
    def getHoverEvent(self) -> 'HoverEvent':
        """public dev.ultreon.quantum.text.HoverEvent<?> dev.ultreon.quantum.text.TextStyle.getHoverEvent()"""
        return 'HoverEvent'._wrap(super(TextStyle, self).getHoverEvent())

    @overload
    def bold(self, arg0: bool) -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextStyle.bold(boolean)"""
        return 'TextStyle'._wrap(super(_TextStyle, self).bold(_boolean.valueOf(arg0)))

    @overload
    def italic(self, arg0: bool) -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextStyle.italic(boolean)"""
        return 'TextStyle'._wrap(super(_TextStyle, self).italic(_boolean.valueOf(arg0)))

    @overload
    def strikethrough(self, arg0: bool) -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextStyle.strikethrough(boolean)"""
        return 'TextStyle'._wrap(super(_TextStyle, self).strikethrough(_boolean.valueOf(arg0)))

    @staticmethod
    @overload
    def deserialize(arg0: 'MapType') -> 'TextStyle':
        """public static dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextStyle.deserialize(dev.ultreon.ubo.types.MapType)"""
        return TextStyle._wrap(_TextStyle.deserialize(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def size(self, arg0: int) -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextStyle.size(int)"""
        return 'TextStyle'._wrap(super(_TextStyle, self).size(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def serialize(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.text.TextStyle.serialize()"""
        return 'types.MapType'._wrap(super(TextStyle, self).serialize())

    @overload
    def isStrikethrough(self) -> bool:
        """public boolean dev.ultreon.quantum.text.TextStyle.isStrikethrough()"""
        return bool._wrap(super(TextStyle, self).isStrikethrough())

    @overload
    def font(self, arg0: 'Identifier') -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextStyle.font(dev.ultreon.quantum.util.Identifier)"""
        return 'TextStyle'._wrap(super(_TextStyle, self).font(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.text.TextStyle()"""
        val = _TextStyle()
        self.__wrapper = val

    @overload
    def getFont(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.text.TextStyle.getFont()"""
        return 'util.Identifier'._wrap(super(TextStyle, self).getFont())

    @overload
    def isItalic(self) -> bool:
        """public boolean dev.ultreon.quantum.text.TextStyle.isItalic()"""
        return bool._wrap(super(TextStyle, self).isItalic())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getSize(self) -> int:
        """public int dev.ultreon.quantum.text.TextStyle.getSize()"""
        return int._wrap(super(TextStyle, self).getSize())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.text.TextStyle()"""
        val = _TextStyle()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isUnderline(self) -> bool:
        """public boolean dev.ultreon.quantum.text.TextStyle.isUnderline()"""
        return bool._wrap(super(TextStyle, self).isUnderline())

    @overload
    def clickEvent(self, arg0: 'ClickEvent') -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextStyle.clickEvent(dev.ultreon.quantum.text.ClickEvent)"""
        return 'TextStyle'._wrap(super(_TextStyle, self).clickEvent(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.text.TextKey
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum.api import commands
except ImportError:
    commands = _import_once("pyquantum.api.commands")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.text.TextKey as _TextKey
_TextKey = _TextKey
 
class TextKey():
    """dev.ultreon.quantum.text.TextKey"""
 
    @staticmethod
    def _wrap(java_value: _TextKey) -> 'TextKey':
        return TextKey(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextKey):
        """
        Dynamic initializer for TextKey.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextKey__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextKey__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def get(self, arg0: 'CommandSender'):
        """public abstract java.lang.String dev.ultreon.quantum.text.TextKey.get(dev.ultreon.quantum.api.commands.CommandSender)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.text.TranslationText
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import dev.ultreon.quantum.util.RgbColor as _RgbColor
_RgbColor = _RgbColor
import java.util.function.Consumer as Consumer
import java.lang.String as _string
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.util.Spliterator as Spliterator
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.text.MutableText as _MutableText
_MutableText = _MutableText
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import dev.ultreon.quantum.text.TranslationText as _TranslationText
_TranslationText = _TranslationText
import java.util.Iterator as Iterator
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.text.LiteralText as _LiteralText
_LiteralText = _LiteralText
import dev.ultreon.ubo.types.MapType as _MapType
_MapType = _MapType
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.lang.Long as _long
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

from builtins import int
import dev.ultreon.quantum.text.TextStyle as _TextStyle
_TextStyle = _TextStyle
import java.lang.Class as _Class
_Class = _Class
 
class TranslationText():
    """dev.ultreon.quantum.text.TranslationText"""
 
    @staticmethod
    def _wrap(java_value: _TranslationText) -> 'TranslationText':
        return TranslationText(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TranslationText):
        """
        Dynamic initializer for TranslationText.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TranslationText__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TranslationText__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def empty() -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.empty()"""
        return TextObject._wrap(_TextObject.empty())

    @staticmethod
    @overload
    def deserialize(arg0: 'MapType') -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.deserialize(dev.ultreon.ubo.types.MapType)"""
        return TextObject._wrap(_TextObject.deserialize(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setUnderlined(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setUnderlined(boolean)"""
        return 'MutableText'._wrap(super(_MutableText, self).setUnderlined(_boolean.valueOf(arg0)))

    @overload
    def setStrikethrough(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setStrikethrough(boolean)"""
        return 'MutableText'._wrap(super(_MutableText, self).setStrikethrough(_boolean.valueOf(arg0)))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

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
    def deserialize(arg0: 'MapType') -> 'TranslationText':
        """public static dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.text.TranslationText.deserialize(dev.ultreon.ubo.types.MapType)"""
        return TranslationText._wrap(_TranslationText.deserialize(arg0))

    @overload
    def append(self, arg0: str) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.append(java.lang.String)"""
        return 'MutableText'._wrap(super(_MutableText, self).append(arg0))

    @override
    @overload
    def isItalic(self) -> bool:
        """public boolean dev.ultreon.quantum.text.MutableText.isItalic()"""
        return bool._wrap(super(MutableText, self).isItalic())

    @staticmethod
    @overload
    def nullToEmpty(arg0: str) -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.nullToEmpty(java.lang.String)"""
        return TextObject._wrap(_TextObject.nullToEmpty(arg0))

    @override
    @overload
    def getSize(self) -> int:
        """public int dev.ultreon.quantum.text.MutableText.getSize()"""
        return int._wrap(super(MutableText, self).getSize())

    @override
    @overload
    def isBold(self) -> bool:
        """public boolean dev.ultreon.quantum.text.MutableText.isBold()"""
        return bool._wrap(super(MutableText, self).isBold())

    @override
    @overload
    def createString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.text.TranslationText.createString()"""
        return str._wrap(super(TranslationText, self).createString())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.text.TextObject.iterator()"""
        return 'Iterator'._wrap(super(TextObject, self).iterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def literal(arg0: str) -> 'LiteralText':
        """public static dev.ultreon.quantum.text.LiteralText dev.ultreon.quantum.text.TextObject.literal(java.lang.String)"""
        return LiteralText._wrap(_TextObject.literal(arg0))

    @override
    @overload
    def getText(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.text.MutableText.getText()"""
        return str._wrap(super(MutableText, self).getText())

    @overload
    def style(self, arg0: 'Consumer') -> 'TranslationText':
        """public dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.text.TranslationText.style(java.util.function.Consumer<dev.ultreon.quantum.text.TextStyle>)"""
        return 'TranslationText'._wrap(super(_TranslationText, self).style(arg0))

    @override
    @overload
    def isStrikethrough(self) -> bool:
        """public boolean dev.ultreon.quantum.text.MutableText.isStrikethrough()"""
        return bool._wrap(super(MutableText, self).isStrikethrough())

    @override
    @overload
    def setSize(self, arg0: int):
        """public void dev.ultreon.quantum.text.MutableText.setSize(int)"""
        super(_MutableText, self).setSize(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'TextObject') -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.nullToEmpty(dev.ultreon.quantum.text.TextObject)"""
        return TextObject._wrap(_TextObject.nullToEmpty(arg0))

    @overload
    def setItalic(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setItalic(boolean)"""
        return 'MutableText'._wrap(super(_MutableText, self).setItalic(_boolean.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def isUnderlined(self) -> bool:
        """public boolean dev.ultreon.quantum.text.MutableText.isUnderlined()"""
        return bool._wrap(super(MutableText, self).isUnderlined())

    @overload
    def setColor(self, arg0: 'RgbColor') -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setColor(dev.ultreon.quantum.util.RgbColor)"""
        return 'MutableText'._wrap(super(_MutableText, self).setColor(arg0))

    @override
    @overload
    def serialize(self) -> 'types.MapType':
        """public dev.ultreon.ubo.types.MapType dev.ultreon.quantum.text.TranslationText.serialize()"""
        return 'types.MapType'._wrap(super(TranslationText, self).serialize())

    @override
    @overload
    def getColor(self) -> 'util.RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.text.MutableText.getColor()"""
        return 'util.RgbColor'._wrap(super(MutableText, self).getColor())

    @overload
    def append(self, arg0: object) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.append(java.lang.Object)"""
        return 'MutableText'._wrap(super(_MutableText, self).append(arg0))

    @overload
    def setBold(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setBold(boolean)"""
        return 'MutableText'._wrap(super(_MutableText, self).setBold(_boolean.valueOf(arg0)))

    @overload
    def append(self, arg0: 'TextObject') -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.append(dev.ultreon.quantum.text.TextObject)"""
        return 'MutableText'._wrap(super(_MutableText, self).append(arg0))

    @staticmethod
    @overload
    def translation(arg0: str, *arg1: object) -> 'TranslationText':
        """public static dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.text.TextObject.translation(java.lang.String,java.lang.Object...)"""
        return TranslationText._wrap(_TextObject.translation(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getStyle(self) -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextObject.getStyle()"""
        return 'TextStyle'._wrap(super(TextObject, self).getStyle())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def copy(self) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.TranslationText.copy()"""
        return 'MutableText'._wrap(super(TranslationText, self).copy())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.text.Translations
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import dev.ultreon.quantum.text.Translations as _Translations
_Translations = _Translations
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Translations():
    """dev.ultreon.quantum.text.Translations"""
 
    @staticmethod
    def _wrap(java_value: _Translations) -> 'Translations':
        return Translations(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Translations):
        """
        Dynamic initializer for Translations.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Translations__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Translations__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.Translations.NULL_OBJECT
    NULL_OBJECT: 'TextObject' = _wrap(_TextObject.NULL_OBJECT)


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
        """public dev.ultreon.quantum.text.Translations()"""
        val = _Translations()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.text.Translations()"""
        val = _Translations()
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.text.FontTexture
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.text.FontTexture as _FontTexture
_FontTexture = _FontTexture
import java.lang.Integer as _int
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FontTexture():
    """dev.ultreon.quantum.text.FontTexture"""
 
    @staticmethod
    def _wrap(java_value: _FontTexture) -> 'FontTexture':
        return FontTexture(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FontTexture):
        """
        Dynamic initializer for FontTexture.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FontTexture__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FontTexture__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.text.FontTexture.hashCode()"""
        return int._wrap(super(FontTexture, self).hashCode())

    @overload
    def __init__(self, arg0: str, arg1: 'Identifier'):
        """public dev.ultreon.quantum.text.FontTexture(char,dev.ultreon.quantum.util.Identifier)"""
        val = _FontTexture(_char.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getFont(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.text.FontTexture.getFont()"""
        return 'util.Identifier'._wrap(super(FontTexture, self).getFont())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.text.FontTexture.equals(java.lang.Object)"""
        return bool._wrap(super(_FontTexture, self).equals(arg0))

    @overload
    def __init__(self, arg0: int, arg1: 'Identifier'):
        """public dev.ultreon.quantum.text.FontTexture(int,dev.ultreon.quantum.util.Identifier)"""
        val = _FontTexture(_int.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getChar(self) -> str:
        """public char dev.ultreon.quantum.text.FontTexture.getChar()"""
        return str._wrap(super(FontTexture, self).getChar())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.text.HoverEvent$Action
import dev.ultreon.quantum.text.HoverEvent as _HoverEvent_Action
_Action = _HoverEvent_Action.Action
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Action():
    """dev.ultreon.quantum.text.HoverEvent.Action"""
 
    @staticmethod
    def _wrap(java_value: _Action) -> 'Action':
        return Action(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Action):
        """
        Dynamic initializer for Action.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Action__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Action__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Action':
        """public static dev.ultreon.quantum.text.HoverEvent$Action dev.ultreon.quantum.text.HoverEvent$Action.valueOf(java.lang.String)"""
        return Action._wrap(_Action.valueOf(arg0))

    @staticmethod
    @overload
    def values() -> List['Action']:
        """public static dev.ultreon.quantum.text.HoverEvent$Action[] dev.ultreon.quantum.text.HoverEvent$Action.values()"""
        return List[Action]._wrap(_Action.values())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


Action.LOCATION = Action._wrap(_LOCATION.LOCATION)

Action.PLAYER = Action._wrap(_PLAYER.PLAYER)

Action.ENTITY = Action._wrap(_ENTITY.ENTITY)

Action.ITEM = Action._wrap(_ITEM.ITEM)

Action.TEXT = Action._wrap(_TEXT.TEXT) 
 
 
# CLASS: dev.ultreon.quantum.text.ClickEvent
from builtins import str
from pyquantum_helper import override
import java.net.URI as URI
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.text.ClickEvent as _ClickEvent
_ClickEvent = _ClickEvent
import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.text.ClickEvent as _ClickEvent_Action
_Action = _ClickEvent_Action.Action
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ClickEvent():
    """dev.ultreon.quantum.text.ClickEvent"""
 
    @staticmethod
    def _wrap(java_value: _ClickEvent) -> 'ClickEvent':
        return ClickEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClickEvent):
        """
        Dynamic initializer for ClickEvent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClickEvent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClickEvent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.text.ClickEvent.equals(java.lang.Object)"""
        return bool._wrap(super(_ClickEvent, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.text.ClickEvent.hashCode()"""
        return int._wrap(super(ClickEvent, self).hashCode())

    @overload
    def action(self) -> 'Action':
        """public dev.ultreon.quantum.text.ClickEvent$Action dev.ultreon.quantum.text.ClickEvent.action()"""
        return 'Action'._wrap(super(ClickEvent, self).action())

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

    @staticmethod
    @overload
    def openUri(arg0: 'URI') -> 'ClickEvent':
        """public static dev.ultreon.quantum.text.ClickEvent dev.ultreon.quantum.text.ClickEvent.openUri(java.net.URI)"""
        return ClickEvent._wrap(_ClickEvent.openUri(arg0))

    @staticmethod
    @overload
    def runCommand(arg0: str) -> 'ClickEvent':
        """public static dev.ultreon.quantum.text.ClickEvent dev.ultreon.quantum.text.ClickEvent.runCommand(java.lang.String)"""
        return ClickEvent._wrap(_ClickEvent.runCommand(arg0))

    @staticmethod
    @overload
    def copyToClipboard(arg0: str) -> 'ClickEvent':
        """public static dev.ultreon.quantum.text.ClickEvent dev.ultreon.quantum.text.ClickEvent.copyToClipboard(java.lang.String)"""
        return ClickEvent._wrap(_ClickEvent.copyToClipboard(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Action', arg1: str):
        """public dev.ultreon.quantum.text.ClickEvent(dev.ultreon.quantum.text.ClickEvent$Action,java.lang.String)"""
        val = _ClickEvent(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def value(self) -> str:
        """public java.lang.String dev.ultreon.quantum.text.ClickEvent.value()"""
        return str._wrap(super(ClickEvent, self).value())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def suggestMessage(arg0: str) -> 'ClickEvent':
        """public static dev.ultreon.quantum.text.ClickEvent dev.ultreon.quantum.text.ClickEvent.suggestMessage(java.lang.String)"""
        return ClickEvent._wrap(_ClickEvent.suggestMessage(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.text.ClickEvent.toString()"""
        return str._wrap(super(ClickEvent, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.text.FormattedText
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.text.FormattedText as _FormattedText_TextFormatElement
_TextFormatElement = _FormattedText_TextFormatElement.TextFormatElement
import java.lang.String as _string
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import dev.ultreon.quantum.text.FormattedText as _FormattedText
_FormattedText = _FormattedText
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class FormattedText():
    """dev.ultreon.quantum.text.FormattedText"""
 
    @staticmethod
    def _wrap(java_value: _FormattedText) -> 'FormattedText':
        return FormattedText(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FormattedText):
        """
        Dynamic initializer for FormattedText.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FormattedText__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FormattedText__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getElementsFromTo(self, arg0: int, arg1: int) -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.text.FormattedText$TextFormatElement> dev.ultreon.quantum.text.FormattedText.getElementsFromTo(int,int)"""
        return 'Iterable'._wrap(super(_FormattedText, self).getElementsFromTo(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def lastIndexOf(self, arg0: str, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.text.FormattedText.lastIndexOf(java.lang.String,int,int)"""
        return int._wrap(super(_FormattedText, self).lastIndexOf(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def getElementsFrom(self, arg0: int) -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.text.FormattedText$TextFormatElement> dev.ultreon.quantum.text.FormattedText.getElementsFrom(int)"""
        return 'Iterable'._wrap(super(_FormattedText, self).getElementsFrom(_int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def copy(self) -> 'FormattedText':
        """public dev.ultreon.quantum.text.FormattedText dev.ultreon.quantum.text.FormattedText.copy()"""
        return 'FormattedText'._wrap(super(FormattedText, self).copy())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getNextElement(self, arg0: int) -> 'TextFormatElement':
        """public dev.ultreon.quantum.text.FormattedText$TextFormatElement dev.ultreon.quantum.text.FormattedText.getNextElement(int)"""
        return 'TextFormatElement'._wrap(super(_FormattedText, self).getNextElement(_int.valueOf(arg0)))

    @overload
    def getPreviousElement(self, arg0: int) -> 'TextFormatElement':
        """public dev.ultreon.quantum.text.FormattedText$TextFormatElement dev.ultreon.quantum.text.FormattedText.getPreviousElement(int)"""
        return 'TextFormatElement'._wrap(super(_FormattedText, self).getPreviousElement(_int.valueOf(arg0)))

    @overload
    def indexOf(self, arg0: str, arg1: int, arg2: int) -> int:
        """public int dev.ultreon.quantum.text.FormattedText.indexOf(java.lang.String,int,int)"""
        return int._wrap(super(_FormattedText, self).indexOf(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @staticmethod
    @overload
    def from(arg0: 'TextObject') -> 'FormattedText':
        """public static dev.ultreon.quantum.text.FormattedText dev.ultreon.quantum.text.FormattedText.from(dev.ultreon.quantum.text.TextObject)"""
        return FormattedText._wrap(_FormattedText.from(arg0))

    @staticmethod
    @overload
    def from(arg0: str) -> 'FormattedText':
        """public static dev.ultreon.quantum.text.FormattedText dev.ultreon.quantum.text.FormattedText.from(java.lang.String)"""
        return FormattedText._wrap(_FormattedText.from(arg0))

    @overload
    def indexOf(self, arg0: str) -> int:
        """public int dev.ultreon.quantum.text.FormattedText.indexOf(java.lang.String)"""
        return int._wrap(super(_FormattedText, self).indexOf(arg0))

    @overload
    def lastIndexOf(self, arg0: str, arg1: int) -> int:
        """public int dev.ultreon.quantum.text.FormattedText.lastIndexOf(java.lang.String,int)"""
        return int._wrap(super(_FormattedText, self).lastIndexOf(arg0, _int.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getElementsWithin(self, arg0: int, arg1: int) -> 'Iterable':
        """public java.lang.Iterable<dev.ultreon.quantum.text.FormattedText$TextFormatElement> dev.ultreon.quantum.text.FormattedText.getElementsWithin(int,int)"""
        return 'Iterable'._wrap(super(_FormattedText, self).getElementsWithin(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def indexOf(self, arg0: str, arg1: int) -> int:
        """public int dev.ultreon.quantum.text.FormattedText.indexOf(java.lang.String,int)"""
        return int._wrap(super(_FormattedText, self).indexOf(arg0, _int.valueOf(arg1)))

    @overload
    def getText(self) -> str:
        """public java.lang.String dev.ultreon.quantum.text.FormattedText.getText()"""
        return str._wrap(super(FormattedText, self).getText())

    @overload
    def __init__(self, arg0: 'List'):
        """public dev.ultreon.quantum.text.FormattedText(java.util.List<dev.ultreon.quantum.text.FormattedText$TextFormatElement>)"""
        val = _FormattedText(arg0)
        self.__wrapper = val

    @overload
    def length(self) -> int:
        """public int dev.ultreon.quantum.text.FormattedText.length()"""
        return int._wrap(super(FormattedText, self).length())

    @staticmethod
    @overload
    def from(arg0: 'MutableText') -> 'FormattedText':
        """public static dev.ultreon.quantum.text.FormattedText dev.ultreon.quantum.text.FormattedText.from(dev.ultreon.quantum.text.MutableText)"""
        return FormattedText._wrap(_FormattedText.from(arg0))

    @overload
    def getElements(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.text.FormattedText$TextFormatElement> dev.ultreon.quantum.text.FormattedText.getElements()"""
        return 'List'._wrap(super(FormattedText, self).getElements())

    @overload
    def indexOf(self, arg0: 'TextFormatElement') -> int:
        """public int dev.ultreon.quantum.text.FormattedText.indexOf(dev.ultreon.quantum.text.FormattedText$TextFormatElement)"""
        return int._wrap(super(_FormattedText, self).indexOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.text.FormattedText.toString()"""
        return str._wrap(super(FormattedText, self).toString())

    @overload
    def lastIndexOf(self, arg0: str) -> int:
        """public int dev.ultreon.quantum.text.FormattedText.lastIndexOf(java.lang.String)"""
        return int._wrap(super(_FormattedText, self).lastIndexOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.text.IconMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.text.IconMap as _IconMap
_IconMap = _IconMap
import java.lang.String as _string
import dev.ultreon.quantum.text.FontTexture as _FontTexture
_FontTexture = _FontTexture
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IconMap():
    """dev.ultreon.quantum.text.IconMap"""
 
    @staticmethod
    def _wrap(java_value: _IconMap) -> 'IconMap':
        return IconMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IconMap):
        """
        Dynamic initializer for IconMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IconMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IconMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.text.IconMap()"""
        val = _IconMap()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def get(arg0: str) -> 'FontTexture':
        """public static dev.ultreon.quantum.text.FontTexture dev.ultreon.quantum.text.IconMap.get(java.lang.String)"""
        return FontTexture._wrap(_IconMap.get(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

        @staticmethod
        @overload
        def register():
            """public static void dev.ultreon.quantum.text.IconMap.register()"""
            _IconMap.register()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def set(arg0: str, arg1: 'FontTexture'):
        """public static void dev.ultreon.quantum.text.IconMap.set(java.lang.String,dev.ultreon.quantum.text.FontTexture)"""
        _IconMap.set(arg0, arg1)

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.text.IconMap()"""
        val = _IconMap()
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
 
 
# CLASS: dev.ultreon.quantum.text.ServerLanguage
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.util.Locale as Locale
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.text.ServerLanguage as _ServerLanguage
_ServerLanguage = _ServerLanguage
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
import java.util.Locale as _Locale
_Locale = _Locale
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ServerLanguage():
    """dev.ultreon.quantum.text.ServerLanguage"""
 
    @staticmethod
    def _wrap(java_value: _ServerLanguage) -> 'ServerLanguage':
        return ServerLanguage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServerLanguage):
        """
        Dynamic initializer for ServerLanguage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServerLanguage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServerLanguage__wrapper":
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
    def getLocale(self) -> 'Locale':
        """public java.util.Locale dev.ultreon.quantum.text.ServerLanguage.getLocale()"""
        return 'Locale'._wrap(super(ServerLanguage, self).getLocale())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def get(self, arg0: str, *arg1: object) -> str:
        """public java.lang.String dev.ultreon.quantum.text.ServerLanguage.get(java.lang.String,java.lang.Object...)"""
        return str._wrap(super(_ServerLanguage, self).get(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Locale', arg1: 'Map', arg2: 'Identifier'):
        """public dev.ultreon.quantum.text.ServerLanguage(java.util.Locale,java.util.Map<java.lang.String, java.lang.String>,dev.ultreon.quantum.util.Identifier)"""
        val = _ServerLanguage(arg0, arg1, arg2)
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
    def getId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.text.ServerLanguage.getId()"""
        return 'util.Identifier'._wrap(super(ServerLanguage, self).getId())

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
 
 
# CLASS: dev.ultreon.quantum.text.HoverEvent
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
import dev.ultreon.quantum.text.HoverEvent as _HoverEvent_Action
_Action = _HoverEvent_Action.Action
from pyquantum_helper import override
try:
    from pyquantum.entity import player
except ImportError:
    player = _import_once("pyquantum.entity.player")

import java.lang.Object as _Object
_Object = _Object
try:
    from pyquantum import entity
except ImportError:
    entity = _import_once("pyquantum.entity")

import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

from builtins import object
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.text.HoverEvent as _HoverEvent
_HoverEvent = _HoverEvent
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HoverEvent():
    """dev.ultreon.quantum.text.HoverEvent"""
 
    @staticmethod
    def _wrap(java_value: _HoverEvent) -> 'HoverEvent':
        return HoverEvent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HoverEvent):
        """
        Dynamic initializer for HoverEvent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HoverEvent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HoverEvent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.text.HoverEvent.equals(java.lang.Object)"""
        return bool._wrap(super(_HoverEvent, self).equals(arg0))

    @staticmethod
    @overload
    def location(arg0: 'Player') -> 'HoverEvent':
        """public static dev.ultreon.quantum.text.HoverEvent<dev.ultreon.quantum.entity.player.Player> dev.ultreon.quantum.text.HoverEvent.location(dev.ultreon.quantum.entity.player.Player)"""
        return HoverEvent._wrap(_HoverEvent.location(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.text.HoverEvent.toString()"""
        return str._wrap(super(HoverEvent, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.text.HoverEvent.hashCode()"""
        return int._wrap(super(HoverEvent, self).hashCode())

    @overload
    def __init__(self, arg0: 'Action', arg1: object):
        """public dev.ultreon.quantum.text.HoverEvent(dev.ultreon.quantum.text.HoverEvent$Action,T)"""
        val = _HoverEvent(arg0, arg1)
        self.__wrapper = val

    @staticmethod
    @overload
    def location(arg0: 'Entity') -> 'HoverEvent':
        """public static dev.ultreon.quantum.text.HoverEvent<dev.ultreon.quantum.entity.Entity> dev.ultreon.quantum.text.HoverEvent.location(dev.ultreon.quantum.entity.Entity)"""
        return HoverEvent._wrap(_HoverEvent.location(arg0))

    @overload
    def value(self) -> object:
        """public T dev.ultreon.quantum.text.HoverEvent.value()"""
        return object._wrap(super(HoverEvent, self).value())

    @staticmethod
    @overload
    def location(arg0: 'Location') -> 'HoverEvent':
        """public static dev.ultreon.quantum.text.HoverEvent<dev.ultreon.quantum.world.Location> dev.ultreon.quantum.text.HoverEvent.location(dev.ultreon.quantum.world.Location)"""
        return HoverEvent._wrap(_HoverEvent.location(arg0))

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

    @staticmethod
    @overload
    def item(arg0: 'ItemStack') -> 'HoverEvent':
        """public static dev.ultreon.quantum.text.HoverEvent<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.text.HoverEvent.item(dev.ultreon.quantum.item.ItemStack)"""
        return HoverEvent._wrap(_HoverEvent.item(arg0))

    @staticmethod
    @overload
    def text(arg0: str) -> 'HoverEvent':
        """public static dev.ultreon.quantum.text.HoverEvent<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.text.HoverEvent.text(java.lang.String)"""
        return HoverEvent._wrap(_HoverEvent.text(arg0))

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
    def action(self) -> 'Action':
        """public dev.ultreon.quantum.text.HoverEvent$Action dev.ultreon.quantum.text.HoverEvent.action()"""
        return 'Action'._wrap(super(HoverEvent, self).action())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def text(arg0: 'TextObject') -> 'HoverEvent':
        """public static dev.ultreon.quantum.text.HoverEvent<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.text.HoverEvent.text(dev.ultreon.quantum.text.TextObject)"""
        return HoverEvent._wrap(_HoverEvent.text(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: dev.ultreon.quantum.text.TextElement
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.lang.Integer as _int
import dev.ultreon.quantum.text.TextElement as _TextElement
_TextElement = _TextElement
from builtins import bool
import java.lang.Long as _long
from builtins import int
import dev.ultreon.quantum.text.TextStyle as _TextStyle
_TextStyle = _TextStyle
import java.lang.Class as _Class
_Class = _Class
 
class TextElement():
    """dev.ultreon.quantum.text.TextElement"""
 
    @staticmethod
    def _wrap(java_value: _TextElement) -> 'TextElement':
        return TextElement(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextElement):
        """
        Dynamic initializer for TextElement.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextElement__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextElement__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.text.TextElement.hashCode()"""
        return int._wrap(super(TextElement, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.text.TextElement.equals(java.lang.Object)"""
        return bool._wrap(super(_TextElement, self).equals(arg0))

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

    @overload
    def style(self) -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextElement.style()"""
        return 'TextStyle'._wrap(super(TextElement, self).style())

    @overload
    def text(self) -> 'TextObject':
        """public dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextElement.text()"""
        return 'TextObject'._wrap(super(TextElement, self).text())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.text.TextElement.toString()"""
        return str._wrap(super(TextElement, self).toString())

    @overload
    def __init__(self, arg0: 'TextObject', arg1: 'TextStyle'):
        """public dev.ultreon.quantum.text.TextElement(dev.ultreon.quantum.text.TextObject,dev.ultreon.quantum.text.TextStyle)"""
        val = _TextElement(arg0, arg1)
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.text.Translatable
from builtins import str
import dev.ultreon.quantum.text.Translatable as _Translatable
_Translatable = _Translatable
import dev.ultreon.quantum.text.MutableText as _MutableText
_MutableText = _MutableText
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
 
class Translatable():
    """dev.ultreon.quantum.text.Translatable"""
 
    @staticmethod
    def _wrap(java_value: _Translatable) -> 'Translatable':
        return Translatable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Translatable):
        """
        Dynamic initializer for Translatable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Translatable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Translatable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getTranslation(self) -> 'MutableText':
        """public default dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.Translatable.getTranslation()"""
        return 'MutableText'._wrap(super(Translatable, self).getTranslation())

    @overload
    def getTranslationText(self) -> str:
        """public default java.lang.String dev.ultreon.quantum.text.Translatable.getTranslationText()"""
        return str._wrap(super(Translatable, self).getTranslationText())

    @abstractmethod
    def getTranslationId(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.text.Translatable.getTranslationId()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.text.ClickEvent$Action
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
import dev.ultreon.quantum.text.ClickEvent as _ClickEvent_Action
_Action = _ClickEvent_Action.Action
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Action():
    """dev.ultreon.quantum.text.ClickEvent.Action"""
 
    @staticmethod
    def _wrap(java_value: _Action) -> 'Action':
        return Action(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Action):
        """
        Dynamic initializer for Action.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Action__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Action__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Action':
        """public static dev.ultreon.quantum.text.ClickEvent$Action dev.ultreon.quantum.text.ClickEvent$Action.valueOf(java.lang.String)"""
        return Action._wrap(_Action.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @staticmethod
    @overload
    def values() -> List['Action']:
        """public static dev.ultreon.quantum.text.ClickEvent$Action[] dev.ultreon.quantum.text.ClickEvent$Action.values()"""
        return List[Action]._wrap(_Action.values())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()


Action.COPY_TO_CLIPBOARD = Action._wrap(_COPY_TO_CLIPBOARD.COPY_TO_CLIPBOARD)

Action.SUGGEST_MESSAGE = Action._wrap(_SUGGEST_MESSAGE.SUGGEST_MESSAGE)

Action.RUN_COMMAND = Action._wrap(_RUN_COMMAND.RUN_COMMAND)

Action.OPEN_URL = Action._wrap(_OPEN_URL.OPEN_URL) 
 
 
# CLASS: dev.ultreon.quantum.text.FormattedText$TextFormatElement
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import dev.ultreon.quantum.text.FormattedText as _FormattedText_TextFormatElement
_TextFormatElement = _FormattedText_TextFormatElement.TextFormatElement
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import dev.ultreon.quantum.text.TextStyle as _TextStyle
_TextStyle = _TextStyle
import java.lang.Class as _Class
_Class = _Class
 
class TextFormatElement():
    """dev.ultreon.quantum.text.FormattedText.TextFormatElement"""
 
    @staticmethod
    def _wrap(java_value: _TextFormatElement) -> 'TextFormatElement':
        return TextFormatElement(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextFormatElement):
        """
        Dynamic initializer for TextFormatElement.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextFormatElement__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextFormatElement__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def index(self) -> int:
        """public int dev.ultreon.quantum.text.FormattedText$TextFormatElement.index()"""
        return int._wrap(super(TextFormatElement, self).index())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def copy(self) -> 'TextFormatElement':
        """public dev.ultreon.quantum.text.FormattedText$TextFormatElement dev.ultreon.quantum.text.FormattedText$TextFormatElement.copy()"""
        return 'TextFormatElement'._wrap(super(TextFormatElement, self).copy())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.text.FormattedText$TextFormatElement.hashCode()"""
        return int._wrap(super(TextFormatElement, self).hashCode())

    @overload
    def split(self, arg0: int) -> List['TextFormatElement']:
        """public dev.ultreon.quantum.text.FormattedText$TextFormatElement[] dev.ultreon.quantum.text.FormattedText$TextFormatElement.split(int)"""
        return List['TextFormatElement']._wrap(super(_TextFormatElement, self).split(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'TextStyle', arg1: str, arg2: int):
        """public dev.ultreon.quantum.text.FormattedText$TextFormatElement(dev.ultreon.quantum.text.TextStyle,java.lang.String,int)"""
        val = _TextFormatElement(arg0, arg1, _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def length(self) -> int:
        """public int dev.ultreon.quantum.text.FormattedText$TextFormatElement.length()"""
        return int._wrap(super(TextFormatElement, self).length())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.text.FormattedText$TextFormatElement.equals(java.lang.Object)"""
        return bool._wrap(super(_TextFormatElement, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.text.FormattedText$TextFormatElement.toString()"""
        return str._wrap(super(TextFormatElement, self).toString())

    @overload
    def text(self) -> str:
        """public java.lang.String dev.ultreon.quantum.text.FormattedText$TextFormatElement.text()"""
        return str._wrap(super(TextFormatElement, self).text())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def indexOf(self, arg0: str) -> int:
        """public int dev.ultreon.quantum.text.FormattedText$TextFormatElement.indexOf(java.lang.String)"""
        return int._wrap(super(_TextFormatElement, self).indexOf(arg0))

    @overload
    def style(self) -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.FormattedText$TextFormatElement.style()"""
        return 'TextStyle'._wrap(super(TextFormatElement, self).style()) 
 
 
# CLASS: dev.ultreon.quantum.text.ParseResult
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Exception as Exception
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import dev.ultreon.quantum.text.ParseResult as _ParseResult
_ParseResult = _ParseResult
import java.lang.Integer as _int
import dev.ultreon.quantum.text.MutableText as _MutableText
_MutableText = _MutableText
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
import java.util.List as List
 
class ParseResult():
    """dev.ultreon.quantum.text.ParseResult"""
 
    @staticmethod
    def _wrap(java_value: _ParseResult) -> 'ParseResult':
        return ParseResult(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParseResult):
        """
        Dynamic initializer for ParseResult.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParseResult__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParseResult__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getTextResult(self) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.ParseResult.getTextResult()"""
        return 'MutableText'._wrap(super(ParseResult, self).getTextResult())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getResult(self) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.ParseResult.getResult()"""
        return 'MutableText'._wrap(super(ParseResult, self).getResult())

    @staticmethod
    @overload
    def error(arg0: 'Exception') -> 'ParseResult':
        """public static dev.ultreon.quantum.text.ParseResult dev.ultreon.quantum.text.ParseResult.error(java.lang.Exception)"""
        return ParseResult._wrap(_ParseResult.error(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getMutableTexts(self) -> List['TextObject']:
        """public dev.ultreon.quantum.text.TextObject[] dev.ultreon.quantum.text.ParseResult.getMutableTexts()"""
        return List['TextObject']._wrap(super(ParseResult, self).getMutableTexts())

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'List', arg1: 'TextObject', arg2: 'TextObject', arg3: 'MutableText'):
        """public dev.ultreon.quantum.text.ParseResult(java.util.List<dev.ultreon.quantum.entity.player.Player>,dev.ultreon.quantum.text.TextObject,dev.ultreon.quantum.text.TextObject,dev.ultreon.quantum.text.MutableText)"""
        val = _ParseResult(arg0, arg1, arg2, arg3)
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.text.MutableText
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
from abc import abstractmethod, ABC
import dev.ultreon.quantum.util.RgbColor as _RgbColor
_RgbColor = _RgbColor
import java.util.function.Consumer as Consumer
import java.lang.String as _string
import dev.ultreon.quantum.text.TextObject as _TextObject
_TextObject = _TextObject
import java.util.Spliterator as Spliterator
import java.lang.Boolean as _boolean
import dev.ultreon.quantum.text.MutableText as _MutableText
_MutableText = _MutableText
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import dev.ultreon.quantum.text.TranslationText as _TranslationText
_TranslationText = _TranslationText
import java.util.Iterator as Iterator
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.text.LiteralText as _LiteralText
_LiteralText = _LiteralText
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.lang.Long as _long
from builtins import int
try:
    from pyubo import types
except ImportError:
    types = _import_once("pyubo.types")

import dev.ultreon.quantum.text.TextStyle as _TextStyle
_TextStyle = _TextStyle
import java.lang.Class as _Class
_Class = _Class
 
class MutableText():
    """dev.ultreon.quantum.text.MutableText"""
 
    @staticmethod
    def _wrap(java_value: _MutableText) -> 'MutableText':
        return MutableText(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MutableText):
        """
        Dynamic initializer for MutableText.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MutableText__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MutableText__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def copy(self, ):
        """public abstract dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.copy()"""
        pass

    @staticmethod
    @overload
    def empty() -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.empty()"""
        return TextObject._wrap(_TextObject.empty())

    @overload
    def isItalic(self) -> bool:
        """public boolean dev.ultreon.quantum.text.MutableText.isItalic()"""
        return bool._wrap(super(MutableText, self).isItalic())

    @staticmethod
    @overload
    def deserialize(arg0: 'MapType') -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.deserialize(dev.ultreon.ubo.types.MapType)"""
        return TextObject._wrap(_TextObject.deserialize(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setUnderlined(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setUnderlined(boolean)"""
        return 'MutableText'._wrap(super(_MutableText, self).setUnderlined(_boolean.valueOf(arg0)))

    @overload
    def isStrikethrough(self) -> bool:
        """public boolean dev.ultreon.quantum.text.MutableText.isStrikethrough()"""
        return bool._wrap(super(MutableText, self).isStrikethrough())

    @overload
    def setStrikethrough(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setStrikethrough(boolean)"""
        return 'MutableText'._wrap(super(_MutableText, self).setStrikethrough(_boolean.valueOf(arg0)))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

    @overload
    def isUnderlined(self) -> bool:
        """public boolean dev.ultreon.quantum.text.MutableText.isUnderlined()"""
        return bool._wrap(super(MutableText, self).isUnderlined())

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
    def append(self, arg0: str) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.append(java.lang.String)"""
        return 'MutableText'._wrap(super(_MutableText, self).append(arg0))

    @staticmethod
    @overload
    def nullToEmpty(arg0: str) -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.nullToEmpty(java.lang.String)"""
        return TextObject._wrap(_TextObject.nullToEmpty(arg0))

    @overload
    def getSize(self) -> int:
        """public int dev.ultreon.quantum.text.MutableText.getSize()"""
        return int._wrap(super(MutableText, self).getSize())

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<dev.ultreon.quantum.text.TextObject> dev.ultreon.quantum.text.TextObject.iterator()"""
        return 'Iterator'._wrap(super(TextObject, self).iterator())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def literal(arg0: str) -> 'LiteralText':
        """public static dev.ultreon.quantum.text.LiteralText dev.ultreon.quantum.text.TextObject.literal(java.lang.String)"""
        return LiteralText._wrap(_TextObject.literal(arg0))

    @override
    @overload
    def getText(self) -> str:
        """public final java.lang.String dev.ultreon.quantum.text.MutableText.getText()"""
        return str._wrap(super(MutableText, self).getText())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @abstractmethod
    def createString(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.text.TextObject.createString()"""
        pass

    @staticmethod
    @overload
    def nullToEmpty(arg0: 'TextObject') -> 'TextObject':
        """public static dev.ultreon.quantum.text.TextObject dev.ultreon.quantum.text.TextObject.nullToEmpty(dev.ultreon.quantum.text.TextObject)"""
        return TextObject._wrap(_TextObject.nullToEmpty(arg0))

    @overload
    def isBold(self) -> bool:
        """public boolean dev.ultreon.quantum.text.MutableText.isBold()"""
        return bool._wrap(super(MutableText, self).isBold())

    @overload
    def setItalic(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setItalic(boolean)"""
        return 'MutableText'._wrap(super(_MutableText, self).setItalic(_boolean.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setColor(self, arg0: 'RgbColor') -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setColor(dev.ultreon.quantum.util.RgbColor)"""
        return 'MutableText'._wrap(super(_MutableText, self).setColor(arg0))

    @overload
    def getColor(self) -> 'util.RgbColor':
        """public dev.ultreon.quantum.util.RgbColor dev.ultreon.quantum.text.MutableText.getColor()"""
        return 'util.RgbColor'._wrap(super(MutableText, self).getColor())

    @overload
    def append(self, arg0: object) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.append(java.lang.Object)"""
        return 'MutableText'._wrap(super(_MutableText, self).append(arg0))

    @overload
    def setBold(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.setBold(boolean)"""
        return 'MutableText'._wrap(super(_MutableText, self).setBold(_boolean.valueOf(arg0)))

    @overload
    def append(self, arg0: 'TextObject') -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.append(dev.ultreon.quantum.text.TextObject)"""
        return 'MutableText'._wrap(super(_MutableText, self).append(arg0))

    @staticmethod
    @overload
    def translation(arg0: str, *arg1: object) -> 'TranslationText':
        """public static dev.ultreon.quantum.text.TranslationText dev.ultreon.quantum.text.TextObject.translation(java.lang.String,java.lang.Object...)"""
        return TranslationText._wrap(_TextObject.translation(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def style(self, arg0: 'Consumer') -> 'MutableText':
        """public dev.ultreon.quantum.text.MutableText dev.ultreon.quantum.text.MutableText.style(java.util.function.Consumer<dev.ultreon.quantum.text.TextStyle>)"""
        return 'MutableText'._wrap(super(_MutableText, self).style(arg0))

    @overload
    def setSize(self, arg0: int):
        """public void dev.ultreon.quantum.text.MutableText.setSize(int)"""
        super(_MutableText, self).setSize(_int.valueOf(arg0))

    @abstractmethod
    def serialize(self, ):
        """public abstract dev.ultreon.ubo.types.MapType dev.ultreon.quantum.text.TextObject.serialize()"""
        pass

    @override
    @overload
    def getStyle(self) -> 'TextStyle':
        """public dev.ultreon.quantum.text.TextStyle dev.ultreon.quantum.text.TextObject.getStyle()"""
        return 'TextStyle'._wrap(super(TextObject, self).getStyle())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.text.LanguageBootstrap
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.String as _string
from builtins import str
import dev.ultreon.quantum.text.LanguageBootstrap as _LanguageBootstrap
_LanguageBootstrap = _LanguageBootstrap
from builtins import object
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
 
class LanguageBootstrap():
    """dev.ultreon.quantum.text.LanguageBootstrap"""
 
    @staticmethod
    def _wrap(java_value: _LanguageBootstrap) -> 'LanguageBootstrap':
        return LanguageBootstrap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LanguageBootstrap):
        """
        Dynamic initializer for LanguageBootstrap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LanguageBootstrap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LanguageBootstrap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.util.LazyValue<dev.ultreon.quantum.text.LanguageBootstrap> dev.ultreon.quantum.text.LanguageBootstrap.bootstrap
    bootstrap: 'util.LazyValue' = _wrap(_util.LazyValue.bootstrap)


    @staticmethod
    @overload
    def translate(arg0: str, *arg1: object) -> str:
        """public static java.lang.String dev.ultreon.quantum.text.LanguageBootstrap.translate(java.lang.String,java.lang.Object...)"""
        return str._wrap(_LanguageBootstrap.translate(arg0, arg1))

    @abstractmethod
    def handleTranslation(self, arg0: str, *arg1: object):
        """public abstract java.lang.String dev.ultreon.quantum.text.LanguageBootstrap.handleTranslation(java.lang.String,java.lang.Object...)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.text.EmoteMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import dev.ultreon.quantum.text.FontTexture as _FontTexture
_FontTexture = _FontTexture
import java.lang.Integer as _int
import dev.ultreon.quantum.text.EmoteMap as _EmoteMap
_EmoteMap = _EmoteMap
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EmoteMap():
    """dev.ultreon.quantum.text.EmoteMap"""
 
    @staticmethod
    def _wrap(java_value: _EmoteMap) -> 'EmoteMap':
        return EmoteMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EmoteMap):
        """
        Dynamic initializer for EmoteMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EmoteMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EmoteMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def set(arg0: str, arg1: 'FontTexture'):
        """public static void dev.ultreon.quantum.text.EmoteMap.set(java.lang.String,dev.ultreon.quantum.text.FontTexture)"""
        _EmoteMap.set(arg0, arg1)

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

    @staticmethod
    @overload
    def get(arg0: str) -> 'FontTexture':
        """public static dev.ultreon.quantum.text.FontTexture dev.ultreon.quantum.text.EmoteMap.get(java.lang.String)"""
        return FontTexture._wrap(_EmoteMap.get(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.text.EmoteMap()"""
        val = _EmoteMap()
        self.__wrapper = val

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
        def register():
            """public static void dev.ultreon.quantum.text.EmoteMap.register()"""
            _EmoteMap.register()

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
        """public dev.ultreon.quantum.text.EmoteMap()"""
        val = _EmoteMap()
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