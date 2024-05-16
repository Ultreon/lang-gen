from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

from builtins import type
import com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable as __BaseDrawable
__BaseDrawable = __BaseDrawable
try:
    import pyshapedrawer
except ImportError:
    pyshapedrawer = __import_once__("pyshapedrawer")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable as __GraphDrawerDrawable
__GraphDrawerDrawable = __GraphDrawerDrawable
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import space.earlygrey.shapedrawer.JoinType as __JoinType
__JoinType = __JoinType
from builtins import bool
import space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable as __ShapeDrawerDrawable
__ShapeDrawerDrawable = __ShapeDrawerDrawable
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import space.earlygrey.shapedrawer.GraphDrawer as __GraphDrawer
__GraphDrawer = __GraphDrawer
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import space.earlygrey.shapedrawer.ShapeDrawer as __ShapeDrawer
__ShapeDrawer = __ShapeDrawer
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class GraphDrawerDrawable(__ShapeDrawerDrawable, ShapeDrawerDrawable):
    """space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable"""
 
    @staticmethod
    def __wrap(java_value: __GraphDrawerDrawable) -> 'GraphDrawerDrawable':
        return GraphDrawerDrawable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GraphDrawerDrawable):
        """
        Dynamic initializer for GraphDrawerDrawable.
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
    def setMinSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinSize(float,float)"""
        super(__utils.BaseDrawable, self).setMinSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def setMinHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinHeight(float)"""
        super(__utils.BaseDrawable, self).setMinHeight(__float.valueOf(arg0))

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float)"""
        super(__ShapeDrawerDrawable, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setPadding(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setPadding(float,float,float,float)"""
        super(__utils.BaseDrawable, self).setPadding(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def getLineWidth(self) -> float:
        """public float space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getLineWidth()"""
        return float.__wrap(super(GraphDrawerDrawable, self).getLineWidth())

    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getInterpolation()"""
        return 'math.Interpolation'.__wrap(super(GraphDrawerDrawable, self).getInterpolation())

    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(__GraphDrawerDrawable, self).setInterpolation(arg0)

    @override
    @overload
    def setBottomHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setBottomHeight(float)"""
        super(__utils.BaseDrawable, self).setBottomHeight(__float.valueOf(arg0))

    @overload
    def setJoinType(self, arg0: 'JoinType'):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setJoinType(space.earlygrey.shapedrawer.JoinType)"""
        super(__GraphDrawerDrawable, self).setJoinType(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setColor(self, arg0: float):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setColor(float)"""
        super(__GraphDrawerDrawable, self).setColor(__float.valueOf(arg0))

    @overload
    def setLineWidth(self, arg0: float):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setLineWidth(float)"""
        super(__GraphDrawerDrawable, self).setLineWidth(__float.valueOf(arg0))

    @override
    @overload
    def setMinWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinWidth(float)"""
        super(__utils.BaseDrawable, self).setMinWidth(__float.valueOf(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getName()"""
        return str.__wrap(super(utils.BaseDrawable, self).getName())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getGraphDrawer(self) -> 'pyshapedrawer.GraphDrawer':
        """public space.earlygrey.shapedrawer.GraphDrawer space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getGraphDrawer()"""
        return 'pyshapedrawer.GraphDrawer'.__wrap(super(GraphDrawerDrawable, self).getGraphDrawer())

    @overload
    def setPlotEnd(self, arg0: float):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setPlotEnd(float)"""
        super(__GraphDrawerDrawable, self).setPlotEnd(__float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.toString()"""
        return str.__wrap(super(utils.BaseDrawable, self).toString())

    @overload
    def getDomainBegin(self) -> float:
        """public float space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getDomainBegin()"""
        return float.__wrap(super(GraphDrawerDrawable, self).getDomainBegin())

    @override
    @overload
    def getBottomHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getBottomHeight()"""
        return float.__wrap(super(utils.BaseDrawable, self).getBottomHeight())

    @override
    @overload
    def getTopHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getTopHeight()"""
        return float.__wrap(super(utils.BaseDrawable, self).getTopHeight())

    @override
    @overload
    def setTopHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setTopHeight(float)"""
        super(__utils.BaseDrawable, self).setTopHeight(__float.valueOf(arg0))

    @overload
    def setSamples(self, arg0: int):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setSamples(int)"""
        super(__GraphDrawerDrawable, self).setSamples(__int.valueOf(arg0))

    @overload
    def getDomainEnd(self) -> float:
        """public float space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getDomainEnd()"""
        return float.__wrap(super(GraphDrawerDrawable, self).getDomainEnd())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'GraphDrawer'):
        """public space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable(space.earlygrey.shapedrawer.GraphDrawer)"""
        val = __GraphDrawerDrawable(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getLeftWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getLeftWidth()"""
        return float.__wrap(super(utils.BaseDrawable, self).getLeftWidth())

    @overload
    def getPlotEnd(self) -> float:
        """public float space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getPlotEnd()"""
        return float.__wrap(super(GraphDrawerDrawable, self).getPlotEnd())

    @overload
    def getSamples(self) -> int:
        """public int space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getSamples()"""
        return int.__wrap(super(GraphDrawerDrawable, self).getSamples())

    @overload
    def getPackedColor(self) -> float:
        """public float space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getPackedColor()"""
        return float.__wrap(super(GraphDrawerDrawable, self).getPackedColor())

    @overload
    def setGraphDrawer(self, arg0: 'GraphDrawer'):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setGraphDrawer(space.earlygrey.shapedrawer.GraphDrawer)"""
        super(__GraphDrawerDrawable, self).setGraphDrawer(arg0)

    @overload
    def isRescale(self) -> bool:
        """public boolean space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.isRescale()"""
        return bool.__wrap(super(GraphDrawerDrawable, self).isRescale())

    @overload
    def setColor(self, arg0: 'Color'):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__GraphDrawerDrawable, self).setColor(arg0)

    @override
    @overload
    def getRightWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getRightWidth()"""
        return float.__wrap(super(utils.BaseDrawable, self).getRightWidth())

    @overload
    def setPlotBegin(self, arg0: float):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setPlotBegin(float)"""
        super(__GraphDrawerDrawable, self).setPlotBegin(__float.valueOf(arg0))

    @override
    @overload
    def getMinWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinWidth()"""
        return float.__wrap(super(utils.BaseDrawable, self).getMinWidth())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getJoinType(self) -> 'pyshapedrawer.JoinType':
        """public space.earlygrey.shapedrawer.JoinType space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getJoinType()"""
        return 'pyshapedrawer.JoinType'.__wrap(super(GraphDrawerDrawable, self).getJoinType())

    @overload
    def setDomainEnd(self, arg0: float):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setDomainEnd(float)"""
        super(__GraphDrawerDrawable, self).setDomainEnd(__float.valueOf(arg0))

    @override
    @overload
    def setRightWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setRightWidth(float)"""
        super(__utils.BaseDrawable, self).setRightWidth(__float.valueOf(arg0))

    @override
    @overload
    def getShapeDrawer(self) -> 'pyshapedrawer.ShapeDrawer':
        """public space.earlygrey.shapedrawer.ShapeDrawer space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable.getShapeDrawer()"""
        return 'pyshapedrawer.ShapeDrawer'.__wrap(super(ShapeDrawerDrawable, self).getShapeDrawer())

    @override
    @overload
    def setShapeDrawer(self, arg0: 'ShapeDrawer'):
        """public void space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable.setShapeDrawer(space.earlygrey.shapedrawer.ShapeDrawer)"""
        super(__ShapeDrawerDrawable, self).setShapeDrawer(arg0)

    @overload
    def setRescale(self, arg0: bool):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setRescale(boolean)"""
        super(__GraphDrawerDrawable, self).setRescale(__boolean.valueOf(arg0))

    @overload
    def setDomainBegin(self, arg0: float):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setDomainBegin(float)"""
        super(__GraphDrawerDrawable, self).setDomainBegin(__float.valueOf(arg0))

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
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setName(java.lang.String)"""
        super(__utils.BaseDrawable, self).setName(arg0)

    @override
    @overload
    def drawShapes(self, arg0: 'ShapeDrawer', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.drawShapes(space.earlygrey.shapedrawer.ShapeDrawer,float,float,float,float)"""
        super(__GraphDrawerDrawable, self).drawShapes(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def setLeftWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setLeftWidth(float)"""
        super(__utils.BaseDrawable, self).setLeftWidth(__float.valueOf(arg0))

    @override
    @overload
    def getMinHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinHeight()"""
        return float.__wrap(super(utils.BaseDrawable, self).getMinHeight())

    @overload
    def getPlotBegin(self) -> float:
        """public float space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getPlotBegin()"""
        return float.__wrap(super(GraphDrawerDrawable, self).getPlotBegin())

 
 
 
# CLASS: space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

from builtins import type
import com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable as __BaseDrawable
__BaseDrawable = __BaseDrawable
try:
    import pyshapedrawer
except ImportError:
    pyshapedrawer = __import_once__("pyshapedrawer")

import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable as __GraphDrawerDrawable
__GraphDrawerDrawable = __GraphDrawerDrawable
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import space.earlygrey.shapedrawer.JoinType as __JoinType
__JoinType = __JoinType
from builtins import bool
import space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable as __ShapeDrawerDrawable
__ShapeDrawerDrawable = __ShapeDrawerDrawable
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import space.earlygrey.shapedrawer.GraphDrawer as __GraphDrawer
__GraphDrawer = __GraphDrawer
from builtins import float
import com.badlogic.gdx.math.Interpolation as __Interpolation
__Interpolation = __Interpolation
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import space.earlygrey.shapedrawer.ShapeDrawer as __ShapeDrawer
__ShapeDrawer = __ShapeDrawer
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class GraphDrawerDrawable(__ShapeDrawerDrawable, ShapeDrawerDrawable):
    """space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable"""
 
    @staticmethod
    def __wrap(java_value: __GraphDrawerDrawable) -> 'GraphDrawerDrawable':
        return GraphDrawerDrawable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GraphDrawerDrawable):
        """
        Dynamic initializer for GraphDrawerDrawable.
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
    def setMinSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinSize(float,float)"""
        super(__utils.BaseDrawable, self).setMinSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def setMinHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinHeight(float)"""
        super(__utils.BaseDrawable, self).setMinHeight(__float.valueOf(arg0))

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float)"""
        super(__ShapeDrawerDrawable, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setPadding(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setPadding(float,float,float,float)"""
        super(__utils.BaseDrawable, self).setPadding(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def getLineWidth(self) -> float:
        """public float space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getLineWidth()"""
        return float.__wrap(super(GraphDrawerDrawable, self).getLineWidth())

    @overload
    def getInterpolation(self) -> 'math.Interpolation':
        """public com.badlogic.gdx.math.Interpolation space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getInterpolation()"""
        return 'math.Interpolation'.__wrap(super(GraphDrawerDrawable, self).getInterpolation())

    @overload
    def setInterpolation(self, arg0: 'Interpolation'):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setInterpolation(com.badlogic.gdx.math.Interpolation)"""
        super(__GraphDrawerDrawable, self).setInterpolation(arg0)

    @override
    @overload
    def setBottomHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setBottomHeight(float)"""
        super(__utils.BaseDrawable, self).setBottomHeight(__float.valueOf(arg0))

    @overload
    def setJoinType(self, arg0: 'JoinType'):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setJoinType(space.earlygrey.shapedrawer.JoinType)"""
        super(__GraphDrawerDrawable, self).setJoinType(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setColor(self, arg0: float):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setColor(float)"""
        super(__GraphDrawerDrawable, self).setColor(__float.valueOf(arg0))

    @overload
    def setLineWidth(self, arg0: float):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setLineWidth(float)"""
        super(__GraphDrawerDrawable, self).setLineWidth(__float.valueOf(arg0))

    @override
    @overload
    def setMinWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinWidth(float)"""
        super(__utils.BaseDrawable, self).setMinWidth(__float.valueOf(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getName()"""
        return str.__wrap(super(utils.BaseDrawable, self).getName())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getGraphDrawer(self) -> 'pyshapedrawer.GraphDrawer':
        """public space.earlygrey.shapedrawer.GraphDrawer space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getGraphDrawer()"""
        return 'pyshapedrawer.GraphDrawer'.__wrap(super(GraphDrawerDrawable, self).getGraphDrawer())

    @overload
    def setPlotEnd(self, arg0: float):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setPlotEnd(float)"""
        super(__GraphDrawerDrawable, self).setPlotEnd(__float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.toString()"""
        return str.__wrap(super(utils.BaseDrawable, self).toString())

    @overload
    def getDomainBegin(self) -> float:
        """public float space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getDomainBegin()"""
        return float.__wrap(super(GraphDrawerDrawable, self).getDomainBegin())

    @override
    @overload
    def getBottomHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getBottomHeight()"""
        return float.__wrap(super(utils.BaseDrawable, self).getBottomHeight())

    @override
    @overload
    def getTopHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getTopHeight()"""
        return float.__wrap(super(utils.BaseDrawable, self).getTopHeight())

    @override
    @overload
    def setTopHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setTopHeight(float)"""
        super(__utils.BaseDrawable, self).setTopHeight(__float.valueOf(arg0))

    @overload
    def setSamples(self, arg0: int):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setSamples(int)"""
        super(__GraphDrawerDrawable, self).setSamples(__int.valueOf(arg0))

    @overload
    def getDomainEnd(self) -> float:
        """public float space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getDomainEnd()"""
        return float.__wrap(super(GraphDrawerDrawable, self).getDomainEnd())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'GraphDrawer'):
        """public space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable(space.earlygrey.shapedrawer.GraphDrawer)"""
        val = __GraphDrawerDrawable(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getLeftWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getLeftWidth()"""
        return float.__wrap(super(utils.BaseDrawable, self).getLeftWidth())

    @overload
    def getPlotEnd(self) -> float:
        """public float space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getPlotEnd()"""
        return float.__wrap(super(GraphDrawerDrawable, self).getPlotEnd())

    @overload
    def getSamples(self) -> int:
        """public int space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getSamples()"""
        return int.__wrap(super(GraphDrawerDrawable, self).getSamples())

    @overload
    def getPackedColor(self) -> float:
        """public float space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getPackedColor()"""
        return float.__wrap(super(GraphDrawerDrawable, self).getPackedColor())

    @overload
    def setGraphDrawer(self, arg0: 'GraphDrawer'):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setGraphDrawer(space.earlygrey.shapedrawer.GraphDrawer)"""
        super(__GraphDrawerDrawable, self).setGraphDrawer(arg0)

    @overload
    def isRescale(self) -> bool:
        """public boolean space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.isRescale()"""
        return bool.__wrap(super(GraphDrawerDrawable, self).isRescale())

    @overload
    def setColor(self, arg0: 'Color'):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__GraphDrawerDrawable, self).setColor(arg0)

    @override
    @overload
    def getRightWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getRightWidth()"""
        return float.__wrap(super(utils.BaseDrawable, self).getRightWidth())

    @overload
    def setPlotBegin(self, arg0: float):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setPlotBegin(float)"""
        super(__GraphDrawerDrawable, self).setPlotBegin(__float.valueOf(arg0))

    @override
    @overload
    def getMinWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinWidth()"""
        return float.__wrap(super(utils.BaseDrawable, self).getMinWidth())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getJoinType(self) -> 'pyshapedrawer.JoinType':
        """public space.earlygrey.shapedrawer.JoinType space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getJoinType()"""
        return 'pyshapedrawer.JoinType'.__wrap(super(GraphDrawerDrawable, self).getJoinType())

    @overload
    def setDomainEnd(self, arg0: float):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setDomainEnd(float)"""
        super(__GraphDrawerDrawable, self).setDomainEnd(__float.valueOf(arg0))

    @override
    @overload
    def setRightWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setRightWidth(float)"""
        super(__utils.BaseDrawable, self).setRightWidth(__float.valueOf(arg0))

    @override
    @overload
    def getShapeDrawer(self) -> 'pyshapedrawer.ShapeDrawer':
        """public space.earlygrey.shapedrawer.ShapeDrawer space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable.getShapeDrawer()"""
        return 'pyshapedrawer.ShapeDrawer'.__wrap(super(ShapeDrawerDrawable, self).getShapeDrawer())

    @override
    @overload
    def setShapeDrawer(self, arg0: 'ShapeDrawer'):
        """public void space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable.setShapeDrawer(space.earlygrey.shapedrawer.ShapeDrawer)"""
        super(__ShapeDrawerDrawable, self).setShapeDrawer(arg0)

    @overload
    def setRescale(self, arg0: bool):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setRescale(boolean)"""
        super(__GraphDrawerDrawable, self).setRescale(__boolean.valueOf(arg0))

    @overload
    def setDomainBegin(self, arg0: float):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.setDomainBegin(float)"""
        super(__GraphDrawerDrawable, self).setDomainBegin(__float.valueOf(arg0))

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
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setName(java.lang.String)"""
        super(__utils.BaseDrawable, self).setName(arg0)

    @override
    @overload
    def drawShapes(self, arg0: 'ShapeDrawer', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.drawShapes(space.earlygrey.shapedrawer.ShapeDrawer,float,float,float,float)"""
        super(__GraphDrawerDrawable, self).drawShapes(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def setLeftWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setLeftWidth(float)"""
        super(__utils.BaseDrawable, self).setLeftWidth(__float.valueOf(arg0))

    @override
    @overload
    def getMinHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinHeight()"""
        return float.__wrap(super(utils.BaseDrawable, self).getMinHeight())

    @overload
    def getPlotBegin(self) -> float:
        """public float space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable.getPlotBegin()"""
        return float.__wrap(super(GraphDrawerDrawable, self).getPlotBegin())

 
 
 
# CLASS: space.earlygrey.shapedrawer.scene2d.GraphDrawerDrawable 
 
 
# CLASS: space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable as __BaseDrawable
__BaseDrawable = __BaseDrawable
from builtins import float
from abc import abstractmethod, ABC
try:
    import pyshapedrawer
except ImportError:
    pyshapedrawer = __import_once__("pyshapedrawer")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import space.earlygrey.shapedrawer.ShapeDrawer as __ShapeDrawer
__ShapeDrawer = __ShapeDrawer
import java.lang.Integer as __int
from builtins import bool
import space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable as __ShapeDrawerDrawable
__ShapeDrawerDrawable = __ShapeDrawerDrawable
from builtins import int
 
class ShapeDrawerDrawable(ABC, scene2d.__BaseDrawable, utils.BaseDrawable):
    """space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable"""
 
    @staticmethod
    def __wrap(java_value: __ShapeDrawerDrawable) -> 'ShapeDrawerDrawable':
        return ShapeDrawerDrawable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ShapeDrawerDrawable):
        """
        Dynamic initializer for ShapeDrawerDrawable.
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
    def setMinSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinSize(float,float)"""
        super(__utils.BaseDrawable, self).setMinSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'ShapeDrawer'):
        """public space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable(space.earlygrey.shapedrawer.ShapeDrawer)"""
        val = __ShapeDrawerDrawable(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable()"""
        val = __ShapeDrawerDrawable()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getLeftWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getLeftWidth()"""
        return float.__wrap(super(utils.BaseDrawable, self).getLeftWidth())

    @override
    @overload
    def setMinHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinHeight(float)"""
        super(__utils.BaseDrawable, self).setMinHeight(__float.valueOf(arg0))

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float)"""
        super(__ShapeDrawerDrawable, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setPadding(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setPadding(float,float,float,float)"""
        super(__utils.BaseDrawable, self).setPadding(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def getShapeDrawer(self) -> 'pyshapedrawer.ShapeDrawer':
        """public space.earlygrey.shapedrawer.ShapeDrawer space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable.getShapeDrawer()"""
        return 'pyshapedrawer.ShapeDrawer'.__wrap(super(ShapeDrawerDrawable, self).getShapeDrawer())

    @override
    @overload
    def setBottomHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setBottomHeight(float)"""
        super(__utils.BaseDrawable, self).setBottomHeight(__float.valueOf(arg0))

    @override
    @overload
    def getRightWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getRightWidth()"""
        return float.__wrap(super(utils.BaseDrawable, self).getRightWidth())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getMinWidth(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinWidth()"""
        return float.__wrap(super(utils.BaseDrawable, self).getMinWidth())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setShapeDrawer(self, arg0: 'ShapeDrawer'):
        """public void space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable.setShapeDrawer(space.earlygrey.shapedrawer.ShapeDrawer)"""
        super(__ShapeDrawerDrawable, self).setShapeDrawer(arg0)

    @overload
    def __init__(self):
        """public space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable()"""
        val = __ShapeDrawerDrawable()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setMinWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setMinWidth(float)"""
        super(__utils.BaseDrawable, self).setMinWidth(__float.valueOf(arg0))

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getName()"""
        return str.__wrap(super(utils.BaseDrawable, self).getName())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setRightWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setRightWidth(float)"""
        super(__utils.BaseDrawable, self).setRightWidth(__float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.toString()"""
        return str.__wrap(super(utils.BaseDrawable, self).toString())

    @override
    @overload
    def getBottomHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getBottomHeight()"""
        return float.__wrap(super(utils.BaseDrawable, self).getBottomHeight())

    @override
    @overload
    def getTopHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getTopHeight()"""
        return float.__wrap(super(utils.BaseDrawable, self).getTopHeight())

    @override
    @overload
    def setTopHeight(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setTopHeight(float)"""
        super(__utils.BaseDrawable, self).setTopHeight(__float.valueOf(arg0))

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
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setName(java.lang.String)"""
        super(__utils.BaseDrawable, self).setName(arg0)

    @abstractmethod
    def drawShapes(self, arg0: 'ShapeDrawer', arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void space.earlygrey.shapedrawer.scene2d.ShapeDrawerDrawable.drawShapes(space.earlygrey.shapedrawer.ShapeDrawer,float,float,float,float)"""
        pass

    @override
    @overload
    def setLeftWidth(self, arg0: float):
        """public void com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.setLeftWidth(float)"""
        super(__utils.BaseDrawable, self).setLeftWidth(__float.valueOf(arg0))

    @override
    @overload
    def getMinHeight(self) -> float:
        """public float com.badlogic.gdx.scenes.scene2d.utils.BaseDrawable.getMinHeight()"""
        return float.__wrap(super(utils.BaseDrawable, self).getMinHeight())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()