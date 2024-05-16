from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable as _BaseDrawable
_BaseDrawable = _BaseDrawable
from builtins import float
import space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable as _ShapeDrawerDrawable
_ShapeDrawerDrawable = _ShapeDrawerDrawable
import space.earlygrey.shapedrawer.ShapeDrawer as _ShapeDrawer
_ShapeDrawer = _ShapeDrawer
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
try:
    import pyshapedrawer
except ImportError:
    pyshapedrawer = _import_once("pyshapedrawer")

import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ShapeDrawerDrawable():
    """space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable"""
 
    @staticmethod
    def _wrap(java_value: _ShapeDrawerDrawable) -> 'ShapeDrawerDrawable':
        return ShapeDrawerDrawable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShapeDrawerDrawable):
        """
        Dynamic initializer for ShapeDrawerDrawable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShapeDrawerDrawable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShapeDrawerDrawable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setLeftWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setLeftWidth(float)"""
        super(_utils.BaseDrawable, self).setLeftWidth(_float.valueOf(arg0))

    @override
    @overload
    def getMinWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinWidth()"""
        return float._wrap(super(utils.BaseDrawable, self).getMinWidth())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getName()"""
        return str._wrap(super(utils.BaseDrawable, self).getName())

    @override
    @overload
    def setTopHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setTopHeight(float)"""
        super(_utils.BaseDrawable, self).setTopHeight(_float.valueOf(arg0))

    @override
    @overload
    def setMinWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinWidth(float)"""
        super(_utils.BaseDrawable, self).setMinWidth(_float.valueOf(arg0))

    @override
    @overload
    def setMinHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinHeight(float)"""
        super(_utils.BaseDrawable, self).setMinHeight(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getLeftWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getLeftWidth()"""
        return float._wrap(super(utils.BaseDrawable, self).getLeftWidth())

    @override
    @overload
    def setBottomHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setBottomHeight(float)"""
        super(_utils.BaseDrawable, self).setBottomHeight(_float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getTopHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getTopHeight()"""
        return float._wrap(super(utils.BaseDrawable, self).getTopHeight())

    @overload
    def __init__(self):
        """public space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable()"""
        val = _ShapeDrawerDrawable()
        self.__wrapper = val

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float)"""
        super(_ShapeDrawerDrawable, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def getBottomHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getBottomHeight()"""
        return float._wrap(super(utils.BaseDrawable, self).getBottomHeight())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'ShapeDrawer'):
        """public space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable(space.earlygrey.shapedrawer.ShapeDrawer)"""
        val = _ShapeDrawerDrawable(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.toString()"""
        return str._wrap(super(utils.BaseDrawable, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setMinSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinSize(float,float)"""
        super(_utils.BaseDrawable, self).setMinSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def getMinHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinHeight()"""
        return float._wrap(super(utils.BaseDrawable, self).getMinHeight())

    @overload
    def getShapeDrawer(self) -> 'pyshapedrawer.ShapeDrawer':
        """public space.earlygrey.shapedrawer.ShapeDrawer space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable.getShapeDrawer()"""
        return 'pyshapedrawer.ShapeDrawer'._wrap(super(ShapeDrawerDrawable, self).getShapeDrawer())

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setName(java.lang.String)"""
        super(_utils.BaseDrawable, self).setName(arg0)

    @override
    @overload
    def setPadding(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setPadding(float,float,float,float)"""
        super(_utils.BaseDrawable, self).setPadding(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @abstractmethod
    def drawShapes(self, arg0: 'ShapeDrawer', arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable.drawShapes(space.earlygrey.shapedrawer.ShapeDrawer,float,float,float,float)"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setRightWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setRightWidth(float)"""
        super(_utils.BaseDrawable, self).setRightWidth(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable()"""
        val = _ShapeDrawerDrawable()
        self.__wrapper = val

    @overload
    def setShapeDrawer(self, arg0: 'ShapeDrawer'):
        """public void space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable.setShapeDrawer(space.earlygrey.shapedrawer.ShapeDrawer)"""
        super(_ShapeDrawerDrawable, self).setShapeDrawer(arg0)

    @override
    @overload
    def getRightWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getRightWidth()"""
        return float._wrap(super(utils.BaseDrawable, self).getRightWidth())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable as _BaseDrawable
_BaseDrawable = _BaseDrawable
from builtins import float
import space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable as _ShapeDrawerDrawable
_ShapeDrawerDrawable = _ShapeDrawerDrawable
import space.earlygrey.shapedrawer.ShapeDrawer as _ShapeDrawer
_ShapeDrawer = _ShapeDrawer
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
try:
    import pyshapedrawer
except ImportError:
    pyshapedrawer = _import_once("pyshapedrawer")

import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ShapeDrawerDrawable():
    """space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable"""
 
    @staticmethod
    def _wrap(java_value: _ShapeDrawerDrawable) -> 'ShapeDrawerDrawable':
        return ShapeDrawerDrawable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShapeDrawerDrawable):
        """
        Dynamic initializer for ShapeDrawerDrawable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShapeDrawerDrawable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShapeDrawerDrawable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setLeftWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setLeftWidth(float)"""
        super(_utils.BaseDrawable, self).setLeftWidth(_float.valueOf(arg0))

    @override
    @overload
    def getMinWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinWidth()"""
        return float._wrap(super(utils.BaseDrawable, self).getMinWidth())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getName()"""
        return str._wrap(super(utils.BaseDrawable, self).getName())

    @override
    @overload
    def setTopHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setTopHeight(float)"""
        super(_utils.BaseDrawable, self).setTopHeight(_float.valueOf(arg0))

    @override
    @overload
    def setMinWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinWidth(float)"""
        super(_utils.BaseDrawable, self).setMinWidth(_float.valueOf(arg0))

    @override
    @overload
    def setMinHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinHeight(float)"""
        super(_utils.BaseDrawable, self).setMinHeight(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getLeftWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getLeftWidth()"""
        return float._wrap(super(utils.BaseDrawable, self).getLeftWidth())

    @override
    @overload
    def setBottomHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setBottomHeight(float)"""
        super(_utils.BaseDrawable, self).setBottomHeight(_float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getTopHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getTopHeight()"""
        return float._wrap(super(utils.BaseDrawable, self).getTopHeight())

    @overload
    def __init__(self):
        """public space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable()"""
        val = _ShapeDrawerDrawable()
        self.__wrapper = val

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float)"""
        super(_ShapeDrawerDrawable, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def getBottomHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getBottomHeight()"""
        return float._wrap(super(utils.BaseDrawable, self).getBottomHeight())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'ShapeDrawer'):
        """public space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable(space.earlygrey.shapedrawer.ShapeDrawer)"""
        val = _ShapeDrawerDrawable(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.toString()"""
        return str._wrap(super(utils.BaseDrawable, self).toString())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setMinSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinSize(float,float)"""
        super(_utils.BaseDrawable, self).setMinSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @override
    @overload
    def getMinHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinHeight()"""
        return float._wrap(super(utils.BaseDrawable, self).getMinHeight())

    @overload
    def getShapeDrawer(self) -> 'pyshapedrawer.ShapeDrawer':
        """public space.earlygrey.shapedrawer.ShapeDrawer space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable.getShapeDrawer()"""
        return 'pyshapedrawer.ShapeDrawer'._wrap(super(ShapeDrawerDrawable, self).getShapeDrawer())

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setName(java.lang.String)"""
        super(_utils.BaseDrawable, self).setName(arg0)

    @override
    @overload
    def setPadding(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setPadding(float,float,float,float)"""
        super(_utils.BaseDrawable, self).setPadding(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @abstractmethod
    def drawShapes(self, arg0: 'ShapeDrawer', arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable.drawShapes(space.earlygrey.shapedrawer.ShapeDrawer,float,float,float,float)"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setRightWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setRightWidth(float)"""
        super(_utils.BaseDrawable, self).setRightWidth(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable()"""
        val = _ShapeDrawerDrawable()
        self.__wrapper = val

    @overload
    def setShapeDrawer(self, arg0: 'ShapeDrawer'):
        """public void space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable.setShapeDrawer(space.earlygrey.shapedrawer.ShapeDrawer)"""
        super(_ShapeDrawerDrawable, self).setShapeDrawer(arg0)

    @override
    @overload
    def getRightWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getRightWidth()"""
        return float._wrap(super(utils.BaseDrawable, self).getRightWidth())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable 
 
 
# CLASS: space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
import space.earlygrey.shapedrawer.JoinType as _JoinType
_JoinType = _JoinType
try:
    import pyshapedrawer
except ImportError:
    pyshapedrawer = _import_once("pyshapedrawer")

import java.lang.String as _string
import java.lang.Boolean as _boolean
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable as _BaseDrawable
_BaseDrawable = _BaseDrawable
from builtins import float
import space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable as _ShapeDrawerDrawable
_ShapeDrawerDrawable = _ShapeDrawerDrawable
import space.earlygrey.shapedrawer.ShapeDrawer as _ShapeDrawer
_ShapeDrawer = _ShapeDrawer
import space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable as _GraphDrawerDrawable
_GraphDrawerDrawable = _GraphDrawerDrawable
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.math.Interpolation as _Interpolation
_Interpolation = _Interpolation
import java.lang.Float as _float
import java.lang.Integer as _int
import space.earlygrey.shapedrawer.GraphDrawer as _GraphDrawer
_GraphDrawer = _GraphDrawer
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GraphDrawerDrawable():
    """space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable"""
 
    @staticmethod
    def _wrap(java_value: _GraphDrawerDrawable) -> 'GraphDrawerDrawable':
        return GraphDrawerDrawable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GraphDrawerDrawable):
        """
        Dynamic initializer for GraphDrawerDrawable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GraphDrawerDrawable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GraphDrawerDrawable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setLeftWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setLeftWidth(float)"""
        super(_utils.BaseDrawable, self).setLeftWidth(_float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setSamples(self, arg0: int):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setSamples(int)"""
        super(_GraphDrawerDrawable, self).setSamples(_int.valueOf(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getName()"""
        return str._wrap(super(utils.BaseDrawable, self).getName())

    @overload
    def getPackedColor(self) -> float:
        """public float space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getPackedColor()"""
        return float._wrap(super(GraphDrawerDrawable, self).getPackedColor())

    @override
    @overload
    def setMinWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinWidth(float)"""
        super(_utils.BaseDrawable, self).setMinWidth(_float.valueOf(arg0))

    @override
    @overload
    def setMinHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinHeight(float)"""
        super(_utils.BaseDrawable, self).setMinHeight(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def setBottomHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setBottomHeight(float)"""
        super(_utils.BaseDrawable, self).setBottomHeight(_float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def isRescale(self) -> bool:
        """public boolean space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.isRescale()"""
        return bool._wrap(super(GraphDrawerDrawable, self).isRescale())

    @overload
    def setDomainEnd(self, arg0: float):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setDomainEnd(float)"""
        super(_GraphDrawerDrawable, self).setDomainEnd(_float.valueOf(arg0))

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float)"""
        super(_ShapeDrawerDrawable, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def setRescale(self, arg0: bool):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setRescale(boolean)"""
        super(_GraphDrawerDrawable, self).setRescale(_boolean.valueOf(arg0))

    @override
    @overload
    def getBottomHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getBottomHeight()"""
        return float._wrap(super(utils.BaseDrawable, self).getBottomHeight())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.toString()"""
        return str._wrap(super(utils.BaseDrawable, self).toString())

    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(_GraphDrawerDrawable, self).setInterpolation(arg0)

    @overload
    def getLineWidth(self) -> float:
        """public float space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getLineWidth()"""
        return float._wrap(super(GraphDrawerDrawable, self).getLineWidth())

    @overload
    def setGraphDrawer(self, arg0: 'GraphDrawer'):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setGraphDrawer(space.earlygrey.shapedrawer.GraphDrawer)"""
        super(_GraphDrawerDrawable, self).setGraphDrawer(arg0)

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setName(java.lang.String)"""
        super(_utils.BaseDrawable, self).setName(arg0)

    @overload
    def setColor(self, arg0: 'Color'):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_GraphDrawerDrawable, self).setColor(arg0)

    @overload
    def getDomainBegin(self) -> float:
        """public float space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getDomainBegin()"""
        return float._wrap(super(GraphDrawerDrawable, self).getDomainBegin())

    @overload
    def getSamples(self) -> int:
        """public int space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getSamples()"""
        return int._wrap(super(GraphDrawerDrawable, self).getSamples())

    @override
    @overload
    def getShapeDrawer(self) -> 'pyshapedrawer.ShapeDrawer':
        """public space.earlygrey.shapedrawer.ShapeDrawer space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable.getShapeDrawer()"""
        return 'pyshapedrawer.ShapeDrawer'._wrap(super(ShapeDrawerDrawable, self).getShapeDrawer())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setPlotBegin(self, arg0: float):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setPlotBegin(float)"""
        super(_GraphDrawerDrawable, self).setPlotBegin(_float.valueOf(arg0))

    @override
    @overload
    def setShapeDrawer(self, arg0: 'ShapeDrawer'):
        """public void space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable.setShapeDrawer(space.earlygrey.shapedrawer.ShapeDrawer)"""
        super(_ShapeDrawerDrawable, self).setShapeDrawer(arg0)

    @overload
    def getPlotBegin(self) -> float:
        """public float space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getPlotBegin()"""
        return float._wrap(super(GraphDrawerDrawable, self).getPlotBegin())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def setColor(self, arg0: float):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setColor(float)"""
        super(_GraphDrawerDrawable, self).setColor(_float.valueOf(arg0))

    @override
    @overload
    def getMinWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinWidth()"""
        return float._wrap(super(utils.BaseDrawable, self).getMinWidth())

    @override
    @overload
    def setTopHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setTopHeight(float)"""
        super(_utils.BaseDrawable, self).setTopHeight(_float.valueOf(arg0))

    @override
    @overload
    def getLeftWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getLeftWidth()"""
        return float._wrap(super(utils.BaseDrawable, self).getLeftWidth())

    @override
    @overload
    def getTopHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getTopHeight()"""
        return float._wrap(super(utils.BaseDrawable, self).getTopHeight())

    @overload
    def getJoinType(self) -> 'pyshapedrawer.JoinType':
        """public space.earlygrey.shapedrawer.JoinType space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getJoinType()"""
        return 'pyshapedrawer.JoinType'._wrap(super(GraphDrawerDrawable, self).getJoinType())

    @overload
    def getPlotEnd(self) -> float:
        """public float space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getPlotEnd()"""
        return float._wrap(super(GraphDrawerDrawable, self).getPlotEnd())

    @override
    @overload
    def drawShapes(self, arg0: 'ShapeDrawer', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.drawShapes(space.earlygrey.shapedrawer.ShapeDrawer,float,float,float,float)"""
        super(_GraphDrawerDrawable, self).drawShapes(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def getGraphDrawer(self) -> 'pyshapedrawer.GraphDrawer':
        """public space.earlygrey.shapedrawer.GraphDrawer space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getGraphDrawer()"""
        return 'pyshapedrawer.GraphDrawer'._wrap(super(GraphDrawerDrawable, self).getGraphDrawer())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setMinSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinSize(float,float)"""
        super(_utils.BaseDrawable, self).setMinSize(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getInterpolation()"""
        return 'math.Interpolation'._wrap(super(GraphDrawerDrawable, self).getInterpolation())

    @override
    @overload
    def getMinHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinHeight()"""
        return float._wrap(super(utils.BaseDrawable, self).getMinHeight())

    @overload
    def setJoinType(self, arg0: 'JoinType'):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setJoinType(space.earlygrey.shapedrawer.JoinType)"""
        super(_GraphDrawerDrawable, self).setJoinType(arg0)

    @overload
    def setDomainBegin(self, arg0: float):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setDomainBegin(float)"""
        super(_GraphDrawerDrawable, self).setDomainBegin(_float.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'GraphDrawer'):
        """public space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable(space.earlygrey.shapedrawer.GraphDrawer)"""
        val = _GraphDrawerDrawable(arg0)
        self.__wrapper = val

    @override
    @overload
    def setPadding(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setPadding(float,float,float,float)"""
        super(_utils.BaseDrawable, self).setPadding(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setPlotEnd(self, arg0: float):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setPlotEnd(float)"""
        super(_GraphDrawerDrawable, self).setPlotEnd(_float.valueOf(arg0))

    @override
    @overload
    def setRightWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setRightWidth(float)"""
        super(_utils.BaseDrawable, self).setRightWidth(_float.valueOf(arg0))

    @overload
    def setLineWidth(self, arg0: float):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setLineWidth(float)"""
        super(_GraphDrawerDrawable, self).setLineWidth(_float.valueOf(arg0))

    @overload
    def getDomainEnd(self) -> float:
        """public float space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getDomainEnd()"""
        return float._wrap(super(GraphDrawerDrawable, self).getDomainEnd())

    @override
    @overload
    def getRightWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getRightWidth()"""
        return float._wrap(super(utils.BaseDrawable, self).getRightWidth())