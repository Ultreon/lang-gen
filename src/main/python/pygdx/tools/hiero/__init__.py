from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.File as File
import com.badlogic.gdx.tools.hiero.BMFontUtil as __BMFontUtil
__BMFontUtil = __BMFontUtil
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = __import_once__("pygdx.tools.hiero.unicodefont")

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
 
class BMFontUtil():
    """com.badlogic.gdx.tools.hiero.BMFontUtil"""
 
    @staticmethod
    def __wrap(java_value: __BMFontUtil) -> 'BMFontUtil':
        return BMFontUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BMFontUtil):
        """
        Dynamic initializer for BMFontUtil.
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
    def save(self, arg0: 'File'):
        """public void com.badlogic.gdx.tools.hiero.BMFontUtil.save(java.io.File) throws java.io.IOException"""
        super(__BMFontUtil, self).save(arg0)

    @overload
    def __init__(self, arg0: 'UnicodeFont'):
        """public com.badlogic.gdx.tools.hiero.BMFontUtil(com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont)"""
        val = __BMFontUtil(arg0)
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

 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.BMFontUtil
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.File as File
import com.badlogic.gdx.tools.hiero.BMFontUtil as __BMFontUtil
__BMFontUtil = __BMFontUtil
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = __import_once__("pygdx.tools.hiero.unicodefont")

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
 
class BMFontUtil():
    """com.badlogic.gdx.tools.hiero.BMFontUtil"""
 
    @staticmethod
    def __wrap(java_value: __BMFontUtil) -> 'BMFontUtil':
        return BMFontUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BMFontUtil):
        """
        Dynamic initializer for BMFontUtil.
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
    def save(self, arg0: 'File'):
        """public void com.badlogic.gdx.tools.hiero.BMFontUtil.save(java.io.File) throws java.io.IOException"""
        super(__BMFontUtil, self).save(arg0)

    @overload
    def __init__(self, arg0: 'UnicodeFont'):
        """public com.badlogic.gdx.tools.hiero.BMFontUtil(com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont)"""
        val = __BMFontUtil(arg0)
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

 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.BMFontUtil 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.HieroSettings
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.io.File as File
from builtins import float
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.tools.hiero.HieroSettings as __HieroSettings
__HieroSettings = __HieroSettings
from builtins import int
import java.util.List as List
 
class HieroSettings():
    """com.badlogic.gdx.tools.hiero.HieroSettings"""
 
    @staticmethod
    def __wrap(java_value: __HieroSettings) -> 'HieroSettings':
        return HieroSettings(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __HieroSettings):
        """
        Dynamic initializer for HieroSettings.
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
    def isItalic(self) -> bool:
        """public boolean com.badlogic.gdx.tools.hiero.HieroSettings.isItalic()"""
        return bool.__wrap(super(HieroSettings, self).isItalic())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setItalic(self, arg0: bool):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setItalic(boolean)"""
        super(__HieroSettings, self).setItalic(__boolean.valueOf(arg0))

    @overload
    def setGamma(self, arg0: float):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setGamma(float)"""
        super(__HieroSettings, self).setGamma(__float.valueOf(arg0))

    @overload
    def getPaddingRight(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.HieroSettings.getPaddingRight()"""
        return int.__wrap(super(HieroSettings, self).getPaddingRight())

    @overload
    def setMono(self, arg0: bool):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setMono(boolean)"""
        super(__HieroSettings, self).setMono(__boolean.valueOf(arg0))

    @overload
    def isFont2Active(self) -> bool:
        """public boolean com.badlogic.gdx.tools.hiero.HieroSettings.isFont2Active()"""
        return bool.__wrap(super(HieroSettings, self).isFont2Active())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getGlyphPageWidth(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.HieroSettings.getGlyphPageWidth()"""
        return int.__wrap(super(HieroSettings, self).getGlyphPageWidth())

    @overload
    def setFont2File(self, arg0: str):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setFont2File(java.lang.String)"""
        super(__HieroSettings, self).setFont2File(arg0)

    @overload
    def setNativeRendering(self, arg0: bool):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setNativeRendering(boolean)"""
        super(__HieroSettings, self).setNativeRendering(__boolean.valueOf(arg0))

    @overload
    def setBold(self, arg0: bool):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setBold(boolean)"""
        super(__HieroSettings, self).setBold(__boolean.valueOf(arg0))

    @overload
    def getFontSize(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.HieroSettings.getFontSize()"""
        return int.__wrap(super(HieroSettings, self).getFontSize())

    @overload
    def getPaddingBottom(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.HieroSettings.getPaddingBottom()"""
        return int.__wrap(super(HieroSettings, self).getPaddingBottom())

    @overload
    def setFontSize(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setFontSize(int)"""
        super(__HieroSettings, self).setFontSize(__int.valueOf(arg0))

    @overload
    def getPaddingAdvanceX(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.HieroSettings.getPaddingAdvanceX()"""
        return int.__wrap(super(HieroSettings, self).getPaddingAdvanceX())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def save(self, arg0: 'File'):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.save(java.io.File) throws java.io.IOException"""
        super(__HieroSettings, self).save(arg0)

    @overload
    def getPaddingTop(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.HieroSettings.getPaddingTop()"""
        return int.__wrap(super(HieroSettings, self).getPaddingTop())

    @overload
    def getFont2File(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.hiero.HieroSettings.getFont2File()"""
        return str.__wrap(super(HieroSettings, self).getFont2File())

    @overload
    def getEffects(self) -> 'List':
        """public java.util.List com.badlogic.gdx.tools.hiero.HieroSettings.getEffects()"""
        return 'List'.__wrap(super(HieroSettings, self).getEffects())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getPaddingAdvanceY(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.HieroSettings.getPaddingAdvanceY()"""
        return int.__wrap(super(HieroSettings, self).getPaddingAdvanceY())

    @overload
    def getGamma(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.HieroSettings.getGamma()"""
        return float.__wrap(super(HieroSettings, self).getGamma())

    @overload
    def getFontName(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.hiero.HieroSettings.getFontName()"""
        return str.__wrap(super(HieroSettings, self).getFontName())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.hiero.HieroSettings()"""
        val = __HieroSettings()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getGlyphText(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.hiero.HieroSettings.getGlyphText()"""
        return str.__wrap(super(HieroSettings, self).getGlyphText())

    @overload
    def setPaddingLeft(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setPaddingLeft(int)"""
        super(__HieroSettings, self).setPaddingLeft(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.tools.hiero.HieroSettings(java.lang.String)"""
        val = __HieroSettings(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setFontName(self, arg0: str):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setFontName(java.lang.String)"""
        super(__HieroSettings, self).setFontName(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def isMono(self) -> bool:
        """public boolean com.badlogic.gdx.tools.hiero.HieroSettings.isMono()"""
        return bool.__wrap(super(HieroSettings, self).isMono())

    @overload
    def setPaddingBottom(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setPaddingBottom(int)"""
        super(__HieroSettings, self).setPaddingBottom(__int.valueOf(arg0))

    @overload
    def setPaddingAdvanceY(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setPaddingAdvanceY(int)"""
        super(__HieroSettings, self).setPaddingAdvanceY(__int.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.hiero.HieroSettings()"""
        val = __HieroSettings()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setRenderType(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setRenderType(int)"""
        super(__HieroSettings, self).setRenderType(__int.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def isBold(self) -> bool:
        """public boolean com.badlogic.gdx.tools.hiero.HieroSettings.isBold()"""
        return bool.__wrap(super(HieroSettings, self).isBold())

    @overload
    def setGlyphPageHeight(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setGlyphPageHeight(int)"""
        super(__HieroSettings, self).setGlyphPageHeight(__int.valueOf(arg0))

    @overload
    def setPaddingTop(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setPaddingTop(int)"""
        super(__HieroSettings, self).setPaddingTop(__int.valueOf(arg0))

    @overload
    def setPaddingRight(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setPaddingRight(int)"""
        super(__HieroSettings, self).setPaddingRight(__int.valueOf(arg0))

    @overload
    def setPaddingAdvanceX(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setPaddingAdvanceX(int)"""
        super(__HieroSettings, self).setPaddingAdvanceX(__int.valueOf(arg0))

    @overload
    def setFont2Active(self, arg0: bool):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setFont2Active(boolean)"""
        super(__HieroSettings, self).setFont2Active(__boolean.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getGlyphPageHeight(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.HieroSettings.getGlyphPageHeight()"""
        return int.__wrap(super(HieroSettings, self).getGlyphPageHeight())

    @overload
    def getPaddingLeft(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.HieroSettings.getPaddingLeft()"""
        return int.__wrap(super(HieroSettings, self).getPaddingLeft())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setGlyphText(self, arg0: str):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setGlyphText(java.lang.String)"""
        super(__HieroSettings, self).setGlyphText(arg0)

    @overload
    def getRenderType(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.HieroSettings.getRenderType()"""
        return int.__wrap(super(HieroSettings, self).getRenderType())

    @overload
    def getNativeRendering(self) -> bool:
        """public boolean com.badlogic.gdx.tools.hiero.HieroSettings.getNativeRendering()"""
        return bool.__wrap(super(HieroSettings, self).getNativeRendering())

    @overload
    def setGlyphPageWidth(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setGlyphPageWidth(int)"""
        super(__HieroSettings, self).setGlyphPageWidth(__int.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.Hiero
import javax.accessibility.AccessibleContext as AccessibleContext
import java.awt.im.InputMethodRequests as __InputMethodRequests
__InputMethodRequests = __InputMethodRequests
import java.awt.event.HierarchyBoundsListener as HierarchyBoundsListener
import java.awt.image.ImageProducer as ImageProducer
import java.awt.Image as __Image
__Image = __Image
import java.awt.BufferCapabilities as BufferCapabilities
import java.awt.GraphicsConfiguration as GraphicsConfiguration
import java.awt.image.VolatileImage as __VolatileImage
__VolatileImage = __VolatileImage
import java.awt.MenuComponent as MenuComponent
import java.lang.Byte as __byte
import java.awt.im.InputContext as __InputContext
__InputContext = __InputContext
import java.awt.Dimension as Dimension
import java.awt.event.MouseListener as __MouseListener
__MouseListener = __MouseListener
import java.awt.event.ContainerListener as ContainerListener
import java.awt.AWTEvent as AWTEvent
import java.awt.event.HierarchyListener as __HierarchyListener
__HierarchyListener = __HierarchyListener
import java.awt.ComponentOrientation as ComponentOrientation
import java.awt.dnd.DropTarget as __DropTarget
__DropTarget = __DropTarget
import java.util.Set as __Set
__Set = __Set
from builtins import float
import java.awt.event.HierarchyListener as HierarchyListener
import java.awt.event.InputMethodListener as InputMethodListener
from typing import List
import java.awt.Window as __Window
__Window = __Window
import java.lang.Float as __float
import java.awt.Graphics as __Graphics
__Graphics = __Graphics
import java.awt.Shape as __Shape
__Shape = __Shape
import java.lang.String as __String
__String = __String
import java.awt.Dialog as __Dialog_ModalExclusionType
__ModalExclusionType = __Dialog_ModalExclusionType.ModalExclusionType
import java.awt.Window.Type as Type
import java.awt.event.KeyListener as KeyListener
import java.awt.Component as Component
import java.util.Locale as __Locale
__Locale = __Locale
import java.awt.event.WindowListener as __WindowListener
__WindowListener = __WindowListener
from builtins import int
import java.awt.Frame as Frame
import java.awt.LayoutManager as LayoutManager
import java.awt.Container as Container
import javax.swing.JMenuBar as JMenuBar
from builtins import type
import java.awt.Rectangle as __Rectangle
__Rectangle = __Rectangle
import java.awt.Shape as Shape
import java.util.ResourceBundle as ResourceBundle
import java.awt.event.InputMethodListener as __InputMethodListener
__InputMethodListener = __InputMethodListener
import java.awt.Rectangle as Rectangle
import java.awt.Toolkit as __Toolkit
__Toolkit = __Toolkit
import java.lang.String as __string
import java.awt.event.FocusListener as __FocusListener
__FocusListener = __FocusListener
import java.awt.event.ComponentListener as ComponentListener
import java.awt.event.WindowFocusListener as WindowFocusListener
from builtins import object
import java.awt.Cursor as __Cursor
__Cursor = __Cursor
import java.awt.MenuBar as MenuBar
import java.awt.Component.BaselineResizeBehavior as BaselineResizeBehavior
import javax.swing.JRootPane as __JRootPane
__JRootPane = __JRootPane
import java.awt.image.BufferStrategy as __BufferStrategy
__BufferStrategy = __BufferStrategy
import java.awt.Dimension as __Dimension
__Dimension = __Dimension
import java.awt.Component as __Component_BaselineResizeBehavior
__BaselineResizeBehavior = __Component_BaselineResizeBehavior.BaselineResizeBehavior
import java.awt.im.InputMethodRequests as InputMethodRequests
import java.awt.event.MouseWheelListener as __MouseWheelListener
__MouseWheelListener = __MouseWheelListener
import javax.swing.JLayeredPane as JLayeredPane
import java.util.List as List
import javax.swing.TransferHandler as TransferHandler
import java.awt.MenuBar as __MenuBar
__MenuBar = __MenuBar
import java.awt.GraphicsConfiguration as __GraphicsConfiguration
__GraphicsConfiguration = __GraphicsConfiguration
import java.awt.event.FocusEvent.Cause as Cause
import java.beans.PropertyChangeListener as __PropertyChangeListener
__PropertyChangeListener = __PropertyChangeListener
import java.awt.event.MouseWheelListener as MouseWheelListener
import com.badlogic.gdx.tools.hiero.Hiero as __Hiero
__Hiero = __Hiero
import java.awt.Point as __Point
__Point = __Point
import java.awt.image.ColorModel as ColorModel
import java.lang.Class as __Class
__Class = __Class
import java.awt.event.WindowStateListener as WindowStateListener
import java.awt.event.MouseMotionListener as MouseMotionListener
import java.util.EventListener as EventListener
import java.lang.Short as __short
import java.awt.Insets as Insets
import java.awt.Font as __Font
__Font = __Font
import java.awt.event.ComponentListener as __ComponentListener
__ComponentListener = __ComponentListener
import javax.swing.JLayeredPane as __JLayeredPane
__JLayeredPane = __JLayeredPane
import javax.swing.TransferHandler as __TransferHandler
__TransferHandler = __TransferHandler
import javax.swing.JMenuBar as __JMenuBar
__JMenuBar = __JMenuBar
import java.lang.Double as __double
from builtins import bool
import java.awt.Window as Window
import java.awt.PopupMenu as PopupMenu
import java.util.EventListener as __EventListener
__EventListener = __EventListener
import java.awt.LayoutManager as __LayoutManager
__LayoutManager = __LayoutManager
import java.awt.FontMetrics as __FontMetrics
__FontMetrics = __FontMetrics
import javax.swing.JFrame as __JFrame
__JFrame = __JFrame
import java.awt.im.InputContext as InputContext
import java.awt.Font as Font
import javax.accessibility.AccessibleContext as __AccessibleContext
__AccessibleContext = __AccessibleContext
import java.awt.image.VolatileImage as VolatileImage
import java.awt.dnd.DropTarget as DropTarget
import java.awt.Cursor as Cursor
import java.util.List as __List
__List = __List
import java.io.PrintStream as PrintStream
import java.awt.image.BufferStrategy as BufferStrategy
import java.lang.Object as __Object
__Object = __Object
import java.awt.Dialog.ModalExclusionType as ModalExclusionType
import java.awt.event.MouseListener as MouseListener
import java.util.Locale as Locale
import java.lang.Character as __char
import java.lang.Boolean as __boolean
import java.beans.PropertyChangeListener as PropertyChangeListener
import java.io.PrintWriter as PrintWriter
import java.awt.Point as Point
import java.awt.Color as __Color
__Color = __Color
import java.awt.event.KeyListener as __KeyListener
__KeyListener = __KeyListener
import java.awt.Toolkit as Toolkit
import java.awt.event.MouseMotionListener as __MouseMotionListener
__MouseMotionListener = __MouseMotionListener
import java.awt.event.WindowFocusListener as __WindowFocusListener
__WindowFocusListener = __WindowFocusListener
import java.awt.image.ColorModel as __ColorModel
__ColorModel = __ColorModel
import javax.swing.JRootPane as JRootPane
import java.awt.Event as Event
import java.awt.event.FocusListener as FocusListener
import java.awt.image.ImageObserver as ImageObserver
import java.awt.Insets as __Insets
__Insets = __Insets
from builtins import str
from pyquantum_helper import override
import java.awt.Component as __Component
__Component = __Component
import java.lang.Object as __object
import java.awt.ComponentOrientation as __ComponentOrientation
__ComponentOrientation = __ComponentOrientation
import java.awt.event.ContainerListener as __ContainerListener
__ContainerListener = __ContainerListener
import java.awt.event.WindowListener as WindowListener
import java.awt.event.WindowStateListener as __WindowStateListener
__WindowStateListener = __WindowStateListener
import java.awt.FocusTraversalPolicy as FocusTraversalPolicy
import java.lang.Long as __long
import java.util.Set as Set
import java.awt.Container as __Container
__Container = __Container
import java.awt.Window as __Window_Type
__Type = __Window_Type.Type
import java.awt.FontMetrics as FontMetrics
import java.awt.Color as Color
import java.awt.event.HierarchyBoundsListener as __HierarchyBoundsListener
__HierarchyBoundsListener = __HierarchyBoundsListener
import java.awt.Image as Image
import java.awt.Graphics as Graphics
import java.lang.Integer as __int
import java.awt.FocusTraversalPolicy as __FocusTraversalPolicy
__FocusTraversalPolicy = __FocusTraversalPolicy
import java.awt.ImageCapabilities as ImageCapabilities
import java.awt.Frame as __Frame
__Frame = __Frame
 
class Hiero():
    """com.badlogic.gdx.tools.hiero.Hiero"""
 
    @staticmethod
    def __wrap(java_value: __Hiero) -> 'Hiero':
        return Hiero(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Hiero):
        """
        Dynamic initializer for Hiero.
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
    def getComponentOrientation(self) -> 'ComponentOrientation':
        """public java.awt.ComponentOrientation java.awt.Component.getComponentOrientation()"""
        return 'ComponentOrientation'.__wrap(super(Component, self).getComponentOrientation())

    @staticmethod
    @overload
    def isDefaultLookAndFeelDecorated() -> bool:
        """public static boolean javax.swing.JFrame.isDefaultLookAndFeelDecorated()"""
        return bool.__wrap(__JFrame.isDefaultLookAndFeelDecorated())

    @override
    @overload
    def getLayeredPane(self) -> 'JLayeredPane':
        """public javax.swing.JLayeredPane javax.swing.JFrame.getLayeredPane()"""
        return 'JLayeredPane'.__wrap(super(JFrame, self).getLayeredPane())

    @override
    @overload
    def removeNotify(self):
        """public void java.awt.Frame.removeNotify()"""
        super(Frame, self).removeNotify()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def location(self) -> 'Point':
        """public java.awt.Point java.awt.Component.location()"""
        return 'Point'.__wrap(super(Component, self).location())

    @override
    @overload
    def isMaximumSizeSet(self) -> bool:
        """public boolean java.awt.Component.isMaximumSizeSet()"""
        return bool.__wrap(super(Component, self).isMaximumSizeSet())

    @overload
    def mouseUp(self, arg0: 'Event', arg1: int, arg2: int) -> bool:
        """public boolean java.awt.Component.mouseUp(java.awt.Event,int,int)"""
        return bool.__wrap(super(__Component, self).mouseUp(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def getHeight(self) -> int:
        """public int java.awt.Component.getHeight()"""
        return int.__wrap(super(Component, self).getHeight())

    @override
    @overload
    def addInputMethodListener(self, arg0: 'InputMethodListener'):
        """public synchronized void java.awt.Component.addInputMethodListener(java.awt.event.InputMethodListener)"""
        super(__Component, self).addInputMethodListener(arg0)

    @overload
    def createImage(self, arg0: int, arg1: int) -> 'Image':
        """public java.awt.Image java.awt.Component.createImage(int,int)"""
        return 'Image'.__wrap(super(__Component, self).createImage(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def getSize(self, arg0: 'Dimension') -> 'Dimension':
        """public java.awt.Dimension java.awt.Component.getSize(java.awt.Dimension)"""
        return 'Dimension'.__wrap(super(__Component, self).getSize(arg0))

    @override
    @overload
    def getShape(self) -> 'Shape':
        """public java.awt.Shape java.awt.Window.getShape()"""
        return 'Shape'.__wrap(super(Window, self).getShape())

    @override
    @overload
    def removePropertyChangeListener(self, arg0: str, arg1: 'PropertyChangeListener'):
        """public void java.awt.Component.removePropertyChangeListener(java.lang.String,java.beans.PropertyChangeListener)"""
        super(__Component, self).removePropertyChangeListener(arg0, arg1)

    @override
    @overload
    def disable(self):
        """public void java.awt.Component.disable()"""
        super(Component, self).disable()

    @override
    @overload
    def getAlignmentX(self) -> float:
        """public float java.awt.Container.getAlignmentX()"""
        return float.__wrap(super(Container, self).getAlignmentX())

    @override
    @overload
    def getFocusableWindowState(self) -> bool:
        """public boolean java.awt.Window.getFocusableWindowState()"""
        return bool.__wrap(super(Window, self).getFocusableWindowState())

    @override
    @overload
    def repaint(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void javax.swing.JFrame.repaint(long,int,int,int,int)"""
        super(__JFrame, self).repaint(__long.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def dispose(self):
        """public void java.awt.Window.dispose()"""
        super(Window, self).dispose()

    @override
    @overload
    def nextFocus(self):
        """public void java.awt.Component.nextFocus()"""
        super(Component, self).nextFocus()

    @override
    @overload
    def getComponentCount(self) -> int:
        """public int java.awt.Container.getComponentCount()"""
        return int.__wrap(super(Container, self).getComponentCount())

    @override
    @overload
    def setFocusTraversalKeysEnabled(self, arg0: bool):
        """public void java.awt.Component.setFocusTraversalKeysEnabled(boolean)"""
        super(__Component, self).setFocusTraversalKeysEnabled(__boolean.valueOf(arg0))

    @override
    @overload
    def setComponentOrientation(self, arg0: 'ComponentOrientation'):
        """public void java.awt.Component.setComponentOrientation(java.awt.ComponentOrientation)"""
        super(__Component, self).setComponentOrientation(arg0)

    @override
    @overload
    def setCursor(self, arg0: int):
        """public void java.awt.Frame.setCursor(int)"""
        super(__Frame, self).setCursor(__int.valueOf(arg0))

    @overload
    def inside(self, arg0: int, arg1: int) -> bool:
        """public boolean java.awt.Component.inside(int,int)"""
        return bool.__wrap(super(__Component, self).inside(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def revalidate(self):
        """public void java.awt.Component.revalidate()"""
        super(Component, self).revalidate()

    @overload
    def getLocation(self, arg0: 'Point') -> 'Point':
        """public java.awt.Point java.awt.Component.getLocation(java.awt.Point)"""
        return 'Point'.__wrap(super(__Component, self).getLocation(arg0))

    @override
    @overload
    def isAutoRequestFocus(self) -> bool:
        """public boolean java.awt.Window.isAutoRequestFocus()"""
        return bool.__wrap(super(Window, self).isAutoRequestFocus())

    @override
    @overload
    def getPropertyChangeListeners(self) -> List['PropertyChangeListener']:
        """public java.beans.PropertyChangeListener[] java.awt.Component.getPropertyChangeListeners()"""
        return List['PropertyChangeListener'].__wrap(super(Component, self).getPropertyChangeListeners())

    @overload
    def createVolatileImage(self, arg0: int, arg1: int, arg2: 'ImageCapabilities') -> 'VolatileImage':
        """public java.awt.image.VolatileImage java.awt.Component.createVolatileImage(int,int,java.awt.ImageCapabilities) throws java.awt.AWTException"""
        return 'VolatileImage'.__wrap(super(__Component, self).createVolatileImage(__int.valueOf(arg0), __int.valueOf(arg1), arg2))

    @override
    @overload
    def getOwner(self) -> 'Window':
        """public java.awt.Window java.awt.Window.getOwner()"""
        return 'Window'.__wrap(super(Window, self).getOwner())

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean java.awt.Component.isVisible()"""
        return bool.__wrap(super(Component, self).isVisible())

    @override
    @overload
    def removeComponentListener(self, arg0: 'ComponentListener'):
        """public synchronized void java.awt.Component.removeComponentListener(java.awt.event.ComponentListener)"""
        super(__Component, self).removeComponentListener(arg0)

    @override
    @overload
    def getMenuBar(self) -> 'MenuBar':
        """public java.awt.MenuBar java.awt.Frame.getMenuBar()"""
        return 'MenuBar'.__wrap(super(Frame, self).getMenuBar())

    @override
    @overload
    def getLocation(self) -> 'Point':
        """public java.awt.Point java.awt.Component.getLocation()"""
        return 'Point'.__wrap(super(Component, self).getLocation())

    @override
    @overload
    def removeWindowStateListener(self, arg0: 'WindowStateListener'):
        """public synchronized void java.awt.Window.removeWindowStateListener(java.awt.event.WindowStateListener)"""
        super(__Window, self).removeWindowStateListener(arg0)

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean java.awt.Window.isFocused()"""
        return bool.__wrap(super(Window, self).isFocused())

    @override
    @overload
    def firePropertyChange(self, arg0: str, arg1: float, arg2: float):
        """public void java.awt.Component.firePropertyChange(java.lang.String,double,double)"""
        super(__Component, self).firePropertyChange(arg0, __double.valueOf(arg1), __double.valueOf(arg2))

    @override
    @overload
    def getModalExclusionType(self) -> 'ModalExclusionType.Dialog$ModalExclusionType':
        """public java.awt.Dialog$ModalExclusionType java.awt.Window.getModalExclusionType()"""
        return 'ModalExclusionType.Dialog$ModalExclusionType'.__wrap(super(Window, self).getModalExclusionType())

    @overload
    def contains(self, arg0: 'Point') -> bool:
        """public boolean java.awt.Component.contains(java.awt.Point)"""
        return bool.__wrap(super(__Component, self).contains(arg0))

    @override
    @overload
    def setTitle(self, arg0: str):
        """public void java.awt.Frame.setTitle(java.lang.String)"""
        super(__Frame, self).setTitle(arg0)

    @override
    @overload
    def setCursor(self, arg0: 'Cursor'):
        """public void java.awt.Window.setCursor(java.awt.Cursor)"""
        super(__Window, self).setCursor(arg0)

    @override
    @overload
    def hasFocus(self) -> bool:
        """public boolean java.awt.Component.hasFocus()"""
        return bool.__wrap(super(Component, self).hasFocus())

    @override
    @overload
    def setBackground(self, arg0: 'Color'):
        """public void java.awt.Frame.setBackground(java.awt.Color)"""
        super(__Frame, self).setBackground(arg0)

    @override
    @overload
    def getColorModel(self) -> 'ColorModel':
        """public java.awt.image.ColorModel java.awt.Component.getColorModel()"""
        return 'ColorModel'.__wrap(super(Component, self).getColorModel())

    @override
    @overload
    def setLocation(self, arg0: 'Point'):
        """public void java.awt.Window.setLocation(java.awt.Point)"""
        super(__Window, self).setLocation(arg0)

    @override
    @overload
    def getHierarchyListeners(self) -> List['HierarchyListener']:
        """public synchronized java.awt.event.HierarchyListener[] java.awt.Component.getHierarchyListeners()"""
        return List['HierarchyListener'].__wrap(super(Component, self).getHierarchyListeners())

    @override
    @overload
    def getIgnoreRepaint(self) -> bool:
        """public boolean java.awt.Component.getIgnoreRepaint()"""
        return bool.__wrap(super(Component, self).getIgnoreRepaint())

    @override
    @overload
    def isFocusTraversalPolicyProvider(self) -> bool:
        """public final boolean java.awt.Container.isFocusTraversalPolicyProvider()"""
        return bool.__wrap(super(Container, self).isFocusTraversalPolicyProvider())

    @override
    @overload
    def getTransferHandler(self) -> 'TransferHandler':
        """public javax.swing.TransferHandler javax.swing.JFrame.getTransferHandler()"""
        return 'TransferHandler'.__wrap(super(JFrame, self).getTransferHandler())

    @override
    @overload
    def addHierarchyBoundsListener(self, arg0: 'HierarchyBoundsListener'):
        """public void java.awt.Component.addHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)"""
        super(__Component, self).addHierarchyBoundsListener(arg0)

    @override
    @overload
    def getWindowFocusListeners(self) -> List['WindowFocusListener']:
        """public synchronized java.awt.event.WindowFocusListener[] java.awt.Window.getWindowFocusListeners()"""
        return List['WindowFocusListener'].__wrap(super(Window, self).getWindowFocusListeners())

    @override
    @overload
    def getMaximumSize(self) -> 'Dimension':
        """public java.awt.Dimension java.awt.Container.getMaximumSize()"""
        return 'Dimension'.__wrap(super(Container, self).getMaximumSize())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def list(self, arg0: 'PrintStream', arg1: int):
        """public void java.awt.Container.list(java.io.PrintStream,int)"""
        super(__Container, self).list(arg0, __int.valueOf(arg1))

    @override
    @overload
    def doLayout(self):
        """public void java.awt.Container.doLayout()"""
        super(Container, self).doLayout()

    @override
    @overload
    def isFocusTraversable(self) -> bool:
        """public boolean java.awt.Component.isFocusTraversable()"""
        return bool.__wrap(super(Component, self).isFocusTraversable())

    @override
    @overload
    def setBounds(self, arg0: 'Rectangle'):
        """public void java.awt.Window.setBounds(java.awt.Rectangle)"""
        super(__Window, self).setBounds(arg0)

    @override
    @overload
    def setLocationRelativeTo(self, arg0: 'Component'):
        """public void java.awt.Window.setLocationRelativeTo(java.awt.Component)"""
        super(__Window, self).setLocationRelativeTo(arg0)

    @override
    @overload
    def removeFocusListener(self, arg0: 'FocusListener'):
        """public synchronized void java.awt.Component.removeFocusListener(java.awt.event.FocusListener)"""
        super(__Component, self).removeFocusListener(arg0)

    @override
    @overload
    def getInputMethodListeners(self) -> List['InputMethodListener']:
        """public synchronized java.awt.event.InputMethodListener[] java.awt.Component.getInputMethodListeners()"""
        return List['InputMethodListener'].__wrap(super(Component, self).getInputMethodListeners())

    @override
    @overload
    def invalidate(self):
        """public void java.awt.Container.invalidate()"""
        super(Container, self).invalidate()

    @override
    @overload
    def getPreferredSize(self) -> 'Dimension':
        """public java.awt.Dimension java.awt.Container.getPreferredSize()"""
        return 'Dimension'.__wrap(super(Container, self).getPreferredSize())

    @overload
    def mouseDown(self, arg0: 'Event', arg1: int, arg2: int) -> bool:
        """public boolean java.awt.Component.mouseDown(java.awt.Event,int,int)"""
        return bool.__wrap(super(__Component, self).mouseDown(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def setGlassPane(self, arg0: 'Component'):
        """public void javax.swing.JFrame.setGlassPane(java.awt.Component)"""
        super(__JFrame, self).setGlassPane(arg0)

    @overload
    def contains(self, arg0: int, arg1: int) -> bool:
        """public boolean java.awt.Component.contains(int,int)"""
        return bool.__wrap(super(__Component, self).contains(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def addMouseListener(self, arg0: 'MouseListener'):
        """public synchronized void java.awt.Component.addMouseListener(java.awt.event.MouseListener)"""
        super(__Component, self).addMouseListener(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setFocusTraversalPolicy(self, arg0: 'FocusTraversalPolicy'):
        """public void java.awt.Container.setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)"""
        super(__Container, self).setFocusTraversalPolicy(arg0)

    @override
    @overload
    def setForeground(self, arg0: 'Color'):
        """public void java.awt.Component.setForeground(java.awt.Color)"""
        super(__Component, self).setForeground(arg0)

    @override
    @overload
    def toBack(self):
        """public void java.awt.Window.toBack()"""
        super(Window, self).toBack()

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void java.awt.Window.setSize(int,int)"""
        super(__Window, self).setSize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def isFocusOwner(self) -> bool:
        """public boolean java.awt.Component.isFocusOwner()"""
        return bool.__wrap(super(Component, self).isFocusOwner())

    @overload
    def add(self, arg0: 'Component') -> 'Component':
        """public java.awt.Component java.awt.Container.add(java.awt.Component)"""
        return 'Component'.__wrap(super(__Container, self).add(arg0))

    @override
    @overload
    def addMouseMotionListener(self, arg0: 'MouseMotionListener'):
        """public synchronized void java.awt.Component.addMouseMotionListener(java.awt.event.MouseMotionListener)"""
        super(__Component, self).addMouseMotionListener(arg0)

    @override
    @overload
    def list(self, arg0: 'PrintWriter', arg1: int):
        """public void java.awt.Container.list(java.io.PrintWriter,int)"""
        super(__Container, self).list(arg0, __int.valueOf(arg1))

    @override
    @overload
    def isFontSet(self) -> bool:
        """public boolean java.awt.Component.isFontSet()"""
        return bool.__wrap(super(Component, self).isFontSet())

    @override
    @overload
    def requestFocusInWindow(self) -> bool:
        """public boolean java.awt.Component.requestFocusInWindow()"""
        return bool.__wrap(super(Component, self).requestFocusInWindow())

    @override
    @overload
    def repaint(self, arg0: int):
        """public void java.awt.Component.repaint(long)"""
        super(__Component, self).repaint(__long.valueOf(arg0))

    @override
    @overload
    def setMaximizedBounds(self, arg0: 'Rectangle'):
        """public void java.awt.Frame.setMaximizedBounds(java.awt.Rectangle)"""
        super(__Frame, self).setMaximizedBounds(arg0)

    @override
    @overload
    def removeContainerListener(self, arg0: 'ContainerListener'):
        """public synchronized void java.awt.Container.removeContainerListener(java.awt.event.ContainerListener)"""
        super(__Container, self).removeContainerListener(arg0)

    @override
    @overload
    def list(self, arg0: 'PrintWriter'):
        """public void java.awt.Component.list(java.io.PrintWriter)"""
        super(__Component, self).list(arg0)

    @override
    @overload
    def removeWindowFocusListener(self, arg0: 'WindowFocusListener'):
        """public synchronized void java.awt.Window.removeWindowFocusListener(java.awt.event.WindowFocusListener)"""
        super(__Window, self).removeWindowFocusListener(arg0)

    @override
    @overload
    def removeHierarchyListener(self, arg0: 'HierarchyListener'):
        """public void java.awt.Component.removeHierarchyListener(java.awt.event.HierarchyListener)"""
        super(__Component, self).removeHierarchyListener(arg0)

    @override
    @overload
    def getKeyListeners(self) -> List['KeyListener']:
        """public synchronized java.awt.event.KeyListener[] java.awt.Component.getKeyListeners()"""
        return List['KeyListener'].__wrap(super(Component, self).getKeyListeners())

    @override
    @overload
    def getParent(self) -> 'Container':
        """public java.awt.Container java.awt.Component.getParent()"""
        return 'Container'.__wrap(super(Component, self).getParent())

    @override
    @overload
    def getGraphicsConfiguration(self) -> 'GraphicsConfiguration':
        """public java.awt.GraphicsConfiguration java.awt.Component.getGraphicsConfiguration()"""
        return 'GraphicsConfiguration'.__wrap(super(Component, self).getGraphicsConfiguration())

    @overload
    def keyUp(self, arg0: 'Event', arg1: int) -> bool:
        """public boolean java.awt.Component.keyUp(java.awt.Event,int)"""
        return bool.__wrap(super(__Component, self).keyUp(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def firePropertyChange(self, arg0: str, arg1: int, arg2: int):
        """public void java.awt.Component.firePropertyChange(java.lang.String,short,short)"""
        super(__Component, self).firePropertyChange(arg0, __short.valueOf(arg1), __short.valueOf(arg2))

    @override
    @overload
    def setIconImage(self, arg0: 'Image'):
        """public void javax.swing.JFrame.setIconImage(java.awt.Image)"""
        super(__JFrame, self).setIconImage(arg0)

    @override
    @overload
    def minimumSize(self) -> 'Dimension':
        """public java.awt.Dimension java.awt.Container.minimumSize()"""
        return 'Dimension'.__wrap(super(Container, self).minimumSize())

    @override
    @overload
    def resize(self, arg0: 'Dimension'):
        """public void java.awt.Component.resize(java.awt.Dimension)"""
        super(__Component, self).resize(arg0)

    @override
    @overload
    def removeMouseMotionListener(self, arg0: 'MouseMotionListener'):
        """public synchronized void java.awt.Component.removeMouseMotionListener(java.awt.event.MouseMotionListener)"""
        super(__Component, self).removeMouseMotionListener(arg0)

    @override
    @overload
    def getWarningString(self) -> str:
        """public final java.lang.String java.awt.Window.getWarningString()"""
        return str.__wrap(super(Window, self).getWarningString())

    @override
    @overload
    def getBounds(self) -> 'Rectangle':
        """public java.awt.Rectangle java.awt.Component.getBounds()"""
        return 'Rectangle'.__wrap(super(Component, self).getBounds())

    @override
    @overload
    def createBufferStrategy(self, arg0: int, arg1: 'BufferCapabilities'):
        """public void java.awt.Window.createBufferStrategy(int,java.awt.BufferCapabilities) throws java.awt.AWTException"""
        super(__Window, self).createBufferStrategy(__int.valueOf(arg0), arg1)

    @override
    @overload
    def pack(self):
        """public void java.awt.Window.pack()"""
        super(Window, self).pack()

    @override
    @overload
    def getSize(self) -> 'Dimension':
        """public java.awt.Dimension java.awt.Component.getSize()"""
        return 'Dimension'.__wrap(super(Component, self).getSize())

    @override
    @overload
    def getMinimumSize(self) -> 'Dimension':
        """public java.awt.Dimension java.awt.Container.getMinimumSize()"""
        return 'Dimension'.__wrap(super(Container, self).getMinimumSize())

    @overload
    def getComponentZOrder(self, arg0: 'Component') -> int:
        """public int java.awt.Container.getComponentZOrder(java.awt.Component)"""
        return int.__wrap(super(__Container, self).getComponentZOrder(arg0))

    @override
    @overload
    def firePropertyChange(self, arg0: str, arg1: str, arg2: str):
        """public void java.awt.Component.firePropertyChange(java.lang.String,char,char)"""
        super(__Component, self).firePropertyChange(arg0, __char.valueOf(arg1), __char.valueOf(arg2))

    @override
    @overload
    def setLayout(self, arg0: 'LayoutManager'):
        """public void javax.swing.JFrame.setLayout(java.awt.LayoutManager)"""
        super(__JFrame, self).setLayout(arg0)

    @override
    @overload
    def paint(self, arg0: 'Graphics'):
        """public void java.awt.Window.paint(java.awt.Graphics)"""
        super(__Window, self).paint(arg0)

    @override
    @overload
    def addKeyListener(self, arg0: 'KeyListener'):
        """public synchronized void java.awt.Component.addKeyListener(java.awt.event.KeyListener)"""
        super(__Component, self).addKeyListener(arg0)

    @override
    @overload
    def transferFocusBackward(self):
        """public void java.awt.Component.transferFocusBackward()"""
        super(Component, self).transferFocusBackward()

    @override
    @overload
    def setContentPane(self, arg0: 'Container'):
        """public void javax.swing.JFrame.setContentPane(java.awt.Container)"""
        super(__JFrame, self).setContentPane(arg0)

    @override
    @overload
    def setAlwaysOnTop(self, arg0: bool):
        """public final void java.awt.Window.setAlwaysOnTop(boolean) throws java.lang.SecurityException"""
        super(__Window, self).setAlwaysOnTop(__boolean.valueOf(arg0))

    @override
    @overload
    def addContainerListener(self, arg0: 'ContainerListener'):
        """public synchronized void java.awt.Container.addContainerListener(java.awt.event.ContainerListener)"""
        super(__Container, self).addContainerListener(arg0)

    @override
    @overload
    def setTransferHandler(self, arg0: 'TransferHandler'):
        """public void javax.swing.JFrame.setTransferHandler(javax.swing.TransferHandler)"""
        super(__JFrame, self).setTransferHandler(arg0)

    @override
    @overload
    def requestFocus(self, arg0: 'Cause'):
        """public void java.awt.Component.requestFocus(java.awt.event.FocusEvent$Cause)"""
        super(__Component, self).requestFocus(arg0)

    @override
    @overload
    def getY(self) -> int:
        """public int java.awt.Component.getY()"""
        return int.__wrap(super(Component, self).getY())

    @override
    @overload
    def addNotify(self):
        """public void java.awt.Frame.addNotify()"""
        super(Frame, self).addNotify()

    @override
    @overload
    def setMaximumSize(self, arg0: 'Dimension'):
        """public void java.awt.Component.setMaximumSize(java.awt.Dimension)"""
        super(__Component, self).setMaximumSize(arg0)

    @override
    @overload
    def add(self, arg0: 'PopupMenu'):
        """public void java.awt.Component.add(java.awt.PopupMenu)"""
        super(__Component, self).add(arg0)

    @override
    @overload
    def getLocale(self) -> 'Locale':
        """public java.util.Locale java.awt.Window.getLocale()"""
        return 'Locale'.__wrap(super(Window, self).getLocale())

    @override
    @overload
    def addWindowStateListener(self, arg0: 'WindowStateListener'):
        """public synchronized void java.awt.Window.addWindowStateListener(java.awt.event.WindowStateListener)"""
        super(__Window, self).addWindowStateListener(arg0)

    @override
    @overload
    def getWindowStateListeners(self) -> List['WindowStateListener']:
        """public synchronized java.awt.event.WindowStateListener[] java.awt.Window.getWindowStateListeners()"""
        return List['WindowStateListener'].__wrap(super(Window, self).getWindowStateListeners())

    @override
    @overload
    def isDoubleBuffered(self) -> bool:
        """public boolean java.awt.Component.isDoubleBuffered()"""
        return bool.__wrap(super(Component, self).isDoubleBuffered())

    @overload
    def checkImage(self, arg0: 'Image', arg1: 'ImageObserver') -> int:
        """public int java.awt.Component.checkImage(java.awt.Image,java.awt.image.ImageObserver)"""
        return int.__wrap(super(__Component, self).checkImage(arg0, arg1))

    @override
    @overload
    def setFocusTraversalPolicyProvider(self, arg0: bool):
        """public final void java.awt.Container.setFocusTraversalPolicyProvider(boolean)"""
        super(__Container, self).setFocusTraversalPolicyProvider(__boolean.valueOf(arg0))

    @override
    @overload
    def getComponents(self) -> List['Component']:
        """public java.awt.Component[] java.awt.Container.getComponents()"""
        return List['Component'].__wrap(super(Container, self).getComponents())

    @overload
    def keyDown(self, arg0: 'Event', arg1: int) -> bool:
        """public boolean java.awt.Component.keyDown(java.awt.Event,int)"""
        return bool.__wrap(super(__Component, self).keyDown(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def getHierarchyBoundsListeners(self) -> List['HierarchyBoundsListener']:
        """public synchronized java.awt.event.HierarchyBoundsListener[] java.awt.Component.getHierarchyBoundsListeners()"""
        return List['HierarchyBoundsListener'].__wrap(super(Component, self).getHierarchyBoundsListeners())

    @override
    @overload
    def isShowing(self) -> bool:
        """public boolean java.awt.Window.isShowing()"""
        return bool.__wrap(super(Window, self).isShowing())

    @override
    @overload
    def getContentPane(self) -> 'Container':
        """public java.awt.Container javax.swing.JFrame.getContentPane()"""
        return 'Container'.__wrap(super(JFrame, self).getContentPane())

    @override
    @overload
    def getRootPane(self) -> 'JRootPane':
        """public javax.swing.JRootPane javax.swing.JFrame.getRootPane()"""
        return 'JRootPane'.__wrap(super(JFrame, self).getRootPane())

    @override
    @overload
    def removeWindowListener(self, arg0: 'WindowListener'):
        """public synchronized void java.awt.Window.removeWindowListener(java.awt.event.WindowListener)"""
        super(__Window, self).removeWindowListener(arg0)

    @override
    @overload
    def preferredSize(self) -> 'Dimension':
        """public java.awt.Dimension java.awt.Container.preferredSize()"""
        return 'Dimension'.__wrap(super(Container, self).preferredSize())

    @override
    @overload
    def getOwnedWindows(self) -> List['Window']:
        """public java.awt.Window[] java.awt.Window.getOwnedWindows()"""
        return List['Window'].__wrap(super(Window, self).getOwnedWindows())

    @override
    @overload
    def getInputMethodRequests(self) -> 'InputMethodRequests':
        """public java.awt.im.InputMethodRequests java.awt.Component.getInputMethodRequests()"""
        return 'InputMethodRequests'.__wrap(super(Component, self).getInputMethodRequests())

    @override
    @overload
    def getFocusTraversalPolicy(self) -> 'FocusTraversalPolicy':
        """public java.awt.FocusTraversalPolicy java.awt.Container.getFocusTraversalPolicy()"""
        return 'FocusTraversalPolicy'.__wrap(super(Container, self).getFocusTraversalPolicy())

    @override
    @overload
    def setLocale(self, arg0: 'Locale'):
        """public void java.awt.Component.setLocale(java.util.Locale)"""
        super(__Component, self).setLocale(arg0)

    @override
    @overload
    def getType(self) -> 'Type.Window$Type':
        """public java.awt.Window$Type java.awt.Window.getType()"""
        return 'Type.Window$Type'.__wrap(super(Window, self).getType())

    @override
    @overload
    def getForeground(self) -> 'Color':
        """public java.awt.Color java.awt.Component.getForeground()"""
        return 'Color'.__wrap(super(Component, self).getForeground())

    @override
    @overload
    def remove(self, arg0: 'Component'):
        """public void javax.swing.JFrame.remove(java.awt.Component)"""
        super(__JFrame, self).remove(arg0)

    @override
    @overload
    def getFocusOwner(self) -> 'Component':
        """public java.awt.Component java.awt.Window.getFocusOwner()"""
        return 'Component'.__wrap(super(Window, self).getFocusOwner())

    @override
    @overload
    def setFont(self, arg0: 'Font'):
        """public void java.awt.Container.setFont(java.awt.Font)"""
        super(__Container, self).setFont(arg0)

    @override
    @overload
    def setMixingCutoutShape(self, arg0: 'Shape'):
        """public void java.awt.Component.setMixingCutoutShape(java.awt.Shape)"""
        super(__Component, self).setMixingCutoutShape(arg0)

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String java.awt.Component.getName()"""
        return str.__wrap(super(Component, self).getName())

    @overload
    def getBounds(self, arg0: 'Rectangle') -> 'Rectangle':
        """public java.awt.Rectangle java.awt.Component.getBounds(java.awt.Rectangle)"""
        return 'Rectangle'.__wrap(super(__Component, self).getBounds(arg0))

    @override
    @overload
    def getCursorType(self) -> int:
        """public int java.awt.Frame.getCursorType()"""
        return int.__wrap(super(Frame, self).getCursorType())

    @override
    @overload
    def setFocusableWindowState(self, arg0: bool):
        """public void java.awt.Window.setFocusableWindowState(boolean)"""
        super(__Window, self).setFocusableWindowState(__boolean.valueOf(arg0))

    @override
    @overload
    def transferFocusUpCycle(self):
        """public void java.awt.Component.transferFocusUpCycle()"""
        super(Component, self).transferFocusUpCycle()

    @staticmethod
    @overload
    def setDefaultLookAndFeelDecorated(arg0: bool):
        """public static void javax.swing.JFrame.setDefaultLookAndFeelDecorated(boolean)"""
        __JFrame.setDefaultLookAndFeelDecorated(__boolean.valueOf(arg0))

    @override
    @overload
    def getMouseMotionListeners(self) -> List['MouseMotionListener']:
        """public synchronized java.awt.event.MouseMotionListener[] java.awt.Component.getMouseMotionListeners()"""
        return List['MouseMotionListener'].__wrap(super(Component, self).getMouseMotionListeners())

    @override
    @overload
    def list(self, arg0: 'PrintStream'):
        """public void java.awt.Component.list(java.io.PrintStream)"""
        super(__Component, self).list(arg0)

    @override
    @overload
    def isForegroundSet(self) -> bool:
        """public boolean java.awt.Component.isForegroundSet()"""
        return bool.__wrap(super(Component, self).isForegroundSet())

    @overload
    def mouseEnter(self, arg0: 'Event', arg1: int, arg2: int) -> bool:
        """public boolean java.awt.Component.mouseEnter(java.awt.Event,int,int)"""
        return bool.__wrap(super(__Component, self).mouseEnter(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def mouseDrag(self, arg0: 'Event', arg1: int, arg2: int) -> bool:
        """public boolean java.awt.Component.mouseDrag(java.awt.Event,int,int)"""
        return bool.__wrap(super(__Component, self).mouseDrag(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def removeKeyListener(self, arg0: 'KeyListener'):
        """public synchronized void java.awt.Component.removeKeyListener(java.awt.event.KeyListener)"""
        super(__Component, self).removeKeyListener(arg0)

    @override
    @overload
    def isPreferredSizeSet(self) -> bool:
        """public boolean java.awt.Component.isPreferredSizeSet()"""
        return bool.__wrap(super(Component, self).isPreferredSizeSet())

    @override
    @overload
    def setMinimumSize(self, arg0: 'Dimension'):
        """public void java.awt.Window.setMinimumSize(java.awt.Dimension)"""
        super(__Window, self).setMinimumSize(arg0)

    @override
    @overload
    def toFront(self):
        """public void java.awt.Window.toFront()"""
        super(Window, self).toFront()

    @override
    @overload
    def getWidth(self) -> int:
        """public int java.awt.Component.getWidth()"""
        return int.__wrap(super(Component, self).getWidth())

    @overload
    def findComponentAt(self, arg0: 'Point') -> 'Component':
        """public java.awt.Component java.awt.Container.findComponentAt(java.awt.Point)"""
        return 'Component'.__wrap(super(__Container, self).findComponentAt(arg0))

    @override
    @overload
    def update(self, arg0: 'Graphics'):
        """public void javax.swing.JFrame.update(java.awt.Graphics)"""
        super(__JFrame, self).update(arg0)

    @staticmethod
    @overload
    def getOwnerlessWindows() -> List['Window']:
        """public static java.awt.Window[] java.awt.Window.getOwnerlessWindows()"""
        return List[Window].__wrap(__Window.getOwnerlessWindows())

    @overload
    def mouseMove(self, arg0: 'Event', arg1: int, arg2: int) -> bool:
        """public boolean java.awt.Component.mouseMove(java.awt.Event,int,int)"""
        return bool.__wrap(super(__Component, self).mouseMove(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def getMouseListeners(self) -> List['MouseListener']:
        """public synchronized java.awt.event.MouseListener[] java.awt.Component.getMouseListeners()"""
        return List['MouseListener'].__wrap(super(Component, self).getMouseListeners())

    @override
    @overload
    def getTitle(self) -> str:
        """public java.lang.String java.awt.Frame.getTitle()"""
        return str.__wrap(super(Frame, self).getTitle())

    @overload
    def createImage(self, arg0: 'ImageProducer') -> 'Image':
        """public java.awt.Image java.awt.Component.createImage(java.awt.image.ImageProducer)"""
        return 'Image'.__wrap(super(__Component, self).createImage(arg0))

    @override
    @overload
    def setExtendedState(self, arg0: int):
        """public void java.awt.Frame.setExtendedState(int)"""
        super(__Frame, self).setExtendedState(__int.valueOf(arg0))

    @override
    @overload
    def setResizable(self, arg0: bool):
        """public void java.awt.Frame.setResizable(boolean)"""
        super(__Frame, self).setResizable(__boolean.valueOf(arg0))

    @overload
    def getComponentAt(self, arg0: 'Point') -> 'Component':
        """public java.awt.Component java.awt.Container.getComponentAt(java.awt.Point)"""
        return 'Component'.__wrap(super(__Container, self).getComponentAt(arg0))

    @override
    @overload
    def setModalExclusionType(self, arg0: 'ModalExclusionType'):
        """public void java.awt.Window.setModalExclusionType(java.awt.Dialog$ModalExclusionType)"""
        super(__Window, self).setModalExclusionType(arg0)

    @override
    @overload
    def getWindowListeners(self) -> List['WindowListener']:
        """public synchronized java.awt.event.WindowListener[] java.awt.Window.getWindowListeners()"""
        return List['WindowListener'].__wrap(super(Window, self).getWindowListeners())

    @override
    @overload
    def isAlwaysOnTopSupported(self) -> bool:
        """public boolean java.awt.Window.isAlwaysOnTopSupported()"""
        return bool.__wrap(super(Window, self).isAlwaysOnTopSupported())

    @override
    @overload
    def getGlassPane(self) -> 'Component':
        """public java.awt.Component javax.swing.JFrame.getGlassPane()"""
        return 'Component'.__wrap(super(JFrame, self).getGlassPane())

    @override
    @overload
    def removePropertyChangeListener(self, arg0: 'PropertyChangeListener'):
        """public void java.awt.Component.removePropertyChangeListener(java.beans.PropertyChangeListener)"""
        super(__Component, self).removePropertyChangeListener(arg0)

    @override
    @overload
    def hide(self):
        """public void java.awt.Window.hide()"""
        super(Window, self).hide()

    @override
    @overload
    def setType(self, arg0: 'Type'):
        """public void java.awt.Window.setType(java.awt.Window$Type)"""
        super(__Window, self).setType(arg0)

    @overload
    def add(self, arg0: 'Component', arg1: int) -> 'Component':
        """public java.awt.Component java.awt.Container.add(java.awt.Component,int)"""
        return 'Component'.__wrap(super(__Container, self).add(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def getAccessibleContext(self) -> 'AccessibleContext':
        """public javax.accessibility.AccessibleContext javax.swing.JFrame.getAccessibleContext()"""
        return 'AccessibleContext'.__wrap(super(JFrame, self).getAccessibleContext())

    @override
    @overload
    def list(self):
        """public void java.awt.Component.list()"""
        super(Component, self).list()

    @overload
    def findComponentAt(self, arg0: int, arg1: int) -> 'Component':
        """public java.awt.Component java.awt.Container.findComponentAt(int,int)"""
        return 'Component'.__wrap(super(__Container, self).findComponentAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def createVolatileImage(self, arg0: int, arg1: int) -> 'VolatileImage':
        """public java.awt.image.VolatileImage java.awt.Component.createVolatileImage(int,int)"""
        return 'VolatileImage'.__wrap(super(__Component, self).createVolatileImage(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def addHierarchyListener(self, arg0: 'HierarchyListener'):
        """public void java.awt.Component.addHierarchyListener(java.awt.event.HierarchyListener)"""
        super(__Component, self).addHierarchyListener(arg0)

    @override
    @overload
    def addComponentListener(self, arg0: 'ComponentListener'):
        """public synchronized void java.awt.Component.addComponentListener(java.awt.event.ComponentListener)"""
        super(__Component, self).addComponentListener(arg0)

    @override
    @overload
    def isFocusCycleRoot(self) -> bool:
        """public final boolean java.awt.Window.isFocusCycleRoot()"""
        return bool.__wrap(super(Window, self).isFocusCycleRoot())

    @override
    @overload
    def setAutoRequestFocus(self, arg0: bool):
        """public void java.awt.Window.setAutoRequestFocus(boolean)"""
        super(__Window, self).setAutoRequestFocus(__boolean.valueOf(arg0))

    @override
    @overload
    def paintComponents(self, arg0: 'Graphics'):
        """public void java.awt.Container.paintComponents(java.awt.Graphics)"""
        super(__Container, self).paintComponents(arg0)

    @override
    @overload
    def removeMouseListener(self, arg0: 'MouseListener'):
        """public synchronized void java.awt.Component.removeMouseListener(java.awt.event.MouseListener)"""
        super(__Component, self).removeMouseListener(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setComponentZOrder(self, arg0: 'Component', arg1: int):
        """public void java.awt.Container.setComponentZOrder(java.awt.Component,int)"""
        super(__Container, self).setComponentZOrder(arg0, __int.valueOf(arg1))

    @override
    @overload
    def setDropTarget(self, arg0: 'DropTarget'):
        """public synchronized void java.awt.Component.setDropTarget(java.awt.dnd.DropTarget)"""
        super(__Component, self).setDropTarget(arg0)

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void java.awt.Window.setVisible(boolean)"""
        super(__Window, self).setVisible(__boolean.valueOf(arg0))

    @overload
    def getComponentAt(self, arg0: int, arg1: int) -> 'Component':
        """public java.awt.Component java.awt.Container.getComponentAt(int,int)"""
        return 'Component'.__wrap(super(__Container, self).getComponentAt(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def isValidateRoot(self) -> bool:
        """public boolean java.awt.Window.isValidateRoot()"""
        return bool.__wrap(super(Window, self).isValidateRoot())

    @override
    @overload
    def enable(self):
        """public void java.awt.Component.enable()"""
        super(Component, self).enable()

    @override
    @overload
    def getState(self) -> int:
        """public synchronized int java.awt.Frame.getState()"""
        return int.__wrap(super(Frame, self).getState())

    @override
    @overload
    def isLocationByPlatform(self) -> bool:
        """public boolean java.awt.Window.isLocationByPlatform()"""
        return bool.__wrap(super(Window, self).isLocationByPlatform())

    @override
    @overload
    def setFocusable(self, arg0: bool):
        """public void java.awt.Component.setFocusable(boolean)"""
        super(__Component, self).setFocusable(__boolean.valueOf(arg0))

    @overload
    def gotFocus(self, arg0: 'Event', arg1: object) -> bool:
        """public boolean java.awt.Component.gotFocus(java.awt.Event,java.lang.Object)"""
        return bool.__wrap(super(__Component, self).gotFocus(arg0, arg1))

    @override
    @overload
    def setName(self, arg0: str):
        """public void java.awt.Component.setName(java.lang.String)"""
        super(__Component, self).setName(arg0)

    @override
    @overload
    def requestFocus(self):
        """public void java.awt.Component.requestFocus()"""
        super(Component, self).requestFocus()

    @override
    @overload
    def getMouseWheelListeners(self) -> List['MouseWheelListener']:
        """public synchronized java.awt.event.MouseWheelListener[] java.awt.Component.getMouseWheelListeners()"""
        return List['MouseWheelListener'].__wrap(super(Component, self).getMouseWheelListeners())

    @override
    @overload
    def countComponents(self) -> int:
        """public int java.awt.Container.countComponents()"""
        return int.__wrap(super(Container, self).countComponents())

    @override
    @overload
    def setLocation(self, arg0: int, arg1: int):
        """public void java.awt.Window.setLocation(int,int)"""
        super(__Window, self).setLocation(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getFocusTraversalKeys(self, arg0: int) -> 'Set':
        """public java.util.Set<java.awt.AWTKeyStroke> java.awt.Window.getFocusTraversalKeys(int)"""
        return 'Set'.__wrap(super(__Window, self).getFocusTraversalKeys(__int.valueOf(arg0)))

    @overload
    def isFocusCycleRoot(self, arg0: 'Container') -> bool:
        """public boolean java.awt.Container.isFocusCycleRoot(java.awt.Container)"""
        return bool.__wrap(super(__Container, self).isFocusCycleRoot(arg0))

    @override
    @overload
    def add(self, arg0: 'Component', arg1: object):
        """public void java.awt.Container.add(java.awt.Component,java.lang.Object)"""
        super(__Container, self).add(arg0, arg1)

    @overload
    def areFocusTraversalKeysSet(self, arg0: int) -> bool:
        """public boolean java.awt.Container.areFocusTraversalKeysSet(int)"""
        return bool.__wrap(super(__Container, self).areFocusTraversalKeysSet(__int.valueOf(arg0)))

    @override
    @overload
    def addFocusListener(self, arg0: 'FocusListener'):
        """public synchronized void java.awt.Component.addFocusListener(java.awt.event.FocusListener)"""
        super(__Component, self).addFocusListener(arg0)

    @override
    @overload
    def getIconImage(self) -> 'Image':
        """public java.awt.Image java.awt.Frame.getIconImage()"""
        return 'Image'.__wrap(super(Frame, self).getIconImage())

    @override
    @overload
    def setFocusCycleRoot(self, arg0: bool):
        """public final void java.awt.Window.setFocusCycleRoot(boolean)"""
        super(__Window, self).setFocusCycleRoot(__boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def move(self, arg0: int, arg1: int):
        """public void java.awt.Component.move(int,int)"""
        super(__Component, self).move(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getBaseline(self, arg0: int, arg1: int) -> int:
        """public int java.awt.Component.getBaseline(int,int)"""
        return int.__wrap(super(__Component, self).getBaseline(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def isFocusableWindow(self) -> bool:
        """public final boolean java.awt.Window.isFocusableWindow()"""
        return bool.__wrap(super(Window, self).isFocusableWindow())

    @overload
    def getMousePosition(self, arg0: bool) -> 'Point':
        """public java.awt.Point java.awt.Container.getMousePosition(boolean) throws java.awt.HeadlessException"""
        return 'Point'.__wrap(super(__Container, self).getMousePosition(__boolean.valueOf(arg0)))

    @override
    @overload
    def dispatchEvent(self, arg0: 'AWTEvent'):
        """public final void java.awt.Component.dispatchEvent(java.awt.AWTEvent)"""
        super(__Component, self).dispatchEvent(arg0)

    @override
    @overload
    def print(self, arg0: 'Graphics'):
        """public void java.awt.Container.print(java.awt.Graphics)"""
        super(__Container, self).print(arg0)

    @override
    @overload
    def getLayout(self) -> 'LayoutManager':
        """public java.awt.LayoutManager java.awt.Container.getLayout()"""
        return 'LayoutManager'.__wrap(super(Container, self).getLayout())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getIconImages(self) -> 'List':
        """public java.util.List<java.awt.Image> java.awt.Window.getIconImages()"""
        return 'List'.__wrap(super(Window, self).getIconImages())

    @override
    @overload
    def setOpacity(self, arg0: float):
        """public void java.awt.Frame.setOpacity(float)"""
        super(__Frame, self).setOpacity(__float.valueOf(arg0))

    @override
    @overload
    def applyComponentOrientation(self, arg0: 'ComponentOrientation'):
        """public void java.awt.Container.applyComponentOrientation(java.awt.ComponentOrientation)"""
        super(__Container, self).applyComponentOrientation(arg0)

    @overload
    def lostFocus(self, arg0: 'Event', arg1: object) -> bool:
        """public boolean java.awt.Component.lostFocus(java.awt.Event,java.lang.Object)"""
        return bool.__wrap(super(__Component, self).lostFocus(arg0, arg1))

    @override
    @overload
    def getX(self) -> int:
        """public int java.awt.Component.getX()"""
        return int.__wrap(super(Component, self).getX())

    @override
    @overload
    def isLightweight(self) -> bool:
        """public boolean java.awt.Component.isLightweight()"""
        return bool.__wrap(super(Component, self).isLightweight())

    @overload
    def imageUpdate(self, arg0: 'Image', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public boolean java.awt.Component.imageUpdate(java.awt.Image,int,int,int,int,int)"""
        return bool.__wrap(super(__Component, self).imageUpdate(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def getContainerListeners(self) -> List['ContainerListener']:
        """public synchronized java.awt.event.ContainerListener[] java.awt.Container.getContainerListeners()"""
        return List['ContainerListener'].__wrap(super(Container, self).getContainerListeners())

    @override
    @overload
    def firePropertyChange(self, arg0: str, arg1: int, arg2: int):
        """public void java.awt.Component.firePropertyChange(java.lang.String,byte,byte)"""
        super(__Component, self).firePropertyChange(arg0, __byte.valueOf(arg1), __byte.valueOf(arg2))

    @override
    @overload
    def bounds(self) -> 'Rectangle':
        """public java.awt.Rectangle java.awt.Component.bounds()"""
        return 'Rectangle'.__wrap(super(Component, self).bounds())

    @override
    @overload
    def getMaximizedBounds(self) -> 'Rectangle':
        """public java.awt.Rectangle java.awt.Frame.getMaximizedBounds()"""
        return 'Rectangle'.__wrap(super(Frame, self).getMaximizedBounds())

    @override
    @overload
    def getInputContext(self) -> 'InputContext':
        """public java.awt.im.InputContext java.awt.Window.getInputContext()"""
        return 'InputContext'.__wrap(super(Window, self).getInputContext())

    @override
    @overload
    def isOpaque(self) -> bool:
        """public boolean java.awt.Window.isOpaque()"""
        return bool.__wrap(super(Window, self).isOpaque())

    @override
    @overload
    def isFocusable(self) -> bool:
        """public boolean java.awt.Component.isFocusable()"""
        return bool.__wrap(super(Component, self).isFocusable())

    @staticmethod
    @overload
    def getFrames() -> List['Frame']:
        """public static java.awt.Frame[] java.awt.Frame.getFrames()"""
        return List[Frame].__wrap(__Frame.getFrames())

    @override
    @overload
    def addWindowListener(self, arg0: 'WindowListener'):
        """public synchronized void java.awt.Window.addWindowListener(java.awt.event.WindowListener)"""
        super(__Window, self).addWindowListener(arg0)

    @override
    @overload
    def repaint(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void java.awt.Component.repaint(int,int,int,int)"""
        super(__Component, self).repaint(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def getFontMetrics(self, arg0: 'Font') -> 'FontMetrics':
        """public java.awt.FontMetrics java.awt.Component.getFontMetrics(java.awt.Font)"""
        return 'FontMetrics'.__wrap(super(__Component, self).getFontMetrics(arg0))

    @overload
    def isAncestorOf(self, arg0: 'Component') -> bool:
        """public boolean java.awt.Container.isAncestorOf(java.awt.Component)"""
        return bool.__wrap(super(__Container, self).isAncestorOf(arg0))

    @override
    @overload
    def isMinimumSizeSet(self) -> bool:
        """public boolean java.awt.Component.isMinimumSizeSet()"""
        return bool.__wrap(super(Component, self).isMinimumSizeSet())

    @override
    @overload
    def getComponentListeners(self) -> List['ComponentListener']:
        """public synchronized java.awt.event.ComponentListener[] java.awt.Component.getComponentListeners()"""
        return List['ComponentListener'].__wrap(super(Component, self).getComponentListeners())

    @override
    @overload
    def insets(self) -> 'Insets':
        """public java.awt.Insets java.awt.Container.insets()"""
        return 'Insets'.__wrap(super(Container, self).insets())

    @override
    @overload
    def getTreeLock(self) -> object:
        """public final java.lang.Object java.awt.Component.getTreeLock()"""
        return object.__wrap(super(Component, self).getTreeLock())

    @overload
    def getListeners(self, arg0: 'Class') -> List['EventListener']:
        """public <T extends java.util.EventListener> T[] java.awt.Window.getListeners(java.lang.Class<T>)"""
        return List['EventListener'].__wrap(super(__Window, self).getListeners(arg0))

    @override
    @overload
    def setDefaultCloseOperation(self, arg0: int):
        """public void javax.swing.JFrame.setDefaultCloseOperation(int)"""
        super(__JFrame, self).setDefaultCloseOperation(__int.valueOf(arg0))

    @override
    @overload
    def remove(self, arg0: 'MenuComponent'):
        """public void java.awt.Frame.remove(java.awt.MenuComponent)"""
        super(__Frame, self).remove(arg0)

    @override
    @overload
    def show(self):
        """public void java.awt.Window.show()"""
        super(Window, self).show()

    @override
    @overload
    def size(self) -> 'Dimension':
        """public java.awt.Dimension java.awt.Component.size()"""
        return 'Dimension'.__wrap(super(Component, self).size())

    @override
    @overload
    def getMostRecentFocusOwner(self) -> 'Component':
        """public java.awt.Component java.awt.Window.getMostRecentFocusOwner()"""
        return 'Component'.__wrap(super(Window, self).getMostRecentFocusOwner())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.awt.Component.toString()"""
        return str.__wrap(super(Component, self).toString())

    @overload
    def checkImage(self, arg0: 'Image', arg1: int, arg2: int, arg3: 'ImageObserver') -> int:
        """public int java.awt.Component.checkImage(java.awt.Image,int,int,java.awt.image.ImageObserver)"""
        return int.__wrap(super(__Component, self).checkImage(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @override
    @overload
    def getDefaultCloseOperation(self) -> int:
        """public int javax.swing.JFrame.getDefaultCloseOperation()"""
        return int.__wrap(super(JFrame, self).getDefaultCloseOperation())

    @override
    @overload
    def isDisplayable(self) -> bool:
        """public boolean java.awt.Component.isDisplayable()"""
        return bool.__wrap(super(Component, self).isDisplayable())

    @override
    @overload
    def setJMenuBar(self, arg0: 'JMenuBar'):
        """public void javax.swing.JFrame.setJMenuBar(javax.swing.JMenuBar)"""
        super(__JFrame, self).setJMenuBar(arg0)

    @overload
    def getPropertyChangeListeners(self, arg0: str) -> List['PropertyChangeListener']:
        """public java.beans.PropertyChangeListener[] java.awt.Component.getPropertyChangeListeners(java.lang.String)"""
        return List['PropertyChangeListener'].__wrap(super(__Component, self).getPropertyChangeListeners(arg0))

    @staticmethod
    @overload
    def getWindows() -> List['Window']:
        """public static java.awt.Window[] java.awt.Window.getWindows()"""
        return List[Window].__wrap(__Window.getWindows())

    @override
    @overload
    def setState(self, arg0: int):
        """public synchronized void java.awt.Frame.setState(int)"""
        super(__Frame, self).setState(__int.valueOf(arg0))

    @override
    @overload
    def isFocusTraversalPolicySet(self) -> bool:
        """public boolean java.awt.Container.isFocusTraversalPolicySet()"""
        return bool.__wrap(super(Container, self).isFocusTraversalPolicySet())

    @override
    @overload
    def setIgnoreRepaint(self, arg0: bool):
        """public void java.awt.Component.setIgnoreRepaint(boolean)"""
        super(__Component, self).setIgnoreRepaint(__boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'String'):
        """public com.badlogic.gdx.tools.hiero.Hiero(java.lang.String[])"""
        val = __Hiero(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def removeMouseWheelListener(self, arg0: 'MouseWheelListener'):
        """public synchronized void java.awt.Component.removeMouseWheelListener(java.awt.event.MouseWheelListener)"""
        super(__Component, self).removeMouseWheelListener(arg0)

    @override
    @overload
    def getMousePosition(self) -> 'Point':
        """public java.awt.Point java.awt.Component.getMousePosition() throws java.awt.HeadlessException"""
        return 'Point'.__wrap(super(Component, self).getMousePosition())

    @override
    @overload
    def enable(self, arg0: bool):
        """public void java.awt.Component.enable(boolean)"""
        super(__Component, self).enable(__boolean.valueOf(arg0))

    @override
    @overload
    def repaint(self):
        """public void java.awt.Component.repaint()"""
        super(Component, self).repaint()

    @override
    @overload
    def addWindowFocusListener(self, arg0: 'WindowFocusListener'):
        """public synchronized void java.awt.Window.addWindowFocusListener(java.awt.event.WindowFocusListener)"""
        super(__Window, self).addWindowFocusListener(arg0)

    @override
    @overload
    def getFont(self) -> 'Font':
        """public java.awt.Font java.awt.Component.getFont()"""
        return 'Font'.__wrap(super(Component, self).getFont())

    @override
    @overload
    def getAlignmentY(self) -> float:
        """public float java.awt.Container.getAlignmentY()"""
        return float.__wrap(super(Container, self).getAlignmentY())

    @override
    @overload
    def setLayeredPane(self, arg0: 'JLayeredPane'):
        """public void javax.swing.JFrame.setLayeredPane(javax.swing.JLayeredPane)"""
        super(__JFrame, self).setLayeredPane(arg0)

    @override
    @overload
    def applyResourceBundle(self, arg0: 'ResourceBundle'):
        """public void java.awt.Window.applyResourceBundle(java.util.ResourceBundle)"""
        super(__Window, self).applyResourceBundle(arg0)

    @overload
    def getComponent(self, arg0: int) -> 'Component':
        """public java.awt.Component java.awt.Container.getComponent(int)"""
        return 'Component'.__wrap(super(__Container, self).getComponent(__int.valueOf(arg0)))

    @override
    @overload
    def getBackground(self) -> 'Color':
        """public java.awt.Color java.awt.Window.getBackground()"""
        return 'Color'.__wrap(super(Window, self).getBackground())

    @override
    @overload
    def isValid(self) -> bool:
        """public boolean java.awt.Component.isValid()"""
        return bool.__wrap(super(Component, self).isValid())

    @override
    @overload
    def getFocusCycleRootAncestor(self) -> 'Container':
        """public final java.awt.Container java.awt.Window.getFocusCycleRootAncestor()"""
        return 'Container'.__wrap(super(Window, self).getFocusCycleRootAncestor())

    @override
    @overload
    def isAlwaysOnTop(self) -> bool:
        """public final boolean java.awt.Window.isAlwaysOnTop()"""
        return bool.__wrap(super(Window, self).isAlwaysOnTop())

    @override
    @overload
    def setUndecorated(self, arg0: bool):
        """public void java.awt.Frame.setUndecorated(boolean)"""
        super(__Frame, self).setUndecorated(__boolean.valueOf(arg0))

    @override
    @overload
    def isBackgroundSet(self) -> bool:
        """public boolean java.awt.Component.isBackgroundSet()"""
        return bool.__wrap(super(Component, self).isBackgroundSet())

    @override
    @overload
    def addMouseWheelListener(self, arg0: 'MouseWheelListener'):
        """public synchronized void java.awt.Component.addMouseWheelListener(java.awt.event.MouseWheelListener)"""
        super(__Component, self).addMouseWheelListener(arg0)

    @override
    @overload
    def getOpacity(self) -> float:
        """public float java.awt.Window.getOpacity()"""
        return float.__wrap(super(Window, self).getOpacity())

    @override
    @overload
    def applyResourceBundle(self, arg0: str):
        """public void java.awt.Window.applyResourceBundle(java.lang.String)"""
        super(__Window, self).applyResourceBundle(arg0)

    @override
    @overload
    def show(self, arg0: bool):
        """public void java.awt.Component.show(boolean)"""
        super(__Component, self).show(__boolean.valueOf(arg0))

    @override
    @overload
    def setSize(self, arg0: 'Dimension'):
        """public void java.awt.Window.setSize(java.awt.Dimension)"""
        super(__Window, self).setSize(arg0)

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean java.awt.Window.isActive()"""
        return bool.__wrap(super(Window, self).isActive())

    @override
    @overload
    def printAll(self, arg0: 'Graphics'):
        """public void java.awt.Component.printAll(java.awt.Graphics)"""
        super(__Component, self).printAll(arg0)

    @override
    @overload
    def addPropertyChangeListener(self, arg0: str, arg1: 'PropertyChangeListener'):
        """public void java.awt.Window.addPropertyChangeListener(java.lang.String,java.beans.PropertyChangeListener)"""
        super(__Window, self).addPropertyChangeListener(arg0, arg1)

    @override
    @overload
    def getFocusTraversalKeysEnabled(self) -> bool:
        """public boolean java.awt.Component.getFocusTraversalKeysEnabled()"""
        return bool.__wrap(super(Component, self).getFocusTraversalKeysEnabled())

    @override
    @overload
    def setPreferredSize(self, arg0: 'Dimension'):
        """public void java.awt.Component.setPreferredSize(java.awt.Dimension)"""
        super(__Component, self).setPreferredSize(arg0)

    @override
    @overload
    def setShape(self, arg0: 'Shape'):
        """public void java.awt.Frame.setShape(java.awt.Shape)"""
        super(__Frame, self).setShape(arg0)

    @overload
    def requestFocusInWindow(self, arg0: 'Cause') -> bool:
        """public boolean java.awt.Component.requestFocusInWindow(java.awt.event.FocusEvent$Cause)"""
        return bool.__wrap(super(__Component, self).requestFocusInWindow(arg0))

    @override
    @overload
    def enableInputMethods(self, arg0: bool):
        """public void java.awt.Component.enableInputMethods(boolean)"""
        super(__Component, self).enableInputMethods(__boolean.valueOf(arg0))

    @override
    @overload
    def getExtendedState(self) -> int:
        """public int java.awt.Frame.getExtendedState()"""
        return int.__wrap(super(Frame, self).getExtendedState())

    @override
    @overload
    def firePropertyChange(self, arg0: str, arg1: int, arg2: int):
        """public void java.awt.Component.firePropertyChange(java.lang.String,long,long)"""
        super(__Component, self).firePropertyChange(arg0, __long.valueOf(arg1), __long.valueOf(arg2))

    @override
    @overload
    def getToolkit(self) -> 'Toolkit':
        """public java.awt.Toolkit java.awt.Window.getToolkit()"""
        return 'Toolkit'.__wrap(super(Window, self).getToolkit())

    @override
    @overload
    def setIconImages(self, arg0: 'List'):
        """public synchronized void java.awt.Window.setIconImages(java.util.List<? extends java.awt.Image>)"""
        super(__Window, self).setIconImages(arg0)

    @override
    @overload
    def transferFocusDownCycle(self):
        """public void java.awt.Container.transferFocusDownCycle()"""
        super(Container, self).transferFocusDownCycle()

    @override
    @overload
    def getDropTarget(self) -> 'DropTarget':
        """public synchronized java.awt.dnd.DropTarget java.awt.Component.getDropTarget()"""
        return 'DropTarget'.__wrap(super(Component, self).getDropTarget())

    @override
    @overload
    def isUndecorated(self) -> bool:
        """public boolean java.awt.Frame.isUndecorated()"""
        return bool.__wrap(super(Frame, self).isUndecorated())

    @override
    @overload
    def remove(self, arg0: int):
        """public void java.awt.Container.remove(int)"""
        super(__Container, self).remove(__int.valueOf(arg0))

    @override
    @overload
    def removeHierarchyBoundsListener(self, arg0: 'HierarchyBoundsListener'):
        """public void java.awt.Component.removeHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)"""
        super(__Component, self).removeHierarchyBoundsListener(arg0)

    @override
    @overload
    def printComponents(self, arg0: 'Graphics'):
        """public void java.awt.Container.printComponents(java.awt.Graphics)"""
        super(__Container, self).printComponents(arg0)

    @overload
    def prepareImage(self, arg0: 'Image', arg1: 'ImageObserver') -> bool:
        """public boolean java.awt.Component.prepareImage(java.awt.Image,java.awt.image.ImageObserver)"""
        return bool.__wrap(super(__Component, self).prepareImage(arg0, arg1))

    @overload
    def prepareImage(self, arg0: 'Image', arg1: int, arg2: int, arg3: 'ImageObserver') -> bool:
        """public boolean java.awt.Component.prepareImage(java.awt.Image,int,int,java.awt.image.ImageObserver)"""
        return bool.__wrap(super(__Component, self).prepareImage(arg0, __int.valueOf(arg1), __int.valueOf(arg2), arg3))

    @override
    @overload
    def getInsets(self) -> 'Insets':
        """public java.awt.Insets java.awt.Container.getInsets()"""
        return 'Insets'.__wrap(super(Container, self).getInsets())

    @overload
    def handleEvent(self, arg0: 'Event') -> bool:
        """public boolean java.awt.Component.handleEvent(java.awt.Event)"""
        return bool.__wrap(super(__Component, self).handleEvent(arg0))

    @overload
    def add(self, arg0: str, arg1: 'Component') -> 'Component':
        """public java.awt.Component java.awt.Container.add(java.lang.String,java.awt.Component)"""
        return 'Component'.__wrap(super(__Container, self).add(arg0, arg1))

    @override
    @overload
    def getCursor(self) -> 'Cursor':
        """public java.awt.Cursor java.awt.Component.getCursor()"""
        return 'Cursor'.__wrap(super(Component, self).getCursor())

    @override
    @overload
    def isResizable(self) -> bool:
        """public boolean java.awt.Frame.isResizable()"""
        return bool.__wrap(super(Frame, self).isResizable())

    @override
    @overload
    def layout(self):
        """public void java.awt.Container.layout()"""
        super(Container, self).layout()

    @override
    @overload
    def transferFocus(self):
        """public void java.awt.Component.transferFocus()"""
        super(Component, self).transferFocus()

    @override
    @overload
    def add(self, arg0: 'Component', arg1: object, arg2: int):
        """public void java.awt.Container.add(java.awt.Component,java.lang.Object,int)"""
        super(__Container, self).add(arg0, arg1, __int.valueOf(arg2))

    @override
    @overload
    def getBufferStrategy(self) -> 'BufferStrategy':
        """public java.awt.image.BufferStrategy java.awt.Window.getBufferStrategy()"""
        return 'BufferStrategy'.__wrap(super(Window, self).getBufferStrategy())

    @override
    @overload
    def isCursorSet(self) -> bool:
        """public boolean java.awt.Component.isCursorSet()"""
        return bool.__wrap(super(Component, self).isCursorSet())

    @override
    @overload
    def createBufferStrategy(self, arg0: int):
        """public void java.awt.Window.createBufferStrategy(int)"""
        super(__Window, self).createBufferStrategy(__int.valueOf(arg0))

    @override
    @overload
    def firePropertyChange(self, arg0: str, arg1: float, arg2: float):
        """public void java.awt.Component.firePropertyChange(java.lang.String,float,float)"""
        super(__Component, self).firePropertyChange(arg0, __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void java.awt.Component.setEnabled(boolean)"""
        super(__Component, self).setEnabled(__boolean.valueOf(arg0))

    @overload
    def locate(self, arg0: int, arg1: int) -> 'Component':
        """public java.awt.Component java.awt.Container.locate(int,int)"""
        return 'Component'.__wrap(super(__Container, self).locate(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def paintAll(self, arg0: 'Graphics'):
        """public void java.awt.Component.paintAll(java.awt.Graphics)"""
        super(__Component, self).paintAll(arg0)

    @overload
    def action(self, arg0: 'Event', arg1: object) -> bool:
        """public boolean java.awt.Component.action(java.awt.Event,java.lang.Object)"""
        return bool.__wrap(super(__Component, self).action(arg0, arg1))

    @override
    @overload
    def getJMenuBar(self) -> 'JMenuBar':
        """public javax.swing.JMenuBar javax.swing.JFrame.getJMenuBar()"""
        return 'JMenuBar'.__wrap(super(JFrame, self).getJMenuBar())

    @override
    @overload
    def setBounds(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void java.awt.Window.setBounds(int,int,int,int)"""
        super(__Window, self).setBounds(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def getBaselineResizeBehavior(self) -> 'BaselineResizeBehavior.Component$BaselineResizeBehavior':
        """public java.awt.Component$BaselineResizeBehavior java.awt.Component.getBaselineResizeBehavior()"""
        return 'BaselineResizeBehavior.Component$BaselineResizeBehavior'.__wrap(super(Component, self).getBaselineResizeBehavior())

    @override
    @overload
    def getLocationOnScreen(self) -> 'Point':
        """public java.awt.Point java.awt.Component.getLocationOnScreen()"""
        return 'Point'.__wrap(super(Component, self).getLocationOnScreen())

    @override
    @overload
    def getFocusListeners(self) -> List['FocusListener']:
        """public synchronized java.awt.event.FocusListener[] java.awt.Component.getFocusListeners()"""
        return List['FocusListener'].__wrap(super(Component, self).getFocusListeners())

    @override
    @overload
    def deliverEvent(self, arg0: 'Event'):
        """public void java.awt.Container.deliverEvent(java.awt.Event)"""
        super(__Container, self).deliverEvent(arg0)

    @override
    @overload
    def removeInputMethodListener(self, arg0: 'InputMethodListener'):
        """public synchronized void java.awt.Component.removeInputMethodListener(java.awt.event.InputMethodListener)"""
        super(__Component, self).removeInputMethodListener(arg0)

    @override
    @overload
    def removeAll(self):
        """public void java.awt.Container.removeAll()"""
        super(Container, self).removeAll()

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean java.awt.Component.isEnabled()"""
        return bool.__wrap(super(Component, self).isEnabled())

    @override
    @overload
    def reshape(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void java.awt.Window.reshape(int,int,int,int)"""
        super(__Window, self).reshape(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def setFocusTraversalKeys(self, arg0: int, arg1: 'Set'):
        """public void java.awt.Container.setFocusTraversalKeys(int,java.util.Set<? extends java.awt.AWTKeyStroke>)"""
        super(__Container, self).setFocusTraversalKeys(__int.valueOf(arg0), arg1)

    @override
    @overload
    def addPropertyChangeListener(self, arg0: 'PropertyChangeListener'):
        """public void java.awt.Window.addPropertyChangeListener(java.beans.PropertyChangeListener)"""
        super(__Window, self).addPropertyChangeListener(arg0)

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void java.awt.Component.resize(int,int)"""
        super(__Component, self).resize(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setMenuBar(self, arg0: 'MenuBar'):
        """public void java.awt.Frame.setMenuBar(java.awt.MenuBar)"""
        super(__Frame, self).setMenuBar(arg0)

    @override
    @overload
    def setLocationByPlatform(self, arg0: bool):
        """public void java.awt.Window.setLocationByPlatform(boolean)"""
        super(__Window, self).setLocationByPlatform(__boolean.valueOf(arg0))

    @override
    @overload
    def validate(self):
        """public void java.awt.Container.validate()"""
        super(Container, self).validate()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void com.badlogic.gdx.tools.hiero.Hiero.main(java.lang.String[]) throws java.lang.Exception"""
        __Hiero.main(arg0)

    @override
    @overload
    def getGraphics(self) -> 'Graphics':
        """public java.awt.Graphics javax.swing.JFrame.getGraphics()"""
        return 'Graphics'.__wrap(super(JFrame, self).getGraphics())

    @overload
    def postEvent(self, arg0: 'Event') -> bool:
        """public boolean java.awt.Window.postEvent(java.awt.Event)"""
        return bool.__wrap(super(__Window, self).postEvent(arg0))

    @overload
    def mouseExit(self, arg0: 'Event', arg1: int, arg2: int) -> bool:
        """public boolean java.awt.Component.mouseExit(java.awt.Event,int,int)"""
        return bool.__wrap(super(__Component, self).mouseExit(arg0, __int.valueOf(arg1), __int.valueOf(arg2))) 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.Kerning
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import com.badlogic.gdx.utils.IntIntMap as __IntIntMap
__IntIntMap = __IntIntMap
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.tools.hiero.Kerning as __Kerning
__Kerning = __Kerning
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Kerning():
    """com.badlogic.gdx.tools.hiero.Kerning"""
 
    @staticmethod
    def __wrap(java_value: __Kerning) -> 'Kerning':
        return Kerning(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Kerning):
        """
        Dynamic initializer for Kerning.
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
    def load(self, arg0: 'InputStream', arg1: int):
        """public void com.badlogic.gdx.tools.hiero.Kerning.load(java.io.InputStream,int) throws java.io.IOException"""
        super(__Kerning, self).load(arg0, __int.valueOf(arg1))

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
    def __init__(self, ):
        """public com.badlogic.gdx.tools.hiero.Kerning()"""
        val = __Kerning()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.hiero.Kerning()"""
        val = __Kerning()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getKernings(self) -> 'utils.IntIntMap':
        """public com.badlogic.gdx.utils.IntIntMap com.badlogic.gdx.tools.hiero.Kerning.getKernings()"""
        return 'utils.IntIntMap'.__wrap(super(Kerning, self).getKernings())