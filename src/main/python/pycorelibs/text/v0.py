from __future__ import annotations
from overload import overload


 
import java.lang.Boolean as __boolean
from builtins import type
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.libs.text.v0.TextObject as __TextObject
__TextObject = __TextObject
import java.text.AttributedString as __AttributedString
__AttributedString = __AttributedString
import java.text.AttributedString as AttributedString
import java.awt.Color as __Color
__Color = __Color
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.libs.text.v0.FontWidth as __FontWidth
__FontWidth = __FontWidth
import dev.ultreon.libs.text.v0.LiteralText as __LiteralText
__LiteralText = __LiteralText
import java.lang.Double as __double
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
import dev.ultreon.libs.text.v0.MutableText as __MutableText
__MutableText = __MutableText
from builtins import object
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.awt.Color as Color
import dev.ultreon.libs.text.v0.FontWeight as __FontWeight
__FontWeight = __FontWeight
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import int
 
class LiteralText(__MutableText, MutableText):
    """dev.ultreon.libs.text.v0.LiteralText"""
 
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
 
    @overload
    def setFontWeight(self, arg0: int) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setFontWeight(int)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setFontWeight(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setSize(self, arg0: float) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setSize(double)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setSize(__double.valueOf(arg0)))

    @override
    @overload
    def getAttrs(self) -> 'Map':
        """public java.util.Map<? extends java.text.AttributedCharacterIterator$Attribute, ?> dev.ultreon.libs.text.v0.MutableText.getAttrs()"""
        return 'Map'.__wrap(super(MutableText, self).getAttrs())

    @override
    @overload
    def isLigaturesEnabled(self) -> bool:
        """public boolean dev.ultreon.libs.text.v0.MutableText.isLigaturesEnabled()"""
        return bool.__wrap(super(MutableText, self).isLigaturesEnabled())

    @overload
    def append(self, arg0: object) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.append(java.lang.Object)"""
        return 'MutableText'.__wrap(super(__MutableText, self).append(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getFontWeight(self) -> 'FontWeight':
        """public dev.ultreon.libs.text.v0.FontWeight dev.ultreon.libs.text.v0.MutableText.getFontWeight()"""
        return 'FontWeight'.__wrap(super(MutableText, self).getFontWeight())

    @overload
    def setLigaturesEnabled(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setLigaturesEnabled(boolean)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setLigaturesEnabled(__boolean.valueOf(arg0)))

    @override
    @overload
    def getWidth(self) -> float:
        """public float dev.ultreon.libs.text.v0.MutableText.getWidth()"""
        return float.__wrap(super(MutableText, self).getWidth())

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
    def setUnderlined(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setUnderlined(boolean)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setUnderlined(__boolean.valueOf(arg0)))

    @override
    @overload
    def getColor(self) -> 'Color':
        """public java.awt.Color dev.ultreon.libs.text.v0.MutableText.getColor()"""
        return 'Color'.__wrap(super(MutableText, self).getColor())

    @overload
    def setWeight(self, arg0: float) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setWeight(float)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setWeight(__float.valueOf(arg0)))

    @overload
    def setColor(self, arg0: 'Color') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setColor(java.awt.Color)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setColor(arg0))

    @overload
    def append(self, arg0: str) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.append(java.lang.String)"""
        return 'MutableText'.__wrap(super(__MutableText, self).append(arg0))

    @staticmethod
    @overload
    def literal(arg0: str) -> 'MutableText':
        """public static dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.TextObject.literal(java.lang.String)"""
        return MutableText.__wrap(__TextObject.literal(arg0))

    @overload
    def setFontWeight(self, arg0: 'FontWeight') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setFontWeight(dev.ultreon.libs.text.v0.FontWeight)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setFontWeight(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getWeight(self) -> float:
        """public float dev.ultreon.libs.text.v0.MutableText.getWeight()"""
        return float.__wrap(super(MutableText, self).getWeight())

    @override
    @overload
    def getText(self) -> str:
        """public final java.lang.String dev.ultreon.libs.text.v0.MutableText.getText()"""
        return str.__wrap(super(MutableText, self).getText())

    @override
    @overload
    def getAttrString(self) -> 'AttributedString':
        """public java.text.AttributedString dev.ultreon.libs.text.v0.MutableText.getAttrString()"""
        return 'AttributedString'.__wrap(super(MutableText, self).getAttrString())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setWidth(self, arg0: float) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setWidth(float)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setWidth(__float.valueOf(arg0)))

    @override
    @overload
    def getFontWidth(self) -> 'FontWidth':
        """public dev.ultreon.libs.text.v0.FontWidth dev.ultreon.libs.text.v0.MutableText.getFontWidth()"""
        return 'FontWidth'.__wrap(super(MutableText, self).getFontWidth())

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
    def translation(arg0: str, *arg1: object) -> 'MutableText':
        """public static dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.TextObject.translation(java.lang.String,java.lang.Object...)"""
        return MutableText.__wrap(__TextObject.translation(arg0, arg1))

    @override
    @overload
    def isStrikethrough(self) -> bool:
        """public boolean dev.ultreon.libs.text.v0.MutableText.isStrikethrough()"""
        return bool.__wrap(super(MutableText, self).isStrikethrough())

    @overload
    def setFontWidth(self, arg0: 'FontWidth') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setFontWidth(dev.ultreon.libs.text.v0.FontWidth)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setFontWidth(arg0))

    @override
    @overload
    def getSuperscript(self) -> int:
        """public int dev.ultreon.libs.text.v0.MutableText.getSuperscript()"""
        return int.__wrap(super(MutableText, self).getSuperscript())

    @override
    @overload
    def isUnderlined(self) -> bool:
        """public boolean dev.ultreon.libs.text.v0.MutableText.isUnderlined()"""
        return bool.__wrap(super(MutableText, self).isUnderlined())

    @override
    @overload
    def getSize(self) -> float:
        """public double dev.ultreon.libs.text.v0.MutableText.getSize()"""
        return float.__wrap(super(MutableText, self).getSize())

    @staticmethod
    @overload
    def nullToEmpty(arg0: str) -> 'TextObject':
        """public static dev.ultreon.libs.text.v0.TextObject dev.ultreon.libs.text.v0.TextObject.nullToEmpty(java.lang.String)"""
        return TextObject.__wrap(__TextObject.nullToEmpty(arg0))

    @overload
    def setStrikethrough(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setStrikethrough(boolean)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setStrikethrough(__boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def append(self, arg0: 'TextObject') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.append(dev.ultreon.libs.text.v0.TextObject)"""
        return 'MutableText'.__wrap(super(__MutableText, self).append(arg0))

 
 
 
# CLASS: dev.ultreon.libs.text.v0.LiteralText
import java.lang.Boolean as __boolean
from builtins import type
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.libs.text.v0.TextObject as __TextObject
__TextObject = __TextObject
import java.text.AttributedString as __AttributedString
__AttributedString = __AttributedString
import java.text.AttributedString as AttributedString
import java.awt.Color as __Color
__Color = __Color
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.libs.text.v0.FontWidth as __FontWidth
__FontWidth = __FontWidth
import dev.ultreon.libs.text.v0.LiteralText as __LiteralText
__LiteralText = __LiteralText
import java.lang.Double as __double
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
import dev.ultreon.libs.text.v0.MutableText as __MutableText
__MutableText = __MutableText
from builtins import object
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.awt.Color as Color
import dev.ultreon.libs.text.v0.FontWeight as __FontWeight
__FontWeight = __FontWeight
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import int
 
class LiteralText(__MutableText, MutableText):
    """dev.ultreon.libs.text.v0.LiteralText"""
 
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
 
    @overload
    def setFontWeight(self, arg0: int) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setFontWeight(int)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setFontWeight(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setSize(self, arg0: float) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setSize(double)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setSize(__double.valueOf(arg0)))

    @override
    @overload
    def getAttrs(self) -> 'Map':
        """public java.util.Map<? extends java.text.AttributedCharacterIterator$Attribute, ?> dev.ultreon.libs.text.v0.MutableText.getAttrs()"""
        return 'Map'.__wrap(super(MutableText, self).getAttrs())

    @override
    @overload
    def isLigaturesEnabled(self) -> bool:
        """public boolean dev.ultreon.libs.text.v0.MutableText.isLigaturesEnabled()"""
        return bool.__wrap(super(MutableText, self).isLigaturesEnabled())

    @overload
    def append(self, arg0: object) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.append(java.lang.Object)"""
        return 'MutableText'.__wrap(super(__MutableText, self).append(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getFontWeight(self) -> 'FontWeight':
        """public dev.ultreon.libs.text.v0.FontWeight dev.ultreon.libs.text.v0.MutableText.getFontWeight()"""
        return 'FontWeight'.__wrap(super(MutableText, self).getFontWeight())

    @overload
    def setLigaturesEnabled(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setLigaturesEnabled(boolean)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setLigaturesEnabled(__boolean.valueOf(arg0)))

    @override
    @overload
    def getWidth(self) -> float:
        """public float dev.ultreon.libs.text.v0.MutableText.getWidth()"""
        return float.__wrap(super(MutableText, self).getWidth())

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
    def setUnderlined(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setUnderlined(boolean)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setUnderlined(__boolean.valueOf(arg0)))

    @override
    @overload
    def getColor(self) -> 'Color':
        """public java.awt.Color dev.ultreon.libs.text.v0.MutableText.getColor()"""
        return 'Color'.__wrap(super(MutableText, self).getColor())

    @overload
    def setWeight(self, arg0: float) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setWeight(float)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setWeight(__float.valueOf(arg0)))

    @overload
    def setColor(self, arg0: 'Color') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setColor(java.awt.Color)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setColor(arg0))

    @overload
    def append(self, arg0: str) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.append(java.lang.String)"""
        return 'MutableText'.__wrap(super(__MutableText, self).append(arg0))

    @staticmethod
    @overload
    def literal(arg0: str) -> 'MutableText':
        """public static dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.TextObject.literal(java.lang.String)"""
        return MutableText.__wrap(__TextObject.literal(arg0))

    @overload
    def setFontWeight(self, arg0: 'FontWeight') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setFontWeight(dev.ultreon.libs.text.v0.FontWeight)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setFontWeight(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getWeight(self) -> float:
        """public float dev.ultreon.libs.text.v0.MutableText.getWeight()"""
        return float.__wrap(super(MutableText, self).getWeight())

    @override
    @overload
    def getText(self) -> str:
        """public final java.lang.String dev.ultreon.libs.text.v0.MutableText.getText()"""
        return str.__wrap(super(MutableText, self).getText())

    @override
    @overload
    def getAttrString(self) -> 'AttributedString':
        """public java.text.AttributedString dev.ultreon.libs.text.v0.MutableText.getAttrString()"""
        return 'AttributedString'.__wrap(super(MutableText, self).getAttrString())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setWidth(self, arg0: float) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setWidth(float)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setWidth(__float.valueOf(arg0)))

    @override
    @overload
    def getFontWidth(self) -> 'FontWidth':
        """public dev.ultreon.libs.text.v0.FontWidth dev.ultreon.libs.text.v0.MutableText.getFontWidth()"""
        return 'FontWidth'.__wrap(super(MutableText, self).getFontWidth())

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
    def translation(arg0: str, *arg1: object) -> 'MutableText':
        """public static dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.TextObject.translation(java.lang.String,java.lang.Object...)"""
        return MutableText.__wrap(__TextObject.translation(arg0, arg1))

    @override
    @overload
    def isStrikethrough(self) -> bool:
        """public boolean dev.ultreon.libs.text.v0.MutableText.isStrikethrough()"""
        return bool.__wrap(super(MutableText, self).isStrikethrough())

    @overload
    def setFontWidth(self, arg0: 'FontWidth') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setFontWidth(dev.ultreon.libs.text.v0.FontWidth)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setFontWidth(arg0))

    @override
    @overload
    def getSuperscript(self) -> int:
        """public int dev.ultreon.libs.text.v0.MutableText.getSuperscript()"""
        return int.__wrap(super(MutableText, self).getSuperscript())

    @override
    @overload
    def isUnderlined(self) -> bool:
        """public boolean dev.ultreon.libs.text.v0.MutableText.isUnderlined()"""
        return bool.__wrap(super(MutableText, self).isUnderlined())

    @override
    @overload
    def getSize(self) -> float:
        """public double dev.ultreon.libs.text.v0.MutableText.getSize()"""
        return float.__wrap(super(MutableText, self).getSize())

    @staticmethod
    @overload
    def nullToEmpty(arg0: str) -> 'TextObject':
        """public static dev.ultreon.libs.text.v0.TextObject dev.ultreon.libs.text.v0.TextObject.nullToEmpty(java.lang.String)"""
        return TextObject.__wrap(__TextObject.nullToEmpty(arg0))

    @overload
    def setStrikethrough(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setStrikethrough(boolean)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setStrikethrough(__boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def append(self, arg0: 'TextObject') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.append(dev.ultreon.libs.text.v0.TextObject)"""
        return 'MutableText'.__wrap(super(__MutableText, self).append(arg0))

 
 
 
# CLASS: dev.ultreon.libs.text.v0.LiteralText 
 
 
# CLASS: dev.ultreon.libs.text.v0.Translatable
from builtins import str
import java.lang.String as __String
__String = __String
import dev.ultreon.libs.text.v0.Translatable as __Translatable
__Translatable = __Translatable
import dev.ultreon.libs.text.v0.MutableText as __MutableText
__MutableText = __MutableText
from abc import abstractmethod, ABC
 
class Translatable(ABC):
    """dev.ultreon.libs.text.v0.Translatable"""
 
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
        """public default dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.Translatable.getTranslation()"""
        return 'MutableText'.__wrap(super(Translatable, self).getTranslation())

    @abstractmethod
    def getTranslationPath(self, ):
        """public abstract java.lang.String dev.ultreon.libs.text.v0.Translatable.getTranslationPath()"""
        pass

    @overload
    def getTranslationText(self) -> str:
        """public default java.lang.String dev.ultreon.libs.text.v0.Translatable.getTranslationText()"""
        return str.__wrap(super(Translatable, self).getTranslationText()) 
 
 
# CLASS: dev.ultreon.libs.text.v0.FontWeight
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from builtins import float
import java.util.Collection as Collection
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import dev.ultreon.libs.text.v0.FontWeight as __FontWeight
__FontWeight = __FontWeight
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class FontWeight(__Enum, Enum):
    """dev.ultreon.libs.text.v0.FontWeight"""
 
    @staticmethod
    def __wrap(java_value: __FontWeight) -> 'FontWeight':
        return FontWeight(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FontWeight):
        """
        Dynamic initializer for FontWeight.
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

    @staticmethod
    @overload
    def closestTo(arg0: float, arg1: 'Collection') -> 'FontWeight':
        """public static dev.ultreon.libs.text.v0.FontWeight dev.ultreon.libs.text.v0.FontWeight.closestTo(float,java.util.Collection<dev.ultreon.libs.text.v0.FontWeight>)"""
        return FontWeight.__wrap(__FontWeight.closestTo(__float.valueOf(arg0), arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getWeight(self) -> float:
        """public float dev.ultreon.libs.text.v0.FontWeight.getWeight()"""
        return float.__wrap(super(FontWeight, self).getWeight())

    @staticmethod
    @overload
    def values() -> List['FontWeight']:
        """public static dev.ultreon.libs.text.v0.FontWeight[] dev.ultreon.libs.text.v0.FontWeight.values()"""
        return List[FontWeight].__wrap(__FontWeight.values())

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
    def valueOf(arg0: str) -> 'FontWeight':
        """public static dev.ultreon.libs.text.v0.FontWeight dev.ultreon.libs.text.v0.FontWeight.valueOf(java.lang.String)"""
        return FontWeight.__wrap(__FontWeight.valueOf(arg0))

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
    def closestTo(arg0: float) -> 'FontWeight':
        """public static dev.ultreon.libs.text.v0.FontWeight dev.ultreon.libs.text.v0.FontWeight.closestTo(float)"""
        return FontWeight.__wrap(__FontWeight.closestTo(__float.valueOf(arg0))) 
 
 
# CLASS: dev.ultreon.libs.text.v0.TranslationText
import java.lang.Boolean as __boolean
from builtins import type
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.libs.text.v0.TextObject as __TextObject
__TextObject = __TextObject
import java.text.AttributedString as __AttributedString
__AttributedString = __AttributedString
import java.text.AttributedString as AttributedString
import java.awt.Color as __Color
__Color = __Color
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.libs.text.v0.FontWidth as __FontWidth
__FontWidth = __FontWidth
import java.lang.Double as __double
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
import dev.ultreon.libs.text.v0.MutableText as __MutableText
__MutableText = __MutableText
from builtins import object
import java.lang.Long as __long
import java.lang.Float as __float
import dev.ultreon.libs.text.v0.TranslationText as __TranslationText
__TranslationText = __TranslationText
import java.lang.String as __String
__String = __String
import java.awt.Color as Color
import dev.ultreon.libs.text.v0.FontWeight as __FontWeight
__FontWeight = __FontWeight
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import int
 
class TranslationText(__MutableText, MutableText):
    """dev.ultreon.libs.text.v0.TranslationText"""
 
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
 
    @overload
    def setFontWeight(self, arg0: int) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setFontWeight(int)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setFontWeight(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setSize(self, arg0: float) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setSize(double)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setSize(__double.valueOf(arg0)))

    @override
    @overload
    def getAttrs(self) -> 'Map':
        """public java.util.Map<? extends java.text.AttributedCharacterIterator$Attribute, ?> dev.ultreon.libs.text.v0.MutableText.getAttrs()"""
        return 'Map'.__wrap(super(MutableText, self).getAttrs())

    @override
    @overload
    def isLigaturesEnabled(self) -> bool:
        """public boolean dev.ultreon.libs.text.v0.MutableText.isLigaturesEnabled()"""
        return bool.__wrap(super(MutableText, self).isLigaturesEnabled())

    @overload
    def append(self, arg0: object) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.append(java.lang.Object)"""
        return 'MutableText'.__wrap(super(__MutableText, self).append(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getFontWeight(self) -> 'FontWeight':
        """public dev.ultreon.libs.text.v0.FontWeight dev.ultreon.libs.text.v0.MutableText.getFontWeight()"""
        return 'FontWeight'.__wrap(super(MutableText, self).getFontWeight())

    @overload
    def setLigaturesEnabled(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setLigaturesEnabled(boolean)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setLigaturesEnabled(__boolean.valueOf(arg0)))

    @override
    @overload
    def getWidth(self) -> float:
        """public float dev.ultreon.libs.text.v0.MutableText.getWidth()"""
        return float.__wrap(super(MutableText, self).getWidth())

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
    def setUnderlined(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setUnderlined(boolean)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setUnderlined(__boolean.valueOf(arg0)))

    @override
    @overload
    def getColor(self) -> 'Color':
        """public java.awt.Color dev.ultreon.libs.text.v0.MutableText.getColor()"""
        return 'Color'.__wrap(super(MutableText, self).getColor())

    @overload
    def setWeight(self, arg0: float) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setWeight(float)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setWeight(__float.valueOf(arg0)))

    @overload
    def setColor(self, arg0: 'Color') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setColor(java.awt.Color)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setColor(arg0))

    @overload
    def append(self, arg0: str) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.append(java.lang.String)"""
        return 'MutableText'.__wrap(super(__MutableText, self).append(arg0))

    @staticmethod
    @overload
    def literal(arg0: str) -> 'MutableText':
        """public static dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.TextObject.literal(java.lang.String)"""
        return MutableText.__wrap(__TextObject.literal(arg0))

    @overload
    def setFontWeight(self, arg0: 'FontWeight') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setFontWeight(dev.ultreon.libs.text.v0.FontWeight)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setFontWeight(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getWeight(self) -> float:
        """public float dev.ultreon.libs.text.v0.MutableText.getWeight()"""
        return float.__wrap(super(MutableText, self).getWeight())

    @override
    @overload
    def getText(self) -> str:
        """public final java.lang.String dev.ultreon.libs.text.v0.MutableText.getText()"""
        return str.__wrap(super(MutableText, self).getText())

    @override
    @overload
    def getAttrString(self) -> 'AttributedString':
        """public java.text.AttributedString dev.ultreon.libs.text.v0.MutableText.getAttrString()"""
        return 'AttributedString'.__wrap(super(MutableText, self).getAttrString())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setWidth(self, arg0: float) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setWidth(float)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setWidth(__float.valueOf(arg0)))

    @override
    @overload
    def getFontWidth(self) -> 'FontWidth':
        """public dev.ultreon.libs.text.v0.FontWidth dev.ultreon.libs.text.v0.MutableText.getFontWidth()"""
        return 'FontWidth'.__wrap(super(MutableText, self).getFontWidth())

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
    def translation(arg0: str, *arg1: object) -> 'MutableText':
        """public static dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.TextObject.translation(java.lang.String,java.lang.Object...)"""
        return MutableText.__wrap(__TextObject.translation(arg0, arg1))

    @override
    @overload
    def isStrikethrough(self) -> bool:
        """public boolean dev.ultreon.libs.text.v0.MutableText.isStrikethrough()"""
        return bool.__wrap(super(MutableText, self).isStrikethrough())

    @overload
    def setFontWidth(self, arg0: 'FontWidth') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setFontWidth(dev.ultreon.libs.text.v0.FontWidth)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setFontWidth(arg0))

    @override
    @overload
    def getSuperscript(self) -> int:
        """public int dev.ultreon.libs.text.v0.MutableText.getSuperscript()"""
        return int.__wrap(super(MutableText, self).getSuperscript())

    @override
    @overload
    def isUnderlined(self) -> bool:
        """public boolean dev.ultreon.libs.text.v0.MutableText.isUnderlined()"""
        return bool.__wrap(super(MutableText, self).isUnderlined())

    @override
    @overload
    def getSize(self) -> float:
        """public double dev.ultreon.libs.text.v0.MutableText.getSize()"""
        return float.__wrap(super(MutableText, self).getSize())

    @staticmethod
    @overload
    def nullToEmpty(arg0: str) -> 'TextObject':
        """public static dev.ultreon.libs.text.v0.TextObject dev.ultreon.libs.text.v0.TextObject.nullToEmpty(java.lang.String)"""
        return TextObject.__wrap(__TextObject.nullToEmpty(arg0))

    @overload
    def setStrikethrough(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setStrikethrough(boolean)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setStrikethrough(__boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def append(self, arg0: 'TextObject') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.append(dev.ultreon.libs.text.v0.TextObject)"""
        return 'MutableText'.__wrap(super(__MutableText, self).append(arg0)) 
 
 
# CLASS: dev.ultreon.libs.text.v0.MutableText
import java.lang.Boolean as __boolean
from builtins import type
import java.util.Map as __Map
__Map = __Map
import dev.ultreon.libs.text.v0.TextObject as __TextObject
__TextObject = __TextObject
import java.text.AttributedString as __AttributedString
__AttributedString = __AttributedString
import java.text.AttributedString as AttributedString
import java.awt.Color as __Color
__Color = __Color
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import dev.ultreon.libs.text.v0.FontWidth as __FontWidth
__FontWidth = __FontWidth
import java.lang.Double as __double
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
import dev.ultreon.libs.text.v0.MutableText as __MutableText
__MutableText = __MutableText
from builtins import object
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.awt.Color as Color
import dev.ultreon.libs.text.v0.FontWeight as __FontWeight
__FontWeight = __FontWeight
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import int
 
class MutableText(ABC, __TextObject, TextObject):
    """dev.ultreon.libs.text.v0.MutableText"""
 
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
 
    @overload
    def setFontWeight(self, arg0: int) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setFontWeight(int)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setFontWeight(__int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setSize(self, arg0: float) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setSize(double)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setSize(__double.valueOf(arg0)))

    @overload
    def getSuperscript(self) -> int:
        """public int dev.ultreon.libs.text.v0.MutableText.getSuperscript()"""
        return int.__wrap(super(MutableText, self).getSuperscript())

    @overload
    def append(self, arg0: object) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.append(java.lang.Object)"""
        return 'MutableText'.__wrap(super(__MutableText, self).append(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.text.v0.MutableText()"""
        val = __MutableText()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getColor(self) -> 'Color':
        """public java.awt.Color dev.ultreon.libs.text.v0.MutableText.getColor()"""
        return 'Color'.__wrap(super(MutableText, self).getColor())

    @overload
    def isStrikethrough(self) -> bool:
        """public boolean dev.ultreon.libs.text.v0.MutableText.isStrikethrough()"""
        return bool.__wrap(super(MutableText, self).isStrikethrough())

    @overload
    def setLigaturesEnabled(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setLigaturesEnabled(boolean)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setLigaturesEnabled(__boolean.valueOf(arg0)))

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
    def setUnderlined(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setUnderlined(boolean)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setUnderlined(__boolean.valueOf(arg0)))

    @overload
    def setWeight(self, arg0: float) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setWeight(float)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setWeight(__float.valueOf(arg0)))

    @overload
    def setColor(self, arg0: 'Color') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setColor(java.awt.Color)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setColor(arg0))

    @overload
    def append(self, arg0: str) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.append(java.lang.String)"""
        return 'MutableText'.__wrap(super(__MutableText, self).append(arg0))

    @overload
    def isLigaturesEnabled(self) -> bool:
        """public boolean dev.ultreon.libs.text.v0.MutableText.isLigaturesEnabled()"""
        return bool.__wrap(super(MutableText, self).isLigaturesEnabled())

    @staticmethod
    @overload
    def literal(arg0: str) -> 'MutableText':
        """public static dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.TextObject.literal(java.lang.String)"""
        return MutableText.__wrap(__TextObject.literal(arg0))

    @overload
    def setFontWeight(self, arg0: 'FontWeight') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setFontWeight(dev.ultreon.libs.text.v0.FontWeight)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setFontWeight(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getSize(self) -> float:
        """public double dev.ultreon.libs.text.v0.MutableText.getSize()"""
        return float.__wrap(super(MutableText, self).getSize())

    @override
    @overload
    def getText(self) -> str:
        """public final java.lang.String dev.ultreon.libs.text.v0.MutableText.getText()"""
        return str.__wrap(super(MutableText, self).getText())

    @overload
    def getFontWeight(self) -> 'FontWeight':
        """public dev.ultreon.libs.text.v0.FontWeight dev.ultreon.libs.text.v0.MutableText.getFontWeight()"""
        return 'FontWeight'.__wrap(super(MutableText, self).getFontWeight())

    @override
    @overload
    def getAttrString(self) -> 'AttributedString':
        """public java.text.AttributedString dev.ultreon.libs.text.v0.MutableText.getAttrString()"""
        return 'AttributedString'.__wrap(super(MutableText, self).getAttrString())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.libs.text.v0.MutableText()"""
        val = __MutableText()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setWidth(self, arg0: float) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setWidth(float)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setWidth(__float.valueOf(arg0)))

    @overload
    def getFontWidth(self) -> 'FontWidth':
        """public dev.ultreon.libs.text.v0.FontWidth dev.ultreon.libs.text.v0.MutableText.getFontWidth()"""
        return 'FontWidth'.__wrap(super(MutableText, self).getFontWidth())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getWidth(self) -> float:
        """public float dev.ultreon.libs.text.v0.MutableText.getWidth()"""
        return float.__wrap(super(MutableText, self).getWidth())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def translation(arg0: str, *arg1: object) -> 'MutableText':
        """public static dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.TextObject.translation(java.lang.String,java.lang.Object...)"""
        return MutableText.__wrap(__TextObject.translation(arg0, arg1))

    @overload
    def setFontWidth(self, arg0: 'FontWidth') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setFontWidth(dev.ultreon.libs.text.v0.FontWidth)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setFontWidth(arg0))

    @overload
    def getAttrs(self) -> 'Map':
        """public java.util.Map<? extends java.text.AttributedCharacterIterator$Attribute, ?> dev.ultreon.libs.text.v0.MutableText.getAttrs()"""
        return 'Map'.__wrap(super(MutableText, self).getAttrs())

    @overload
    def isUnderlined(self) -> bool:
        """public boolean dev.ultreon.libs.text.v0.MutableText.isUnderlined()"""
        return bool.__wrap(super(MutableText, self).isUnderlined())

    @staticmethod
    @overload
    def nullToEmpty(arg0: str) -> 'TextObject':
        """public static dev.ultreon.libs.text.v0.TextObject dev.ultreon.libs.text.v0.TextObject.nullToEmpty(java.lang.String)"""
        return TextObject.__wrap(__TextObject.nullToEmpty(arg0))

    @overload
    def setStrikethrough(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setStrikethrough(boolean)"""
        return 'MutableText'.__wrap(super(__MutableText, self).setStrikethrough(__boolean.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def append(self, arg0: 'TextObject') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.append(dev.ultreon.libs.text.v0.TextObject)"""
        return 'MutableText'.__wrap(super(__MutableText, self).append(arg0))

    @overload
    def getWeight(self) -> float:
        """public float dev.ultreon.libs.text.v0.MutableText.getWeight()"""
        return float.__wrap(super(MutableText, self).getWeight()) 
 
 
# CLASS: dev.ultreon.libs.text.v0.TextObject
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.libs.text.v0.TextObject as __TextObject
__TextObject = __TextObject
import dev.ultreon.libs.text.v0.MutableText as __MutableText
__MutableText = __MutableText
from builtins import object
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TextObject(ABC):
    """dev.ultreon.libs.text.v0.TextObject"""
 
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
    def getText(self) -> str:
        """public java.lang.String dev.ultreon.libs.text.v0.TextObject.getText()"""
        return str.__wrap(super(TextObject, self).getText())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.text.v0.TextObject()"""
        val = __TextObject()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def translation(arg0: str, *arg1: object) -> 'MutableText':
        """public static dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.TextObject.translation(java.lang.String,java.lang.Object...)"""
        return MutableText.__wrap(__TextObject.translation(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public dev.ultreon.libs.text.v0.TextObject()"""
        val = __TextObject()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def nullToEmpty(arg0: str) -> 'TextObject':
        """public static dev.ultreon.libs.text.v0.TextObject dev.ultreon.libs.text.v0.TextObject.nullToEmpty(java.lang.String)"""
        return TextObject.__wrap(__TextObject.nullToEmpty(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def literal(arg0: str) -> 'MutableText':
        """public static dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.TextObject.literal(java.lang.String)"""
        return MutableText.__wrap(__TextObject.literal(arg0))

    @abstractmethod
    def getAttrString(self, ):
        """public abstract java.text.AttributedString dev.ultreon.libs.text.v0.TextObject.getAttrString()"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.libs.text.v0.FontWidth
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from builtins import float
import java.util.Collection as Collection
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import dev.ultreon.libs.text.v0.FontWidth as __FontWidth
__FontWidth = __FontWidth
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
 
class FontWidth(__Enum, Enum):
    """dev.ultreon.libs.text.v0.FontWidth"""
 
    @staticmethod
    def __wrap(java_value: __FontWidth) -> 'FontWidth':
        return FontWidth(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FontWidth):
        """
        Dynamic initializer for FontWidth.
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'FontWidth':
        """public static dev.ultreon.libs.text.v0.FontWidth dev.ultreon.libs.text.v0.FontWidth.valueOf(java.lang.String)"""
        return FontWidth.__wrap(__FontWidth.valueOf(arg0))

    @staticmethod
    @overload
    def closestTo(arg0: float, arg1: 'Collection') -> 'FontWidth':
        """public static dev.ultreon.libs.text.v0.FontWidth dev.ultreon.libs.text.v0.FontWidth.closestTo(float,java.util.Collection<dev.ultreon.libs.text.v0.FontWidth>)"""
        return FontWidth.__wrap(__FontWidth.closestTo(__float.valueOf(arg0), arg1))

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
    def closestTo(arg0: float) -> 'FontWidth':
        """public static dev.ultreon.libs.text.v0.FontWidth dev.ultreon.libs.text.v0.FontWidth.closestTo(float)"""
        return FontWidth.__wrap(__FontWidth.closestTo(__float.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @overload
    def getWidth(self) -> float:
        """public float dev.ultreon.libs.text.v0.FontWidth.getWidth()"""
        return float.__wrap(super(FontWidth, self).getWidth())

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
    def values() -> List['FontWidth']:
        """public static dev.ultreon.libs.text.v0.FontWidth[] dev.ultreon.libs.text.v0.FontWidth.values()"""
        return List[FontWidth].__wrap(__FontWidth.values())