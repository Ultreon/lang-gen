from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.awt.Rectangle as Rectangle
import java.lang.String as _string
import java.lang.Boolean as _boolean
import com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont as _UnicodeFont_RenderType
_RenderType = _UnicodeFont_RenderType.RenderType
import java.awt.Font as _Font
_Font = _Font
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.awt.Font as Font
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.tools.hiero.unicodefont.Glyph as _Glyph
_Glyph = _Glyph
import java.util.List as _List
_List = _List
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx.tools import hiero
except ImportError:
    hiero = _import_once("pygdx.tools.hiero")

import java.awt.font.GlyphVector as GlyphVector
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
import com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont as _UnicodeFont
_UnicodeFont = _UnicodeFont
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class UnicodeFont():
    """com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont"""
 
    @staticmethod
    def _wrap(java_value: _UnicodeFont) -> 'UnicodeFont':
        return UnicodeFont(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnicodeFont):
        """
        Dynamic initializer for UnicodeFont.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnicodeFont__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnicodeFont__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addGlyphs(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.addGlyphs(int,int)"""
        super(_UnicodeFont, self).addGlyphs(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def addAsciiGlyphs(self):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.addAsciiGlyphs()"""
        super(UnicodeFont, self).addAsciiGlyphs()

    @overload
    def setPaddingTop(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setPaddingTop(int)"""
        super(_UnicodeFont, self).setPaddingTop(_int.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Font', arg1: str):
        """public com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont(java.awt.Font,java.lang.String)"""
        val = _UnicodeFont(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: 'HieroSettings'):
        """public com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont(java.lang.String,com.badlogic.gdx.tools.hiero.HieroSettings)"""
        val = _UnicodeFont(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: int, arg2: bool, arg3: bool):
        """public com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont(java.lang.String,int,boolean,boolean)"""
        val = _UnicodeFont(arg0, _int.valueOf(arg1), _boolean.valueOf(arg2), _boolean.valueOf(arg3))
        self.__wrapper = val

    @overload
    def getPaddingBottom(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getPaddingBottom()"""
        return int._wrap(super(UnicodeFont, self).getPaddingBottom())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getDescent(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getDescent()"""
        return int._wrap(super(UnicodeFont, self).getDescent())

    @overload
    def getEffects(self) -> 'List':
        """public java.util.List com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getEffects()"""
        return 'List'._wrap(super(UnicodeFont, self).getEffects())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getYOffset(self, arg0: str) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getYOffset(java.lang.String)"""
        return int._wrap(super(_UnicodeFont, self).getYOffset(arg0))

    @overload
    def drawString(self, arg0: float, arg1: float, arg2: str):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.drawString(float,float,java.lang.String)"""
        super(_UnicodeFont, self).drawString(_float.valueOf(arg0), _float.valueOf(arg1), arg2)

    @overload
    def setMono(self, arg0: bool):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setMono(boolean)"""
        super(_UnicodeFont, self).setMono(_boolean.valueOf(arg0))

    @overload
    def drawString(self, arg0: float, arg1: float, arg2: str, arg3: 'Color'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.drawString(float,float,java.lang.String,com.badlogic.gdx.graphics.Color)"""
        super(_UnicodeFont, self).drawString(_float.valueOf(arg0), _float.valueOf(arg1), arg2, arg3)

    @overload
    def setPaddingAdvanceX(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setPaddingAdvanceX(int)"""
        super(_UnicodeFont, self).setPaddingAdvanceX(_int.valueOf(arg0))

    @overload
    def getFontFile(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getFontFile()"""
        return str._wrap(super(UnicodeFont, self).getFontFile())

    @overload
    def setGamma(self, arg0: float):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setGamma(float)"""
        super(_UnicodeFont, self).setGamma(_float.valueOf(arg0))

    @overload
    def setRenderType(self, arg0: 'RenderType'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setRenderType(com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont$RenderType)"""
        super(_UnicodeFont, self).setRenderType(arg0)

    @overload
    def getSpaceWidth(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getSpaceWidth()"""
        return int._wrap(super(UnicodeFont, self).getSpaceWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getWidth(self, arg0: str) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getWidth(java.lang.String)"""
        return int._wrap(super(_UnicodeFont, self).getWidth(arg0))

    @overload
    def getAscent(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getAscent()"""
        return int._wrap(super(UnicodeFont, self).getAscent())

    @overload
    def getLeading(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getLeading()"""
        return int._wrap(super(UnicodeFont, self).getLeading())

    @overload
    def getPaddingRight(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getPaddingRight()"""
        return int._wrap(super(UnicodeFont, self).getPaddingRight())

    @overload
    def getGlyphPages(self) -> 'List':
        """public java.util.List com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getGlyphPages()"""
        return 'List'._wrap(super(UnicodeFont, self).getGlyphPages())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Font', arg1: int, arg2: bool, arg3: bool):
        """public com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont(java.awt.Font,int,boolean,boolean)"""
        val = _UnicodeFont(arg0, _int.valueOf(arg1), _boolean.valueOf(arg2), _boolean.valueOf(arg3))
        self.__wrapper = val

    @overload
    def loadGlyphs(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.loadGlyphs(int)"""
        return bool._wrap(super(_UnicodeFont, self).loadGlyphs(_int.valueOf(arg0)))

    @overload
    def getPaddingAdvanceX(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getPaddingAdvanceX()"""
        return int._wrap(super(UnicodeFont, self).getPaddingAdvanceX())

    @overload
    def getFont(self) -> 'Font':
        """public java.awt.Font com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getFont()"""
        return 'Font'._wrap(super(UnicodeFont, self).getFont())

    @overload
    def getPaddingAdvanceY(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getPaddingAdvanceY()"""
        return int._wrap(super(UnicodeFont, self).getPaddingAdvanceY())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setPaddingAdvanceY(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setPaddingAdvanceY(int)"""
        super(_UnicodeFont, self).setPaddingAdvanceY(_int.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def setGlyphPageHeight(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setGlyphPageHeight(int)"""
        super(_UnicodeFont, self).setGlyphPageHeight(_int.valueOf(arg0))

    @overload
    def getRenderType(self) -> 'RenderType':
        """public com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont$RenderType com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getRenderType()"""
        return 'RenderType'._wrap(super(UnicodeFont, self).getRenderType())

    @overload
    def setPaddingRight(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setPaddingRight(int)"""
        super(_UnicodeFont, self).setPaddingRight(_int.valueOf(arg0))

    @overload
    def setGlyphPageWidth(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setGlyphPageWidth(int)"""
        super(_UnicodeFont, self).setGlyphPageWidth(_int.valueOf(arg0))

    @overload
    def getGamma(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getGamma()"""
        return float._wrap(super(UnicodeFont, self).getGamma())

    @overload
    def drawString(self, arg0: float, arg1: float, arg2: str, arg3: 'Color', arg4: int, arg5: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.drawString(float,float,java.lang.String,com.badlogic.gdx.graphics.Color,int,int)"""
        super(_UnicodeFont, self).drawString(_float.valueOf(arg0), _float.valueOf(arg1), arg2, arg3, _int.valueOf(arg4), _int.valueOf(arg5))

    @overload
    def setPaddingBottom(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setPaddingBottom(int)"""
        super(_UnicodeFont, self).setPaddingBottom(_int.valueOf(arg0))

    @overload
    def getGlyph(self, arg0: int, arg1: int, arg2: 'Rectangle', arg3: 'GlyphVector', arg4: int) -> 'Glyph':
        """public com.badlogic.gdx.tools.hiero.unicodefont.Glyph com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getGlyph(int,int,java.awt.Rectangle,java.awt.font.GlyphVector,int)"""
        return 'Glyph'._wrap(super(_UnicodeFont, self).getGlyph(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, _int.valueOf(arg4)))

    @overload
    def addNeheGlyphs(self):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.addNeheGlyphs()"""
        super(UnicodeFont, self).addNeheGlyphs()

    @overload
    def getHeight(self, arg0: str) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getHeight(java.lang.String)"""
        return int._wrap(super(_UnicodeFont, self).getHeight(arg0))

    @overload
    def setPaddingLeft(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setPaddingLeft(int)"""
        super(_UnicodeFont, self).setPaddingLeft(_int.valueOf(arg0))

    @overload
    def getGlyphPageWidth(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getGlyphPageWidth()"""
        return int._wrap(super(UnicodeFont, self).getGlyphPageWidth())

    @overload
    def getGlyphPageHeight(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getGlyphPageHeight()"""
        return int._wrap(super(UnicodeFont, self).getGlyphPageHeight())

    @overload
    def getPaddingTop(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getPaddingTop()"""
        return int._wrap(super(UnicodeFont, self).getPaddingTop())

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont(java.lang.String,java.lang.String)"""
        val = _UnicodeFont(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Font', arg1: 'HieroSettings'):
        """public com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont(java.awt.Font,com.badlogic.gdx.tools.hiero.HieroSettings)"""
        val = _UnicodeFont(arg0, arg1)
        self.__wrapper = val

    @overload
    def getMono(self) -> bool:
        """public boolean com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getMono()"""
        return bool._wrap(super(UnicodeFont, self).getMono())

    @overload
    def loadGlyphs(self) -> bool:
        """public boolean com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.loadGlyphs()"""
        return bool._wrap(super(UnicodeFont, self).loadGlyphs())

    @overload
    def addGlyphs(self, arg0: str):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.addGlyphs(java.lang.String)"""
        super(_UnicodeFont, self).addGlyphs(arg0)

    @overload
    def getPaddingLeft(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getPaddingLeft()"""
        return int._wrap(super(UnicodeFont, self).getPaddingLeft())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getLineHeight(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getLineHeight()"""
        return int._wrap(super(UnicodeFont, self).getLineHeight())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Font'):
        """public com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont(java.awt.Font)"""
        val = _UnicodeFont(arg0)
        self.__wrapper = val

    @overload
    def dispose(self):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.dispose()"""
        super(UnicodeFont, self).dispose()

 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.awt.Rectangle as Rectangle
import java.lang.String as _string
import java.lang.Boolean as _boolean
import com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont as _UnicodeFont_RenderType
_RenderType = _UnicodeFont_RenderType.RenderType
import java.awt.Font as _Font
_Font = _Font
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.awt.Font as Font
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.tools.hiero.unicodefont.Glyph as _Glyph
_Glyph = _Glyph
import java.util.List as _List
_List = _List
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx.tools import hiero
except ImportError:
    hiero = _import_once("pygdx.tools.hiero")

import java.awt.font.GlyphVector as GlyphVector
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
import com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont as _UnicodeFont
_UnicodeFont = _UnicodeFont
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class UnicodeFont():
    """com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont"""
 
    @staticmethod
    def _wrap(java_value: _UnicodeFont) -> 'UnicodeFont':
        return UnicodeFont(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnicodeFont):
        """
        Dynamic initializer for UnicodeFont.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnicodeFont__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnicodeFont__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addGlyphs(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.addGlyphs(int,int)"""
        super(_UnicodeFont, self).addGlyphs(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def addAsciiGlyphs(self):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.addAsciiGlyphs()"""
        super(UnicodeFont, self).addAsciiGlyphs()

    @overload
    def setPaddingTop(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setPaddingTop(int)"""
        super(_UnicodeFont, self).setPaddingTop(_int.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Font', arg1: str):
        """public com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont(java.awt.Font,java.lang.String)"""
        val = _UnicodeFont(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: 'HieroSettings'):
        """public com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont(java.lang.String,com.badlogic.gdx.tools.hiero.HieroSettings)"""
        val = _UnicodeFont(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: int, arg2: bool, arg3: bool):
        """public com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont(java.lang.String,int,boolean,boolean)"""
        val = _UnicodeFont(arg0, _int.valueOf(arg1), _boolean.valueOf(arg2), _boolean.valueOf(arg3))
        self.__wrapper = val

    @overload
    def getPaddingBottom(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getPaddingBottom()"""
        return int._wrap(super(UnicodeFont, self).getPaddingBottom())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getDescent(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getDescent()"""
        return int._wrap(super(UnicodeFont, self).getDescent())

    @overload
    def getEffects(self) -> 'List':
        """public java.util.List com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getEffects()"""
        return 'List'._wrap(super(UnicodeFont, self).getEffects())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getYOffset(self, arg0: str) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getYOffset(java.lang.String)"""
        return int._wrap(super(_UnicodeFont, self).getYOffset(arg0))

    @overload
    def drawString(self, arg0: float, arg1: float, arg2: str):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.drawString(float,float,java.lang.String)"""
        super(_UnicodeFont, self).drawString(_float.valueOf(arg0), _float.valueOf(arg1), arg2)

    @overload
    def setMono(self, arg0: bool):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setMono(boolean)"""
        super(_UnicodeFont, self).setMono(_boolean.valueOf(arg0))

    @overload
    def drawString(self, arg0: float, arg1: float, arg2: str, arg3: 'Color'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.drawString(float,float,java.lang.String,com.badlogic.gdx.graphics.Color)"""
        super(_UnicodeFont, self).drawString(_float.valueOf(arg0), _float.valueOf(arg1), arg2, arg3)

    @overload
    def setPaddingAdvanceX(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setPaddingAdvanceX(int)"""
        super(_UnicodeFont, self).setPaddingAdvanceX(_int.valueOf(arg0))

    @overload
    def getFontFile(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getFontFile()"""
        return str._wrap(super(UnicodeFont, self).getFontFile())

    @overload
    def setGamma(self, arg0: float):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setGamma(float)"""
        super(_UnicodeFont, self).setGamma(_float.valueOf(arg0))

    @overload
    def setRenderType(self, arg0: 'RenderType'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setRenderType(com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont$RenderType)"""
        super(_UnicodeFont, self).setRenderType(arg0)

    @overload
    def getSpaceWidth(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getSpaceWidth()"""
        return int._wrap(super(UnicodeFont, self).getSpaceWidth())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getWidth(self, arg0: str) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getWidth(java.lang.String)"""
        return int._wrap(super(_UnicodeFont, self).getWidth(arg0))

    @overload
    def getAscent(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getAscent()"""
        return int._wrap(super(UnicodeFont, self).getAscent())

    @overload
    def getLeading(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getLeading()"""
        return int._wrap(super(UnicodeFont, self).getLeading())

    @overload
    def getPaddingRight(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getPaddingRight()"""
        return int._wrap(super(UnicodeFont, self).getPaddingRight())

    @overload
    def getGlyphPages(self) -> 'List':
        """public java.util.List com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getGlyphPages()"""
        return 'List'._wrap(super(UnicodeFont, self).getGlyphPages())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Font', arg1: int, arg2: bool, arg3: bool):
        """public com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont(java.awt.Font,int,boolean,boolean)"""
        val = _UnicodeFont(arg0, _int.valueOf(arg1), _boolean.valueOf(arg2), _boolean.valueOf(arg3))
        self.__wrapper = val

    @overload
    def loadGlyphs(self, arg0: int) -> bool:
        """public boolean com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.loadGlyphs(int)"""
        return bool._wrap(super(_UnicodeFont, self).loadGlyphs(_int.valueOf(arg0)))

    @overload
    def getPaddingAdvanceX(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getPaddingAdvanceX()"""
        return int._wrap(super(UnicodeFont, self).getPaddingAdvanceX())

    @overload
    def getFont(self) -> 'Font':
        """public java.awt.Font com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getFont()"""
        return 'Font'._wrap(super(UnicodeFont, self).getFont())

    @overload
    def getPaddingAdvanceY(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getPaddingAdvanceY()"""
        return int._wrap(super(UnicodeFont, self).getPaddingAdvanceY())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setPaddingAdvanceY(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setPaddingAdvanceY(int)"""
        super(_UnicodeFont, self).setPaddingAdvanceY(_int.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def setGlyphPageHeight(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setGlyphPageHeight(int)"""
        super(_UnicodeFont, self).setGlyphPageHeight(_int.valueOf(arg0))

    @overload
    def getRenderType(self) -> 'RenderType':
        """public com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont$RenderType com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getRenderType()"""
        return 'RenderType'._wrap(super(UnicodeFont, self).getRenderType())

    @overload
    def setPaddingRight(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setPaddingRight(int)"""
        super(_UnicodeFont, self).setPaddingRight(_int.valueOf(arg0))

    @overload
    def setGlyphPageWidth(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setGlyphPageWidth(int)"""
        super(_UnicodeFont, self).setGlyphPageWidth(_int.valueOf(arg0))

    @overload
    def getGamma(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getGamma()"""
        return float._wrap(super(UnicodeFont, self).getGamma())

    @overload
    def drawString(self, arg0: float, arg1: float, arg2: str, arg3: 'Color', arg4: int, arg5: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.drawString(float,float,java.lang.String,com.badlogic.gdx.graphics.Color,int,int)"""
        super(_UnicodeFont, self).drawString(_float.valueOf(arg0), _float.valueOf(arg1), arg2, arg3, _int.valueOf(arg4), _int.valueOf(arg5))

    @overload
    def setPaddingBottom(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setPaddingBottom(int)"""
        super(_UnicodeFont, self).setPaddingBottom(_int.valueOf(arg0))

    @overload
    def getGlyph(self, arg0: int, arg1: int, arg2: 'Rectangle', arg3: 'GlyphVector', arg4: int) -> 'Glyph':
        """public com.badlogic.gdx.tools.hiero.unicodefont.Glyph com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getGlyph(int,int,java.awt.Rectangle,java.awt.font.GlyphVector,int)"""
        return 'Glyph'._wrap(super(_UnicodeFont, self).getGlyph(_int.valueOf(arg0), _int.valueOf(arg1), arg2, arg3, _int.valueOf(arg4)))

    @overload
    def addNeheGlyphs(self):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.addNeheGlyphs()"""
        super(UnicodeFont, self).addNeheGlyphs()

    @overload
    def getHeight(self, arg0: str) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getHeight(java.lang.String)"""
        return int._wrap(super(_UnicodeFont, self).getHeight(arg0))

    @overload
    def setPaddingLeft(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.setPaddingLeft(int)"""
        super(_UnicodeFont, self).setPaddingLeft(_int.valueOf(arg0))

    @overload
    def getGlyphPageWidth(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getGlyphPageWidth()"""
        return int._wrap(super(UnicodeFont, self).getGlyphPageWidth())

    @overload
    def getGlyphPageHeight(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getGlyphPageHeight()"""
        return int._wrap(super(UnicodeFont, self).getGlyphPageHeight())

    @overload
    def getPaddingTop(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getPaddingTop()"""
        return int._wrap(super(UnicodeFont, self).getPaddingTop())

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont(java.lang.String,java.lang.String)"""
        val = _UnicodeFont(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Font', arg1: 'HieroSettings'):
        """public com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont(java.awt.Font,com.badlogic.gdx.tools.hiero.HieroSettings)"""
        val = _UnicodeFont(arg0, arg1)
        self.__wrapper = val

    @overload
    def getMono(self) -> bool:
        """public boolean com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getMono()"""
        return bool._wrap(super(UnicodeFont, self).getMono())

    @overload
    def loadGlyphs(self) -> bool:
        """public boolean com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.loadGlyphs()"""
        return bool._wrap(super(UnicodeFont, self).loadGlyphs())

    @overload
    def addGlyphs(self, arg0: str):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.addGlyphs(java.lang.String)"""
        super(_UnicodeFont, self).addGlyphs(arg0)

    @overload
    def getPaddingLeft(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getPaddingLeft()"""
        return int._wrap(super(UnicodeFont, self).getPaddingLeft())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getLineHeight(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.getLineHeight()"""
        return int._wrap(super(UnicodeFont, self).getLineHeight())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Font'):
        """public com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont(java.awt.Font)"""
        val = _UnicodeFont(arg0)
        self.__wrapper = val

    @overload
    def dispose(self):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.dispose()"""
        super(UnicodeFont, self).dispose()

 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.Glyph
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.Texture as _Texture
_Texture = _Texture
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.awt.Shape as Shape
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.tools.hiero.unicodefont.Glyph as _Glyph
_Glyph = _Glyph
import java.lang.Float as _float
import java.lang.Integer as _int
import java.awt.Shape as _Shape
_Shape = _Shape
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Glyph():
    """com.badlogic.gdx.tools.hiero.unicodefont.Glyph"""
 
    @staticmethod
    def _wrap(java_value: _Glyph) -> 'Glyph':
        return Glyph(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Glyph):
        """
        Dynamic initializer for Glyph.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Glyph__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Glyph__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getV(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.Glyph.getV()"""
        return float._wrap(super(Glyph, self).getV())

    @overload
    def setShape(self, arg0: 'Shape'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.Glyph.setShape(java.awt.Shape)"""
        super(_Glyph, self).setShape(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def isMissing(self) -> bool:
        """public boolean com.badlogic.gdx.tools.hiero.unicodefont.Glyph.isMissing()"""
        return bool._wrap(super(Glyph, self).isMissing())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getYOffset(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.Glyph.getYOffset()"""
        return int._wrap(super(Glyph, self).getYOffset())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getV2(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.Glyph.getV2()"""
        return float._wrap(super(Glyph, self).getV2())

    @overload
    def getShape(self) -> 'Shape':
        """public java.awt.Shape com.badlogic.gdx.tools.hiero.unicodefont.Glyph.getShape()"""
        return 'Shape'._wrap(super(Glyph, self).getShape())

    @overload
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.Glyph.getWidth()"""
        return int._wrap(super(Glyph, self).getWidth())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getXOffset(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.Glyph.getXOffset()"""
        return int._wrap(super(Glyph, self).getXOffset())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getCodePoint(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.Glyph.getCodePoint()"""
        return int._wrap(super(Glyph, self).getCodePoint())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setTexture(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.Glyph.setTexture(com.badlogic.gdx.graphics.Texture,float,float,float,float)"""
        super(_Glyph, self).setTexture(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.Glyph.getHeight()"""
        return int._wrap(super(Glyph, self).getHeight())

    @overload
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.tools.hiero.unicodefont.Glyph.getTexture()"""
        return 'graphics.Texture'._wrap(super(Glyph, self).getTexture())

    @overload
    def getU(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.Glyph.getU()"""
        return float._wrap(super(Glyph, self).getU())

    @overload
    def getXAdvance(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.Glyph.getXAdvance()"""
        return int._wrap(super(Glyph, self).getXAdvance())

    @overload
    def getU2(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.Glyph.getU2()"""
        return float._wrap(super(Glyph, self).getU2())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont$RenderType
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
import com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont as _UnicodeFont_RenderType
_RenderType = _UnicodeFont_RenderType.RenderType
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RenderType():
    """com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont.RenderType"""
 
    @staticmethod
    def _wrap(java_value: _RenderType) -> 'RenderType':
        return RenderType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RenderType):
        """
        Dynamic initializer for RenderType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RenderType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RenderType__wrapper":
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
    def values() -> List['RenderType']:
        """public static com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont$RenderType[] com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont$RenderType.values()"""
        return List[RenderType]._wrap(_RenderType.values())

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
    def valueOf(arg0: str) -> 'RenderType':
        """public static com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont$RenderType com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont$RenderType.valueOf(java.lang.String)"""
        return RenderType._wrap(_RenderType.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.GlyphPage
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.Texture as _Texture
_Texture = _Texture
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.Integer as _int
import com.badlogic.gdx.tools.hiero.unicodefont.GlyphPage as _GlyphPage
_GlyphPage = _GlyphPage
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GlyphPage():
    """com.badlogic.gdx.tools.hiero.unicodefont.GlyphPage"""
 
    @staticmethod
    def _wrap(java_value: _GlyphPage) -> 'GlyphPage':
        return GlyphPage(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GlyphPage):
        """
        Dynamic initializer for GlyphPage.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GlyphPage__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GlyphPage__wrapper":
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

    @overload
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.tools.hiero.unicodefont.GlyphPage.getTexture()"""
        return 'graphics.Texture'._wrap(super(GlyphPage, self).getTexture())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getGlyphs(self) -> 'List':
        """public java.util.List<com.badlogic.gdx.tools.hiero.unicodefont.Glyph> com.badlogic.gdx.tools.hiero.unicodefont.GlyphPage.getGlyphs()"""
        return 'List'._wrap(super(GlyphPage, self).getGlyphs())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())