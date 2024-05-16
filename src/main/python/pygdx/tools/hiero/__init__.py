from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.File as File
import java.lang.String as _String
_String = _String
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = _import_once("pygdx.tools.hiero.unicodefont")

import java.lang.Integer as _int
import com.badlogic.gdx.tools.hiero.BMFontUtil as _BMFontUtil
_BMFontUtil = _BMFontUtil
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BMFontUtil():
    """com.badlogic.gdx.tools.hiero.BMFontUtil"""
 
    @staticmethod
    def _wrap(java_value: _BMFontUtil) -> 'BMFontUtil':
        return BMFontUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BMFontUtil):
        """
        Dynamic initializer for BMFontUtil.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BMFontUtil__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BMFontUtil__wrapper":
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

    @overload
    def __init__(self, arg0: 'UnicodeFont'):
        """public com.badlogic.gdx.tools.hiero.BMFontUtil(com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont)"""
        val = _BMFontUtil(arg0)
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def save(self, arg0: 'File'):
        """public void com.badlogic.gdx.tools.hiero.BMFontUtil.save(java.io.File) throws java.io.IOException"""
        super(_BMFontUtil, self).save(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.BMFontUtil
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.File as File
import java.lang.String as _String
_String = _String
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = _import_once("pygdx.tools.hiero.unicodefont")

import java.lang.Integer as _int
import com.badlogic.gdx.tools.hiero.BMFontUtil as _BMFontUtil
_BMFontUtil = _BMFontUtil
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BMFontUtil():
    """com.badlogic.gdx.tools.hiero.BMFontUtil"""
 
    @staticmethod
    def _wrap(java_value: _BMFontUtil) -> 'BMFontUtil':
        return BMFontUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BMFontUtil):
        """
        Dynamic initializer for BMFontUtil.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BMFontUtil__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BMFontUtil__wrapper":
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

    @overload
    def __init__(self, arg0: 'UnicodeFont'):
        """public com.badlogic.gdx.tools.hiero.BMFontUtil(com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont)"""
        val = _BMFontUtil(arg0)
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def save(self, arg0: 'File'):
        """public void com.badlogic.gdx.tools.hiero.BMFontUtil.save(java.io.File) throws java.io.IOException"""
        super(_BMFontUtil, self).save(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.BMFontUtil 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.Kerning
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.tools.hiero.Kerning as _Kerning
_Kerning = _Kerning
import java.lang.Integer as _int
import com.badlogic.gdx.utils.IntIntMap as _IntIntMap
_IntIntMap = _IntIntMap
import java.io.InputStream as InputStream
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Kerning():
    """com.badlogic.gdx.tools.hiero.Kerning"""
 
    @staticmethod
    def _wrap(java_value: _Kerning) -> 'Kerning':
        return Kerning(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Kerning):
        """
        Dynamic initializer for Kerning.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Kerning__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Kerning__wrapper":
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
    def getKernings(self) -> 'utils.IntIntMap':
        """public com.badlogic.gdx.utils.IntIntMap com.badlogic.gdx.tools.hiero.Kerning.getKernings()"""
        return 'utils.IntIntMap'._wrap(super(Kerning, self).getKernings())

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
    def load(self, arg0: 'InputStream', arg1: int):
        """public void com.badlogic.gdx.tools.hiero.Kerning.load(java.io.InputStream,int) throws java.io.IOException"""
        super(_Kerning, self).load(arg0, _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.hiero.Kerning()"""
        val = _Kerning()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.hiero.Kerning()"""
        val = _Kerning()
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
 
 
# CLASS: com.badlogic.gdx.tools.hiero.Hiero
import javax.accessibility.AccessibleContext as AccessibleContext
import java.awt.event.HierarchyBoundsListener as HierarchyBoundsListener
import java.awt.ComponentOrientation as _ComponentOrientation
_ComponentOrientation = _ComponentOrientation
import java.awt.image.ImageProducer as ImageProducer
import java.awt.BufferCapabilities as BufferCapabilities
import java.awt.Window as _Window
_Window = _Window
import java.awt.GraphicsConfiguration as GraphicsConfiguration
import java.awt.Graphics as _Graphics
_Graphics = _Graphics
import java.awt.Container as _Container
_Container = _Container
import java.awt.MenuComponent as MenuComponent
import java.awt.im.InputMethodRequests as _InputMethodRequests
_InputMethodRequests = _InputMethodRequests
import java.awt.FocusTraversalPolicy as _FocusTraversalPolicy
_FocusTraversalPolicy = _FocusTraversalPolicy
import java.lang.Byte as _byte
import java.awt.Dimension as Dimension
import java.awt.Font as _Font
_Font = _Font
import java.awt.event.ContainerListener as ContainerListener
import java.awt.AWTEvent as AWTEvent
import java.awt.image.ColorModel as _ColorModel
_ColorModel = _ColorModel
import java.lang.Object as _object
import java.awt.ComponentOrientation as ComponentOrientation
import java.awt.im.InputContext as _InputContext
_InputContext = _InputContext
from builtins import float
import java.awt.event.HierarchyListener as HierarchyListener
import java.awt.event.InputMethodListener as InputMethodListener
from typing import List
import com.badlogic.gdx.tools.hiero.Hiero as _Hiero
_Hiero = _Hiero
import java.awt.event.MouseWheelListener as _MouseWheelListener
_MouseWheelListener = _MouseWheelListener
import java.awt.Window.Type as Type
import java.awt.event.KeyListener as KeyListener
import java.awt.Component as Component
import java.awt.MenuBar as _MenuBar
_MenuBar = _MenuBar
from builtins import int
import java.awt.Frame as Frame
import java.awt.LayoutManager as LayoutManager
import java.awt.FontMetrics as _FontMetrics
_FontMetrics = _FontMetrics
import java.awt.Container as Container
import javax.swing.JMenuBar as JMenuBar
from builtins import type
import java.awt.image.VolatileImage as _VolatileImage
_VolatileImage = _VolatileImage
import java.awt.Shape as Shape
import java.util.ResourceBundle as ResourceBundle
import java.awt.Rectangle as Rectangle
import java.awt.event.ContainerListener as _ContainerListener
_ContainerListener = _ContainerListener
import java.awt.event.HierarchyListener as _HierarchyListener
_HierarchyListener = _HierarchyListener
import java.lang.String as _string
import java.awt.Insets as _Insets
_Insets = _Insets
import java.awt.event.ComponentListener as _ComponentListener
_ComponentListener = _ComponentListener
import java.awt.event.ComponentListener as ComponentListener
import java.awt.Frame as _Frame
_Frame = _Frame
import java.awt.event.WindowFocusListener as WindowFocusListener
from builtins import object
import java.awt.event.WindowFocusListener as _WindowFocusListener
_WindowFocusListener = _WindowFocusListener
import java.awt.event.KeyListener as _KeyListener
_KeyListener = _KeyListener
import java.awt.MenuBar as MenuBar
import java.awt.Component.BaselineResizeBehavior as BaselineResizeBehavior
import java.awt.Component as _Component_BaselineResizeBehavior
_BaselineResizeBehavior = _Component_BaselineResizeBehavior.BaselineResizeBehavior
import java.awt.Shape as _Shape
_Shape = _Shape
import java.awt.Cursor as _Cursor
_Cursor = _Cursor
import java.awt.im.InputMethodRequests as InputMethodRequests
import java.lang.Long as _long
import javax.swing.JLayeredPane as JLayeredPane
import java.util.List as List
import java.awt.event.FocusListener as _FocusListener
_FocusListener = _FocusListener
import javax.swing.TransferHandler as TransferHandler
import java.lang.Character as _char
import java.awt.event.FocusEvent.Cause as Cause
import javax.accessibility.AccessibleContext as _AccessibleContext
_AccessibleContext = _AccessibleContext
import java.awt.event.MouseWheelListener as MouseWheelListener
import java.util.Set as _Set
_Set = _Set
import java.awt.event.WindowStateListener as _WindowStateListener
_WindowStateListener = _WindowStateListener
import java.awt.image.ColorModel as ColorModel
import java.lang.Boolean as _boolean
import java.awt.event.WindowStateListener as WindowStateListener
import java.awt.event.MouseMotionListener as MouseMotionListener
import java.util.EventListener as EventListener
import javax.swing.JLayeredPane as _JLayeredPane
_JLayeredPane = _JLayeredPane
import javax.swing.JFrame as _JFrame
_JFrame = _JFrame
import java.awt.Insets as Insets
import java.awt.GraphicsConfiguration as _GraphicsConfiguration
_GraphicsConfiguration = _GraphicsConfiguration
import java.awt.dnd.DropTarget as _DropTarget
_DropTarget = _DropTarget
from builtins import bool
import java.awt.Window as Window
import java.beans.PropertyChangeListener as _PropertyChangeListener
_PropertyChangeListener = _PropertyChangeListener
import java.awt.LayoutManager as _LayoutManager
_LayoutManager = _LayoutManager
import java.awt.PopupMenu as PopupMenu
import java.util.EventListener as _EventListener
_EventListener = _EventListener
import java.awt.im.InputContext as InputContext
import java.awt.Component as _Component
_Component = _Component
import java.awt.Font as Font
import java.awt.image.VolatileImage as VolatileImage
import java.awt.dnd.DropTarget as DropTarget
import java.lang.String as _String
_String = _String
import java.awt.Dialog as _Dialog_ModalExclusionType
_ModalExclusionType = _Dialog_ModalExclusionType.ModalExclusionType
import java.util.List as _List
_List = _List
import java.lang.Float as _float
import java.awt.Cursor as Cursor
import java.awt.event.MouseListener as _MouseListener
_MouseListener = _MouseListener
import java.awt.Toolkit as _Toolkit
_Toolkit = _Toolkit
import java.io.PrintStream as PrintStream
import javax.swing.JRootPane as _JRootPane
_JRootPane = _JRootPane
import java.awt.Dimension as _Dimension
_Dimension = _Dimension
import java.awt.Color as _Color
_Color = _Color
import java.awt.image.BufferStrategy as BufferStrategy
import java.awt.Dialog.ModalExclusionType as ModalExclusionType
import java.awt.event.MouseListener as MouseListener
import java.lang.Class as _Class
_Class = _Class
import java.awt.event.WindowListener as _WindowListener
_WindowListener = _WindowListener
import java.util.Locale as Locale
import java.lang.Double as _double
import java.beans.PropertyChangeListener as PropertyChangeListener
import java.awt.Point as _Point
_Point = _Point
import java.lang.Object as _Object
_Object = _Object
import java.io.PrintWriter as PrintWriter
import java.awt.Point as Point
import java.lang.Short as _short
import java.awt.Toolkit as Toolkit
import java.awt.event.HierarchyBoundsListener as _HierarchyBoundsListener
_HierarchyBoundsListener = _HierarchyBoundsListener
import javax.swing.TransferHandler as _TransferHandler
_TransferHandler = _TransferHandler
import javax.swing.JRootPane as JRootPane
import java.awt.Rectangle as _Rectangle
_Rectangle = _Rectangle
import java.awt.Event as Event
import java.awt.event.FocusListener as FocusListener
import java.awt.image.ImageObserver as ImageObserver
from builtins import str
from pyquantum_helper import override
import java.awt.event.WindowListener as WindowListener
import java.awt.FocusTraversalPolicy as FocusTraversalPolicy
import java.awt.image.BufferStrategy as _BufferStrategy
_BufferStrategy = _BufferStrategy
import java.awt.event.MouseMotionListener as _MouseMotionListener
_MouseMotionListener = _MouseMotionListener
import java.awt.event.InputMethodListener as _InputMethodListener
_InputMethodListener = _InputMethodListener
import javax.swing.JMenuBar as _JMenuBar
_JMenuBar = _JMenuBar
import java.util.Set as Set
import java.lang.Integer as _int
import java.awt.Image as _Image
_Image = _Image
import java.awt.FontMetrics as FontMetrics
import java.awt.Color as Color
import java.awt.Window as _Window_Type
_Type = _Window_Type.Type
import java.awt.Image as Image
import java.awt.Graphics as Graphics
import java.awt.ImageCapabilities as ImageCapabilities
import java.util.Locale as _Locale
_Locale = _Locale
 
class Hiero():
    """com.badlogic.gdx.tools.hiero.Hiero"""
 
    @staticmethod
    def _wrap(java_value: _Hiero) -> 'Hiero':
        return Hiero(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Hiero):
        """
        Dynamic initializer for Hiero.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Hiero__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Hiero__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getAlignmentY(self) -> float:
        """public float java.awt.Container.getAlignmentY()"""
        return float._wrap(super(Container, self).getAlignmentY())

    @override
    @overload
    def getComponents(self) -> List['Component']:
        """public java.awt.Component[] java.awt.Container.getComponents()"""
        return List['Component']._wrap(super(Container, self).getComponents())

    @override
    @overload
    def isValid(self) -> bool:
        """public boolean java.awt.Component.isValid()"""
        return bool._wrap(super(Component, self).isValid())

    @override
    @overload
    def removeNotify(self):
        """public void java.awt.Frame.removeNotify()"""
        super(Frame, self).removeNotify()

    @override
    @overload
    def setFocusTraversalKeys(self, arg0: int, arg1: 'Set'):
        """public void java.awt.Container.setFocusTraversalKeys(int,java.util.Set<? extends java.awt.AWTKeyStroke>)"""
        super(_Container, self).setFocusTraversalKeys(_int.valueOf(arg0), arg1)

    @override
    @overload
    def getWidth(self) -> int:
        """public int java.awt.Component.getWidth()"""
        return int._wrap(super(Component, self).getWidth())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def addPropertyChangeListener(self, arg0: str, arg1: 'PropertyChangeListener'):
        """public void java.awt.Window.addPropertyChangeListener(java.lang.String,java.beans.PropertyChangeListener)"""
        super(_Window, self).addPropertyChangeListener(arg0, arg1)

    @override
    @overload
    def getIconImages(self) -> 'List':
        """public java.util.List<java.awt.Image> java.awt.Window.getIconImages()"""
        return 'List'._wrap(super(Window, self).getIconImages())

    @override
    @overload
    def firePropertyChange(self, arg0: str, arg1: str, arg2: str):
        """public void java.awt.Component.firePropertyChange(java.lang.String,char,char)"""
        super(_Component, self).firePropertyChange(arg0, _char.valueOf(arg1), _char.valueOf(arg2))

    @overload
    def getBounds(self, arg0: 'Rectangle') -> 'Rectangle':
        """public java.awt.Rectangle java.awt.Component.getBounds(java.awt.Rectangle)"""
        return 'Rectangle'._wrap(super(_Component, self).getBounds(arg0))

    @override
    @overload
    def remove(self, arg0: 'MenuComponent'):
        """public void java.awt.Frame.remove(java.awt.MenuComponent)"""
        super(_Frame, self).remove(arg0)

    @override
    @overload
    def list(self, arg0: 'PrintStream', arg1: int):
        """public void java.awt.Container.list(java.io.PrintStream,int)"""
        super(_Container, self).list(arg0, _int.valueOf(arg1))

    @override
    @overload
    def setLocation(self, arg0: 'Point'):
        """public void java.awt.Window.setLocation(java.awt.Point)"""
        super(_Window, self).setLocation(arg0)

    @override
    @overload
    def getFocusTraversalPolicy(self) -> 'FocusTraversalPolicy':
        """public java.awt.FocusTraversalPolicy java.awt.Container.getFocusTraversalPolicy()"""
        return 'FocusTraversalPolicy'._wrap(super(Container, self).getFocusTraversalPolicy())

    @override
    @overload
    def getParent(self) -> 'Container':
        """public java.awt.Container java.awt.Component.getParent()"""
        return 'Container'._wrap(super(Component, self).getParent())

    @override
    @overload
    def getInputContext(self) -> 'InputContext':
        """public java.awt.im.InputContext java.awt.Window.getInputContext()"""
        return 'InputContext'._wrap(super(Window, self).getInputContext())

    @override
    @overload
    def getLayeredPane(self) -> 'JLayeredPane':
        """public javax.swing.JLayeredPane javax.swing.JFrame.getLayeredPane()"""
        return 'JLayeredPane'._wrap(super(JFrame, self).getLayeredPane())

    @override
    @overload
    def firePropertyChange(self, arg0: str, arg1: float, arg2: float):
        """public void java.awt.Component.firePropertyChange(java.lang.String,float,float)"""
        super(_Component, self).firePropertyChange(arg0, _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def disable(self):
        """public void java.awt.Component.disable()"""
        super(Component, self).disable()

    @override
    @overload
    def add(self, arg0: 'Component', arg1: object):
        """public void java.awt.Container.add(java.awt.Component,java.lang.Object)"""
        super(_Container, self).add(arg0, arg1)

    @override
    @overload
    def dispose(self):
        """public void java.awt.Window.dispose()"""
        super(Window, self).dispose()

    @override
    @overload
    def setGlassPane(self, arg0: 'Component'):
        """public void javax.swing.JFrame.setGlassPane(java.awt.Component)"""
        super(_JFrame, self).setGlassPane(arg0)

    @override
    @overload
    def getHierarchyListeners(self) -> List['HierarchyListener']:
        """public synchronized java.awt.event.HierarchyListener[] java.awt.Component.getHierarchyListeners()"""
        return List['HierarchyListener']._wrap(super(Component, self).getHierarchyListeners())

    @override
    @overload
    def getLocale(self) -> 'Locale':
        """public java.util.Locale java.awt.Window.getLocale()"""
        return 'Locale'._wrap(super(Window, self).getLocale())

    @override
    @overload
    def nextFocus(self):
        """public void java.awt.Component.nextFocus()"""
        super(Component, self).nextFocus()

    @override
    @overload
    def isAlwaysOnTopSupported(self) -> bool:
        """public boolean java.awt.Window.isAlwaysOnTopSupported()"""
        return bool._wrap(super(Window, self).isAlwaysOnTopSupported())

    @override
    @overload
    def revalidate(self):
        """public void java.awt.Component.revalidate()"""
        super(Component, self).revalidate()

    @override
    @overload
    def getDefaultCloseOperation(self) -> int:
        """public int javax.swing.JFrame.getDefaultCloseOperation()"""
        return int._wrap(super(JFrame, self).getDefaultCloseOperation())

    @override
    @overload
    def getFocusableWindowState(self) -> bool:
        """public boolean java.awt.Window.getFocusableWindowState()"""
        return bool._wrap(super(Window, self).getFocusableWindowState())

    @override
    @overload
    def isDisplayable(self) -> bool:
        """public boolean java.awt.Component.isDisplayable()"""
        return bool._wrap(super(Component, self).isDisplayable())

    @staticmethod
    @overload
    def setDefaultLookAndFeelDecorated(arg0: bool):
        """public static void javax.swing.JFrame.setDefaultLookAndFeelDecorated(boolean)"""
        _JFrame.setDefaultLookAndFeelDecorated(_boolean.valueOf(arg0))

    @override
    @overload
    def getBounds(self) -> 'Rectangle':
        """public java.awt.Rectangle java.awt.Component.getBounds()"""
        return 'Rectangle'._wrap(super(Component, self).getBounds())

    @override
    @overload
    def removeMouseMotionListener(self, arg0: 'MouseMotionListener'):
        """public synchronized void java.awt.Component.removeMouseMotionListener(java.awt.event.MouseMotionListener)"""
        super(_Component, self).removeMouseMotionListener(arg0)

    @override
    @overload
    def getDropTarget(self) -> 'DropTarget':
        """public synchronized java.awt.dnd.DropTarget java.awt.Component.getDropTarget()"""
        return 'DropTarget'._wrap(super(Component, self).getDropTarget())

    @override
    @overload
    def isFontSet(self) -> bool:
        """public boolean java.awt.Component.isFontSet()"""
        return bool._wrap(super(Component, self).isFontSet())

    @overload
    def mouseUp(self, arg0: 'Event', arg1: int, arg2: int) -> bool:
        """public boolean java.awt.Component.mouseUp(java.awt.Event,int,int)"""
        return bool._wrap(super(_Component, self).mouseUp(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def setIgnoreRepaint(self, arg0: bool):
        """public void java.awt.Component.setIgnoreRepaint(boolean)"""
        super(_Component, self).setIgnoreRepaint(_boolean.valueOf(arg0))

    @override
    @overload
    def getPropertyChangeListeners(self) -> List['PropertyChangeListener']:
        """public java.beans.PropertyChangeListener[] java.awt.Component.getPropertyChangeListeners()"""
        return List['PropertyChangeListener']._wrap(super(Component, self).getPropertyChangeListeners())

    @override
    @overload
    def isBackgroundSet(self) -> bool:
        """public boolean java.awt.Component.isBackgroundSet()"""
        return bool._wrap(super(Component, self).isBackgroundSet())

    @override
    @overload
    def getLocation(self) -> 'Point':
        """public java.awt.Point java.awt.Component.getLocation()"""
        return 'Point'._wrap(super(Component, self).getLocation())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def location(self) -> 'Point':
        """public java.awt.Point java.awt.Component.location()"""
        return 'Point'._wrap(super(Component, self).location())

    @override
    @overload
    def getComponentOrientation(self) -> 'ComponentOrientation':
        """public java.awt.ComponentOrientation java.awt.Component.getComponentOrientation()"""
        return 'ComponentOrientation'._wrap(super(Component, self).getComponentOrientation())

    @override
    @overload
    def addHierarchyListener(self, arg0: 'HierarchyListener'):
        """public void java.awt.Component.addHierarchyListener(java.awt.event.HierarchyListener)"""
        super(_Component, self).addHierarchyListener(arg0)

    @override
    @overload
    def setExtendedState(self, arg0: int):
        """public void java.awt.Frame.setExtendedState(int)"""
        super(_Frame, self).setExtendedState(_int.valueOf(arg0))

    @override
    @overload
    def setComponentOrientation(self, arg0: 'ComponentOrientation'):
        """public void java.awt.Component.setComponentOrientation(java.awt.ComponentOrientation)"""
        super(_Component, self).setComponentOrientation(arg0)

    @override
    @overload
    def show(self, arg0: bool):
        """public void java.awt.Component.show(boolean)"""
        super(_Component, self).show(_boolean.valueOf(arg0))

    @override
    @overload
    def setAutoRequestFocus(self, arg0: bool):
        """public void java.awt.Window.setAutoRequestFocus(boolean)"""
        super(_Window, self).setAutoRequestFocus(_boolean.valueOf(arg0))

    @overload
    def locate(self, arg0: int, arg1: int) -> 'Component':
        """public java.awt.Component java.awt.Container.locate(int,int)"""
        return 'Component'._wrap(super(_Container, self).locate(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def keyDown(self, arg0: 'Event', arg1: int) -> bool:
        """public boolean java.awt.Component.keyDown(java.awt.Event,int)"""
        return bool._wrap(super(_Component, self).keyDown(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def setBackground(self, arg0: 'Color'):
        """public void java.awt.Frame.setBackground(java.awt.Color)"""
        super(_Frame, self).setBackground(arg0)

    @override
    @overload
    def getLayout(self) -> 'LayoutManager':
        """public java.awt.LayoutManager java.awt.Container.getLayout()"""
        return 'LayoutManager'._wrap(super(Container, self).getLayout())

    @override
    @overload
    def preferredSize(self) -> 'Dimension':
        """public java.awt.Dimension java.awt.Container.preferredSize()"""
        return 'Dimension'._wrap(super(Container, self).preferredSize())

    @override
    @overload
    def reshape(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void java.awt.Window.reshape(int,int,int,int)"""
        super(_Window, self).reshape(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def repaint(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void java.awt.Component.repaint(int,int,int,int)"""
        super(_Component, self).repaint(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @overload
    def requestFocusInWindow(self, arg0: 'Cause') -> bool:
        """public boolean java.awt.Component.requestFocusInWindow(java.awt.event.FocusEvent$Cause)"""
        return bool._wrap(super(_Component, self).requestFocusInWindow(arg0))

    @override
    @overload
    def remove(self, arg0: int):
        """public void java.awt.Container.remove(int)"""
        super(_Container, self).remove(_int.valueOf(arg0))

    @override
    @overload
    def firePropertyChange(self, arg0: str, arg1: int, arg2: int):
        """public void java.awt.Component.firePropertyChange(java.lang.String,long,long)"""
        super(_Component, self).firePropertyChange(arg0, _long.valueOf(arg1), _long.valueOf(arg2))

    @override
    @overload
    def getBaselineResizeBehavior(self) -> 'BaselineResizeBehavior.Component$BaselineResizeBehavior':
        """public java.awt.Component$BaselineResizeBehavior java.awt.Component.getBaselineResizeBehavior()"""
        return 'BaselineResizeBehavior.Component$BaselineResizeBehavior'._wrap(super(Component, self).getBaselineResizeBehavior())

    @override
    @overload
    def setLayout(self, arg0: 'LayoutManager'):
        """public void javax.swing.JFrame.setLayout(java.awt.LayoutManager)"""
        super(_JFrame, self).setLayout(arg0)

    @overload
    def keyUp(self, arg0: 'Event', arg1: int) -> bool:
        """public boolean java.awt.Component.keyUp(java.awt.Event,int)"""
        return bool._wrap(super(_Component, self).keyUp(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def getToolkit(self) -> 'Toolkit':
        """public java.awt.Toolkit java.awt.Window.getToolkit()"""
        return 'Toolkit'._wrap(super(Window, self).getToolkit())

    @override
    @overload
    def getCursorType(self) -> int:
        """public int java.awt.Frame.getCursorType()"""
        return int._wrap(super(Frame, self).getCursorType())

    @override
    @overload
    def getFocusOwner(self) -> 'Component':
        """public java.awt.Component java.awt.Window.getFocusOwner()"""
        return 'Component'._wrap(super(Window, self).getFocusOwner())

    @staticmethod
    @overload
    def getWindows() -> List['Window']:
        """public static java.awt.Window[] java.awt.Window.getWindows()"""
        return List[Window]._wrap(_Window.getWindows())

    @override
    @overload
    def doLayout(self):
        """public void java.awt.Container.doLayout()"""
        super(Container, self).doLayout()

    @override
    @overload
    def getBackground(self) -> 'Color':
        """public java.awt.Color java.awt.Window.getBackground()"""
        return 'Color'._wrap(super(Window, self).getBackground())

    @override
    @overload
    def repaint(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void javax.swing.JFrame.repaint(long,int,int,int,int)"""
        super(_JFrame, self).repaint(_long.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4))

    @override
    @overload
    def setTitle(self, arg0: str):
        """public void java.awt.Frame.setTitle(java.lang.String)"""
        super(_Frame, self).setTitle(arg0)

    @override
    @overload
    def getFocusCycleRootAncestor(self) -> 'Container':
        """public final java.awt.Container java.awt.Window.getFocusCycleRootAncestor()"""
        return 'Container'._wrap(super(Window, self).getFocusCycleRootAncestor())

    @overload
    def checkImage(self, arg0: 'Image', arg1: int, arg2: int, arg3: 'ImageObserver') -> int:
        """public int java.awt.Component.checkImage(java.awt.Image,int,int,java.awt.image.ImageObserver)"""
        return int._wrap(super(_Component, self).checkImage(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @override
    @overload
    def setAlwaysOnTop(self, arg0: bool):
        """public final void java.awt.Window.setAlwaysOnTop(boolean) throws java.lang.SecurityException"""
        super(_Window, self).setAlwaysOnTop(_boolean.valueOf(arg0))

    @override
    @overload
    def getFocusTraversalKeysEnabled(self) -> bool:
        """public boolean java.awt.Component.getFocusTraversalKeysEnabled()"""
        return bool._wrap(super(Component, self).getFocusTraversalKeysEnabled())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getHeight(self) -> int:
        """public int java.awt.Component.getHeight()"""
        return int._wrap(super(Component, self).getHeight())

    @override
    @overload
    def invalidate(self):
        """public void java.awt.Container.invalidate()"""
        super(Container, self).invalidate()

    @override
    @overload
    def createBufferStrategy(self, arg0: int, arg1: 'BufferCapabilities'):
        """public void java.awt.Window.createBufferStrategy(int,java.awt.BufferCapabilities) throws java.awt.AWTException"""
        super(_Window, self).createBufferStrategy(_int.valueOf(arg0), arg1)

    @overload
    def getComponent(self, arg0: int) -> 'Component':
        """public java.awt.Component java.awt.Container.getComponent(int)"""
        return 'Component'._wrap(super(_Container, self).getComponent(_int.valueOf(arg0)))

    @override
    @overload
    def setResizable(self, arg0: bool):
        """public void java.awt.Frame.setResizable(boolean)"""
        super(_Frame, self).setResizable(_boolean.valueOf(arg0))

    @override
    @overload
    def setMaximizedBounds(self, arg0: 'Rectangle'):
        """public void java.awt.Frame.setMaximizedBounds(java.awt.Rectangle)"""
        super(_Frame, self).setMaximizedBounds(arg0)

    @overload
    def getListeners(self, arg0: 'Class') -> List['EventListener']:
        """public <T extends java.util.EventListener> T[] java.awt.Window.getListeners(java.lang.Class<T>)"""
        return List['EventListener']._wrap(super(_Window, self).getListeners(arg0))

    @override
    @overload
    def toBack(self):
        """public void java.awt.Window.toBack()"""
        super(Window, self).toBack()

    @override
    @overload
    def isFocused(self) -> bool:
        """public boolean java.awt.Window.isFocused()"""
        return bool._wrap(super(Window, self).isFocused())

    @override
    @overload
    def removePropertyChangeListener(self, arg0: 'PropertyChangeListener'):
        """public void java.awt.Component.removePropertyChangeListener(java.beans.PropertyChangeListener)"""
        super(_Component, self).removePropertyChangeListener(arg0)

    @override
    @overload
    def applyComponentOrientation(self, arg0: 'ComponentOrientation'):
        """public void java.awt.Container.applyComponentOrientation(java.awt.ComponentOrientation)"""
        super(_Container, self).applyComponentOrientation(arg0)

    @override
    @overload
    def list(self, arg0: 'PrintStream'):
        """public void java.awt.Component.list(java.io.PrintStream)"""
        super(_Component, self).list(arg0)

    @override
    @overload
    def removeMouseListener(self, arg0: 'MouseListener'):
        """public synchronized void java.awt.Component.removeMouseListener(java.awt.event.MouseListener)"""
        super(_Component, self).removeMouseListener(arg0)

    @override
    @overload
    def getMostRecentFocusOwner(self) -> 'Component':
        """public java.awt.Component java.awt.Window.getMostRecentFocusOwner()"""
        return 'Component'._wrap(super(Window, self).getMostRecentFocusOwner())

    @override
    @overload
    def list(self, arg0: 'PrintWriter'):
        """public void java.awt.Component.list(java.io.PrintWriter)"""
        super(_Component, self).list(arg0)

    @override
    @overload
    def getKeyListeners(self) -> List['KeyListener']:
        """public synchronized java.awt.event.KeyListener[] java.awt.Component.getKeyListeners()"""
        return List['KeyListener']._wrap(super(Component, self).getKeyListeners())

    @override
    @overload
    def firePropertyChange(self, arg0: str, arg1: float, arg2: float):
        """public void java.awt.Component.firePropertyChange(java.lang.String,double,double)"""
        super(_Component, self).firePropertyChange(arg0, _double.valueOf(arg1), _double.valueOf(arg2))

    @override
    @overload
    def list(self, arg0: 'PrintWriter', arg1: int):
        """public void java.awt.Container.list(java.io.PrintWriter,int)"""
        super(_Container, self).list(arg0, _int.valueOf(arg1))

    @override
    @overload
    def createBufferStrategy(self, arg0: int):
        """public void java.awt.Window.createBufferStrategy(int)"""
        super(_Window, self).createBufferStrategy(_int.valueOf(arg0))

    @overload
    def checkImage(self, arg0: 'Image', arg1: 'ImageObserver') -> int:
        """public int java.awt.Component.checkImage(java.awt.Image,java.awt.image.ImageObserver)"""
        return int._wrap(super(_Component, self).checkImage(arg0, arg1))

    @override
    @overload
    def removeFocusListener(self, arg0: 'FocusListener'):
        """public synchronized void java.awt.Component.removeFocusListener(java.awt.event.FocusListener)"""
        super(_Component, self).removeFocusListener(arg0)

    @overload
    def mouseDown(self, arg0: 'Event', arg1: int, arg2: int) -> bool:
        """public boolean java.awt.Component.mouseDown(java.awt.Event,int,int)"""
        return bool._wrap(super(_Component, self).mouseDown(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def setState(self, arg0: int):
        """public synchronized void java.awt.Frame.setState(int)"""
        super(_Frame, self).setState(_int.valueOf(arg0))

    @override
    @overload
    def getMenuBar(self) -> 'MenuBar':
        """public java.awt.MenuBar java.awt.Frame.getMenuBar()"""
        return 'MenuBar'._wrap(super(Frame, self).getMenuBar())

    @staticmethod
    @overload
    def getFrames() -> List['Frame']:
        """public static java.awt.Frame[] java.awt.Frame.getFrames()"""
        return List[Frame]._wrap(_Frame.getFrames())

    @override
    @overload
    def setIconImages(self, arg0: 'List'):
        """public synchronized void java.awt.Window.setIconImages(java.util.List<? extends java.awt.Image>)"""
        super(_Window, self).setIconImages(arg0)

    @override
    @overload
    def getTreeLock(self) -> object:
        """public final java.lang.Object java.awt.Component.getTreeLock()"""
        return object._wrap(super(Component, self).getTreeLock())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getFocusTraversalKeys(self, arg0: int) -> 'Set':
        """public java.util.Set<java.awt.AWTKeyStroke> java.awt.Window.getFocusTraversalKeys(int)"""
        return 'Set'._wrap(super(_Window, self).getFocusTraversalKeys(_int.valueOf(arg0)))

    @overload
    def contains(self, arg0: 'Point') -> bool:
        """public boolean java.awt.Component.contains(java.awt.Point)"""
        return bool._wrap(super(_Component, self).contains(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setFocusCycleRoot(self, arg0: bool):
        """public final void java.awt.Window.setFocusCycleRoot(boolean)"""
        super(_Window, self).setFocusCycleRoot(_boolean.valueOf(arg0))

    @override
    @overload
    def firePropertyChange(self, arg0: str, arg1: int, arg2: int):
        """public void java.awt.Component.firePropertyChange(java.lang.String,short,short)"""
        super(_Component, self).firePropertyChange(arg0, _short.valueOf(arg1), _short.valueOf(arg2))

    @override
    @overload
    def removeWindowListener(self, arg0: 'WindowListener'):
        """public synchronized void java.awt.Window.removeWindowListener(java.awt.event.WindowListener)"""
        super(_Window, self).removeWindowListener(arg0)

    @override
    @overload
    def dispatchEvent(self, arg0: 'AWTEvent'):
        """public final void java.awt.Component.dispatchEvent(java.awt.AWTEvent)"""
        super(_Component, self).dispatchEvent(arg0)

    @override
    @overload
    def removeContainerListener(self, arg0: 'ContainerListener'):
        """public synchronized void java.awt.Container.removeContainerListener(java.awt.event.ContainerListener)"""
        super(_Container, self).removeContainerListener(arg0)

    @override
    @overload
    def getGraphicsConfiguration(self) -> 'GraphicsConfiguration':
        """public java.awt.GraphicsConfiguration java.awt.Component.getGraphicsConfiguration()"""
        return 'GraphicsConfiguration'._wrap(super(Component, self).getGraphicsConfiguration())

    @override
    @overload
    def getShape(self) -> 'Shape':
        """public java.awt.Shape java.awt.Window.getShape()"""
        return 'Shape'._wrap(super(Window, self).getShape())

    @override
    @overload
    def pack(self):
        """public void java.awt.Window.pack()"""
        super(Window, self).pack()

    @override
    @overload
    def removeWindowFocusListener(self, arg0: 'WindowFocusListener'):
        """public synchronized void java.awt.Window.removeWindowFocusListener(java.awt.event.WindowFocusListener)"""
        super(_Window, self).removeWindowFocusListener(arg0)

    @overload
    def findComponentAt(self, arg0: 'Point') -> 'Component':
        """public java.awt.Component java.awt.Container.findComponentAt(java.awt.Point)"""
        return 'Component'._wrap(super(_Container, self).findComponentAt(arg0))

    @override
    @overload
    def resize(self, arg0: int, arg1: int):
        """public void java.awt.Component.resize(int,int)"""
        super(_Component, self).resize(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def imageUpdate(self, arg0: 'Image', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> bool:
        """public boolean java.awt.Component.imageUpdate(java.awt.Image,int,int,int,int,int)"""
        return bool._wrap(super(_Component, self).imageUpdate(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5)))

    @override
    @overload
    def getGraphics(self) -> 'Graphics':
        """public java.awt.Graphics javax.swing.JFrame.getGraphics()"""
        return 'Graphics'._wrap(super(JFrame, self).getGraphics())

    @override
    @overload
    def transferFocusBackward(self):
        """public void java.awt.Component.transferFocusBackward()"""
        super(Component, self).transferFocusBackward()

    @override
    @overload
    def isOpaque(self) -> bool:
        """public boolean java.awt.Window.isOpaque()"""
        return bool._wrap(super(Window, self).isOpaque())

    @override
    @overload
    def getOwnedWindows(self) -> List['Window']:
        """public java.awt.Window[] java.awt.Window.getOwnedWindows()"""
        return List['Window']._wrap(super(Window, self).getOwnedWindows())

    @overload
    def getPropertyChangeListeners(self, arg0: str) -> List['PropertyChangeListener']:
        """public java.beans.PropertyChangeListener[] java.awt.Component.getPropertyChangeListeners(java.lang.String)"""
        return List['PropertyChangeListener']._wrap(super(_Component, self).getPropertyChangeListeners(arg0))

    @override
    @overload
    def remove(self, arg0: 'Component'):
        """public void javax.swing.JFrame.remove(java.awt.Component)"""
        super(_JFrame, self).remove(arg0)

    @override
    @overload
    def isLocationByPlatform(self) -> bool:
        """public boolean java.awt.Window.isLocationByPlatform()"""
        return bool._wrap(super(Window, self).isLocationByPlatform())

    @override
    @overload
    def addComponentListener(self, arg0: 'ComponentListener'):
        """public synchronized void java.awt.Component.addComponentListener(java.awt.event.ComponentListener)"""
        super(_Component, self).addComponentListener(arg0)

    @override
    @overload
    def setCursor(self, arg0: 'Cursor'):
        """public void java.awt.Window.setCursor(java.awt.Cursor)"""
        super(_Window, self).setCursor(arg0)

    @override
    @overload
    def addNotify(self):
        """public void java.awt.Frame.addNotify()"""
        super(Frame, self).addNotify()

    @override
    @overload
    def getFont(self) -> 'Font':
        """public java.awt.Font java.awt.Component.getFont()"""
        return 'Font'._wrap(super(Component, self).getFont())

    @staticmethod
    @overload
    def isDefaultLookAndFeelDecorated() -> bool:
        """public static boolean javax.swing.JFrame.isDefaultLookAndFeelDecorated()"""
        return bool._wrap(_JFrame.isDefaultLookAndFeelDecorated())

    @overload
    def prepareImage(self, arg0: 'Image', arg1: int, arg2: int, arg3: 'ImageObserver') -> bool:
        """public boolean java.awt.Component.prepareImage(java.awt.Image,int,int,java.awt.image.ImageObserver)"""
        return bool._wrap(super(_Component, self).prepareImage(arg0, _int.valueOf(arg1), _int.valueOf(arg2), arg3))

    @override
    @overload
    def setMaximumSize(self, arg0: 'Dimension'):
        """public void java.awt.Component.setMaximumSize(java.awt.Dimension)"""
        super(_Component, self).setMaximumSize(arg0)

    @override
    @overload
    def setForeground(self, arg0: 'Color'):
        """public void java.awt.Component.setForeground(java.awt.Color)"""
        super(_Component, self).setForeground(arg0)

    @overload
    def mouseDrag(self, arg0: 'Event', arg1: int, arg2: int) -> bool:
        """public boolean java.awt.Component.mouseDrag(java.awt.Event,int,int)"""
        return bool._wrap(super(_Component, self).mouseDrag(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def setSize(self, arg0: 'Dimension'):
        """public void java.awt.Window.setSize(java.awt.Dimension)"""
        super(_Window, self).setSize(arg0)

    @overload
    def createVolatileImage(self, arg0: int, arg1: int, arg2: 'ImageCapabilities') -> 'VolatileImage':
        """public java.awt.image.VolatileImage java.awt.Component.createVolatileImage(int,int,java.awt.ImageCapabilities) throws java.awt.AWTException"""
        return 'VolatileImage'._wrap(super(_Component, self).createVolatileImage(_int.valueOf(arg0), _int.valueOf(arg1), arg2))

    @override
    @overload
    def bounds(self) -> 'Rectangle':
        """public java.awt.Rectangle java.awt.Component.bounds()"""
        return 'Rectangle'._wrap(super(Component, self).bounds())

    @override
    @overload
    def add(self, arg0: 'PopupMenu'):
        """public void java.awt.Component.add(java.awt.PopupMenu)"""
        super(_Component, self).add(arg0)

    @override
    @overload
    def isVisible(self) -> bool:
        """public boolean java.awt.Component.isVisible()"""
        return bool._wrap(super(Component, self).isVisible())

    @override
    @overload
    def setDropTarget(self, arg0: 'DropTarget'):
        """public synchronized void java.awt.Component.setDropTarget(java.awt.dnd.DropTarget)"""
        super(_Component, self).setDropTarget(arg0)

    @override
    @overload
    def isFocusableWindow(self) -> bool:
        """public final boolean java.awt.Window.isFocusableWindow()"""
        return bool._wrap(super(Window, self).isFocusableWindow())

    @override
    @overload
    def getLocationOnScreen(self) -> 'Point':
        """public java.awt.Point java.awt.Component.getLocationOnScreen()"""
        return 'Point'._wrap(super(Component, self).getLocationOnScreen())

    @overload
    def getComponentAt(self, arg0: int, arg1: int) -> 'Component':
        """public java.awt.Component java.awt.Container.getComponentAt(int,int)"""
        return 'Component'._wrap(super(_Container, self).getComponentAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def isAlwaysOnTop(self) -> bool:
        """public final boolean java.awt.Window.isAlwaysOnTop()"""
        return bool._wrap(super(Window, self).isAlwaysOnTop())

    @staticmethod
    @overload
    def getOwnerlessWindows() -> List['Window']:
        """public static java.awt.Window[] java.awt.Window.getOwnerlessWindows()"""
        return List[Window]._wrap(_Window.getOwnerlessWindows())

    @override
    @overload
    def getIconImage(self) -> 'Image':
        """public java.awt.Image java.awt.Frame.getIconImage()"""
        return 'Image'._wrap(super(Frame, self).getIconImage())

    @override
    @overload
    def isMaximumSizeSet(self) -> bool:
        """public boolean java.awt.Component.isMaximumSizeSet()"""
        return bool._wrap(super(Component, self).isMaximumSizeSet())

    @override
    @overload
    def isFocusable(self) -> bool:
        """public boolean java.awt.Component.isFocusable()"""
        return bool._wrap(super(Component, self).isFocusable())

    @override
    @overload
    def requestFocusInWindow(self) -> bool:
        """public boolean java.awt.Component.requestFocusInWindow()"""
        return bool._wrap(super(Component, self).requestFocusInWindow())

    @override
    @overload
    def isFocusTraversalPolicyProvider(self) -> bool:
        """public final boolean java.awt.Container.isFocusTraversalPolicyProvider()"""
        return bool._wrap(super(Container, self).isFocusTraversalPolicyProvider())

    @override
    @overload
    def getMouseListeners(self) -> List['MouseListener']:
        """public synchronized java.awt.event.MouseListener[] java.awt.Component.getMouseListeners()"""
        return List['MouseListener']._wrap(super(Component, self).getMouseListeners())

    @override
    @overload
    def setFont(self, arg0: 'Font'):
        """public void java.awt.Container.setFont(java.awt.Font)"""
        super(_Container, self).setFont(arg0)

    @override
    @overload
    def transferFocusUpCycle(self):
        """public void java.awt.Component.transferFocusUpCycle()"""
        super(Component, self).transferFocusUpCycle()

    @override
    @overload
    def removeKeyListener(self, arg0: 'KeyListener'):
        """public synchronized void java.awt.Component.removeKeyListener(java.awt.event.KeyListener)"""
        super(_Component, self).removeKeyListener(arg0)

    @override
    @overload
    def getMouseMotionListeners(self) -> List['MouseMotionListener']:
        """public synchronized java.awt.event.MouseMotionListener[] java.awt.Component.getMouseMotionListeners()"""
        return List['MouseMotionListener']._wrap(super(Component, self).getMouseMotionListeners())

    @override
    @overload
    def setIconImage(self, arg0: 'Image'):
        """public void javax.swing.JFrame.setIconImage(java.awt.Image)"""
        super(_JFrame, self).setIconImage(arg0)

    @override
    @overload
    def addContainerListener(self, arg0: 'ContainerListener'):
        """public synchronized void java.awt.Container.addContainerListener(java.awt.event.ContainerListener)"""
        super(_Container, self).addContainerListener(arg0)

    @override
    @overload
    def isFocusTraversable(self) -> bool:
        """public boolean java.awt.Component.isFocusTraversable()"""
        return bool._wrap(super(Component, self).isFocusTraversable())

    @overload
    def mouseExit(self, arg0: 'Event', arg1: int, arg2: int) -> bool:
        """public boolean java.awt.Component.mouseExit(java.awt.Event,int,int)"""
        return bool._wrap(super(_Component, self).mouseExit(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def setMixingCutoutShape(self, arg0: 'Shape'):
        """public void java.awt.Component.setMixingCutoutShape(java.awt.Shape)"""
        super(_Component, self).setMixingCutoutShape(arg0)

    @override
    @overload
    def toFront(self):
        """public void java.awt.Window.toFront()"""
        super(Window, self).toFront()

    @override
    @overload
    def addWindowStateListener(self, arg0: 'WindowStateListener'):
        """public synchronized void java.awt.Window.addWindowStateListener(java.awt.event.WindowStateListener)"""
        super(_Window, self).addWindowStateListener(arg0)

    @overload
    def getSize(self, arg0: 'Dimension') -> 'Dimension':
        """public java.awt.Dimension java.awt.Component.getSize(java.awt.Dimension)"""
        return 'Dimension'._wrap(super(_Component, self).getSize(arg0))

    @override
    @overload
    def requestFocus(self, arg0: 'Cause'):
        """public void java.awt.Component.requestFocus(java.awt.event.FocusEvent$Cause)"""
        super(_Component, self).requestFocus(arg0)

    @overload
    def createImage(self, arg0: int, arg1: int) -> 'Image':
        """public java.awt.Image java.awt.Component.createImage(int,int)"""
        return 'Image'._wrap(super(_Component, self).createImage(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def setUndecorated(self, arg0: bool):
        """public void java.awt.Frame.setUndecorated(boolean)"""
        super(_Frame, self).setUndecorated(_boolean.valueOf(arg0))

    @override
    @overload
    def getFocusListeners(self) -> List['FocusListener']:
        """public synchronized java.awt.event.FocusListener[] java.awt.Component.getFocusListeners()"""
        return List['FocusListener']._wrap(super(Component, self).getFocusListeners())

    @override
    @overload
    def setJMenuBar(self, arg0: 'JMenuBar'):
        """public void javax.swing.JFrame.setJMenuBar(javax.swing.JMenuBar)"""
        super(_JFrame, self).setJMenuBar(arg0)

    @overload
    def add(self, arg0: 'Component') -> 'Component':
        """public java.awt.Component java.awt.Container.add(java.awt.Component)"""
        return 'Component'._wrap(super(_Container, self).add(arg0))

    @override
    @overload
    def getMouseWheelListeners(self) -> List['MouseWheelListener']:
        """public synchronized java.awt.event.MouseWheelListener[] java.awt.Component.getMouseWheelListeners()"""
        return List['MouseWheelListener']._wrap(super(Component, self).getMouseWheelListeners())

    @overload
    def contains(self, arg0: int, arg1: int) -> bool:
        """public boolean java.awt.Component.contains(int,int)"""
        return bool._wrap(super(_Component, self).contains(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def removeInputMethodListener(self, arg0: 'InputMethodListener'):
        """public synchronized void java.awt.Component.removeInputMethodListener(java.awt.event.InputMethodListener)"""
        super(_Component, self).removeInputMethodListener(arg0)

    @staticmethod
    @overload
    def main(arg0: 'String'):
        """public static void com.badlogic.gdx.tools.hiero.Hiero.main(java.lang.String[]) throws java.lang.Exception"""
        _Hiero.main(arg0)

    @override
    @overload
    def setFocusable(self, arg0: bool):
        """public void java.awt.Component.setFocusable(boolean)"""
        super(_Component, self).setFocusable(_boolean.valueOf(arg0))

    @override
    @overload
    def setBounds(self, arg0: 'Rectangle'):
        """public void java.awt.Window.setBounds(java.awt.Rectangle)"""
        super(_Window, self).setBounds(arg0)

    @override
    @overload
    def getJMenuBar(self) -> 'JMenuBar':
        """public javax.swing.JMenuBar javax.swing.JFrame.getJMenuBar()"""
        return 'JMenuBar'._wrap(super(JFrame, self).getJMenuBar())

    @override
    @overload
    def paintComponents(self, arg0: 'Graphics'):
        """public void java.awt.Container.paintComponents(java.awt.Graphics)"""
        super(_Container, self).paintComponents(arg0)

    @override
    @overload
    def hide(self):
        """public void java.awt.Window.hide()"""
        super(Window, self).hide()

    @override
    @overload
    def applyResourceBundle(self, arg0: str):
        """public void java.awt.Window.applyResourceBundle(java.lang.String)"""
        super(_Window, self).applyResourceBundle(arg0)

    @override
    @overload
    def addFocusListener(self, arg0: 'FocusListener'):
        """public synchronized void java.awt.Component.addFocusListener(java.awt.event.FocusListener)"""
        super(_Component, self).addFocusListener(arg0)

    @overload
    def prepareImage(self, arg0: 'Image', arg1: 'ImageObserver') -> bool:
        """public boolean java.awt.Component.prepareImage(java.awt.Image,java.awt.image.ImageObserver)"""
        return bool._wrap(super(_Component, self).prepareImage(arg0, arg1))

    @override
    @overload
    def isFocusCycleRoot(self) -> bool:
        """public final boolean java.awt.Window.isFocusCycleRoot()"""
        return bool._wrap(super(Window, self).isFocusCycleRoot())

    @override
    @overload
    def addKeyListener(self, arg0: 'KeyListener'):
        """public synchronized void java.awt.Component.addKeyListener(java.awt.event.KeyListener)"""
        super(_Component, self).addKeyListener(arg0)

    @override
    @overload
    def getBufferStrategy(self) -> 'BufferStrategy':
        """public java.awt.image.BufferStrategy java.awt.Window.getBufferStrategy()"""
        return 'BufferStrategy'._wrap(super(Window, self).getBufferStrategy())

    @override
    @overload
    def isUndecorated(self) -> bool:
        """public boolean java.awt.Frame.isUndecorated()"""
        return bool._wrap(super(Frame, self).isUndecorated())

    @override
    @overload
    def resize(self, arg0: 'Dimension'):
        """public void java.awt.Component.resize(java.awt.Dimension)"""
        super(_Component, self).resize(arg0)

    @override
    @overload
    def setComponentZOrder(self, arg0: 'Component', arg1: int):
        """public void java.awt.Container.setComponentZOrder(java.awt.Component,int)"""
        super(_Container, self).setComponentZOrder(arg0, _int.valueOf(arg1))

    @override
    @overload
    def list(self):
        """public void java.awt.Component.list()"""
        super(Component, self).list()

    @overload
    def add(self, arg0: str, arg1: 'Component') -> 'Component':
        """public java.awt.Component java.awt.Container.add(java.lang.String,java.awt.Component)"""
        return 'Component'._wrap(super(_Container, self).add(arg0, arg1))

    @override
    @overload
    def setShape(self, arg0: 'Shape'):
        """public void java.awt.Frame.setShape(java.awt.Shape)"""
        super(_Frame, self).setShape(arg0)

    @override
    @overload
    def hasFocus(self) -> bool:
        """public boolean java.awt.Component.hasFocus()"""
        return bool._wrap(super(Component, self).hasFocus())

    @override
    @overload
    def applyResourceBundle(self, arg0: 'ResourceBundle'):
        """public void java.awt.Window.applyResourceBundle(java.util.ResourceBundle)"""
        super(_Window, self).applyResourceBundle(arg0)

    @override
    @overload
    def setEnabled(self, arg0: bool):
        """public void java.awt.Component.setEnabled(boolean)"""
        super(_Component, self).setEnabled(_boolean.valueOf(arg0))

    @overload
    def createVolatileImage(self, arg0: int, arg1: int) -> 'VolatileImage':
        """public java.awt.image.VolatileImage java.awt.Component.createVolatileImage(int,int)"""
        return 'VolatileImage'._wrap(super(_Component, self).createVolatileImage(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def removeHierarchyListener(self, arg0: 'HierarchyListener'):
        """public void java.awt.Component.removeHierarchyListener(java.awt.event.HierarchyListener)"""
        super(_Component, self).removeHierarchyListener(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.awt.Component.toString()"""
        return str._wrap(super(Component, self).toString())

    @override
    @overload
    def addMouseListener(self, arg0: 'MouseListener'):
        """public synchronized void java.awt.Component.addMouseListener(java.awt.event.MouseListener)"""
        super(_Component, self).addMouseListener(arg0)

    @override
    @overload
    def getTransferHandler(self) -> 'TransferHandler':
        """public javax.swing.TransferHandler javax.swing.JFrame.getTransferHandler()"""
        return 'TransferHandler'._wrap(super(JFrame, self).getTransferHandler())

    @override
    @overload
    def isFocusOwner(self) -> bool:
        """public boolean java.awt.Component.isFocusOwner()"""
        return bool._wrap(super(Component, self).isFocusOwner())

    @override
    @overload
    def getWindowFocusListeners(self) -> List['WindowFocusListener']:
        """public synchronized java.awt.event.WindowFocusListener[] java.awt.Window.getWindowFocusListeners()"""
        return List['WindowFocusListener']._wrap(super(Window, self).getWindowFocusListeners())

    @override
    @overload
    def enable(self):
        """public void java.awt.Component.enable()"""
        super(Component, self).enable()

    @overload
    def findComponentAt(self, arg0: int, arg1: int) -> 'Component':
        """public java.awt.Component java.awt.Container.findComponentAt(int,int)"""
        return 'Component'._wrap(super(_Container, self).findComponentAt(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def requestFocus(self):
        """public void java.awt.Component.requestFocus()"""
        super(Component, self).requestFocus()

    @override
    @overload
    def setModalExclusionType(self, arg0: 'ModalExclusionType'):
        """public void java.awt.Window.setModalExclusionType(java.awt.Dialog$ModalExclusionType)"""
        super(_Window, self).setModalExclusionType(arg0)

    @override
    @overload
    def getForeground(self) -> 'Color':
        """public java.awt.Color java.awt.Component.getForeground()"""
        return 'Color'._wrap(super(Component, self).getForeground())

    @override
    @overload
    def isAutoRequestFocus(self) -> bool:
        """public boolean java.awt.Window.isAutoRequestFocus()"""
        return bool._wrap(super(Window, self).isAutoRequestFocus())

    @override
    @overload
    def addMouseWheelListener(self, arg0: 'MouseWheelListener'):
        """public synchronized void java.awt.Component.addMouseWheelListener(java.awt.event.MouseWheelListener)"""
        super(_Component, self).addMouseWheelListener(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def addWindowListener(self, arg0: 'WindowListener'):
        """public synchronized void java.awt.Window.addWindowListener(java.awt.event.WindowListener)"""
        super(_Window, self).addWindowListener(arg0)

    @override
    @overload
    def setLocationByPlatform(self, arg0: bool):
        """public void java.awt.Window.setLocationByPlatform(boolean)"""
        super(_Window, self).setLocationByPlatform(_boolean.valueOf(arg0))

    @override
    @overload
    def addWindowFocusListener(self, arg0: 'WindowFocusListener'):
        """public synchronized void java.awt.Window.addWindowFocusListener(java.awt.event.WindowFocusListener)"""
        super(_Window, self).addWindowFocusListener(arg0)

    @overload
    def action(self, arg0: 'Event', arg1: object) -> bool:
        """public boolean java.awt.Component.action(java.awt.Event,java.lang.Object)"""
        return bool._wrap(super(_Component, self).action(arg0, arg1))

    @override
    @overload
    def isLightweight(self) -> bool:
        """public boolean java.awt.Component.isLightweight()"""
        return bool._wrap(super(Component, self).isLightweight())

    @override
    @overload
    def setContentPane(self, arg0: 'Container'):
        """public void javax.swing.JFrame.setContentPane(java.awt.Container)"""
        super(_JFrame, self).setContentPane(arg0)

    @override
    @overload
    def setFocusTraversalKeysEnabled(self, arg0: bool):
        """public void java.awt.Component.setFocusTraversalKeysEnabled(boolean)"""
        super(_Component, self).setFocusTraversalKeysEnabled(_boolean.valueOf(arg0))

    @override
    @overload
    def update(self, arg0: 'Graphics'):
        """public void javax.swing.JFrame.update(java.awt.Graphics)"""
        super(_JFrame, self).update(arg0)

    @override
    @overload
    def setLayeredPane(self, arg0: 'JLayeredPane'):
        """public void javax.swing.JFrame.setLayeredPane(javax.swing.JLayeredPane)"""
        super(_JFrame, self).setLayeredPane(arg0)

    @override
    @overload
    def getAlignmentX(self) -> float:
        """public float java.awt.Container.getAlignmentX()"""
        return float._wrap(super(Container, self).getAlignmentX())

    @override
    @overload
    def getModalExclusionType(self) -> 'ModalExclusionType.Dialog$ModalExclusionType':
        """public java.awt.Dialog$ModalExclusionType java.awt.Window.getModalExclusionType()"""
        return 'ModalExclusionType.Dialog$ModalExclusionType'._wrap(super(Window, self).getModalExclusionType())

    @override
    @overload
    def insets(self) -> 'Insets':
        """public java.awt.Insets java.awt.Container.insets()"""
        return 'Insets'._wrap(super(Container, self).insets())

    @override
    @overload
    def setVisible(self, arg0: bool):
        """public void java.awt.Window.setVisible(boolean)"""
        super(_Window, self).setVisible(_boolean.valueOf(arg0))

    @override
    @overload
    def getOpacity(self) -> float:
        """public float java.awt.Window.getOpacity()"""
        return float._wrap(super(Window, self).getOpacity())

    @override
    @overload
    def setFocusTraversalPolicy(self, arg0: 'FocusTraversalPolicy'):
        """public void java.awt.Container.setFocusTraversalPolicy(java.awt.FocusTraversalPolicy)"""
        super(_Container, self).setFocusTraversalPolicy(arg0)

    @override
    @overload
    def enable(self, arg0: bool):
        """public void java.awt.Component.enable(boolean)"""
        super(_Component, self).enable(_boolean.valueOf(arg0))

    @override
    @overload
    def setSize(self, arg0: int, arg1: int):
        """public void java.awt.Window.setSize(int,int)"""
        super(_Window, self).setSize(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def printAll(self, arg0: 'Graphics'):
        """public void java.awt.Component.printAll(java.awt.Graphics)"""
        super(_Component, self).printAll(arg0)

    @override
    @overload
    def setCursor(self, arg0: int):
        """public void java.awt.Frame.setCursor(int)"""
        super(_Frame, self).setCursor(_int.valueOf(arg0))

    @override
    @overload
    def getWarningString(self) -> str:
        """public final java.lang.String java.awt.Window.getWarningString()"""
        return str._wrap(super(Window, self).getWarningString())

    @override
    @overload
    def setOpacity(self, arg0: float):
        """public void java.awt.Frame.setOpacity(float)"""
        super(_Frame, self).setOpacity(_float.valueOf(arg0))

    @override
    @overload
    def getInsets(self) -> 'Insets':
        """public java.awt.Insets java.awt.Container.getInsets()"""
        return 'Insets'._wrap(super(Container, self).getInsets())

    @override
    @overload
    def setLocation(self, arg0: int, arg1: int):
        """public void java.awt.Window.setLocation(int,int)"""
        super(_Window, self).setLocation(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getComponentAt(self, arg0: 'Point') -> 'Component':
        """public java.awt.Component java.awt.Container.getComponentAt(java.awt.Point)"""
        return 'Component'._wrap(super(_Container, self).getComponentAt(arg0))

    @override
    @overload
    def size(self) -> 'Dimension':
        """public java.awt.Dimension java.awt.Component.size()"""
        return 'Dimension'._wrap(super(Component, self).size())

    @overload
    def mouseMove(self, arg0: 'Event', arg1: int, arg2: int) -> bool:
        """public boolean java.awt.Component.mouseMove(java.awt.Event,int,int)"""
        return bool._wrap(super(_Component, self).mouseMove(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def lostFocus(self, arg0: 'Event', arg1: object) -> bool:
        """public boolean java.awt.Component.lostFocus(java.awt.Event,java.lang.Object)"""
        return bool._wrap(super(_Component, self).lostFocus(arg0, arg1))

    @override
    @overload
    def getMaximizedBounds(self) -> 'Rectangle':
        """public java.awt.Rectangle java.awt.Frame.getMaximizedBounds()"""
        return 'Rectangle'._wrap(super(Frame, self).getMaximizedBounds())

    @override
    @overload
    def isMinimumSizeSet(self) -> bool:
        """public boolean java.awt.Component.isMinimumSizeSet()"""
        return bool._wrap(super(Component, self).isMinimumSizeSet())

    @override
    @overload
    def isForegroundSet(self) -> bool:
        """public boolean java.awt.Component.isForegroundSet()"""
        return bool._wrap(super(Component, self).isForegroundSet())

    @override
    @overload
    def getWindowListeners(self) -> List['WindowListener']:
        """public synchronized java.awt.event.WindowListener[] java.awt.Window.getWindowListeners()"""
        return List['WindowListener']._wrap(super(Window, self).getWindowListeners())

    @overload
    def getMousePosition(self, arg0: bool) -> 'Point':
        """public java.awt.Point java.awt.Container.getMousePosition(boolean) throws java.awt.HeadlessException"""
        return 'Point'._wrap(super(_Container, self).getMousePosition(_boolean.valueOf(arg0)))

    @override
    @overload
    def show(self):
        """public void java.awt.Window.show()"""
        super(Window, self).show()

    @override
    @overload
    def getHierarchyBoundsListeners(self) -> List['HierarchyBoundsListener']:
        """public synchronized java.awt.event.HierarchyBoundsListener[] java.awt.Component.getHierarchyBoundsListeners()"""
        return List['HierarchyBoundsListener']._wrap(super(Component, self).getHierarchyBoundsListeners())

    @override
    @overload
    def minimumSize(self) -> 'Dimension':
        """public java.awt.Dimension java.awt.Container.minimumSize()"""
        return 'Dimension'._wrap(super(Container, self).minimumSize())

    @overload
    def handleEvent(self, arg0: 'Event') -> bool:
        """public boolean java.awt.Component.handleEvent(java.awt.Event)"""
        return bool._wrap(super(_Component, self).handleEvent(arg0))

    @override
    @overload
    def getExtendedState(self) -> int:
        """public int java.awt.Frame.getExtendedState()"""
        return int._wrap(super(Frame, self).getExtendedState())

    @override
    @overload
    def isValidateRoot(self) -> bool:
        """public boolean java.awt.Window.isValidateRoot()"""
        return bool._wrap(super(Window, self).isValidateRoot())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getLocation(self, arg0: 'Point') -> 'Point':
        """public java.awt.Point java.awt.Component.getLocation(java.awt.Point)"""
        return 'Point'._wrap(super(_Component, self).getLocation(arg0))

    @override
    @overload
    def getComponentListeners(self) -> List['ComponentListener']:
        """public synchronized java.awt.event.ComponentListener[] java.awt.Component.getComponentListeners()"""
        return List['ComponentListener']._wrap(super(Component, self).getComponentListeners())

    @override
    @overload
    def deliverEvent(self, arg0: 'Event'):
        """public void java.awt.Container.deliverEvent(java.awt.Event)"""
        super(_Container, self).deliverEvent(arg0)

    @override
    @overload
    def getMinimumSize(self) -> 'Dimension':
        """public java.awt.Dimension java.awt.Container.getMinimumSize()"""
        return 'Dimension'._wrap(super(Container, self).getMinimumSize())

    @override
    @overload
    def addHierarchyBoundsListener(self, arg0: 'HierarchyBoundsListener'):
        """public void java.awt.Component.addHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)"""
        super(_Component, self).addHierarchyBoundsListener(arg0)

    @override
    @overload
    def isResizable(self) -> bool:
        """public boolean java.awt.Frame.isResizable()"""
        return bool._wrap(super(Frame, self).isResizable())

    @override
    @overload
    def getY(self) -> int:
        """public int java.awt.Component.getY()"""
        return int._wrap(super(Component, self).getY())

    @override
    @overload
    def getOwner(self) -> 'Window':
        """public java.awt.Window java.awt.Window.getOwner()"""
        return 'Window'._wrap(super(Window, self).getOwner())

    @overload
    def add(self, arg0: 'Component', arg1: int) -> 'Component':
        """public java.awt.Component java.awt.Container.add(java.awt.Component,int)"""
        return 'Component'._wrap(super(_Container, self).add(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def repaint(self):
        """public void java.awt.Component.repaint()"""
        super(Component, self).repaint()

    @overload
    def gotFocus(self, arg0: 'Event', arg1: object) -> bool:
        """public boolean java.awt.Component.gotFocus(java.awt.Event,java.lang.Object)"""
        return bool._wrap(super(_Component, self).gotFocus(arg0, arg1))

    @overload
    def postEvent(self, arg0: 'Event') -> bool:
        """public boolean java.awt.Window.postEvent(java.awt.Event)"""
        return bool._wrap(super(_Window, self).postEvent(arg0))

    @override
    @overload
    def printComponents(self, arg0: 'Graphics'):
        """public void java.awt.Container.printComponents(java.awt.Graphics)"""
        super(_Container, self).printComponents(arg0)

    @override
    @overload
    def getColorModel(self) -> 'ColorModel':
        """public java.awt.image.ColorModel java.awt.Component.getColorModel()"""
        return 'ColorModel'._wrap(super(Component, self).getColorModel())

    @override
    @overload
    def setFocusTraversalPolicyProvider(self, arg0: bool):
        """public final void java.awt.Container.setFocusTraversalPolicyProvider(boolean)"""
        super(_Container, self).setFocusTraversalPolicyProvider(_boolean.valueOf(arg0))

    @overload
    def getComponentZOrder(self, arg0: 'Component') -> int:
        """public int java.awt.Container.getComponentZOrder(java.awt.Component)"""
        return int._wrap(super(_Container, self).getComponentZOrder(arg0))

    @overload
    def areFocusTraversalKeysSet(self, arg0: int) -> bool:
        """public boolean java.awt.Container.areFocusTraversalKeysSet(int)"""
        return bool._wrap(super(_Container, self).areFocusTraversalKeysSet(_int.valueOf(arg0)))

    @override
    @overload
    def getSize(self) -> 'Dimension':
        """public java.awt.Dimension java.awt.Component.getSize()"""
        return 'Dimension'._wrap(super(Component, self).getSize())

    @override
    @overload
    def setName(self, arg0: str):
        """public void java.awt.Component.setName(java.lang.String)"""
        super(_Component, self).setName(arg0)

    @overload
    def mouseEnter(self, arg0: 'Event', arg1: int, arg2: int) -> bool:
        """public boolean java.awt.Component.mouseEnter(java.awt.Event,int,int)"""
        return bool._wrap(super(_Component, self).mouseEnter(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def setMinimumSize(self, arg0: 'Dimension'):
        """public void java.awt.Window.setMinimumSize(java.awt.Dimension)"""
        super(_Window, self).setMinimumSize(arg0)

    @override
    @overload
    def isCursorSet(self) -> bool:
        """public boolean java.awt.Component.isCursorSet()"""
        return bool._wrap(super(Component, self).isCursorSet())

    @override
    @overload
    def add(self, arg0: 'Component', arg1: object, arg2: int):
        """public void java.awt.Container.add(java.awt.Component,java.lang.Object,int)"""
        super(_Container, self).add(arg0, arg1, _int.valueOf(arg2))

    @override
    @overload
    def paint(self, arg0: 'Graphics'):
        """public void java.awt.Window.paint(java.awt.Graphics)"""
        super(_Window, self).paint(arg0)

    @override
    @overload
    def isFocusTraversalPolicySet(self) -> bool:
        """public boolean java.awt.Container.isFocusTraversalPolicySet()"""
        return bool._wrap(super(Container, self).isFocusTraversalPolicySet())

    @override
    @overload
    def isDoubleBuffered(self) -> bool:
        """public boolean java.awt.Component.isDoubleBuffered()"""
        return bool._wrap(super(Component, self).isDoubleBuffered())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getBaseline(self, arg0: int, arg1: int) -> int:
        """public int java.awt.Component.getBaseline(int,int)"""
        return int._wrap(super(_Component, self).getBaseline(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def isEnabled(self) -> bool:
        """public boolean java.awt.Component.isEnabled()"""
        return bool._wrap(super(Component, self).isEnabled())

    @override
    @overload
    def move(self, arg0: int, arg1: int):
        """public void java.awt.Component.move(int,int)"""
        super(_Component, self).move(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String java.awt.Component.getName()"""
        return str._wrap(super(Component, self).getName())

    @override
    @overload
    def getX(self) -> int:
        """public int java.awt.Component.getX()"""
        return int._wrap(super(Component, self).getX())

    @override
    @overload
    def addMouseMotionListener(self, arg0: 'MouseMotionListener'):
        """public synchronized void java.awt.Component.addMouseMotionListener(java.awt.event.MouseMotionListener)"""
        super(_Component, self).addMouseMotionListener(arg0)

    @override
    @overload
    def addPropertyChangeListener(self, arg0: 'PropertyChangeListener'):
        """public void java.awt.Window.addPropertyChangeListener(java.beans.PropertyChangeListener)"""
        super(_Window, self).addPropertyChangeListener(arg0)

    @override
    @overload
    def getIgnoreRepaint(self) -> bool:
        """public boolean java.awt.Component.getIgnoreRepaint()"""
        return bool._wrap(super(Component, self).getIgnoreRepaint())

    @overload
    def isFocusCycleRoot(self, arg0: 'Container') -> bool:
        """public boolean java.awt.Container.isFocusCycleRoot(java.awt.Container)"""
        return bool._wrap(super(_Container, self).isFocusCycleRoot(arg0))

    @override
    @overload
    def setLocale(self, arg0: 'Locale'):
        """public void java.awt.Component.setLocale(java.util.Locale)"""
        super(_Component, self).setLocale(arg0)

    @override
    @overload
    def paintAll(self, arg0: 'Graphics'):
        """public void java.awt.Component.paintAll(java.awt.Graphics)"""
        super(_Component, self).paintAll(arg0)

    @override
    @overload
    def getContentPane(self) -> 'Container':
        """public java.awt.Container javax.swing.JFrame.getContentPane()"""
        return 'Container'._wrap(super(JFrame, self).getContentPane())

    @override
    @overload
    def getState(self) -> int:
        """public synchronized int java.awt.Frame.getState()"""
        return int._wrap(super(Frame, self).getState())

    @override
    @overload
    def setPreferredSize(self, arg0: 'Dimension'):
        """public void java.awt.Component.setPreferredSize(java.awt.Dimension)"""
        super(_Component, self).setPreferredSize(arg0)

    @override
    @overload
    def isPreferredSizeSet(self) -> bool:
        """public boolean java.awt.Component.isPreferredSizeSet()"""
        return bool._wrap(super(Component, self).isPreferredSizeSet())

    @override
    @overload
    def addInputMethodListener(self, arg0: 'InputMethodListener'):
        """public synchronized void java.awt.Component.addInputMethodListener(java.awt.event.InputMethodListener)"""
        super(_Component, self).addInputMethodListener(arg0)

    @override
    @overload
    def removeMouseWheelListener(self, arg0: 'MouseWheelListener'):
        """public synchronized void java.awt.Component.removeMouseWheelListener(java.awt.event.MouseWheelListener)"""
        super(_Component, self).removeMouseWheelListener(arg0)

    @override
    @overload
    def print(self, arg0: 'Graphics'):
        """public void java.awt.Container.print(java.awt.Graphics)"""
        super(_Container, self).print(arg0)

    @override
    @overload
    def firePropertyChange(self, arg0: str, arg1: int, arg2: int):
        """public void java.awt.Component.firePropertyChange(java.lang.String,byte,byte)"""
        super(_Component, self).firePropertyChange(arg0, _byte.valueOf(arg1), _byte.valueOf(arg2))

    @override
    @overload
    def transferFocusDownCycle(self):
        """public void java.awt.Container.transferFocusDownCycle()"""
        super(Container, self).transferFocusDownCycle()

    @override
    @overload
    def setBounds(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void java.awt.Window.setBounds(int,int,int,int)"""
        super(_Window, self).setBounds(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))

    @override
    @overload
    def removeWindowStateListener(self, arg0: 'WindowStateListener'):
        """public synchronized void java.awt.Window.removeWindowStateListener(java.awt.event.WindowStateListener)"""
        super(_Window, self).removeWindowStateListener(arg0)

    @override
    @overload
    def getAccessibleContext(self) -> 'AccessibleContext':
        """public javax.accessibility.AccessibleContext javax.swing.JFrame.getAccessibleContext()"""
        return 'AccessibleContext'._wrap(super(JFrame, self).getAccessibleContext())

    @override
    @overload
    def setType(self, arg0: 'Type'):
        """public void java.awt.Window.setType(java.awt.Window$Type)"""
        super(_Window, self).setType(arg0)

    @override
    @overload
    def getGlassPane(self) -> 'Component':
        """public java.awt.Component javax.swing.JFrame.getGlassPane()"""
        return 'Component'._wrap(super(JFrame, self).getGlassPane())

    @override
    @overload
    def setFocusableWindowState(self, arg0: bool):
        """public void java.awt.Window.setFocusableWindowState(boolean)"""
        super(_Window, self).setFocusableWindowState(_boolean.valueOf(arg0))

    @override
    @overload
    def repaint(self, arg0: int):
        """public void java.awt.Component.repaint(long)"""
        super(_Component, self).repaint(_long.valueOf(arg0))

    @override
    @overload
    def removeHierarchyBoundsListener(self, arg0: 'HierarchyBoundsListener'):
        """public void java.awt.Component.removeHierarchyBoundsListener(java.awt.event.HierarchyBoundsListener)"""
        super(_Component, self).removeHierarchyBoundsListener(arg0)

    @override
    @overload
    def getMousePosition(self) -> 'Point':
        """public java.awt.Point java.awt.Component.getMousePosition() throws java.awt.HeadlessException"""
        return 'Point'._wrap(super(Component, self).getMousePosition())

    @override
    @overload
    def getType(self) -> 'Type.Window$Type':
        """public java.awt.Window$Type java.awt.Window.getType()"""
        return 'Type.Window$Type'._wrap(super(Window, self).getType())

    @override
    @overload
    def getComponentCount(self) -> int:
        """public int java.awt.Container.getComponentCount()"""
        return int._wrap(super(Container, self).getComponentCount())

    @override
    @overload
    def getPreferredSize(self) -> 'Dimension':
        """public java.awt.Dimension java.awt.Container.getPreferredSize()"""
        return 'Dimension'._wrap(super(Container, self).getPreferredSize())

    @override
    @overload
    def getInputMethodRequests(self) -> 'InputMethodRequests':
        """public java.awt.im.InputMethodRequests java.awt.Component.getInputMethodRequests()"""
        return 'InputMethodRequests'._wrap(super(Component, self).getInputMethodRequests())

    @override
    @overload
    def getRootPane(self) -> 'JRootPane':
        """public javax.swing.JRootPane javax.swing.JFrame.getRootPane()"""
        return 'JRootPane'._wrap(super(JFrame, self).getRootPane())

    @override
    @overload
    def getWindowStateListeners(self) -> List['WindowStateListener']:
        """public synchronized java.awt.event.WindowStateListener[] java.awt.Window.getWindowStateListeners()"""
        return List['WindowStateListener']._wrap(super(Window, self).getWindowStateListeners())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean java.awt.Window.isActive()"""
        return bool._wrap(super(Window, self).isActive())

    @overload
    def __init__(self, arg0: 'String'):
        """public com.badlogic.gdx.tools.hiero.Hiero(java.lang.String[])"""
        val = _Hiero(arg0)
        self.__wrapper = val

    @overload
    def getFontMetrics(self, arg0: 'Font') -> 'FontMetrics':
        """public java.awt.FontMetrics java.awt.Component.getFontMetrics(java.awt.Font)"""
        return 'FontMetrics'._wrap(super(_Component, self).getFontMetrics(arg0))

    @override
    @overload
    def setTransferHandler(self, arg0: 'TransferHandler'):
        """public void javax.swing.JFrame.setTransferHandler(javax.swing.TransferHandler)"""
        super(_JFrame, self).setTransferHandler(arg0)

    @overload
    def inside(self, arg0: int, arg1: int) -> bool:
        """public boolean java.awt.Component.inside(int,int)"""
        return bool._wrap(super(_Component, self).inside(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def setDefaultCloseOperation(self, arg0: int):
        """public void javax.swing.JFrame.setDefaultCloseOperation(int)"""
        super(_JFrame, self).setDefaultCloseOperation(_int.valueOf(arg0))

    @override
    @overload
    def enableInputMethods(self, arg0: bool):
        """public void java.awt.Component.enableInputMethods(boolean)"""
        super(_Component, self).enableInputMethods(_boolean.valueOf(arg0))

    @override
    @overload
    def layout(self):
        """public void java.awt.Container.layout()"""
        super(Container, self).layout()

    @override
    @overload
    def getInputMethodListeners(self) -> List['InputMethodListener']:
        """public synchronized java.awt.event.InputMethodListener[] java.awt.Component.getInputMethodListeners()"""
        return List['InputMethodListener']._wrap(super(Component, self).getInputMethodListeners())

    @override
    @overload
    def transferFocus(self):
        """public void java.awt.Component.transferFocus()"""
        super(Component, self).transferFocus()

    @override
    @overload
    def isShowing(self) -> bool:
        """public boolean java.awt.Window.isShowing()"""
        return bool._wrap(super(Window, self).isShowing())

    @override
    @overload
    def removeComponentListener(self, arg0: 'ComponentListener'):
        """public synchronized void java.awt.Component.removeComponentListener(java.awt.event.ComponentListener)"""
        super(_Component, self).removeComponentListener(arg0)

    @override
    @overload
    def getCursor(self) -> 'Cursor':
        """public java.awt.Cursor java.awt.Component.getCursor()"""
        return 'Cursor'._wrap(super(Component, self).getCursor())

    @override
    @overload
    def setMenuBar(self, arg0: 'MenuBar'):
        """public void java.awt.Frame.setMenuBar(java.awt.MenuBar)"""
        super(_Frame, self).setMenuBar(arg0)

    @override
    @overload
    def getContainerListeners(self) -> List['ContainerListener']:
        """public synchronized java.awt.event.ContainerListener[] java.awt.Container.getContainerListeners()"""
        return List['ContainerListener']._wrap(super(Container, self).getContainerListeners())

    @override
    @overload
    def getMaximumSize(self) -> 'Dimension':
        """public java.awt.Dimension java.awt.Container.getMaximumSize()"""
        return 'Dimension'._wrap(super(Container, self).getMaximumSize())

    @override
    @overload
    def removeAll(self):
        """public void java.awt.Container.removeAll()"""
        super(Container, self).removeAll()

    @overload
    def isAncestorOf(self, arg0: 'Component') -> bool:
        """public boolean java.awt.Container.isAncestorOf(java.awt.Component)"""
        return bool._wrap(super(_Container, self).isAncestorOf(arg0))

    @override
    @overload
    def validate(self):
        """public void java.awt.Container.validate()"""
        super(Container, self).validate()

    @overload
    def createImage(self, arg0: 'ImageProducer') -> 'Image':
        """public java.awt.Image java.awt.Component.createImage(java.awt.image.ImageProducer)"""
        return 'Image'._wrap(super(_Component, self).createImage(arg0))

    @override
    @overload
    def setLocationRelativeTo(self, arg0: 'Component'):
        """public void java.awt.Window.setLocationRelativeTo(java.awt.Component)"""
        super(_Window, self).setLocationRelativeTo(arg0)

    @override
    @overload
    def removePropertyChangeListener(self, arg0: str, arg1: 'PropertyChangeListener'):
        """public void java.awt.Component.removePropertyChangeListener(java.lang.String,java.beans.PropertyChangeListener)"""
        super(_Component, self).removePropertyChangeListener(arg0, arg1)

    @override
    @overload
    def countComponents(self) -> int:
        """public int java.awt.Container.countComponents()"""
        return int._wrap(super(Container, self).countComponents())

    @override
    @overload
    def getTitle(self) -> str:
        """public java.lang.String java.awt.Frame.getTitle()"""
        return str._wrap(super(Frame, self).getTitle()) 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.HieroSettings
from builtins import str
import com.badlogic.gdx.tools.hiero.HieroSettings as _HieroSettings
_HieroSettings = _HieroSettings
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.File as File
from builtins import float
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class HieroSettings():
    """com.badlogic.gdx.tools.hiero.HieroSettings"""
 
    @staticmethod
    def _wrap(java_value: _HieroSettings) -> 'HieroSettings':
        return HieroSettings(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HieroSettings):
        """
        Dynamic initializer for HieroSettings.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HieroSettings__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HieroSettings__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.hiero.HieroSettings()"""
        val = _HieroSettings()
        self.__wrapper = val

    @overload
    def setBold(self, arg0: bool):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setBold(boolean)"""
        super(_HieroSettings, self).setBold(_boolean.valueOf(arg0))

    @overload
    def getNativeRendering(self) -> bool:
        """public boolean com.badlogic.gdx.tools.hiero.HieroSettings.getNativeRendering()"""
        return bool._wrap(super(HieroSettings, self).getNativeRendering())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getGlyphPageHeight(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.HieroSettings.getGlyphPageHeight()"""
        return int._wrap(super(HieroSettings, self).getGlyphPageHeight())

    @overload
    def isMono(self) -> bool:
        """public boolean com.badlogic.gdx.tools.hiero.HieroSettings.isMono()"""
        return bool._wrap(super(HieroSettings, self).isMono())

    @overload
    def getEffects(self) -> 'List':
        """public java.util.List com.badlogic.gdx.tools.hiero.HieroSettings.getEffects()"""
        return 'List'._wrap(super(HieroSettings, self).getEffects())

    @overload
    def setFont2File(self, arg0: str):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setFont2File(java.lang.String)"""
        super(_HieroSettings, self).setFont2File(arg0)

    @overload
    def getPaddingRight(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.HieroSettings.getPaddingRight()"""
        return int._wrap(super(HieroSettings, self).getPaddingRight())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setRenderType(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setRenderType(int)"""
        super(_HieroSettings, self).setRenderType(_int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def isItalic(self) -> bool:
        """public boolean com.badlogic.gdx.tools.hiero.HieroSettings.isItalic()"""
        return bool._wrap(super(HieroSettings, self).isItalic())

    @overload
    def getPaddingAdvanceX(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.HieroSettings.getPaddingAdvanceX()"""
        return int._wrap(super(HieroSettings, self).getPaddingAdvanceX())

    @overload
    def getFontSize(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.HieroSettings.getFontSize()"""
        return int._wrap(super(HieroSettings, self).getFontSize())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getGlyphText(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.hiero.HieroSettings.getGlyphText()"""
        return str._wrap(super(HieroSettings, self).getGlyphText())

    @overload
    def setGlyphPageHeight(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setGlyphPageHeight(int)"""
        super(_HieroSettings, self).setGlyphPageHeight(_int.valueOf(arg0))

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.tools.hiero.HieroSettings(java.lang.String)"""
        val = _HieroSettings(arg0)
        self.__wrapper = val

    @overload
    def getRenderType(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.HieroSettings.getRenderType()"""
        return int._wrap(super(HieroSettings, self).getRenderType())

    @overload
    def isBold(self) -> bool:
        """public boolean com.badlogic.gdx.tools.hiero.HieroSettings.isBold()"""
        return bool._wrap(super(HieroSettings, self).isBold())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setPaddingLeft(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setPaddingLeft(int)"""
        super(_HieroSettings, self).setPaddingLeft(_int.valueOf(arg0))

    @overload
    def setPaddingRight(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setPaddingRight(int)"""
        super(_HieroSettings, self).setPaddingRight(_int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setNativeRendering(self, arg0: bool):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setNativeRendering(boolean)"""
        super(_HieroSettings, self).setNativeRendering(_boolean.valueOf(arg0))

    @overload
    def setMono(self, arg0: bool):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setMono(boolean)"""
        super(_HieroSettings, self).setMono(_boolean.valueOf(arg0))

    @overload
    def setFontName(self, arg0: str):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setFontName(java.lang.String)"""
        super(_HieroSettings, self).setFontName(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def getPaddingLeft(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.HieroSettings.getPaddingLeft()"""
        return int._wrap(super(HieroSettings, self).getPaddingLeft())

    @overload
    def getPaddingBottom(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.HieroSettings.getPaddingBottom()"""
        return int._wrap(super(HieroSettings, self).getPaddingBottom())

    @overload
    def setPaddingAdvanceY(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setPaddingAdvanceY(int)"""
        super(_HieroSettings, self).setPaddingAdvanceY(_int.valueOf(arg0))

    @overload
    def setGamma(self, arg0: float):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setGamma(float)"""
        super(_HieroSettings, self).setGamma(_float.valueOf(arg0))

    @overload
    def setGlyphText(self, arg0: str):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setGlyphText(java.lang.String)"""
        super(_HieroSettings, self).setGlyphText(arg0)

    @overload
    def save(self, arg0: 'File'):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.save(java.io.File) throws java.io.IOException"""
        super(_HieroSettings, self).save(arg0)

    @overload
    def getGamma(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.HieroSettings.getGamma()"""
        return float._wrap(super(HieroSettings, self).getGamma())

    @overload
    def setGlyphPageWidth(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setGlyphPageWidth(int)"""
        super(_HieroSettings, self).setGlyphPageWidth(_int.valueOf(arg0))

    @overload
    def setPaddingBottom(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setPaddingBottom(int)"""
        super(_HieroSettings, self).setPaddingBottom(_int.valueOf(arg0))

    @overload
    def setFontSize(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setFontSize(int)"""
        super(_HieroSettings, self).setFontSize(_int.valueOf(arg0))

    @overload
    def setFont2Active(self, arg0: bool):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setFont2Active(boolean)"""
        super(_HieroSettings, self).setFont2Active(_boolean.valueOf(arg0))

    @overload
    def setPaddingAdvanceX(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setPaddingAdvanceX(int)"""
        super(_HieroSettings, self).setPaddingAdvanceX(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getFont2File(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.hiero.HieroSettings.getFont2File()"""
        return str._wrap(super(HieroSettings, self).getFont2File())

    @overload
    def getPaddingAdvanceY(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.HieroSettings.getPaddingAdvanceY()"""
        return int._wrap(super(HieroSettings, self).getPaddingAdvanceY())

    @overload
    def isFont2Active(self) -> bool:
        """public boolean com.badlogic.gdx.tools.hiero.HieroSettings.isFont2Active()"""
        return bool._wrap(super(HieroSettings, self).isFont2Active())

    @overload
    def getFontName(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.hiero.HieroSettings.getFontName()"""
        return str._wrap(super(HieroSettings, self).getFontName())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setItalic(self, arg0: bool):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setItalic(boolean)"""
        super(_HieroSettings, self).setItalic(_boolean.valueOf(arg0))

    @overload
    def getGlyphPageWidth(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.HieroSettings.getGlyphPageWidth()"""
        return int._wrap(super(HieroSettings, self).getGlyphPageWidth())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.hiero.HieroSettings()"""
        val = _HieroSettings()
        self.__wrapper = val

    @overload
    def getPaddingTop(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.HieroSettings.getPaddingTop()"""
        return int._wrap(super(HieroSettings, self).getPaddingTop())

    @overload
    def setPaddingTop(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.HieroSettings.setPaddingTop(int)"""
        super(_HieroSettings, self).setPaddingTop(_int.valueOf(arg0))