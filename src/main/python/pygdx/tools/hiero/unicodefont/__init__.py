from __future__ import annotations
from overload import overload


 
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
import com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont as __UnicodeFont_RenderType
__RenderType = __UnicodeFont_RenderType.RenderType
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class RenderType():
    """com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.RenderType"""
 
    @staticmethod
    def __wrap(java_value: __RenderType) -> 'RenderType':
        return RenderType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RenderType):
        """
        Dynamic initializer for RenderType.
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
    def values() -> List['RenderType']:
        """public static com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont$RenderType[] com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont$RenderType.values()"""
        return List[RenderType].__wrap(__RenderType.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'RenderType':
        """public static com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont$RenderType com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont$RenderType.valueOf(java.lang.String)"""
        return RenderType.__wrap(__RenderType.valueOf(arg0))

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

 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont$RenderType
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
import com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont as __UnicodeFont_RenderType
__RenderType = __UnicodeFont_RenderType.RenderType
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class RenderType():
    """com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.RenderType"""
 
    @staticmethod
    def __wrap(java_value: __RenderType) -> 'RenderType':
        return RenderType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RenderType):
        """
        Dynamic initializer for RenderType.
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
    def values() -> List['RenderType']:
        """public static com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont$RenderType[] com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont$RenderType.values()"""
        return List[RenderType].__wrap(__RenderType.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'RenderType':
        """public static com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont$RenderType com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont$RenderType.valueOf(java.lang.String)"""
        return RenderType.__wrap(__RenderType.valueOf(arg0))

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

 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont$RenderType 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
from builtins import type
import java.awt.Rectangle as Rectangle
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.tools.hiero.unicodefont.Glyph as __Glyph
__Glyph = __Glyph
import java.lang.String as __string
import java.awt.Font as __Font
__Font = __Font
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.awt.Font as Font
from builtins import float
import com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont as __UnicodeFont
__UnicodeFont = __UnicodeFont
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont as __UnicodeFont_RenderType
__RenderType = __UnicodeFont_RenderType.RenderType
try:
    from pygdx.tools import hiero
except ImportError:
    hiero = __import_once__("pygdx.tools.hiero")

import java.awt.font.GlyphVector as GlyphVector
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
import java.util.List as List
 
class UnicodeFont():
    """com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont"""
 
    @staticmethod
    def __wrap(java_value: __UnicodeFont) -> 'UnicodeFont':
        return UnicodeFont(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnicodeFont):
        """
        Dynamic initializer for UnicodeFont.
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
    def setPaddingRight(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setPaddingRight(int)"""
        super(__UnicodeFont, self).setPaddingRight(__int.valueOf(arg0))

    @overload
    def getPaddingLeft(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getPaddingLeft()"""
        return int.__wrap(super(UnicodeFont, self).getPaddingLeft())

    @overload
    def addAsciiGlyphs(self):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.addAsciiGlyphs()"""
        super(UnicodeFont, self).addAsciiGlyphs()

    @overload
    def getPaddingRight(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getPaddingRight()"""
        return int.__wrap(super(UnicodeFont, self).getPaddingRight())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getPaddingBottom(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getPaddingBottom()"""
        return int.__wrap(super(UnicodeFont, self).getPaddingBottom())

    @overload
    def getDescent(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getDescent()"""
        return int.__wrap(super(UnicodeFont, self).getDescent())

    @overload
    def getRenderType(self) -> 'RenderType':
        """public com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont$RenderType com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getRenderType()"""
        return 'RenderType'.__wrap(super(UnicodeFont, self).getRenderType())

    @overload
    def getYOffset(self, arg0: str) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getYOffset(java.lang.String)"""
        return int.__wrap(super(__UnicodeFont, self).getYOffset(arg0))

    @overload
    def setGlyphPageWidth(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setGlyphPageWidth(int)"""
        super(__UnicodeFont, self).setGlyphPageWidth(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont(java.lang.String,java.lang.String)"""
        val = __UnicodeFont(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setPaddingAdvanceX(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setPaddingAdvanceX(int)"""
        super(__UnicodeFont, self).setPaddingAdvanceX(__int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def loadGlyphs(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.loadGlyphs(int)"""
        return bool.__wrap(super(__UnicodeFont, self).loadGlyphs(__int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'Font', arg1: int, arg2: bool, arg3: bool):
        """public com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont(java.awt.Font,int,boolean,boolean)"""
        val = __UnicodeFont(arg0, __int.valueOf(arg1), __boolean.valueOf(arg2), __boolean.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Font', arg1: 'HieroSettings'):
        """public com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont(java.awt.Font,com.badlogic.gdx.tools.hiero.HieroSettings)"""
        val = __UnicodeFont(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setPaddingLeft(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setPaddingLeft(int)"""
        super(__UnicodeFont, self).setPaddingLeft(__int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getMono(self) -> bool:
        """public boolean com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getMono()"""
        return bool.__wrap(super(UnicodeFont, self).getMono())

    @overload
    def getEffects(self) -> 'List':
        """public java.util.List com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getEffects()"""
        return 'List'.__wrap(super(UnicodeFont, self).getEffects())

    @overload
    def getLeading(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getLeading()"""
        return int.__wrap(super(UnicodeFont, self).getLeading())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getLineHeight(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getLineHeight()"""
        return int.__wrap(super(UnicodeFont, self).getLineHeight())

    @overload
    def getFontFile(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getFontFile()"""
        return str.__wrap(super(UnicodeFont, self).getFontFile())

    @overload
    def getGlyphPageWidth(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getGlyphPageWidth()"""
        return int.__wrap(super(UnicodeFont, self).getGlyphPageWidth())

    @overload
    def __init__(self, arg0: str, arg1: 'HieroSettings'):
        """public com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont(java.lang.String,com.badlogic.gdx.tools.hiero.HieroSettings)"""
        val = __UnicodeFont(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Font'):
        """public com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont(java.awt.Font)"""
        val = __UnicodeFont(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getPaddingAdvanceY(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getPaddingAdvanceY()"""
        return int.__wrap(super(UnicodeFont, self).getPaddingAdvanceY())

    @overload
    def getGlyphPageHeight(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getGlyphPageHeight()"""
        return int.__wrap(super(UnicodeFont, self).getGlyphPageHeight())

    @overload
    def addGlyphs(self, arg0: str):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.addGlyphs(java.lang.String)"""
        super(__UnicodeFont, self).addGlyphs(arg0)

    @overload
    def __init__(self, arg0: str, arg1: int, arg2: bool, arg3: bool):
        """public com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont(java.lang.String,int,boolean,boolean)"""
        val = __UnicodeFont(arg0, __int.valueOf(arg1), __boolean.valueOf(arg2), __boolean.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Font', arg1: str):
        """public com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont(java.awt.Font,java.lang.String)"""
        val = __UnicodeFont(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def loadGlyphs(self) -> bool:
        """public boolean com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.loadGlyphs()"""
        return bool.__wrap(super(UnicodeFont, self).loadGlyphs())

    @overload
    def getPaddingTop(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getPaddingTop()"""
        return int.__wrap(super(UnicodeFont, self).getPaddingTop())

    @overload
    def setPaddingBottom(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setPaddingBottom(int)"""
        super(__UnicodeFont, self).setPaddingBottom(__int.valueOf(arg0))

    @overload
    def getPaddingAdvanceX(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getPaddingAdvanceX()"""
        return int.__wrap(super(UnicodeFont, self).getPaddingAdvanceX())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getGlyphPages(self) -> 'List':
        """public java.util.List com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getGlyphPages()"""
        return 'List'.__wrap(super(UnicodeFont, self).getGlyphPages())

    @overload
    def drawString(self, arg0: float, arg1: float, arg2: str, arg3: 'Color'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.drawString(float,float,java.lang.String,com.badlogic.gdx.graphics.Color)"""
        super(__UnicodeFont, self).drawString(__float.valueOf(arg0), __float.valueOf(arg1), arg2, arg3)

    @overload
    def getWidth(self, arg0: str) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getWidth(java.lang.String)"""
        return int.__wrap(super(__UnicodeFont, self).getWidth(arg0))

    @overload
    def getFont(self) -> 'Font':
        """public java.awt.Font com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getFont()"""
        return 'Font'.__wrap(super(UnicodeFont, self).getFont())

    @overload
    def setGlyphPageHeight(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setGlyphPageHeight(int)"""
        super(__UnicodeFont, self).setGlyphPageHeight(__int.valueOf(arg0))

    @overload
    def setPaddingTop(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setPaddingTop(int)"""
        super(__UnicodeFont, self).setPaddingTop(__int.valueOf(arg0))

    @overload
    def addNeheGlyphs(self):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.addNeheGlyphs()"""
        super(UnicodeFont, self).addNeheGlyphs()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getAscent(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getAscent()"""
        return int.__wrap(super(UnicodeFont, self).getAscent())

    @overload
    def getSpaceWidth(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getSpaceWidth()"""
        return int.__wrap(super(UnicodeFont, self).getSpaceWidth())

    @overload
    def drawString(self, arg0: float, arg1: float, arg2: str, arg3: 'Color', arg4: int, arg5: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.drawString(float,float,java.lang.String,com.badlogic.gdx.graphics.Color,int,int)"""
        super(__UnicodeFont, self).drawString(__float.valueOf(arg0), __float.valueOf(arg1), arg2, arg3, __int.valueOf(arg4), __int.valueOf(arg5))

    @overload
    def addGlyphs(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.addGlyphs(int,int)"""
        super(__UnicodeFont, self).addGlyphs(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def drawString(self, arg0: float, arg1: float, arg2: str):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.drawString(float,float,java.lang.String)"""
        super(__UnicodeFont, self).drawString(__float.valueOf(arg0), __float.valueOf(arg1), arg2)

    @overload
    def setRenderType(self, arg0: 'RenderType'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setRenderType(com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont$RenderType)"""
        super(__UnicodeFont, self).setRenderType(arg0)

    @overload
    def getHeight(self, arg0: str) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getHeight(java.lang.String)"""
        return int.__wrap(super(__UnicodeFont, self).getHeight(arg0))

    @overload
    def getGlyph(self, arg0: int, arg1: int, arg2: 'Rectangle', arg3: 'GlyphVector', arg4: int) -> 'Glyph':
        """public com.badlogic.gdx.tools.hiero.unicodefont.Glyph com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getGlyph(int,int,java.awt.Rectangle,java.awt.font.GlyphVector,int)"""
        return 'Glyph'.__wrap(super(__UnicodeFont, self).getGlyph(__int.valueOf(arg0), __int.valueOf(arg1), arg2, arg3, __int.valueOf(arg4)))

    @overload
    def setPaddingAdvanceY(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setPaddingAdvanceY(int)"""
        super(__UnicodeFont, self).setPaddingAdvanceY(__int.valueOf(arg0))

    @overload
    def getGamma(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getGamma()"""
        return float.__wrap(super(UnicodeFont, self).getGamma())

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
    def setGamma(self, arg0: float):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setGamma(float)"""
        super(__UnicodeFont, self).setGamma(__float.valueOf(arg0))

    @overload
    def dispose(self):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.dispose()"""
        super(UnicodeFont, self).dispose()

    @overload
    def setMono(self, arg0: bool):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setMono(boolean)"""
        super(__UnicodeFont, self).setMono(__boolean.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.GlyphPage
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import com.badlogic.gdx.tools.hiero.unicodefont.GlyphPage as __GlyphPage
__GlyphPage = __GlyphPage
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Texture as __Texture
__Texture = __Texture
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
import java.util.List as List
from builtins import int
 
class GlyphPage():
    """com.badlogic.gdx.tools.hiero.unicodefont.GlyphPage"""
 
    @staticmethod
    def __wrap(java_value: __GlyphPage) -> 'GlyphPage':
        return GlyphPage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GlyphPage):
        """
        Dynamic initializer for GlyphPage.
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

    @overload
    def getGlyphs(self) -> 'List':
        """public java.util.List<com.badlogic.gdx.tools.hiero.unicodefont.Glyph> com.badlogic.gdx.tools.hiero.unicodefont.GlyphPage.getGlyphs()"""
        return 'List'.__wrap(super(GlyphPage, self).getGlyphs())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.tools.hiero.unicodefont.GlyphPage.getTexture()"""
        return 'graphics.Texture'.__wrap(super(GlyphPage, self).getTexture())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.Glyph
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.awt.Shape as Shape
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.tools.hiero.unicodefont.Glyph as __Glyph
__Glyph = __Glyph
import java.awt.Shape as __Shape
__Shape = __Shape
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Texture as __Texture
__Texture = __Texture
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class Glyph():
    """com.badlogic.gdx.tools.hiero.unicodefont.Glyph"""
 
    @staticmethod
    def __wrap(java_value: __Glyph) -> 'Glyph':
        return Glyph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Glyph):
        """
        Dynamic initializer for Glyph.
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
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.tools.hiero.unicodefont.Glyph.getTexture()"""
        return 'graphics.Texture'.__wrap(super(Glyph, self).getTexture())

    @overload
    def getV(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.Glyph.getV()"""
        return float.__wrap(super(Glyph, self).getV())

    @overload
    def getYOffset(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.Glyph.getYOffset()"""
        return int.__wrap(super(Glyph, self).getYOffset())

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

    @overload
    def getCodePoint(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.Glyph.getCodePoint()"""
        return int.__wrap(super(Glyph, self).getCodePoint())

    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.Glyph.getHeight()"""
        return int.__wrap(super(Glyph, self).getHeight())

    @overload
    def getXAdvance(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.Glyph.getXAdvance()"""
        return int.__wrap(super(Glyph, self).getXAdvance())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setShape(self, arg0: 'Shape'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.Glyph.setShape(java.awt.Shape)"""
        super(__Glyph, self).setShape(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getShape(self) -> 'Shape':
        """public java.awt.Shape com.badlogic.gdx.tools.hiero.unicodefont.Glyph.getShape()"""
        return 'Shape'.__wrap(super(Glyph, self).getShape())

    @overload
    def isMissing(self) -> bool:
        """public boolean com.badlogic.gdx.tools.hiero.unicodefont.Glyph.isMissing()"""
        return bool.__wrap(super(Glyph, self).isMissing())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getXOffset(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.Glyph.getXOffset()"""
        return int.__wrap(super(Glyph, self).getXOffset())

    @overload
    def getV2(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.Glyph.getV2()"""
        return float.__wrap(super(Glyph, self).getV2())

    @overload
    def getU(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.Glyph.getU()"""
        return float.__wrap(super(Glyph, self).getU())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.Glyph.getWidth()"""
        return int.__wrap(super(Glyph, self).getWidth())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getU2(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.Glyph.getU2()"""
        return float.__wrap(super(Glyph, self).getU2())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setTexture(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.Glyph.setTexture(com.badlogic.gdx.graphics.Texture,float,float,float,float)"""
        super(__Glyph, self).setTexture(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))