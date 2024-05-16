from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g2d.TextureRegion as _TextureRegion
_TextureRegion = _TextureRegion
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

import com.badlogic.gdx.graphics.g2d.Batch as _Batch
_Batch = _Batch
from pyquantum_helper import override
import space.earlygrey.shapedrawer.AbstractShapeDrawer as _AbstractShapeDrawer
_AbstractShapeDrawer = _AbstractShapeDrawer
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import space.earlygrey.shapedrawer.Drawing as _Drawing
_Drawing = _Drawing
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import space.earlygrey.shapedrawer.ShapeDrawer as _ShapeDrawer
_ShapeDrawer = _ShapeDrawer
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import space.earlygrey.shapedrawer.SideEstimator as _SideEstimator
_SideEstimator = _SideEstimator
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ShapeDrawer():
    """space.earlygrey.shapedrawer.ShapeDrawer"""
 
    @staticmethod
    def _wrap(java_value: _ShapeDrawer) -> 'ShapeDrawer':
        return ShapeDrawer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShapeDrawer):
        """
        Dynamic initializer for ShapeDrawer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShapeDrawer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShapeDrawer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def rectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(float,float,float,float,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).rectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4)

    @overload
    def triangle(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: float, arg4: 'JoinType', arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,float,space.earlygrey.shapedrawer.JoinType,float)"""
        super(_ShapeDrawer, self).triangle(arg0, arg1, arg2, _float.valueOf(arg3), arg4, _float.valueOf(arg5))

    @overload
    def filledRectangle(self, arg0: 'Rectangle', arg1: 'Color', arg2: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledRectangle(arg0, arg1, arg2)

    @overload
    def triangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: 'JoinType', arg8: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(float,float,float,float,float,float,float,space.earlygrey.shapedrawer.JoinType,float)"""
        super(_ShapeDrawer, self).triangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), arg7, _float.valueOf(arg8))

    @overload
    def __init__(self, arg0: 'Batch', arg1: 'TextureRegion'):
        """public space.earlygrey.shapedrawer.ShapeDrawer(com.badlogic.gdx.graphics.g2d.Batch,com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = _ShapeDrawer(arg0, arg1)
        self.__wrapper = val

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).line(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4)

    @overload
    def path(self, arg0: 'FloatArray', arg1: float, arg2: 'JoinType', arg3: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(com.badlogic.gdx.utils.FloatArray,float,space.earlygrey.shapedrawer.JoinType,boolean)"""
        super(_ShapeDrawer, self).path(arg0, _float.valueOf(arg1), arg2, _boolean.valueOf(arg3))

    @overload
    def circle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.circle(float,float,float,float,space.earlygrey.shapedrawer.JoinType)"""
        super(_ShapeDrawer, self).circle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def polygon(self, arg0: 'float'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float[])"""
        super(_ShapeDrawer, self).polygon(arg0)

    @overload
    def setTextureRegion(self, arg0: 'TextureRegion') -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion space.earlygrey.shapedrawer.AbstractShapeDrawer.setTextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return 'g2d.TextureRegion'._wrap(super(_AbstractShapeDrawer, self).setTextureRegion(arg0))

    @overload
    def path(self, arg0: 'Array', arg1: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.Vector2>,float)"""
        super(_ShapeDrawer, self).path(arg0, _float.valueOf(arg1))

    @overload
    def filledRectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'Color', arg6: 'Color', arg7: 'Color', arg8: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledRectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), arg5, arg6, arg7, arg8)

    @overload
    def polygon(self, arg0: 'float', arg1: int, arg2: int, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float[],int,int,float)"""
        super(_ShapeDrawer, self).polygon(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def setDefaultLineWidth(self, arg0: float) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.setDefaultLineWidth(float)"""
        return float._wrap(super(_AbstractShapeDrawer, self).setDefaultLineWidth(_float.valueOf(arg0)))

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float,com.badlogic.gdx.graphics.Color,float)"""
        super(_ShapeDrawer, self).line(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4, _float.valueOf(arg5))

    @overload
    def sector(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.sector(float,float,float,float,float)"""
        super(_ShapeDrawer, self).sector(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def getBatch(self) -> 'g2d.Batch':
        """public com.badlogic.gdx.graphics.g2d.Batch space.earlygrey.shapedrawer.AbstractShapeDrawer.getBatch()"""
        return 'g2d.Batch'._wrap(super(AbstractShapeDrawer, self).getBatch())

    @overload
    def rectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(float,float,float,float,float,float,space.earlygrey.shapedrawer.JoinType)"""
        super(_ShapeDrawer, self).rectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6)

    @overload
    def filledRectangle(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(float,float,float,float)"""
        super(_ShapeDrawer, self).filledRectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def __init__(self, arg0: 'Batch', arg1: 'TextureRegion', arg2: 'SideEstimator'):
        """public space.earlygrey.shapedrawer.ShapeDrawer(com.badlogic.gdx.graphics.g2d.Batch,com.badlogic.gdx.graphics.g2d.TextureRegion,space.earlygrey.shapedrawer.SideEstimator)"""
        val = _ShapeDrawer(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def circle(self, arg0: float, arg1: float, arg2: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.circle(float,float,float)"""
        super(_ShapeDrawer, self).circle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def filledCircle(self, arg0: 'Vector2', arg1: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledCircle(com.badlogic.gdx.math.Vector2,float)"""
        super(_ShapeDrawer, self).filledCircle(arg0, _float.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def filledRectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'Color', arg6: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledRectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), arg5, arg6)

    @overload
    def polygon(self, arg0: 'Polygon', arg1: float, arg2: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(com.badlogic.gdx.math.Polygon,float,space.earlygrey.shapedrawer.JoinType)"""
        super(_ShapeDrawer, self).polygon(arg0, _float.valueOf(arg1), arg2)

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.setColor(float,float,float,float)"""
        return float._wrap(super(_AbstractShapeDrawer, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def filledRectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledRectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4, arg5)

    @overload
    def triangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(float,float,float,float,float,float,float,float)"""
        super(_ShapeDrawer, self).triangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7))

    @overload
    def arc(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: bool, arg7: int):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.arc(float,float,float,float,float,float,boolean,int)"""
        super(_ShapeDrawer, self).arc(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _boolean.valueOf(arg6), _int.valueOf(arg7))

    @overload
    def triangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(float,float,float,float,float,float,float)"""
        super(_ShapeDrawer, self).triangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6))

    @overload
    def line(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).line(arg0, arg1, arg2)

    @overload
    def rectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(float,float,float,float,float,float)"""
        super(_ShapeDrawer, self).rectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))

    @overload
    def rectangle(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(float,float,float,float)"""
        super(_ShapeDrawer, self).rectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def filledEllipse(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledEllipse(float,float,float,float)"""
        super(_ShapeDrawer, self).filledEllipse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def filledRectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(float,float,float,float,float)"""
        super(_ShapeDrawer, self).filledRectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def updatePixelSize(self) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.updatePixelSize()"""
        return float._wrap(super(AbstractShapeDrawer, self).updatePixelSize())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def sector(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.sector(float,float,float,float,float,int)"""
        super(_ShapeDrawer, self).sector(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5))

    @overload
    def line(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Color', arg3: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).line(arg0, arg1, arg2, arg3)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def filledRectangle(self, arg0: 'Rectangle', arg1: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledRectangle(arg0, arg1)

    @override
    @overload
    def getSideEstimator(self) -> 'SideEstimator':
        """public final space.earlygrey.shapedrawer.SideEstimator space.earlygrey.shapedrawer.AbstractShapeDrawer.getSideEstimator()"""
        return 'SideEstimator'._wrap(super(AbstractShapeDrawer, self).getSideEstimator())

    @overload
    def filledPolygon(self, arg0: 'Polygon', arg1: 'ShortArray'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(com.badlogic.gdx.math.Polygon,com.badlogic.gdx.utils.ShortArray)"""
        super(_ShapeDrawer, self).filledPolygon(arg0, arg1)

    @overload
    def circle(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.circle(float,float,float,float)"""
        super(_ShapeDrawer, self).circle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def filledEllipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledEllipse(float,float,float,float,float)"""
        super(_ShapeDrawer, self).filledEllipse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def filledPolygon(self, arg0: 'float', arg1: 'ShortArray'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float[],com.badlogic.gdx.utils.ShortArray)"""
        super(_ShapeDrawer, self).filledPolygon(arg0, arg1)

    @overload
    def triangles(self, arg0: 'float', arg1: 'short', arg2: float, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangles(float[],short[],float,float)"""
        super(_ShapeDrawer, self).triangles(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def rectangle(self, arg0: 'Rectangle', arg1: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(com.badlogic.gdx.math.Rectangle,float)"""
        super(_ShapeDrawer, self).rectangle(arg0, _float.valueOf(arg1))

    @overload
    def filledPolygon(self, arg0: 'Polygon', arg1: 'short'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(com.badlogic.gdx.math.Polygon,short[])"""
        super(_ShapeDrawer, self).filledPolygon(arg0, arg1)

    @overload
    def polygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float,float,int,float,float,float,float)"""
        super(_ShapeDrawer, self).polygon(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6))

    @overload
    def path(self, arg0: 'float', arg1: int, arg2: int, arg3: float, arg4: 'JoinType', arg5: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(float[],int,int,float,space.earlygrey.shapedrawer.JoinType,boolean)"""
        super(_ShapeDrawer, self).path(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), arg4, _boolean.valueOf(arg5))

    @overload
    def filledRectangle(self, arg0: 'Rectangle', arg1: float, arg2: 'Color', arg3: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(com.badlogic.gdx.math.Rectangle,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledRectangle(arg0, _float.valueOf(arg1), arg2, arg3)

    @overload
    def filledCircle(self, arg0: float, arg1: float, arg2: float, arg3: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledCircle(float,float,float,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledCircle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), arg3)

    @overload
    def filledRectangle(self, arg0: 'Rectangle'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(com.badlogic.gdx.math.Rectangle)"""
        super(_ShapeDrawer, self).filledRectangle(arg0)

    @overload
    def filledCircle(self, arg0: 'Vector2', arg1: float, arg2: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledCircle(com.badlogic.gdx.math.Vector2,float,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledCircle(arg0, _float.valueOf(arg1), arg2)

    @overload
    def filledPolygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float,float,int,float,float)"""
        super(_ShapeDrawer, self).filledPolygon(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def polygon(self, arg0: 'Polygon', arg1: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(com.badlogic.gdx.math.Polygon,float)"""
        super(_ShapeDrawer, self).polygon(arg0, _float.valueOf(arg1))

    @overload
    def setColor(self, arg0: float) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.setColor(float)"""
        return float._wrap(super(_AbstractShapeDrawer, self).setColor(_float.valueOf(arg0)))

    @overload
    def polygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float,float,int,float,float,float,space.earlygrey.shapedrawer.JoinType)"""
        super(_ShapeDrawer, self).polygon(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6)

    @overload
    def rectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(float,float,float,float,float,space.earlygrey.shapedrawer.JoinType)"""
        super(_ShapeDrawer, self).rectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), arg5)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def arc(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.arc(float,float,float,float,float,float)"""
        super(_ShapeDrawer, self).arc(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))

    @override
    @overload
    def getPixelSize(self) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.getPixelSize()"""
        return float._wrap(super(AbstractShapeDrawer, self).getPixelSize())

    @overload
    def setDefaultSnap(self, arg0: bool) -> bool:
        """public boolean space.earlygrey.shapedrawer.AbstractShapeDrawer.setDefaultSnap(boolean)"""
        return bool._wrap(super(_AbstractShapeDrawer, self).setDefaultSnap(_boolean.valueOf(arg0)))

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: bool, arg6: 'Color', arg7: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float,float,boolean,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).line(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _boolean.valueOf(arg5), arg6, arg7)

    @overload
    def triangle(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,float)"""
        super(_ShapeDrawer, self).triangle(arg0, arg1, arg2, _float.valueOf(arg3))

    @overload
    def rectangle(self, arg0: 'Rectangle', arg1: 'Color', arg2: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.graphics.Color,float)"""
        super(_ShapeDrawer, self).rectangle(arg0, arg1, _float.valueOf(arg2))

    @overload
    def rectangle(self, arg0: 'Rectangle', arg1: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).rectangle(arg0, arg1)

    @overload
    def filledRectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: 'Color', arg6: 'Color', arg7: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledRectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4, arg5, arg6, arg7)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def update(self):
        """public void space.earlygrey.shapedrawer.AbstractShapeDrawer.update()"""
        super(AbstractShapeDrawer, self).update()

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).line(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4, arg5)

    @overload
    def path(self, arg0: 'float', arg1: float, arg2: 'JoinType', arg3: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(float[],float,space.earlygrey.shapedrawer.JoinType,boolean)"""
        super(_ShapeDrawer, self).path(arg0, _float.valueOf(arg1), arg2, _boolean.valueOf(arg3))

    @overload
    def circle(self, arg0: float, arg1: float, arg2: float, arg3: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.circle(float,float,float,space.earlygrey.shapedrawer.JoinType)"""
        super(_ShapeDrawer, self).circle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), arg3)

    @overload
    def filledPolygon(self, arg0: 'Polygon'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(com.badlogic.gdx.math.Polygon)"""
        super(_ShapeDrawer, self).filledPolygon(arg0)

    @overload
    def filledPolygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float,float,int,float,float,float)"""
        super(_ShapeDrawer, self).filledPolygon(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float,float)"""
        super(_ShapeDrawer, self).line(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def arc(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.arc(float,float,float,float,float)"""
        super(_ShapeDrawer, self).arc(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def filledTriangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'Color', arg7: 'Color', arg8: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledTriangle(float,float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledTriangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8)

    @overload
    def path(self, arg0: 'Array', arg1: float, arg2: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.Vector2>,float,boolean)"""
        super(_ShapeDrawer, self).path(arg0, _float.valueOf(arg1), _boolean.valueOf(arg2))

    @overload
    def filledTriangle(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Color', arg4: 'Color', arg5: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledTriangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledTriangle(arg0, arg1, arg2, arg3, arg4, arg5)

    @overload
    def sector(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: float, arg7: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.sector(float,float,float,float,float,int,float,float)"""
        super(_ShapeDrawer, self).sector(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7))

    @overload
    def filledTriangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledTriangle(float,float,float,float,float,float)"""
        super(_ShapeDrawer, self).filledTriangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def filledPolygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float,float,int,float,float,float,float,float)"""
        super(_ShapeDrawer, self).filledPolygon(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7))

    @overload
    def filledRectangle(self, arg0: 'Rectangle', arg1: float, arg2: 'Color', arg3: 'Color', arg4: 'Color', arg5: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(com.badlogic.gdx.math.Rectangle,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledRectangle(arg0, _float.valueOf(arg1), arg2, arg3, arg4, arg5)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def filledEllipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'Color', arg6: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledEllipse(float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledEllipse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), arg5, arg6)

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: bool, arg6: float, arg7: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float,float,boolean,float,float)"""
        super(_ShapeDrawer, self).line(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _boolean.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7))

    @overload
    def filledPolygon(self, arg0: float, arg1: float, arg2: int, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float,float,int,float)"""
        super(_ShapeDrawer, self).filledPolygon(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def setColor(self, arg0: 'Color') -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.setColor(com.badlogic.gdx.graphics.Color)"""
        return float._wrap(super(_AbstractShapeDrawer, self).setColor(arg0))

    @overload
    def filledRectangle(self, arg0: 'Rectangle', arg1: 'Color', arg2: 'Color', arg3: 'Color', arg4: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledRectangle(arg0, arg1, arg2, arg3, arg4)

    @overload
    def filledPolygon(self, arg0: 'float', arg1: int, arg2: int):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float[],int,int)"""
        super(_ShapeDrawer, self).filledPolygon(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def polygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float,float,int,float,float,float)"""
        super(_ShapeDrawer, self).polygon(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))

    @overload
    def rectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(float,float,float,float,float)"""
        super(_ShapeDrawer, self).rectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def polygon(self, arg0: 'Polygon'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(com.badlogic.gdx.math.Polygon)"""
        super(_ShapeDrawer, self).polygon(arg0)

    @overload
    def path(self, arg0: 'Array', arg1: float, arg2: 'JoinType', arg3: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.Vector2>,float,space.earlygrey.shapedrawer.JoinType,boolean)"""
        super(_ShapeDrawer, self).path(arg0, _float.valueOf(arg1), arg2, _boolean.valueOf(arg3))

    @overload
    def arc(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.arc(float,float,float,float,float,float,boolean)"""
        super(_ShapeDrawer, self).arc(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _boolean.valueOf(arg6))

    @overload
    def filledRectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(float,float,float,float,float,float,float,float,float)"""
        super(_ShapeDrawer, self).filledRectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8))

    @overload
    def filledPolygon(self, arg0: 'float'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float[])"""
        super(_ShapeDrawer, self).filledPolygon(arg0)

    @override
    @overload
    def getPackedColor(self) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.getPackedColor()"""
        return float._wrap(super(AbstractShapeDrawer, self).getPackedColor())

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float)"""
        super(_ShapeDrawer, self).line(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def triangle(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(_ShapeDrawer, self).triangle(arg0, arg1, arg2)

    @overload
    def filledCircle(self, arg0: float, arg1: float, arg2: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledCircle(float,float,float)"""
        super(_ShapeDrawer, self).filledCircle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def filledPolygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: 'Color', arg7: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float,float,int,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledPolygon(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6, arg7)

    @override
    @overload
    def startRecording(self):
        """public void space.earlygrey.shapedrawer.AbstractShapeDrawer.startRecording()"""
        super(AbstractShapeDrawer, self).startRecording()

    @overload
    def path(self, arg0: 'Array', arg1: 'JoinType', arg2: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.Vector2>,space.earlygrey.shapedrawer.JoinType,boolean)"""
        super(_ShapeDrawer, self).path(arg0, arg1, _boolean.valueOf(arg2))

    @override
    @overload
    def update(self, arg0: bool):
        """public void space.earlygrey.shapedrawer.AbstractShapeDrawer.update(boolean)"""
        super(_AbstractShapeDrawer, self).update(_boolean.valueOf(arg0))

    @overload
    def filledEllipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledEllipse(float,float,float,float,float,float,float)"""
        super(_ShapeDrawer, self).filledEllipse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6))

    @overload
    def rectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(float,float,float,float,com.badlogic.gdx.graphics.Color,float)"""
        super(_ShapeDrawer, self).rectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4, _float.valueOf(arg5))

    @override
    @overload
    def getDefaultLineWidth(self) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.getDefaultLineWidth()"""
        return float._wrap(super(AbstractShapeDrawer, self).getDefaultLineWidth())

    @overload
    def path(self, arg0: 'Array', arg1: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.Vector2>,space.earlygrey.shapedrawer.JoinType)"""
        super(_ShapeDrawer, self).path(arg0, arg1)

    @overload
    def polygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float,float,int,float,float)"""
        super(_ShapeDrawer, self).polygon(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def isDefaultSnap(self) -> bool:
        """public boolean space.earlygrey.shapedrawer.AbstractShapeDrawer.isDefaultSnap()"""
        return bool._wrap(super(AbstractShapeDrawer, self).isDefaultSnap())

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float,float,boolean)"""
        super(_ShapeDrawer, self).line(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _boolean.valueOf(arg5))

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'Color', arg6: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).line(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), arg5, arg6)

    @overload
    def polygon(self, arg0: 'float', arg1: int, arg2: int, arg3: float, arg4: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float[],int,int,float,space.earlygrey.shapedrawer.JoinType)"""
        super(_ShapeDrawer, self).polygon(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), arg4)

    @overload
    def polygon(self, arg0: 'float', arg1: float, arg2: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float[],float,space.earlygrey.shapedrawer.JoinType)"""
        super(_ShapeDrawer, self).polygon(arg0, _float.valueOf(arg1), arg2)

    @overload
    def filledTriangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledTriangle(float,float,float,float,float,float,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledTriangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6)

    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.ellipse(float,float,float,float,float,float,space.earlygrey.shapedrawer.JoinType)"""
        super(_ShapeDrawer, self).ellipse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6)

    @overload
    def triangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(float,float,float,float,float,float)"""
        super(_ShapeDrawer, self).triangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))

    @overload
    def __init__(self, arg0: 'Batch'):
        """public space.earlygrey.shapedrawer.ShapeDrawer(com.badlogic.gdx.graphics.g2d.Batch)"""
        val = _ShapeDrawer(arg0)
        self.__wrapper = val

    @overload
    def filledPolygon(self, arg0: 'float', arg1: 'short', arg2: float, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float[],short[],float,float)"""
        super(_ShapeDrawer, self).filledPolygon(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def line(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Color', arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.graphics.Color,float)"""
        super(_ShapeDrawer, self).line(arg0, arg1, arg2, _float.valueOf(arg3))

    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.ellipse(float,float,float,float)"""
        super(_ShapeDrawer, self).ellipse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def triangle(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,float,float)"""
        super(_ShapeDrawer, self).triangle(arg0, arg1, arg2, _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def path(self, arg0: 'float', arg1: int, arg2: int, arg3: float, arg4: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(float[],int,int,float,boolean)"""
        super(_ShapeDrawer, self).path(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _boolean.valueOf(arg4))

    @overload
    def filledRectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(float,float,float,float,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledRectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4)

    @overload
    def line(self, arg0: 'Vector2', arg1: 'Vector2', arg2: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,float)"""
        super(_ShapeDrawer, self).line(arg0, arg1, _float.valueOf(arg2))

    @overload
    def sector(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'Color', arg6: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.sector(float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).sector(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), arg5, arg6)

    @overload
    def setSideEstimator(self, arg0: 'SideEstimator') -> 'SideEstimator':
        """public space.earlygrey.shapedrawer.SideEstimator space.earlygrey.shapedrawer.AbstractShapeDrawer.setSideEstimator(space.earlygrey.shapedrawer.SideEstimator)"""
        return 'SideEstimator'._wrap(super(_AbstractShapeDrawer, self).setSideEstimator(arg0))

    @overload
    def rectangle(self, arg0: 'Rectangle'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(com.badlogic.gdx.math.Rectangle)"""
        super(_ShapeDrawer, self).rectangle(arg0)

    @overload
    def polygon(self, arg0: 'Polygon', arg1: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(com.badlogic.gdx.math.Polygon,space.earlygrey.shapedrawer.JoinType)"""
        super(_ShapeDrawer, self).polygon(arg0, arg1)

    @overload
    def line(self, arg0: 'Vector2', arg1: 'Vector2'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(_ShapeDrawer, self).line(arg0, arg1)

    @overload
    def triangle(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).triangle(arg0, arg1, arg2, arg3)

    @overload
    def filledPolygon(self, arg0: 'float', arg1: 'short'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float[],short[])"""
        super(_ShapeDrawer, self).filledPolygon(arg0, arg1)

    @override
    @overload
    def getRegion(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion space.earlygrey.shapedrawer.AbstractShapeDrawer.getRegion()"""
        return 'g2d.TextureRegion'._wrap(super(AbstractShapeDrawer, self).getRegion())

    @overload
    def polygon(self, arg0: float, arg1: float, arg2: int, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float,float,int,float)"""
        super(_ShapeDrawer, self).polygon(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def path(self, arg0: 'Array', arg1: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.Vector2>,boolean)"""
        super(_ShapeDrawer, self).path(arg0, _boolean.valueOf(arg1))

    @overload
    def filledTriangle(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledTriangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(_ShapeDrawer, self).filledTriangle(arg0, arg1, arg2)

    @overload
    def setPixelSize(self, arg0: float) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.setPixelSize(float)"""
        return float._wrap(super(_AbstractShapeDrawer, self).setPixelSize(_float.valueOf(arg0)))

    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.ellipse(float,float,float,float,float,float)"""
        super(_ShapeDrawer, self).ellipse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))

    @overload
    def path(self, arg0: 'Array'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.Vector2>)"""
        super(_ShapeDrawer, self).path(arg0)

    @overload
    def polygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float,float,int,float,float,float,float,space.earlygrey.shapedrawer.JoinType)"""
        super(_ShapeDrawer, self).polygon(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), arg7)

    @overload
    def filledTriangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledTriangle(float,float,float,float,float,float,float,float,float)"""
        super(_ShapeDrawer, self).filledTriangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8))

    @overload
    def triangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(float,float,float,float,float,float,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).triangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6)

    @overload
    def filledTriangle(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledTriangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledTriangle(arg0, arg1, arg2, arg3)

    @override
    @overload
    def stopRecording(self) -> 'Drawing':
        """public space.earlygrey.shapedrawer.Drawing space.earlygrey.shapedrawer.AbstractShapeDrawer.stopRecording()"""
        return 'Drawing'._wrap(super(AbstractShapeDrawer, self).stopRecording())

    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.ellipse(float,float,float,float,float)"""
        super(_ShapeDrawer, self).ellipse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

 
 
 
# CLASS: space.earlygrey.shapedrawer.ShapeDrawer
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g2d.TextureRegion as _TextureRegion
_TextureRegion = _TextureRegion
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

import com.badlogic.gdx.graphics.g2d.Batch as _Batch
_Batch = _Batch
from pyquantum_helper import override
import space.earlygrey.shapedrawer.AbstractShapeDrawer as _AbstractShapeDrawer
_AbstractShapeDrawer = _AbstractShapeDrawer
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import space.earlygrey.shapedrawer.Drawing as _Drawing
_Drawing = _Drawing
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import space.earlygrey.shapedrawer.ShapeDrawer as _ShapeDrawer
_ShapeDrawer = _ShapeDrawer
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import space.earlygrey.shapedrawer.SideEstimator as _SideEstimator
_SideEstimator = _SideEstimator
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ShapeDrawer():
    """space.earlygrey.shapedrawer.ShapeDrawer"""
 
    @staticmethod
    def _wrap(java_value: _ShapeDrawer) -> 'ShapeDrawer':
        return ShapeDrawer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShapeDrawer):
        """
        Dynamic initializer for ShapeDrawer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShapeDrawer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShapeDrawer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def rectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(float,float,float,float,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).rectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4)

    @overload
    def triangle(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: float, arg4: 'JoinType', arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,float,space.earlygrey.shapedrawer.JoinType,float)"""
        super(_ShapeDrawer, self).triangle(arg0, arg1, arg2, _float.valueOf(arg3), arg4, _float.valueOf(arg5))

    @overload
    def filledRectangle(self, arg0: 'Rectangle', arg1: 'Color', arg2: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledRectangle(arg0, arg1, arg2)

    @overload
    def triangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: 'JoinType', arg8: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(float,float,float,float,float,float,float,space.earlygrey.shapedrawer.JoinType,float)"""
        super(_ShapeDrawer, self).triangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), arg7, _float.valueOf(arg8))

    @overload
    def __init__(self, arg0: 'Batch', arg1: 'TextureRegion'):
        """public space.earlygrey.shapedrawer.ShapeDrawer(com.badlogic.gdx.graphics.g2d.Batch,com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = _ShapeDrawer(arg0, arg1)
        self.__wrapper = val

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).line(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4)

    @overload
    def path(self, arg0: 'FloatArray', arg1: float, arg2: 'JoinType', arg3: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(com.badlogic.gdx.utils.FloatArray,float,space.earlygrey.shapedrawer.JoinType,boolean)"""
        super(_ShapeDrawer, self).path(arg0, _float.valueOf(arg1), arg2, _boolean.valueOf(arg3))

    @overload
    def circle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.circle(float,float,float,float,space.earlygrey.shapedrawer.JoinType)"""
        super(_ShapeDrawer, self).circle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def polygon(self, arg0: 'float'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float[])"""
        super(_ShapeDrawer, self).polygon(arg0)

    @overload
    def setTextureRegion(self, arg0: 'TextureRegion') -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion space.earlygrey.shapedrawer.AbstractShapeDrawer.setTextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return 'g2d.TextureRegion'._wrap(super(_AbstractShapeDrawer, self).setTextureRegion(arg0))

    @overload
    def path(self, arg0: 'Array', arg1: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.Vector2>,float)"""
        super(_ShapeDrawer, self).path(arg0, _float.valueOf(arg1))

    @overload
    def filledRectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'Color', arg6: 'Color', arg7: 'Color', arg8: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledRectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), arg5, arg6, arg7, arg8)

    @overload
    def polygon(self, arg0: 'float', arg1: int, arg2: int, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float[],int,int,float)"""
        super(_ShapeDrawer, self).polygon(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def setDefaultLineWidth(self, arg0: float) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.setDefaultLineWidth(float)"""
        return float._wrap(super(_AbstractShapeDrawer, self).setDefaultLineWidth(_float.valueOf(arg0)))

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float,com.badlogic.gdx.graphics.Color,float)"""
        super(_ShapeDrawer, self).line(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4, _float.valueOf(arg5))

    @overload
    def sector(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.sector(float,float,float,float,float)"""
        super(_ShapeDrawer, self).sector(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def getBatch(self) -> 'g2d.Batch':
        """public com.badlogic.gdx.graphics.g2d.Batch space.earlygrey.shapedrawer.AbstractShapeDrawer.getBatch()"""
        return 'g2d.Batch'._wrap(super(AbstractShapeDrawer, self).getBatch())

    @overload
    def rectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(float,float,float,float,float,float,space.earlygrey.shapedrawer.JoinType)"""
        super(_ShapeDrawer, self).rectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6)

    @overload
    def filledRectangle(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(float,float,float,float)"""
        super(_ShapeDrawer, self).filledRectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def __init__(self, arg0: 'Batch', arg1: 'TextureRegion', arg2: 'SideEstimator'):
        """public space.earlygrey.shapedrawer.ShapeDrawer(com.badlogic.gdx.graphics.g2d.Batch,com.badlogic.gdx.graphics.g2d.TextureRegion,space.earlygrey.shapedrawer.SideEstimator)"""
        val = _ShapeDrawer(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def circle(self, arg0: float, arg1: float, arg2: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.circle(float,float,float)"""
        super(_ShapeDrawer, self).circle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def filledCircle(self, arg0: 'Vector2', arg1: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledCircle(com.badlogic.gdx.math.Vector2,float)"""
        super(_ShapeDrawer, self).filledCircle(arg0, _float.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def filledRectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'Color', arg6: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledRectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), arg5, arg6)

    @overload
    def polygon(self, arg0: 'Polygon', arg1: float, arg2: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(com.badlogic.gdx.math.Polygon,float,space.earlygrey.shapedrawer.JoinType)"""
        super(_ShapeDrawer, self).polygon(arg0, _float.valueOf(arg1), arg2)

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.setColor(float,float,float,float)"""
        return float._wrap(super(_AbstractShapeDrawer, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def filledRectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledRectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4, arg5)

    @overload
    def triangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(float,float,float,float,float,float,float,float)"""
        super(_ShapeDrawer, self).triangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7))

    @overload
    def arc(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: bool, arg7: int):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.arc(float,float,float,float,float,float,boolean,int)"""
        super(_ShapeDrawer, self).arc(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _boolean.valueOf(arg6), _int.valueOf(arg7))

    @overload
    def triangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(float,float,float,float,float,float,float)"""
        super(_ShapeDrawer, self).triangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6))

    @overload
    def line(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).line(arg0, arg1, arg2)

    @overload
    def rectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(float,float,float,float,float,float)"""
        super(_ShapeDrawer, self).rectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))

    @overload
    def rectangle(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(float,float,float,float)"""
        super(_ShapeDrawer, self).rectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def filledEllipse(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledEllipse(float,float,float,float)"""
        super(_ShapeDrawer, self).filledEllipse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def filledRectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(float,float,float,float,float)"""
        super(_ShapeDrawer, self).filledRectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def updatePixelSize(self) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.updatePixelSize()"""
        return float._wrap(super(AbstractShapeDrawer, self).updatePixelSize())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def sector(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.sector(float,float,float,float,float,int)"""
        super(_ShapeDrawer, self).sector(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5))

    @overload
    def line(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Color', arg3: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).line(arg0, arg1, arg2, arg3)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def filledRectangle(self, arg0: 'Rectangle', arg1: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledRectangle(arg0, arg1)

    @override
    @overload
    def getSideEstimator(self) -> 'SideEstimator':
        """public final space.earlygrey.shapedrawer.SideEstimator space.earlygrey.shapedrawer.AbstractShapeDrawer.getSideEstimator()"""
        return 'SideEstimator'._wrap(super(AbstractShapeDrawer, self).getSideEstimator())

    @overload
    def filledPolygon(self, arg0: 'Polygon', arg1: 'ShortArray'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(com.badlogic.gdx.math.Polygon,com.badlogic.gdx.utils.ShortArray)"""
        super(_ShapeDrawer, self).filledPolygon(arg0, arg1)

    @overload
    def circle(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.circle(float,float,float,float)"""
        super(_ShapeDrawer, self).circle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def filledEllipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledEllipse(float,float,float,float,float)"""
        super(_ShapeDrawer, self).filledEllipse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def filledPolygon(self, arg0: 'float', arg1: 'ShortArray'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float[],com.badlogic.gdx.utils.ShortArray)"""
        super(_ShapeDrawer, self).filledPolygon(arg0, arg1)

    @overload
    def triangles(self, arg0: 'float', arg1: 'short', arg2: float, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangles(float[],short[],float,float)"""
        super(_ShapeDrawer, self).triangles(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def rectangle(self, arg0: 'Rectangle', arg1: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(com.badlogic.gdx.math.Rectangle,float)"""
        super(_ShapeDrawer, self).rectangle(arg0, _float.valueOf(arg1))

    @overload
    def filledPolygon(self, arg0: 'Polygon', arg1: 'short'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(com.badlogic.gdx.math.Polygon,short[])"""
        super(_ShapeDrawer, self).filledPolygon(arg0, arg1)

    @overload
    def polygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float,float,int,float,float,float,float)"""
        super(_ShapeDrawer, self).polygon(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6))

    @overload
    def path(self, arg0: 'float', arg1: int, arg2: int, arg3: float, arg4: 'JoinType', arg5: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(float[],int,int,float,space.earlygrey.shapedrawer.JoinType,boolean)"""
        super(_ShapeDrawer, self).path(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), arg4, _boolean.valueOf(arg5))

    @overload
    def filledRectangle(self, arg0: 'Rectangle', arg1: float, arg2: 'Color', arg3: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(com.badlogic.gdx.math.Rectangle,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledRectangle(arg0, _float.valueOf(arg1), arg2, arg3)

    @overload
    def filledCircle(self, arg0: float, arg1: float, arg2: float, arg3: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledCircle(float,float,float,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledCircle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), arg3)

    @overload
    def filledRectangle(self, arg0: 'Rectangle'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(com.badlogic.gdx.math.Rectangle)"""
        super(_ShapeDrawer, self).filledRectangle(arg0)

    @overload
    def filledCircle(self, arg0: 'Vector2', arg1: float, arg2: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledCircle(com.badlogic.gdx.math.Vector2,float,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledCircle(arg0, _float.valueOf(arg1), arg2)

    @overload
    def filledPolygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float,float,int,float,float)"""
        super(_ShapeDrawer, self).filledPolygon(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def polygon(self, arg0: 'Polygon', arg1: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(com.badlogic.gdx.math.Polygon,float)"""
        super(_ShapeDrawer, self).polygon(arg0, _float.valueOf(arg1))

    @overload
    def setColor(self, arg0: float) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.setColor(float)"""
        return float._wrap(super(_AbstractShapeDrawer, self).setColor(_float.valueOf(arg0)))

    @overload
    def polygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float,float,int,float,float,float,space.earlygrey.shapedrawer.JoinType)"""
        super(_ShapeDrawer, self).polygon(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6)

    @overload
    def rectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(float,float,float,float,float,space.earlygrey.shapedrawer.JoinType)"""
        super(_ShapeDrawer, self).rectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), arg5)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def arc(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.arc(float,float,float,float,float,float)"""
        super(_ShapeDrawer, self).arc(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))

    @override
    @overload
    def getPixelSize(self) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.getPixelSize()"""
        return float._wrap(super(AbstractShapeDrawer, self).getPixelSize())

    @overload
    def setDefaultSnap(self, arg0: bool) -> bool:
        """public boolean space.earlygrey.shapedrawer.AbstractShapeDrawer.setDefaultSnap(boolean)"""
        return bool._wrap(super(_AbstractShapeDrawer, self).setDefaultSnap(_boolean.valueOf(arg0)))

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: bool, arg6: 'Color', arg7: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float,float,boolean,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).line(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _boolean.valueOf(arg5), arg6, arg7)

    @overload
    def triangle(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,float)"""
        super(_ShapeDrawer, self).triangle(arg0, arg1, arg2, _float.valueOf(arg3))

    @overload
    def rectangle(self, arg0: 'Rectangle', arg1: 'Color', arg2: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.graphics.Color,float)"""
        super(_ShapeDrawer, self).rectangle(arg0, arg1, _float.valueOf(arg2))

    @overload
    def rectangle(self, arg0: 'Rectangle', arg1: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).rectangle(arg0, arg1)

    @overload
    def filledRectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: 'Color', arg6: 'Color', arg7: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledRectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4, arg5, arg6, arg7)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def update(self):
        """public void space.earlygrey.shapedrawer.AbstractShapeDrawer.update()"""
        super(AbstractShapeDrawer, self).update()

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).line(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4, arg5)

    @overload
    def path(self, arg0: 'float', arg1: float, arg2: 'JoinType', arg3: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(float[],float,space.earlygrey.shapedrawer.JoinType,boolean)"""
        super(_ShapeDrawer, self).path(arg0, _float.valueOf(arg1), arg2, _boolean.valueOf(arg3))

    @overload
    def circle(self, arg0: float, arg1: float, arg2: float, arg3: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.circle(float,float,float,space.earlygrey.shapedrawer.JoinType)"""
        super(_ShapeDrawer, self).circle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), arg3)

    @overload
    def filledPolygon(self, arg0: 'Polygon'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(com.badlogic.gdx.math.Polygon)"""
        super(_ShapeDrawer, self).filledPolygon(arg0)

    @overload
    def filledPolygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float,float,int,float,float,float)"""
        super(_ShapeDrawer, self).filledPolygon(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float,float)"""
        super(_ShapeDrawer, self).line(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def arc(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.arc(float,float,float,float,float)"""
        super(_ShapeDrawer, self).arc(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def filledTriangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'Color', arg7: 'Color', arg8: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledTriangle(float,float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledTriangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6, arg7, arg8)

    @overload
    def path(self, arg0: 'Array', arg1: float, arg2: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.Vector2>,float,boolean)"""
        super(_ShapeDrawer, self).path(arg0, _float.valueOf(arg1), _boolean.valueOf(arg2))

    @overload
    def filledTriangle(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Color', arg4: 'Color', arg5: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledTriangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledTriangle(arg0, arg1, arg2, arg3, arg4, arg5)

    @overload
    def sector(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: float, arg7: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.sector(float,float,float,float,float,int,float,float)"""
        super(_ShapeDrawer, self).sector(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7))

    @overload
    def filledTriangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledTriangle(float,float,float,float,float,float)"""
        super(_ShapeDrawer, self).filledTriangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def filledPolygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float,float,int,float,float,float,float,float)"""
        super(_ShapeDrawer, self).filledPolygon(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7))

    @overload
    def filledRectangle(self, arg0: 'Rectangle', arg1: float, arg2: 'Color', arg3: 'Color', arg4: 'Color', arg5: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(com.badlogic.gdx.math.Rectangle,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledRectangle(arg0, _float.valueOf(arg1), arg2, arg3, arg4, arg5)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def filledEllipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'Color', arg6: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledEllipse(float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledEllipse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), arg5, arg6)

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: bool, arg6: float, arg7: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float,float,boolean,float,float)"""
        super(_ShapeDrawer, self).line(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _boolean.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7))

    @overload
    def filledPolygon(self, arg0: float, arg1: float, arg2: int, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float,float,int,float)"""
        super(_ShapeDrawer, self).filledPolygon(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def setColor(self, arg0: 'Color') -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.setColor(com.badlogic.gdx.graphics.Color)"""
        return float._wrap(super(_AbstractShapeDrawer, self).setColor(arg0))

    @overload
    def filledRectangle(self, arg0: 'Rectangle', arg1: 'Color', arg2: 'Color', arg3: 'Color', arg4: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(com.badlogic.gdx.math.Rectangle,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledRectangle(arg0, arg1, arg2, arg3, arg4)

    @overload
    def filledPolygon(self, arg0: 'float', arg1: int, arg2: int):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float[],int,int)"""
        super(_ShapeDrawer, self).filledPolygon(arg0, _int.valueOf(arg1), _int.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def polygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float,float,int,float,float,float)"""
        super(_ShapeDrawer, self).polygon(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))

    @overload
    def rectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(float,float,float,float,float)"""
        super(_ShapeDrawer, self).rectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def polygon(self, arg0: 'Polygon'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(com.badlogic.gdx.math.Polygon)"""
        super(_ShapeDrawer, self).polygon(arg0)

    @overload
    def path(self, arg0: 'Array', arg1: float, arg2: 'JoinType', arg3: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.Vector2>,float,space.earlygrey.shapedrawer.JoinType,boolean)"""
        super(_ShapeDrawer, self).path(arg0, _float.valueOf(arg1), arg2, _boolean.valueOf(arg3))

    @overload
    def arc(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.arc(float,float,float,float,float,float,boolean)"""
        super(_ShapeDrawer, self).arc(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _boolean.valueOf(arg6))

    @overload
    def filledRectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(float,float,float,float,float,float,float,float,float)"""
        super(_ShapeDrawer, self).filledRectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8))

    @overload
    def filledPolygon(self, arg0: 'float'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float[])"""
        super(_ShapeDrawer, self).filledPolygon(arg0)

    @override
    @overload
    def getPackedColor(self) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.getPackedColor()"""
        return float._wrap(super(AbstractShapeDrawer, self).getPackedColor())

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float)"""
        super(_ShapeDrawer, self).line(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def triangle(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(_ShapeDrawer, self).triangle(arg0, arg1, arg2)

    @overload
    def filledCircle(self, arg0: float, arg1: float, arg2: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledCircle(float,float,float)"""
        super(_ShapeDrawer, self).filledCircle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def filledPolygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: 'Color', arg7: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float,float,int,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledPolygon(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6, arg7)

    @override
    @overload
    def startRecording(self):
        """public void space.earlygrey.shapedrawer.AbstractShapeDrawer.startRecording()"""
        super(AbstractShapeDrawer, self).startRecording()

    @overload
    def path(self, arg0: 'Array', arg1: 'JoinType', arg2: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.Vector2>,space.earlygrey.shapedrawer.JoinType,boolean)"""
        super(_ShapeDrawer, self).path(arg0, arg1, _boolean.valueOf(arg2))

    @override
    @overload
    def update(self, arg0: bool):
        """public void space.earlygrey.shapedrawer.AbstractShapeDrawer.update(boolean)"""
        super(_AbstractShapeDrawer, self).update(_boolean.valueOf(arg0))

    @overload
    def filledEllipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledEllipse(float,float,float,float,float,float,float)"""
        super(_ShapeDrawer, self).filledEllipse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6))

    @overload
    def rectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color', arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(float,float,float,float,com.badlogic.gdx.graphics.Color,float)"""
        super(_ShapeDrawer, self).rectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4, _float.valueOf(arg5))

    @override
    @overload
    def getDefaultLineWidth(self) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.getDefaultLineWidth()"""
        return float._wrap(super(AbstractShapeDrawer, self).getDefaultLineWidth())

    @overload
    def path(self, arg0: 'Array', arg1: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.Vector2>,space.earlygrey.shapedrawer.JoinType)"""
        super(_ShapeDrawer, self).path(arg0, arg1)

    @overload
    def polygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float,float,int,float,float)"""
        super(_ShapeDrawer, self).polygon(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @override
    @overload
    def isDefaultSnap(self) -> bool:
        """public boolean space.earlygrey.shapedrawer.AbstractShapeDrawer.isDefaultSnap()"""
        return bool._wrap(super(AbstractShapeDrawer, self).isDefaultSnap())

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float,float,boolean)"""
        super(_ShapeDrawer, self).line(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _boolean.valueOf(arg5))

    @overload
    def line(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'Color', arg6: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).line(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), arg5, arg6)

    @overload
    def polygon(self, arg0: 'float', arg1: int, arg2: int, arg3: float, arg4: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float[],int,int,float,space.earlygrey.shapedrawer.JoinType)"""
        super(_ShapeDrawer, self).polygon(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), arg4)

    @overload
    def polygon(self, arg0: 'float', arg1: float, arg2: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float[],float,space.earlygrey.shapedrawer.JoinType)"""
        super(_ShapeDrawer, self).polygon(arg0, _float.valueOf(arg1), arg2)

    @overload
    def filledTriangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledTriangle(float,float,float,float,float,float,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledTriangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6)

    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.ellipse(float,float,float,float,float,float,space.earlygrey.shapedrawer.JoinType)"""
        super(_ShapeDrawer, self).ellipse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6)

    @overload
    def triangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(float,float,float,float,float,float)"""
        super(_ShapeDrawer, self).triangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))

    @overload
    def __init__(self, arg0: 'Batch'):
        """public space.earlygrey.shapedrawer.ShapeDrawer(com.badlogic.gdx.graphics.g2d.Batch)"""
        val = _ShapeDrawer(arg0)
        self.__wrapper = val

    @overload
    def filledPolygon(self, arg0: 'float', arg1: 'short', arg2: float, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float[],short[],float,float)"""
        super(_ShapeDrawer, self).filledPolygon(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def line(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Color', arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.graphics.Color,float)"""
        super(_ShapeDrawer, self).line(arg0, arg1, arg2, _float.valueOf(arg3))

    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.ellipse(float,float,float,float)"""
        super(_ShapeDrawer, self).ellipse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def triangle(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,float,float)"""
        super(_ShapeDrawer, self).triangle(arg0, arg1, arg2, _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def path(self, arg0: 'float', arg1: int, arg2: int, arg3: float, arg4: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(float[],int,int,float,boolean)"""
        super(_ShapeDrawer, self).path(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _boolean.valueOf(arg4))

    @overload
    def filledRectangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledRectangle(float,float,float,float,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledRectangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4)

    @overload
    def line(self, arg0: 'Vector2', arg1: 'Vector2', arg2: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,float)"""
        super(_ShapeDrawer, self).line(arg0, arg1, _float.valueOf(arg2))

    @overload
    def sector(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'Color', arg6: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.sector(float,float,float,float,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).sector(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), arg5, arg6)

    @overload
    def setSideEstimator(self, arg0: 'SideEstimator') -> 'SideEstimator':
        """public space.earlygrey.shapedrawer.SideEstimator space.earlygrey.shapedrawer.AbstractShapeDrawer.setSideEstimator(space.earlygrey.shapedrawer.SideEstimator)"""
        return 'SideEstimator'._wrap(super(_AbstractShapeDrawer, self).setSideEstimator(arg0))

    @overload
    def rectangle(self, arg0: 'Rectangle'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.rectangle(com.badlogic.gdx.math.Rectangle)"""
        super(_ShapeDrawer, self).rectangle(arg0)

    @overload
    def polygon(self, arg0: 'Polygon', arg1: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(com.badlogic.gdx.math.Polygon,space.earlygrey.shapedrawer.JoinType)"""
        super(_ShapeDrawer, self).polygon(arg0, arg1)

    @overload
    def line(self, arg0: 'Vector2', arg1: 'Vector2'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.line(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(_ShapeDrawer, self).line(arg0, arg1)

    @overload
    def triangle(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).triangle(arg0, arg1, arg2, arg3)

    @overload
    def filledPolygon(self, arg0: 'float', arg1: 'short'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledPolygon(float[],short[])"""
        super(_ShapeDrawer, self).filledPolygon(arg0, arg1)

    @override
    @overload
    def getRegion(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion space.earlygrey.shapedrawer.AbstractShapeDrawer.getRegion()"""
        return 'g2d.TextureRegion'._wrap(super(AbstractShapeDrawer, self).getRegion())

    @overload
    def polygon(self, arg0: float, arg1: float, arg2: int, arg3: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float,float,int,float)"""
        super(_ShapeDrawer, self).polygon(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def path(self, arg0: 'Array', arg1: bool):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.Vector2>,boolean)"""
        super(_ShapeDrawer, self).path(arg0, _boolean.valueOf(arg1))

    @overload
    def filledTriangle(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledTriangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        super(_ShapeDrawer, self).filledTriangle(arg0, arg1, arg2)

    @overload
    def setPixelSize(self, arg0: float) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.setPixelSize(float)"""
        return float._wrap(super(_AbstractShapeDrawer, self).setPixelSize(_float.valueOf(arg0)))

    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.ellipse(float,float,float,float,float,float)"""
        super(_ShapeDrawer, self).ellipse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5))

    @overload
    def path(self, arg0: 'Array'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.path(com.badlogic.gdx.utils.Array<com.badlogic.gdx.math.Vector2>)"""
        super(_ShapeDrawer, self).path(arg0)

    @overload
    def polygon(self, arg0: float, arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: 'JoinType'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.polygon(float,float,int,float,float,float,float,space.earlygrey.shapedrawer.JoinType)"""
        super(_ShapeDrawer, self).polygon(_float.valueOf(arg0), _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), arg7)

    @overload
    def filledTriangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledTriangle(float,float,float,float,float,float,float,float,float)"""
        super(_ShapeDrawer, self).filledTriangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8))

    @overload
    def triangle(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.triangle(float,float,float,float,float,float,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).triangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), arg6)

    @overload
    def filledTriangle(self, arg0: 'Vector2', arg1: 'Vector2', arg2: 'Vector2', arg3: 'Color'):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.filledTriangle(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2,com.badlogic.gdx.graphics.Color)"""
        super(_ShapeDrawer, self).filledTriangle(arg0, arg1, arg2, arg3)

    @override
    @overload
    def stopRecording(self) -> 'Drawing':
        """public space.earlygrey.shapedrawer.Drawing space.earlygrey.shapedrawer.AbstractShapeDrawer.stopRecording()"""
        return 'Drawing'._wrap(super(AbstractShapeDrawer, self).stopRecording())

    @overload
    def ellipse(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.ShapeDrawer.ellipse(float,float,float,float,float)"""
        super(_ShapeDrawer, self).ellipse(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

 
 
 
# CLASS: space.earlygrey.shapedrawer.ShapeDrawer 
 
 
# CLASS: space.earlygrey.shapedrawer.JoinType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import space.earlygrey.shapedrawer.JoinType as _JoinType
_JoinType = _JoinType
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
 
class JoinType():
    """space.earlygrey.shapedrawer.JoinType"""
 
    @staticmethod
    def _wrap(java_value: _JoinType) -> 'JoinType':
        return JoinType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _JoinType):
        """
        Dynamic initializer for JoinType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_JoinType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_JoinType__wrapper":
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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'JoinType':
        """public static space.earlygrey.shapedrawer.JoinType space.earlygrey.shapedrawer.JoinType.valueOf(java.lang.String)"""
        return JoinType._wrap(_JoinType.valueOf(arg0))

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
    def values() -> List['JoinType']:
        """public static space.earlygrey.shapedrawer.JoinType[] space.earlygrey.shapedrawer.JoinType.values()"""
        return List[JoinType]._wrap(_JoinType.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: space.earlygrey.shapedrawer.Drawing
from builtins import str
from pyquantum_helper import override
import space.earlygrey.shapedrawer.Drawing as _Drawing
_Drawing = _Drawing
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Drawing():
    """space.earlygrey.shapedrawer.Drawing"""
 
    @staticmethod
    def _wrap(java_value: _Drawing) -> 'Drawing':
        return Drawing(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Drawing):
        """
        Dynamic initializer for Drawing.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Drawing__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Drawing__wrapper":
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
    def draw(self):
        """public void space.earlygrey.shapedrawer.Drawing.draw()"""
        super(Drawing, self).draw()

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
 
 
# CLASS: space.earlygrey.shapedrawer.ShapeUtils
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import space.earlygrey.shapedrawer.ShapeUtils as _ShapeUtils
_ShapeUtils = _ShapeUtils
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ShapeUtils():
    """space.earlygrey.shapedrawer.ShapeUtils"""
 
    @staticmethod
    def _wrap(java_value: _ShapeUtils) -> 'ShapeUtils':
        return ShapeUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShapeUtils):
        """
        Dynamic initializer for ShapeUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShapeUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShapeUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public space.earlygrey.shapedrawer.ShapeUtils()"""
        val = _ShapeUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def angleRad(arg0: 'Vector2', arg1: 'Vector2') -> float:
        """public static float space.earlygrey.shapedrawer.ShapeUtils.angleRad(com.badlogic.gdx.math.Vector2,com.badlogic.gdx.math.Vector2)"""
        return float._wrap(_ShapeUtils.angleRad(arg0, arg1))

    @staticmethod
    @overload
    def floor(arg0: float, arg1: float) -> float:
        """public static float space.earlygrey.shapedrawer.ShapeUtils.floor(float,float)"""
        return float._wrap(_ShapeUtils.floor(_float.valueOf(arg0), _float.valueOf(arg1)))

    @staticmethod
    @overload
    def snap(arg0: float, arg1: float, arg2: float) -> float:
        """public static float space.earlygrey.shapedrawer.ShapeUtils.snap(float,float,float)"""
        return float._wrap(_ShapeUtils.snap(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def epsilonEquals(arg0: float, arg1: float) -> bool:
        """public static boolean space.earlygrey.shapedrawer.ShapeUtils.epsilonEquals(float,float)"""
        return bool._wrap(_ShapeUtils.epsilonEquals(_float.valueOf(arg0), _float.valueOf(arg1)))

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

    @overload
    def __init__(self, ):
        """public space.earlygrey.shapedrawer.ShapeUtils()"""
        val = _ShapeUtils()
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
    def ceil(arg0: float, arg1: float) -> float:
        """public static float space.earlygrey.shapedrawer.ShapeUtils.ceil(float,float)"""
        return float._wrap(_ShapeUtils.ceil(_float.valueOf(arg0), _float.valueOf(arg1)))

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
    def normaliseAngleToPositive(arg0: float) -> float:
        """public static float space.earlygrey.shapedrawer.ShapeUtils.normaliseAngleToPositive(float)"""
        return float._wrap(_ShapeUtils.normaliseAngleToPositive(_float.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: space.earlygrey.shapedrawer.GraphDrawer
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import space.earlygrey.shapedrawer.JoinType as _JoinType
_JoinType = _JoinType
from builtins import float
import space.earlygrey.shapedrawer.ShapeDrawer as _ShapeDrawer
_ShapeDrawer = _ShapeDrawer
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import space.earlygrey.shapedrawer.GraphDrawer as _GraphDrawer
_GraphDrawer = _GraphDrawer
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GraphDrawer():
    """space.earlygrey.shapedrawer.GraphDrawer"""
 
    @staticmethod
    def _wrap(java_value: _GraphDrawer) -> 'GraphDrawer':
        return GraphDrawer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GraphDrawer):
        """
        Dynamic initializer for GraphDrawer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GraphDrawer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GraphDrawer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def draw(self, arg0: 'Interpolation', arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'JoinType', arg6: int, arg7: float, arg8: float, arg9: float, arg10: float, arg11: bool):
        """public void space.earlygrey.shapedrawer.GraphDrawer.draw(com.badlogic.gdx.math.Interpolation,float,float,float,float,space.earlygrey.shapedrawer.JoinType,int,float,float,float,float,boolean)"""
        super(_GraphDrawer, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), arg5, _int.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10), _boolean.valueOf(arg11))

    @overload
    def getDomainEnd(self) -> float:
        """public float space.earlygrey.shapedrawer.GraphDrawer.getDomainEnd()"""
        return float._wrap(super(GraphDrawer, self).getDomainEnd())

    @overload
    def getPlotBegin(self) -> float:
        """public float space.earlygrey.shapedrawer.GraphDrawer.getPlotBegin()"""
        return float._wrap(super(GraphDrawer, self).getPlotBegin())

    @overload
    def setShapeDrawer(self, arg0: 'ShapeDrawer'):
        """public void space.earlygrey.shapedrawer.GraphDrawer.setShapeDrawer(space.earlygrey.shapedrawer.ShapeDrawer)"""
        super(_GraphDrawer, self).setShapeDrawer(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setJoinType(self, arg0: 'JoinType'):
        """public void space.earlygrey.shapedrawer.GraphDrawer.setJoinType(space.earlygrey.shapedrawer.JoinType)"""
        super(_GraphDrawer, self).setJoinType(arg0)

    @overload
    def setDomainBegin(self, arg0: float):
        """public void space.earlygrey.shapedrawer.GraphDrawer.setDomainBegin(float)"""
        super(_GraphDrawer, self).setDomainBegin(_float.valueOf(arg0))

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
    def getSamples(self) -> int:
        """public int space.earlygrey.shapedrawer.GraphDrawer.getSamples()"""
        return int._wrap(super(GraphDrawer, self).getSamples())

    @overload
    def draw(self, arg0: 'Interpolation', arg1: float, arg2: float, arg3: float, arg4: float, arg5: 'JoinType'):
        """public void space.earlygrey.shapedrawer.GraphDrawer.draw(com.badlogic.gdx.math.Interpolation,float,float,float,float,space.earlygrey.shapedrawer.JoinType)"""
        super(_GraphDrawer, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), arg5)

    @overload
    def draw(self, arg0: 'Interpolation', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void space.earlygrey.shapedrawer.GraphDrawer.draw(com.badlogic.gdx.math.Interpolation,float,float,float,float)"""
        super(_GraphDrawer, self).draw(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getShapeDrawer(self) -> 'ShapeDrawer':
        """public space.earlygrey.shapedrawer.ShapeDrawer space.earlygrey.shapedrawer.GraphDrawer.getShapeDrawer()"""
        return 'ShapeDrawer'._wrap(super(GraphDrawer, self).getShapeDrawer())

    @overload
    def getJoinType(self) -> 'JoinType':
        """public space.earlygrey.shapedrawer.JoinType space.earlygrey.shapedrawer.GraphDrawer.getJoinType()"""
        return 'JoinType'._wrap(super(GraphDrawer, self).getJoinType())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getPlotEnd(self) -> float:
        """public float space.earlygrey.shapedrawer.GraphDrawer.getPlotEnd()"""
        return float._wrap(super(GraphDrawer, self).getPlotEnd())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setPlotBegin(self, arg0: float):
        """public void space.earlygrey.shapedrawer.GraphDrawer.setPlotBegin(float)"""
        super(_GraphDrawer, self).setPlotBegin(_float.valueOf(arg0))

    @overload
    def draw(self, arg0: 'Interpolation', arg1: 'Rectangle'):
        """public void space.earlygrey.shapedrawer.GraphDrawer.draw(com.badlogic.gdx.math.Interpolation,com.badlogic.gdx.math.Rectangle)"""
        super(_GraphDrawer, self).draw(arg0, arg1)

    @overload
    def setRescale(self, arg0: bool):
        """public void space.earlygrey.shapedrawer.GraphDrawer.setRescale(boolean)"""
        super(_GraphDrawer, self).setRescale(_boolean.valueOf(arg0))

    @overload
    def getDomainBegin(self) -> float:
        """public float space.earlygrey.shapedrawer.GraphDrawer.getDomainBegin()"""
        return float._wrap(super(GraphDrawer, self).getDomainBegin())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def draw(self, arg0: 'Interpolation', arg1: 'Rectangle', arg2: 'JoinType'):
        """public void space.earlygrey.shapedrawer.GraphDrawer.draw(com.badlogic.gdx.math.Interpolation,com.badlogic.gdx.math.Rectangle,space.earlygrey.shapedrawer.JoinType)"""
        super(_GraphDrawer, self).draw(arg0, arg1, arg2)

    @overload
    def __init__(self, arg0: 'ShapeDrawer'):
        """public space.earlygrey.shapedrawer.GraphDrawer(space.earlygrey.shapedrawer.ShapeDrawer)"""
        val = _GraphDrawer(arg0)
        self.__wrapper = val

    @overload
    def setDomainEnd(self, arg0: float):
        """public void space.earlygrey.shapedrawer.GraphDrawer.setDomainEnd(float)"""
        super(_GraphDrawer, self).setDomainEnd(_float.valueOf(arg0))

    @overload
    def setPlotEnd(self, arg0: float):
        """public void space.earlygrey.shapedrawer.GraphDrawer.setPlotEnd(float)"""
        super(_GraphDrawer, self).setPlotEnd(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setSamples(self, arg0: int):
        """public void space.earlygrey.shapedrawer.GraphDrawer.setSamples(int)"""
        super(_GraphDrawer, self).setSamples(_int.valueOf(arg0))

    @overload
    def isRescale(self) -> bool:
        """public boolean space.earlygrey.shapedrawer.GraphDrawer.isRescale()"""
        return bool._wrap(super(GraphDrawer, self).isRescale())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: space.earlygrey.shapedrawer.SideEstimator
import space.earlygrey.shapedrawer.SideEstimator as _SideEstimator
_SideEstimator = _SideEstimator
from abc import abstractmethod, ABC
 
class SideEstimator():
    """space.earlygrey.shapedrawer.SideEstimator"""
 
    @staticmethod
    def _wrap(java_value: _SideEstimator) -> 'SideEstimator':
        return SideEstimator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SideEstimator):
        """
        Dynamic initializer for SideEstimator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SideEstimator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SideEstimator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def estimateSidesRequired(self, arg0: float, arg1: float, arg2: float):
        """public abstract int space.earlygrey.shapedrawer.SideEstimator.estimateSidesRequired(float,float,float)"""
        pass 
 
 
# CLASS: space.earlygrey.shapedrawer.DefaultSideEstimator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import space.earlygrey.shapedrawer.DefaultSideEstimator as _DefaultSideEstimator
_DefaultSideEstimator = _DefaultSideEstimator
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DefaultSideEstimator():
    """space.earlygrey.shapedrawer.DefaultSideEstimator"""
 
    @staticmethod
    def _wrap(java_value: _DefaultSideEstimator) -> 'DefaultSideEstimator':
        return DefaultSideEstimator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DefaultSideEstimator):
        """
        Dynamic initializer for DefaultSideEstimator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DefaultSideEstimator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DefaultSideEstimator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setSideMultiplier(self, arg0: float):
        """public void space.earlygrey.shapedrawer.DefaultSideEstimator.setSideMultiplier(float)"""
        super(_DefaultSideEstimator, self).setSideMultiplier(_float.valueOf(arg0))

    @overload
    def __init__(self):
        """public space.earlygrey.shapedrawer.DefaultSideEstimator()"""
        val = _DefaultSideEstimator()
        self.__wrapper = val

    @overload
    def setMinimumSides(self, arg0: int):
        """public void space.earlygrey.shapedrawer.DefaultSideEstimator.setMinimumSides(int)"""
        super(_DefaultSideEstimator, self).setMinimumSides(_int.valueOf(arg0))

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

    @overload
    def getSideMultiplier(self) -> float:
        """public float space.earlygrey.shapedrawer.DefaultSideEstimator.getSideMultiplier()"""
        return float._wrap(super(DefaultSideEstimator, self).getSideMultiplier())

    @overload
    def setMaximumSides(self, arg0: int):
        """public void space.earlygrey.shapedrawer.DefaultSideEstimator.setMaximumSides(int)"""
        super(_DefaultSideEstimator, self).setMaximumSides(_int.valueOf(arg0))

    @overload
    def getMinimumSides(self) -> int:
        """public int space.earlygrey.shapedrawer.DefaultSideEstimator.getMinimumSides()"""
        return int._wrap(super(DefaultSideEstimator, self).getMinimumSides())

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
    def __init__(self, arg0: int, arg1: int, arg2: float):
        """public space.earlygrey.shapedrawer.DefaultSideEstimator(int,int,float)"""
        val = _DefaultSideEstimator(_int.valueOf(arg0), _int.valueOf(arg1), _float.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getMaximumSides(self) -> int:
        """public int space.earlygrey.shapedrawer.DefaultSideEstimator.getMaximumSides()"""
        return int._wrap(super(DefaultSideEstimator, self).getMaximumSides())

    @overload
    def __init__(self, ):
        """public space.earlygrey.shapedrawer.DefaultSideEstimator()"""
        val = _DefaultSideEstimator()
        self.__wrapper = val

    @overload
    def estimateSidesRequired(self, arg0: float, arg1: float, arg2: float) -> int:
        """public int space.earlygrey.shapedrawer.DefaultSideEstimator.estimateSidesRequired(float,float,float)"""
        return int._wrap(super(_DefaultSideEstimator, self).estimateSidesRequired(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: space.earlygrey.shapedrawer.AbstractShapeDrawer
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g2d.TextureRegion as _TextureRegion
_TextureRegion = _TextureRegion
from builtins import str
import com.badlogic.gdx.graphics.g2d.Batch as _Batch
_Batch = _Batch
import space.earlygrey.shapedrawer.AbstractShapeDrawer as _AbstractShapeDrawer
_AbstractShapeDrawer = _AbstractShapeDrawer
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import space.earlygrey.shapedrawer.Drawing as _Drawing
_Drawing = _Drawing
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import space.earlygrey.shapedrawer.SideEstimator as _SideEstimator
_SideEstimator = _SideEstimator
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractShapeDrawer():
    """space.earlygrey.shapedrawer.AbstractShapeDrawer"""
 
    @staticmethod
    def _wrap(java_value: _AbstractShapeDrawer) -> 'AbstractShapeDrawer':
        return AbstractShapeDrawer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractShapeDrawer):
        """
        Dynamic initializer for AbstractShapeDrawer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractShapeDrawer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractShapeDrawer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getPackedColor(self) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.getPackedColor()"""
        return float._wrap(super(AbstractShapeDrawer, self).getPackedColor())

    @overload
    def getRegion(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion space.earlygrey.shapedrawer.AbstractShapeDrawer.getRegion()"""
        return 'g2d.TextureRegion'._wrap(super(AbstractShapeDrawer, self).getRegion())

    @overload
    def update(self):
        """public void space.earlygrey.shapedrawer.AbstractShapeDrawer.update()"""
        super(AbstractShapeDrawer, self).update()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setTextureRegion(self, arg0: 'TextureRegion') -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion space.earlygrey.shapedrawer.AbstractShapeDrawer.setTextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return 'g2d.TextureRegion'._wrap(super(_AbstractShapeDrawer, self).setTextureRegion(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def updatePixelSize(self) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.updatePixelSize()"""
        return float._wrap(super(AbstractShapeDrawer, self).updatePixelSize())

    @overload
    def setDefaultLineWidth(self, arg0: float) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.setDefaultLineWidth(float)"""
        return float._wrap(super(_AbstractShapeDrawer, self).setDefaultLineWidth(_float.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getSideEstimator(self) -> 'SideEstimator':
        """public final space.earlygrey.shapedrawer.SideEstimator space.earlygrey.shapedrawer.AbstractShapeDrawer.getSideEstimator()"""
        return 'SideEstimator'._wrap(super(AbstractShapeDrawer, self).getSideEstimator())

    @overload
    def stopRecording(self) -> 'Drawing':
        """public space.earlygrey.shapedrawer.Drawing space.earlygrey.shapedrawer.AbstractShapeDrawer.stopRecording()"""
        return 'Drawing'._wrap(super(AbstractShapeDrawer, self).stopRecording())

    @overload
    def getDefaultLineWidth(self) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.getDefaultLineWidth()"""
        return float._wrap(super(AbstractShapeDrawer, self).getDefaultLineWidth())

    @overload
    def setSideEstimator(self, arg0: 'SideEstimator') -> 'SideEstimator':
        """public space.earlygrey.shapedrawer.SideEstimator space.earlygrey.shapedrawer.AbstractShapeDrawer.setSideEstimator(space.earlygrey.shapedrawer.SideEstimator)"""
        return 'SideEstimator'._wrap(super(_AbstractShapeDrawer, self).setSideEstimator(arg0))

    @overload
    def setColor(self, arg0: 'Color') -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.setColor(com.badlogic.gdx.graphics.Color)"""
        return float._wrap(super(_AbstractShapeDrawer, self).setColor(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getPixelSize(self) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.getPixelSize()"""
        return float._wrap(super(AbstractShapeDrawer, self).getPixelSize())

    @overload
    def setColor(self, arg0: float) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.setColor(float)"""
        return float._wrap(super(_AbstractShapeDrawer, self).setColor(_float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setDefaultSnap(self, arg0: bool) -> bool:
        """public boolean space.earlygrey.shapedrawer.AbstractShapeDrawer.setDefaultSnap(boolean)"""
        return bool._wrap(super(_AbstractShapeDrawer, self).setDefaultSnap(_boolean.valueOf(arg0)))

    @overload
    def startRecording(self):
        """public void space.earlygrey.shapedrawer.AbstractShapeDrawer.startRecording()"""
        super(AbstractShapeDrawer, self).startRecording()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setPixelSize(self, arg0: float) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.setPixelSize(float)"""
        return float._wrap(super(_AbstractShapeDrawer, self).setPixelSize(_float.valueOf(arg0)))

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float) -> float:
        """public float space.earlygrey.shapedrawer.AbstractShapeDrawer.setColor(float,float,float,float)"""
        return float._wrap(super(_AbstractShapeDrawer, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def isDefaultSnap(self) -> bool:
        """public boolean space.earlygrey.shapedrawer.AbstractShapeDrawer.isDefaultSnap()"""
        return bool._wrap(super(AbstractShapeDrawer, self).isDefaultSnap())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def update(self, arg0: bool):
        """public void space.earlygrey.shapedrawer.AbstractShapeDrawer.update(boolean)"""
        super(_AbstractShapeDrawer, self).update(_boolean.valueOf(arg0))

    @overload
    def getBatch(self) -> 'g2d.Batch':
        """public com.badlogic.gdx.graphics.g2d.Batch space.earlygrey.shapedrawer.AbstractShapeDrawer.getBatch()"""
        return 'g2d.Batch'._wrap(super(AbstractShapeDrawer, self).getBatch())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())