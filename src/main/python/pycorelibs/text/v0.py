from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
from typing import List
import dev.ultreon.libs.text.v0.FontWidth as _FontWidth
_FontWidth = _FontWidth
import java.lang.Float as _float
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
 
class FontWidth():
    """dev.ultreon.libs.text.v0.FontWidth"""
 
    @staticmethod
    def _wrap(java_value: _FontWidth) -> 'FontWidth':
        return FontWidth(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FontWidth):
        """
        Dynamic initializer for FontWidth.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FontWidth__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FontWidth__wrapper":
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
    def values() -> List['FontWidth']:
        """public static dev.ultreon.libs.text.v0.FontWidth[] dev.ultreon.libs.text.v0.FontWidth.values()"""
        return List[FontWidth]._wrap(_FontWidth.values())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'FontWidth':
        """public static dev.ultreon.libs.text.v0.FontWidth dev.ultreon.libs.text.v0.FontWidth.valueOf(java.lang.String)"""
        return FontWidth._wrap(_FontWidth.valueOf(arg0))

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
    def getWidth(self) -> float:
        """public float dev.ultreon.libs.text.v0.FontWidth.getWidth()"""
        return float._wrap(super(FontWidth, self).getWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @staticmethod
    @overload
    def closestTo(arg0: float, arg1: 'Collection') -> 'FontWidth':
        """public static dev.ultreon.libs.text.v0.FontWidth dev.ultreon.libs.text.v0.FontWidth.closestTo(float,java.util.Collection<dev.ultreon.libs.text.v0.FontWidth>)"""
        return FontWidth._wrap(_FontWidth.closestTo(_float.valueOf(arg0), arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @staticmethod
    @overload
    def closestTo(arg0: float) -> 'FontWidth':
        """public static dev.ultreon.libs.text.v0.FontWidth dev.ultreon.libs.text.v0.FontWidth.closestTo(float)"""
        return FontWidth._wrap(_FontWidth.closestTo(_float.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: dev.ultreon.libs.text.v0.FontWidth
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
from typing import List
import dev.ultreon.libs.text.v0.FontWidth as _FontWidth
_FontWidth = _FontWidth
import java.lang.Float as _float
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
 
class FontWidth():
    """dev.ultreon.libs.text.v0.FontWidth"""
 
    @staticmethod
    def _wrap(java_value: _FontWidth) -> 'FontWidth':
        return FontWidth(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FontWidth):
        """
        Dynamic initializer for FontWidth.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FontWidth__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FontWidth__wrapper":
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
    def values() -> List['FontWidth']:
        """public static dev.ultreon.libs.text.v0.FontWidth[] dev.ultreon.libs.text.v0.FontWidth.values()"""
        return List[FontWidth]._wrap(_FontWidth.values())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'FontWidth':
        """public static dev.ultreon.libs.text.v0.FontWidth dev.ultreon.libs.text.v0.FontWidth.valueOf(java.lang.String)"""
        return FontWidth._wrap(_FontWidth.valueOf(arg0))

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
    def getWidth(self) -> float:
        """public float dev.ultreon.libs.text.v0.FontWidth.getWidth()"""
        return float._wrap(super(FontWidth, self).getWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @staticmethod
    @overload
    def closestTo(arg0: float, arg1: 'Collection') -> 'FontWidth':
        """public static dev.ultreon.libs.text.v0.FontWidth dev.ultreon.libs.text.v0.FontWidth.closestTo(float,java.util.Collection<dev.ultreon.libs.text.v0.FontWidth>)"""
        return FontWidth._wrap(_FontWidth.closestTo(_float.valueOf(arg0), arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @staticmethod
    @overload
    def closestTo(arg0: float) -> 'FontWidth':
        """public static dev.ultreon.libs.text.v0.FontWidth dev.ultreon.libs.text.v0.FontWidth.closestTo(float)"""
        return FontWidth._wrap(_FontWidth.closestTo(_float.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: dev.ultreon.libs.text.v0.FontWidth 
 
 
# CLASS: dev.ultreon.libs.text.v0.FontWeight
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Float as _float
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
import dev.ultreon.libs.text.v0.FontWeight as _FontWeight
_FontWeight = _FontWeight
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FontWeight():
    """dev.ultreon.libs.text.v0.FontWeight"""
 
    @staticmethod
    def _wrap(java_value: _FontWeight) -> 'FontWeight':
        return FontWeight(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FontWeight):
        """
        Dynamic initializer for FontWeight.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FontWeight__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FontWeight__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def closestTo(arg0: float, arg1: 'Collection') -> 'FontWeight':
        """public static dev.ultreon.libs.text.v0.FontWeight dev.ultreon.libs.text.v0.FontWeight.closestTo(float,java.util.Collection<dev.ultreon.libs.text.v0.FontWeight>)"""
        return FontWeight._wrap(_FontWeight.closestTo(_float.valueOf(arg0), arg1))

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

    @overload
    def getWeight(self) -> float:
        """public float dev.ultreon.libs.text.v0.FontWeight.getWeight()"""
        return float._wrap(super(FontWeight, self).getWeight())

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

    @staticmethod
    @overload
    def values() -> List['FontWeight']:
        """public static dev.ultreon.libs.text.v0.FontWeight[] dev.ultreon.libs.text.v0.FontWeight.values()"""
        return List[FontWeight]._wrap(_FontWeight.values())

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
    def closestTo(arg0: float) -> 'FontWeight':
        """public static dev.ultreon.libs.text.v0.FontWeight dev.ultreon.libs.text.v0.FontWeight.closestTo(float)"""
        return FontWeight._wrap(_FontWeight.closestTo(_float.valueOf(arg0)))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'FontWeight':
        """public static dev.ultreon.libs.text.v0.FontWeight dev.ultreon.libs.text.v0.FontWeight.valueOf(java.lang.String)"""
        return FontWeight._wrap(_FontWeight.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.libs.text.v0.LiteralText
import java.lang.Double as _double
import java.text.AttributedString as _AttributedString
_AttributedString = _AttributedString
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.libs.text.v0.LiteralText as _LiteralText
_LiteralText = _LiteralText
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.text.AttributedString as AttributedString
import java.lang.String as _string
import java.lang.Boolean as _boolean
import dev.ultreon.libs.text.v0.TextObject as _TextObject
_TextObject = _TextObject
import dev.ultreon.libs.text.v0.FontWeight as _FontWeight
_FontWeight = _FontWeight
import dev.ultreon.libs.text.v0.MutableText as _MutableText
_MutableText = _MutableText
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.Float as _float
import dev.ultreon.libs.text.v0.FontWidth as _FontWidth
_FontWidth = _FontWidth
import java.lang.Integer as _int
import java.awt.Color as Color
import java.awt.Color as _Color
_Color = _Color
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LiteralText():
    """dev.ultreon.libs.text.v0.LiteralText"""
 
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
 
    @override
    @overload
    def getWeight(self) -> float:
        """public float dev.ultreon.libs.text.v0.MutableText.getWeight()"""
        return float._wrap(super(MutableText, self).getWeight())

    @overload
    def setLigaturesEnabled(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setLigaturesEnabled(boolean)"""
        return 'MutableText'._wrap(super(_MutableText, self).setLigaturesEnabled(_boolean.valueOf(arg0)))

    @override
    @overload
    def isLigaturesEnabled(self) -> bool:
        """public boolean dev.ultreon.libs.text.v0.MutableText.isLigaturesEnabled()"""
        return bool._wrap(super(MutableText, self).isLigaturesEnabled())

    @overload
    def append(self, arg0: 'TextObject') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.append(dev.ultreon.libs.text.v0.TextObject)"""
        return 'MutableText'._wrap(super(_MutableText, self).append(arg0))

    @overload
    def setUnderlined(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setUnderlined(boolean)"""
        return 'MutableText'._wrap(super(_MutableText, self).setUnderlined(_boolean.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def append(self, arg0: object) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.append(java.lang.Object)"""
        return 'MutableText'._wrap(super(_MutableText, self).append(arg0))

    @override
    @overload
    def getWidth(self) -> float:
        """public float dev.ultreon.libs.text.v0.MutableText.getWidth()"""
        return float._wrap(super(MutableText, self).getWidth())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setSize(self, arg0: float) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setSize(double)"""
        return 'MutableText'._wrap(super(_MutableText, self).setSize(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def translation(arg0: str, *arg1: object) -> 'MutableText':
        """public static dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.TextObject.translation(java.lang.String,java.lang.Object...)"""
        return MutableText._wrap(_TextObject.translation(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getFontWeight(self) -> 'FontWeight':
        """public dev.ultreon.libs.text.v0.FontWeight dev.ultreon.libs.text.v0.MutableText.getFontWeight()"""
        return 'FontWeight'._wrap(super(MutableText, self).getFontWeight())

    @override
    @overload
    def getSize(self) -> float:
        """public double dev.ultreon.libs.text.v0.MutableText.getSize()"""
        return float._wrap(super(MutableText, self).getSize())

    @staticmethod
    @overload
    def literal(arg0: str) -> 'MutableText':
        """public static dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.TextObject.literal(java.lang.String)"""
        return MutableText._wrap(_TextObject.literal(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getFontWidth(self) -> 'FontWidth':
        """public dev.ultreon.libs.text.v0.FontWidth dev.ultreon.libs.text.v0.MutableText.getFontWidth()"""
        return 'FontWidth'._wrap(super(MutableText, self).getFontWidth())

    @override
    @overload
    def isStrikethrough(self) -> bool:
        """public boolean dev.ultreon.libs.text.v0.MutableText.isStrikethrough()"""
        return bool._wrap(super(MutableText, self).isStrikethrough())

    @overload
    def setFontWidth(self, arg0: 'FontWidth') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setFontWidth(dev.ultreon.libs.text.v0.FontWidth)"""
        return 'MutableText'._wrap(super(_MutableText, self).setFontWidth(arg0))

    @overload
    def append(self, arg0: str) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.append(java.lang.String)"""
        return 'MutableText'._wrap(super(_MutableText, self).append(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setFontWeight(self, arg0: 'FontWeight') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setFontWeight(dev.ultreon.libs.text.v0.FontWeight)"""
        return 'MutableText'._wrap(super(_MutableText, self).setFontWeight(arg0))

    @overload
    def setStrikethrough(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setStrikethrough(boolean)"""
        return 'MutableText'._wrap(super(_MutableText, self).setStrikethrough(_boolean.valueOf(arg0)))

    @override
    @overload
    def getAttrs(self) -> 'Map':
        """public java.util.Map<? extends java.text.AttributedCharacterIterator$Attribute, ?> dev.ultreon.libs.text.v0.MutableText.getAttrs()"""
        return 'Map'._wrap(super(MutableText, self).getAttrs())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def isUnderlined(self) -> bool:
        """public boolean dev.ultreon.libs.text.v0.MutableText.isUnderlined()"""
        return bool._wrap(super(MutableText, self).isUnderlined())

    @overload
    def setWeight(self, arg0: float) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setWeight(float)"""
        return 'MutableText'._wrap(super(_MutableText, self).setWeight(_float.valueOf(arg0)))

    @overload
    def setWidth(self, arg0: float) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setWidth(float)"""
        return 'MutableText'._wrap(super(_MutableText, self).setWidth(_float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getSuperscript(self) -> int:
        """public int dev.ultreon.libs.text.v0.MutableText.getSuperscript()"""
        return int._wrap(super(MutableText, self).getSuperscript())

    @override
    @overload
    def getText(self) -> str:
        """public final java.lang.String dev.ultreon.libs.text.v0.MutableText.getText()"""
        return str._wrap(super(MutableText, self).getText())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getAttrString(self) -> 'AttributedString':
        """public java.text.AttributedString dev.ultreon.libs.text.v0.MutableText.getAttrString()"""
        return 'AttributedString'._wrap(super(MutableText, self).getAttrString())

    @overload
    def setFontWeight(self, arg0: int) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setFontWeight(int)"""
        return 'MutableText'._wrap(super(_MutableText, self).setFontWeight(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nullToEmpty(arg0: str) -> 'TextObject':
        """public static dev.ultreon.libs.text.v0.TextObject dev.ultreon.libs.text.v0.TextObject.nullToEmpty(java.lang.String)"""
        return TextObject._wrap(_TextObject.nullToEmpty(arg0))

    @overload
    def setColor(self, arg0: 'Color') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setColor(java.awt.Color)"""
        return 'MutableText'._wrap(super(_MutableText, self).setColor(arg0))

    @override
    @overload
    def getColor(self) -> 'Color':
        """public java.awt.Color dev.ultreon.libs.text.v0.MutableText.getColor()"""
        return 'Color'._wrap(super(MutableText, self).getColor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.libs.text.v0.TranslationText
import java.lang.Double as _double
import java.text.AttributedString as _AttributedString
_AttributedString = _AttributedString
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import dev.ultreon.libs.text.v0.TranslationText as _TranslationText
_TranslationText = _TranslationText
import java.util.Map as _Map
_Map = _Map
import java.text.AttributedString as AttributedString
import java.lang.String as _string
import java.lang.Boolean as _boolean
import dev.ultreon.libs.text.v0.TextObject as _TextObject
_TextObject = _TextObject
import dev.ultreon.libs.text.v0.FontWeight as _FontWeight
_FontWeight = _FontWeight
import dev.ultreon.libs.text.v0.MutableText as _MutableText
_MutableText = _MutableText
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.Float as _float
import dev.ultreon.libs.text.v0.FontWidth as _FontWidth
_FontWidth = _FontWidth
import java.lang.Integer as _int
import java.awt.Color as Color
import java.awt.Color as _Color
_Color = _Color
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TranslationText():
    """dev.ultreon.libs.text.v0.TranslationText"""
 
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
 
    @override
    @overload
    def getWeight(self) -> float:
        """public float dev.ultreon.libs.text.v0.MutableText.getWeight()"""
        return float._wrap(super(MutableText, self).getWeight())

    @overload
    def setLigaturesEnabled(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setLigaturesEnabled(boolean)"""
        return 'MutableText'._wrap(super(_MutableText, self).setLigaturesEnabled(_boolean.valueOf(arg0)))

    @override
    @overload
    def isLigaturesEnabled(self) -> bool:
        """public boolean dev.ultreon.libs.text.v0.MutableText.isLigaturesEnabled()"""
        return bool._wrap(super(MutableText, self).isLigaturesEnabled())

    @overload
    def append(self, arg0: 'TextObject') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.append(dev.ultreon.libs.text.v0.TextObject)"""
        return 'MutableText'._wrap(super(_MutableText, self).append(arg0))

    @overload
    def setUnderlined(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setUnderlined(boolean)"""
        return 'MutableText'._wrap(super(_MutableText, self).setUnderlined(_boolean.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def append(self, arg0: object) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.append(java.lang.Object)"""
        return 'MutableText'._wrap(super(_MutableText, self).append(arg0))

    @override
    @overload
    def getWidth(self) -> float:
        """public float dev.ultreon.libs.text.v0.MutableText.getWidth()"""
        return float._wrap(super(MutableText, self).getWidth())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setSize(self, arg0: float) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setSize(double)"""
        return 'MutableText'._wrap(super(_MutableText, self).setSize(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def translation(arg0: str, *arg1: object) -> 'MutableText':
        """public static dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.TextObject.translation(java.lang.String,java.lang.Object...)"""
        return MutableText._wrap(_TextObject.translation(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getFontWeight(self) -> 'FontWeight':
        """public dev.ultreon.libs.text.v0.FontWeight dev.ultreon.libs.text.v0.MutableText.getFontWeight()"""
        return 'FontWeight'._wrap(super(MutableText, self).getFontWeight())

    @override
    @overload
    def getSize(self) -> float:
        """public double dev.ultreon.libs.text.v0.MutableText.getSize()"""
        return float._wrap(super(MutableText, self).getSize())

    @staticmethod
    @overload
    def literal(arg0: str) -> 'MutableText':
        """public static dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.TextObject.literal(java.lang.String)"""
        return MutableText._wrap(_TextObject.literal(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def getFontWidth(self) -> 'FontWidth':
        """public dev.ultreon.libs.text.v0.FontWidth dev.ultreon.libs.text.v0.MutableText.getFontWidth()"""
        return 'FontWidth'._wrap(super(MutableText, self).getFontWidth())

    @override
    @overload
    def isStrikethrough(self) -> bool:
        """public boolean dev.ultreon.libs.text.v0.MutableText.isStrikethrough()"""
        return bool._wrap(super(MutableText, self).isStrikethrough())

    @overload
    def setFontWidth(self, arg0: 'FontWidth') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setFontWidth(dev.ultreon.libs.text.v0.FontWidth)"""
        return 'MutableText'._wrap(super(_MutableText, self).setFontWidth(arg0))

    @overload
    def append(self, arg0: str) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.append(java.lang.String)"""
        return 'MutableText'._wrap(super(_MutableText, self).append(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setFontWeight(self, arg0: 'FontWeight') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setFontWeight(dev.ultreon.libs.text.v0.FontWeight)"""
        return 'MutableText'._wrap(super(_MutableText, self).setFontWeight(arg0))

    @overload
    def setStrikethrough(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setStrikethrough(boolean)"""
        return 'MutableText'._wrap(super(_MutableText, self).setStrikethrough(_boolean.valueOf(arg0)))

    @override
    @overload
    def getAttrs(self) -> 'Map':
        """public java.util.Map<? extends java.text.AttributedCharacterIterator$Attribute, ?> dev.ultreon.libs.text.v0.MutableText.getAttrs()"""
        return 'Map'._wrap(super(MutableText, self).getAttrs())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def isUnderlined(self) -> bool:
        """public boolean dev.ultreon.libs.text.v0.MutableText.isUnderlined()"""
        return bool._wrap(super(MutableText, self).isUnderlined())

    @overload
    def setWeight(self, arg0: float) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setWeight(float)"""
        return 'MutableText'._wrap(super(_MutableText, self).setWeight(_float.valueOf(arg0)))

    @overload
    def setWidth(self, arg0: float) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setWidth(float)"""
        return 'MutableText'._wrap(super(_MutableText, self).setWidth(_float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getSuperscript(self) -> int:
        """public int dev.ultreon.libs.text.v0.MutableText.getSuperscript()"""
        return int._wrap(super(MutableText, self).getSuperscript())

    @override
    @overload
    def getText(self) -> str:
        """public final java.lang.String dev.ultreon.libs.text.v0.MutableText.getText()"""
        return str._wrap(super(MutableText, self).getText())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getAttrString(self) -> 'AttributedString':
        """public java.text.AttributedString dev.ultreon.libs.text.v0.MutableText.getAttrString()"""
        return 'AttributedString'._wrap(super(MutableText, self).getAttrString())

    @overload
    def setFontWeight(self, arg0: int) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setFontWeight(int)"""
        return 'MutableText'._wrap(super(_MutableText, self).setFontWeight(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nullToEmpty(arg0: str) -> 'TextObject':
        """public static dev.ultreon.libs.text.v0.TextObject dev.ultreon.libs.text.v0.TextObject.nullToEmpty(java.lang.String)"""
        return TextObject._wrap(_TextObject.nullToEmpty(arg0))

    @overload
    def setColor(self, arg0: 'Color') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setColor(java.awt.Color)"""
        return 'MutableText'._wrap(super(_MutableText, self).setColor(arg0))

    @override
    @overload
    def getColor(self) -> 'Color':
        """public java.awt.Color dev.ultreon.libs.text.v0.MutableText.getColor()"""
        return 'Color'._wrap(super(MutableText, self).getColor())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.libs.text.v0.MutableText
import java.lang.Double as _double
import java.text.AttributedString as _AttributedString
_AttributedString = _AttributedString
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.text.AttributedString as AttributedString
import java.lang.String as _string
import java.lang.Boolean as _boolean
import dev.ultreon.libs.text.v0.TextObject as _TextObject
_TextObject = _TextObject
import dev.ultreon.libs.text.v0.FontWeight as _FontWeight
_FontWeight = _FontWeight
import dev.ultreon.libs.text.v0.MutableText as _MutableText
_MutableText = _MutableText
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.Float as _float
import dev.ultreon.libs.text.v0.FontWidth as _FontWidth
_FontWidth = _FontWidth
import java.lang.Integer as _int
import java.awt.Color as Color
import java.awt.Color as _Color
_Color = _Color
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MutableText():
    """dev.ultreon.libs.text.v0.MutableText"""
 
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
 
    @overload
    def setLigaturesEnabled(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setLigaturesEnabled(boolean)"""
        return 'MutableText'._wrap(super(_MutableText, self).setLigaturesEnabled(_boolean.valueOf(arg0)))

    @overload
    def getFontWidth(self) -> 'FontWidth':
        """public dev.ultreon.libs.text.v0.FontWidth dev.ultreon.libs.text.v0.MutableText.getFontWidth()"""
        return 'FontWidth'._wrap(super(MutableText, self).getFontWidth())

    @overload
    def append(self, arg0: 'TextObject') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.append(dev.ultreon.libs.text.v0.TextObject)"""
        return 'MutableText'._wrap(super(_MutableText, self).append(arg0))

    @overload
    def isStrikethrough(self) -> bool:
        """public boolean dev.ultreon.libs.text.v0.MutableText.isStrikethrough()"""
        return bool._wrap(super(MutableText, self).isStrikethrough())

    @overload
    def setUnderlined(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setUnderlined(boolean)"""
        return 'MutableText'._wrap(super(_MutableText, self).setUnderlined(_boolean.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getWeight(self) -> float:
        """public float dev.ultreon.libs.text.v0.MutableText.getWeight()"""
        return float._wrap(super(MutableText, self).getWeight())

    @overload
    def getFontWeight(self) -> 'FontWeight':
        """public dev.ultreon.libs.text.v0.FontWeight dev.ultreon.libs.text.v0.MutableText.getFontWeight()"""
        return 'FontWeight'._wrap(super(MutableText, self).getFontWeight())

    @overload
    def append(self, arg0: object) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.append(java.lang.Object)"""
        return 'MutableText'._wrap(super(_MutableText, self).append(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setSize(self, arg0: float) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setSize(double)"""
        return 'MutableText'._wrap(super(_MutableText, self).setSize(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def translation(arg0: str, *arg1: object) -> 'MutableText':
        """public static dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.TextObject.translation(java.lang.String,java.lang.Object...)"""
        return MutableText._wrap(_TextObject.translation(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getWidth(self) -> float:
        """public float dev.ultreon.libs.text.v0.MutableText.getWidth()"""
        return float._wrap(super(MutableText, self).getWidth())

    @staticmethod
    @overload
    def literal(arg0: str) -> 'MutableText':
        """public static dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.TextObject.literal(java.lang.String)"""
        return MutableText._wrap(_TextObject.literal(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.text.v0.MutableText()"""
        val = _MutableText()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def isUnderlined(self) -> bool:
        """public boolean dev.ultreon.libs.text.v0.MutableText.isUnderlined()"""
        return bool._wrap(super(MutableText, self).isUnderlined())

    @overload
    def setFontWidth(self, arg0: 'FontWidth') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setFontWidth(dev.ultreon.libs.text.v0.FontWidth)"""
        return 'MutableText'._wrap(super(_MutableText, self).setFontWidth(arg0))

    @overload
    def append(self, arg0: str) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.append(java.lang.String)"""
        return 'MutableText'._wrap(super(_MutableText, self).append(arg0))

    @overload
    def getSize(self) -> float:
        """public double dev.ultreon.libs.text.v0.MutableText.getSize()"""
        return float._wrap(super(MutableText, self).getSize())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getAttrs(self) -> 'Map':
        """public java.util.Map<? extends java.text.AttributedCharacterIterator$Attribute, ?> dev.ultreon.libs.text.v0.MutableText.getAttrs()"""
        return 'Map'._wrap(super(MutableText, self).getAttrs())

    @overload
    def getSuperscript(self) -> int:
        """public int dev.ultreon.libs.text.v0.MutableText.getSuperscript()"""
        return int._wrap(super(MutableText, self).getSuperscript())

    @overload
    def setFontWeight(self, arg0: 'FontWeight') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setFontWeight(dev.ultreon.libs.text.v0.FontWeight)"""
        return 'MutableText'._wrap(super(_MutableText, self).setFontWeight(arg0))

    @overload
    def setStrikethrough(self, arg0: bool) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setStrikethrough(boolean)"""
        return 'MutableText'._wrap(super(_MutableText, self).setStrikethrough(_boolean.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getColor(self) -> 'Color':
        """public java.awt.Color dev.ultreon.libs.text.v0.MutableText.getColor()"""
        return 'Color'._wrap(super(MutableText, self).getColor())

    @overload
    def setWeight(self, arg0: float) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setWeight(float)"""
        return 'MutableText'._wrap(super(_MutableText, self).setWeight(_float.valueOf(arg0)))

    @overload
    def setWidth(self, arg0: float) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setWidth(float)"""
        return 'MutableText'._wrap(super(_MutableText, self).setWidth(_float.valueOf(arg0)))

    @overload
    def __init__(self):
        """public dev.ultreon.libs.text.v0.MutableText()"""
        val = _MutableText()
        self.__wrapper = val

    @overload
    def isLigaturesEnabled(self) -> bool:
        """public boolean dev.ultreon.libs.text.v0.MutableText.isLigaturesEnabled()"""
        return bool._wrap(super(MutableText, self).isLigaturesEnabled())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getText(self) -> str:
        """public final java.lang.String dev.ultreon.libs.text.v0.MutableText.getText()"""
        return str._wrap(super(MutableText, self).getText())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getAttrString(self) -> 'AttributedString':
        """public java.text.AttributedString dev.ultreon.libs.text.v0.MutableText.getAttrString()"""
        return 'AttributedString'._wrap(super(MutableText, self).getAttrString())

    @overload
    def setFontWeight(self, arg0: int) -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setFontWeight(int)"""
        return 'MutableText'._wrap(super(_MutableText, self).setFontWeight(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def nullToEmpty(arg0: str) -> 'TextObject':
        """public static dev.ultreon.libs.text.v0.TextObject dev.ultreon.libs.text.v0.TextObject.nullToEmpty(java.lang.String)"""
        return TextObject._wrap(_TextObject.nullToEmpty(arg0))

    @overload
    def setColor(self, arg0: 'Color') -> 'MutableText':
        """public dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.MutableText.setColor(java.awt.Color)"""
        return 'MutableText'._wrap(super(_MutableText, self).setColor(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.libs.text.v0.TextObject
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import object
from abc import abstractmethod, ABC
import java.lang.String as _string
import dev.ultreon.libs.text.v0.TextObject as _TextObject
_TextObject = _TextObject
import java.lang.Integer as _int
import dev.ultreon.libs.text.v0.MutableText as _MutableText
_MutableText = _MutableText
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TextObject():
    """dev.ultreon.libs.text.v0.TextObject"""
 
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
 
    @overload
    def __init__(self):
        """public dev.ultreon.libs.text.v0.TextObject()"""
        val = _TextObject()
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
    def translation(arg0: str, *arg1: object) -> 'MutableText':
        """public static dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.TextObject.translation(java.lang.String,java.lang.Object...)"""
        return MutableText._wrap(_TextObject.translation(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getText(self) -> str:
        """public java.lang.String dev.ultreon.libs.text.v0.TextObject.getText()"""
        return str._wrap(super(TextObject, self).getText())

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
    def literal(arg0: str) -> 'MutableText':
        """public static dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.TextObject.literal(java.lang.String)"""
        return MutableText._wrap(_TextObject.literal(arg0))

    @abstractmethod
    def getAttrString(self, ):
        """public abstract java.text.AttributedString dev.ultreon.libs.text.v0.TextObject.getAttrString()"""
        pass

    @overload
    def __init__(self, ):
        """public dev.ultreon.libs.text.v0.TextObject()"""
        val = _TextObject()
        self.__wrapper = val

    @staticmethod
    @overload
    def nullToEmpty(arg0: str) -> 'TextObject':
        """public static dev.ultreon.libs.text.v0.TextObject dev.ultreon.libs.text.v0.TextObject.nullToEmpty(java.lang.String)"""
        return TextObject._wrap(_TextObject.nullToEmpty(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.libs.text.v0.Translatable
from builtins import str
import dev.ultreon.libs.text.v0.MutableText as _MutableText
_MutableText = _MutableText
import dev.ultreon.libs.text.v0.Translatable as _Translatable
_Translatable = _Translatable
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
 
class Translatable():
    """dev.ultreon.libs.text.v0.Translatable"""
 
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
        """public default dev.ultreon.libs.text.v0.MutableText dev.ultreon.libs.text.v0.Translatable.getTranslation()"""
        return 'MutableText'._wrap(super(Translatable, self).getTranslation())

    @abstractmethod
    def getTranslationPath(self, ):
        """public abstract java.lang.String dev.ultreon.libs.text.v0.Translatable.getTranslationPath()"""
        pass

    @overload
    def getTranslationText(self) -> str:
        """public default java.lang.String dev.ultreon.libs.text.v0.Translatable.getTranslationText()"""
        return str._wrap(super(Translatable, self).getTranslationText())