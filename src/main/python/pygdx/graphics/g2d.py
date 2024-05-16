from __future__ import annotations
from overload import overload


 
from builtins import str
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_GradientColorValue
__GradientColorValue = __ParticleEmitter_GradientColorValue.GradientColorValue
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_ParticleValue
__ParticleValue = __ParticleEmitter_ParticleValue.ParticleValue
from typing import List
import java.io.BufferedReader as BufferedReader
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GradientColorValue():
    """com.badlogic.gdx.graphics.g2d.ParticleEmitter.GradientColorValue"""
 
    @staticmethod
    def __wrap(java_value: __GradientColorValue) -> 'GradientColorValue':
        return GradientColorValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GradientColorValue):
        """
        Dynamic initializer for GradientColorValue.
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
    def getColor(self, arg0: float) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue.getColor(float)"""
        return List[float].__wrap(super(__GradientColorValue, self).getColor(__float.valueOf(arg0)))

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setActive(boolean)"""
        super(__ParticleValue, self).setActive(__boolean.valueOf(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isActive()"""
        return bool.__wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getTimeline(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue.getTimeline()"""
        return List[float].__wrap(super(GradientColorValue, self).getTimeline())

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue)"""
        super(__ParticleValue, self).load(arg0)

    @overload
    def setColors(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue.setColors(float[])"""
        super(__GradientColorValue, self).setColors(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue()"""
        val = __GradientColorValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getColors(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue.getColors()"""
        return List[float].__wrap(super(GradientColorValue, self).getColors())

    @overload
    def setTimeline(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue.setTimeline(float[])"""
        super(__GradientColorValue, self).setTimeline(arg0)

    @override
    @overload
    def load(self, arg0: 'BufferedReader'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue.load(java.io.BufferedReader) throws java.io.IOException"""
        super(__GradientColorValue, self).load(arg0)

    @override
    @overload
    def isAlwaysActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isAlwaysActive()"""
        return bool.__wrap(super(ParticleValue, self).isAlwaysActive())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue()"""
        val = __GradientColorValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def save(self, arg0: 'Writer'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue.save(java.io.Writer) throws java.io.IOException"""
        super(__GradientColorValue, self).save(arg0)

    @override
    @overload
    def setAlwaysActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setAlwaysActive(boolean)"""
        super(__ParticleValue, self).setAlwaysActive(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def load(self, arg0: 'GradientColorValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue)"""
        super(__GradientColorValue, self).load(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue
from builtins import str
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_GradientColorValue
__GradientColorValue = __ParticleEmitter_GradientColorValue.GradientColorValue
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_ParticleValue
__ParticleValue = __ParticleEmitter_ParticleValue.ParticleValue
from typing import List
import java.io.BufferedReader as BufferedReader
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GradientColorValue():
    """com.badlogic.gdx.graphics.g2d.ParticleEmitter.GradientColorValue"""
 
    @staticmethod
    def __wrap(java_value: __GradientColorValue) -> 'GradientColorValue':
        return GradientColorValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GradientColorValue):
        """
        Dynamic initializer for GradientColorValue.
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
    def getColor(self, arg0: float) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue.getColor(float)"""
        return List[float].__wrap(super(__GradientColorValue, self).getColor(__float.valueOf(arg0)))

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setActive(boolean)"""
        super(__ParticleValue, self).setActive(__boolean.valueOf(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isActive()"""
        return bool.__wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getTimeline(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue.getTimeline()"""
        return List[float].__wrap(super(GradientColorValue, self).getTimeline())

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue)"""
        super(__ParticleValue, self).load(arg0)

    @overload
    def setColors(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue.setColors(float[])"""
        super(__GradientColorValue, self).setColors(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue()"""
        val = __GradientColorValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getColors(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue.getColors()"""
        return List[float].__wrap(super(GradientColorValue, self).getColors())

    @overload
    def setTimeline(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue.setTimeline(float[])"""
        super(__GradientColorValue, self).setTimeline(arg0)

    @override
    @overload
    def load(self, arg0: 'BufferedReader'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue.load(java.io.BufferedReader) throws java.io.IOException"""
        super(__GradientColorValue, self).load(arg0)

    @override
    @overload
    def isAlwaysActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isAlwaysActive()"""
        return bool.__wrap(super(ParticleValue, self).isAlwaysActive())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue()"""
        val = __GradientColorValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def save(self, arg0: 'Writer'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue.save(java.io.Writer) throws java.io.IOException"""
        super(__GradientColorValue, self).save(arg0)

    @override
    @overload
    def setAlwaysActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setAlwaysActive(boolean)"""
        super(__ParticleValue, self).setAlwaysActive(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def load(self, arg0: 'GradientColorValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue)"""
        super(__GradientColorValue, self).load(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.NinePatch
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.graphics.g2d.NinePatch as __NinePatch
__NinePatch = __NinePatch
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
 
class NinePatch():
    """com.badlogic.gdx.graphics.g2d.NinePatch"""
 
    @staticmethod
    def __wrap(java_value: __NinePatch) -> 'NinePatch':
        return NinePatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NinePatch):
        """
        Dynamic initializer for NinePatch.
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
    def __init__(self, arg0: 'TextureRegion'):
        """public com.badlogic.gdx.graphics.g2d.NinePatch(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = __NinePatch(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, *arg0: 'TextureRegion'):
        """public com.badlogic.gdx.graphics.g2d.NinePatch(com.badlogic.gdx.graphics.g2d.TextureRegion...)"""
        val = __NinePatch(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.NinePatch.getColor()"""
        return 'graphics.Color'.__wrap(super(NinePatch, self).getColor())

    @overload
    def setPadBottom(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.setPadBottom(float)"""
        super(__NinePatch, self).setPadBottom(__float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__NinePatch, self).setColor(arg0)

    @overload
    def __init__(self, arg0: 'NinePatch'):
        """public com.badlogic.gdx.graphics.g2d.NinePatch(com.badlogic.gdx.graphics.g2d.NinePatch)"""
        val = __NinePatch(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setMiddleHeight(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.setMiddleHeight(float)"""
        super(__NinePatch, self).setMiddleHeight(__float.valueOf(arg0))

    @overload
    def getPadLeft(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.NinePatch.getPadLeft()"""
        return float.__wrap(super(NinePatch, self).getPadLeft())

    @overload
    def __init__(self, arg0: 'TextureRegion', arg1: int, arg2: int, arg3: int, arg4: int):
        """public com.badlogic.gdx.graphics.g2d.NinePatch(com.badlogic.gdx.graphics.g2d.TextureRegion,int,int,int,int)"""
        val = __NinePatch(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getTopHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.NinePatch.getTopHeight()"""
        return float.__wrap(super(NinePatch, self).getTopHeight())

    @overload
    def getTotalWidth(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.NinePatch.getTotalWidth()"""
        return float.__wrap(super(NinePatch, self).getTotalWidth())

    @overload
    def setRightWidth(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.setRightWidth(float)"""
        super(__NinePatch, self).setRightWidth(__float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setPadding(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.setPadding(float,float,float,float)"""
        super(__NinePatch, self).setPadding(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def __init__(self, arg0: 'Texture', arg1: int, arg2: int, arg3: int, arg4: int):
        """public com.badlogic.gdx.graphics.g2d.NinePatch(com.badlogic.gdx.graphics.Texture,int,int,int,int)"""
        val = __NinePatch(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getPadTop(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.NinePatch.getPadTop()"""
        return float.__wrap(super(NinePatch, self).getPadTop())

    @overload
    def setLeftWidth(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.setLeftWidth(float)"""
        super(__NinePatch, self).setLeftWidth(__float.valueOf(arg0))

    @overload
    def getPadRight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.NinePatch.getPadRight()"""
        return float.__wrap(super(NinePatch, self).getPadRight())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def scale(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.scale(float,float)"""
        super(__NinePatch, self).scale(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def getLeftWidth(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.NinePatch.getLeftWidth()"""
        return float.__wrap(super(NinePatch, self).getLeftWidth())

    @overload
    def __init__(self, arg0: 'Texture'):
        """public com.badlogic.gdx.graphics.g2d.NinePatch(com.badlogic.gdx.graphics.Texture)"""
        val = __NinePatch(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getMiddleHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.NinePatch.getMiddleHeight()"""
        return float.__wrap(super(NinePatch, self).getMiddleHeight())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float)"""
        super(__NinePatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def getRightWidth(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.NinePatch.getRightWidth()"""
        return float.__wrap(super(NinePatch, self).getRightWidth())

    @overload
    def __init__(self, arg0: 'Texture', arg1: 'Color'):
        """public com.badlogic.gdx.graphics.g2d.NinePatch(com.badlogic.gdx.graphics.Texture,com.badlogic.gdx.graphics.Color)"""
        val = __NinePatch(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getMiddleWidth(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.NinePatch.getMiddleWidth()"""
        return float.__wrap(super(NinePatch, self).getMiddleWidth())

    @overload
    def getTotalHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.NinePatch.getTotalHeight()"""
        return float.__wrap(super(NinePatch, self).getTotalHeight())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setMiddleWidth(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.setMiddleWidth(float)"""
        super(__NinePatch, self).setMiddleWidth(__float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setPadRight(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.setPadRight(float)"""
        super(__NinePatch, self).setPadRight(__float.valueOf(arg0))

    @overload
    def setBottomHeight(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.setBottomHeight(float)"""
        super(__NinePatch, self).setBottomHeight(__float.valueOf(arg0))

    @overload
    def setTopHeight(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.setTopHeight(float)"""
        super(__NinePatch, self).setTopHeight(__float.valueOf(arg0))

    @overload
    def getBottomHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.NinePatch.getBottomHeight()"""
        return float.__wrap(super(NinePatch, self).getBottomHeight())

    @overload
    def setPadLeft(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.setPadLeft(float)"""
        super(__NinePatch, self).setPadLeft(__float.valueOf(arg0))

    @overload
    def getPadBottom(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.NinePatch.getPadBottom()"""
        return float.__wrap(super(NinePatch, self).getPadBottom())

    @overload
    def __init__(self, arg0: 'TextureRegion', arg1: 'Color'):
        """public com.badlogic.gdx.graphics.g2d.NinePatch(com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.graphics.Color)"""
        val = __NinePatch(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'NinePatch', arg1: 'Color'):
        """public com.badlogic.gdx.graphics.g2d.NinePatch(com.badlogic.gdx.graphics.g2d.NinePatch,com.badlogic.gdx.graphics.Color)"""
        val = __NinePatch(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.graphics.g2d.NinePatch.getTexture()"""
        return 'graphics.Texture'.__wrap(super(NinePatch, self).getTexture())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setPadTop(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.setPadTop(float)"""
        super(__NinePatch, self).setPadTop(__float.valueOf(arg0))

    @overload
    def draw(self, arg0: 'Batch', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.graphics.g2d.NinePatch.draw(com.badlogic.gdx.graphics.g2d.Batch,float,float,float,float,float,float,float,float,float)"""
        super(__NinePatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEffect
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter
__ParticleEmitter = __ParticleEmitter
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pygdx.math import collision
except ImportError:
    collision = __import_once__("pygdx.math.collision")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g2d.ParticleEffect as __ParticleEffect
__ParticleEffect = __ParticleEffect
import com.badlogic.gdx.math.collision.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ParticleEffect():
    """com.badlogic.gdx.graphics.g2d.ParticleEffect"""
 
    @staticmethod
    def __wrap(java_value: __ParticleEffect) -> 'ParticleEffect':
        return ParticleEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleEffect):
        """
        Dynamic initializer for ParticleEffect.
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
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.dispose()"""
        super(ParticleEffect, self).dispose()

    @overload
    def preAllocateParticles(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.preAllocateParticles()"""
        super(ParticleEffect, self).preAllocateParticles()

    @overload
    def save(self, arg0: 'Writer'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.save(java.io.Writer) throws java.io.IOException"""
        super(__ParticleEffect, self).save(arg0)

    @overload
    def update(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.update(float)"""
        super(__ParticleEffect, self).update(__float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def loadEmitterImages(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.loadEmitterImages(com.badlogic.gdx.files.FileHandle)"""
        super(__ParticleEffect, self).loadEmitterImages(arg0)

    @overload
    def allowCompletion(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.allowCompletion()"""
        super(ParticleEffect, self).allowCompletion()

    @overload
    def draw(self, arg0: 'Batch', arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.draw(com.badlogic.gdx.graphics.g2d.Batch,float)"""
        super(__ParticleEffect, self).draw(arg0, __float.valueOf(arg1))

    @overload
    def scaleEffect(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.scaleEffect(float,float,float)"""
        super(__ParticleEffect, self).scaleEffect(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.ParticleEffect()"""
        val = __ParticleEffect()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEffect.isComplete()"""
        return bool.__wrap(super(ParticleEffect, self).isComplete())

    @overload
    def flipY(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.flipY()"""
        super(ParticleEffect, self).flipY()

    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.reset()"""
        super(ParticleEffect, self).reset()

    @overload
    def reset(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.reset(boolean)"""
        super(__ParticleEffect, self).reset(__boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.ParticleEffect()"""
        val = __ParticleEffect()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def loadEmitters(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.loadEmitters(com.badlogic.gdx.files.FileHandle)"""
        super(__ParticleEffect, self).loadEmitters(arg0)

    @overload
    def scaleEffect(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.scaleEffect(float)"""
        super(__ParticleEffect, self).scaleEffect(__float.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.start()"""
        super(ParticleEffect, self).start()

    @overload
    def __init__(self, arg0: 'ParticleEffect'):
        """public com.badlogic.gdx.graphics.g2d.ParticleEffect(com.badlogic.gdx.graphics.g2d.ParticleEffect)"""
        val = __ParticleEffect(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setDuration(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.setDuration(int)"""
        super(__ParticleEffect, self).setDuration(__int.valueOf(arg0))

    @overload
    def loadEmitterImages(self, arg0: 'TextureAtlas'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.loadEmitterImages(com.badlogic.gdx.graphics.g2d.TextureAtlas)"""
        super(__ParticleEffect, self).loadEmitterImages(arg0)

    @overload
    def load(self, arg0: 'FileHandle', arg1: 'TextureAtlas'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.load(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g2d.TextureAtlas)"""
        super(__ParticleEffect, self).load(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def findEmitter(self, arg0: str) -> 'ParticleEmitter':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter com.badlogic.gdx.graphics.g2d.ParticleEffect.findEmitter(java.lang.String)"""
        return 'ParticleEmitter'.__wrap(super(__ParticleEffect, self).findEmitter(arg0))

    @overload
    def load(self, arg0: 'FileHandle', arg1: 'FileHandle'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.load(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        super(__ParticleEffect, self).load(arg0, arg1)

    @overload
    def setFlip(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.setFlip(boolean,boolean)"""
        super(__ParticleEffect, self).setFlip(__boolean.valueOf(arg0), __boolean.valueOf(arg1))

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
    def load(self, arg0: 'FileHandle', arg1: 'TextureAtlas', arg2: str):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.load(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g2d.TextureAtlas,java.lang.String)"""
        super(__ParticleEffect, self).load(arg0, arg1, arg2)

    @overload
    def getEmitters(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.ParticleEmitter> com.badlogic.gdx.graphics.g2d.ParticleEffect.getEmitters()"""
        return 'utils.Array'.__wrap(super(ParticleEffect, self).getEmitters())

    @overload
    def loadEmitterImages(self, arg0: 'TextureAtlas', arg1: str):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.loadEmitterImages(com.badlogic.gdx.graphics.g2d.TextureAtlas,java.lang.String)"""
        super(__ParticleEffect, self).loadEmitterImages(arg0, arg1)

    @overload
    def draw(self, arg0: 'Batch'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.draw(com.badlogic.gdx.graphics.g2d.Batch)"""
        super(__ParticleEffect, self).draw(arg0)

    @overload
    def getBoundingBox(self) -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g2d.ParticleEffect.getBoundingBox()"""
        return 'collision.BoundingBox'.__wrap(super(ParticleEffect, self).getBoundingBox())

    @overload
    def scaleEffect(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.scaleEffect(float,float)"""
        super(__ParticleEffect, self).scaleEffect(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.setPosition(float,float)"""
        super(__ParticleEffect, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def setEmittersCleanUpBlendFunction(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.setEmittersCleanUpBlendFunction(boolean)"""
        super(__ParticleEffect, self).setEmittersCleanUpBlendFunction(__boolean.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.SpriteBatch
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.g2d.SpriteBatch as __SpriteBatch
__SpriteBatch = __SpriteBatch
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import com.badlogic.gdx.graphics.glutils.ShaderProgram as __ShaderProgram
__ShaderProgram = __ShaderProgram
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Matrix4 as __Matrix4
__Matrix4 = __Matrix4
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class SpriteBatch():
    """com.badlogic.gdx.graphics.g2d.SpriteBatch"""
 
    @staticmethod
    def __wrap(java_value: __SpriteBatch) -> 'SpriteBatch':
        return SpriteBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SpriteBatch):
        """
        Dynamic initializer for SpriteBatch.
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
    def getBlendDstFunc(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.SpriteBatch.getBlendDstFunc()"""
        return int.__wrap(super(SpriteBatch, self).getBlendDstFunc())

    @override
    @overload
    def getBlendSrcFuncAlpha(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.SpriteBatch.getBlendSrcFuncAlpha()"""
        return int.__wrap(super(SpriteBatch, self).getBlendSrcFuncAlpha())

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float)"""
        super(__SpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__SpriteBatch, self).setColor(arg0)

    @override
    @overload
    def isDrawing(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.SpriteBatch.isDrawing()"""
        return bool.__wrap(super(SpriteBatch, self).isDrawing())

    @override
    @overload
    def getTransformMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.SpriteBatch.getTransformMatrix()"""
        return 'math.Matrix4'.__wrap(super(SpriteBatch, self).getTransformMatrix())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,float,float,float,float)"""
        super(__SpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9))

    @staticmethod
    @overload
    def createDefaultShader() -> 'glutils.ShaderProgram':
        """public static com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g2d.SpriteBatch.createDefaultShader()"""
        return glutils.ShaderProgram.__wrap(__SpriteBatch.createDefaultShader())

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.end()"""
        super(SpriteBatch, self).end()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def disableBlending(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.disableBlending()"""
        super(SpriteBatch, self).disableBlending()

    @override
    @overload
    def getBlendSrcFunc(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.SpriteBatch.getBlendSrcFunc()"""
        return int.__wrap(super(SpriteBatch, self).getBlendSrcFunc())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setTransformMatrix(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setTransformMatrix(com.badlogic.gdx.math.Matrix4)"""
        super(__SpriteBatch, self).setTransformMatrix(arg0)

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,int,int,int,int)"""
        super(__SpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6))

    @override
    @overload
    def setBlendFunction(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setBlendFunction(int,int)"""
        super(__SpriteBatch, self).setBlendFunction(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: 'Affine2'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,com.badlogic.gdx.math.Affine2)"""
        super(__SpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3)

    @override
    @overload
    def isBlendingEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.SpriteBatch.isBlendingEnabled()"""
        return bool.__wrap(super(SpriteBatch, self).isBlendingEnabled())

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float)"""
        super(__SpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def setPackedColor(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setPackedColor(float)"""
        super(__SpriteBatch, self).setPackedColor(__float.valueOf(arg0))

    @override
    @overload
    def setShader(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setShader(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(__SpriteBatch, self).setShader(arg0)

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

    @override
    @overload
    def flush(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.flush()"""
        super(SpriteBatch, self).flush()

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float)"""
        super(__SpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g2d.SpriteBatch(int)"""
        val = __SpriteBatch(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def enableBlending(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.enableBlending()"""
        super(SpriteBatch, self).enableBlending()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float)"""
        super(__SpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def getPackedColor(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.SpriteBatch.getPackedColor()"""
        return float.__wrap(super(SpriteBatch, self).getPackedColor())

    @override
    @overload
    def getProjectionMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.SpriteBatch.getProjectionMatrix()"""
        return 'math.Matrix4'.__wrap(super(SpriteBatch, self).getProjectionMatrix())

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: bool):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,int,int,int,int,boolean,boolean)"""
        super(__SpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __boolean.valueOf(arg9), __boolean.valueOf(arg10))

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.SpriteBatch.getColor()"""
        return 'graphics.Color'.__wrap(super(SpriteBatch, self).getColor())

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: bool):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,float,float,float,float,boolean)"""
        super(__SpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __boolean.valueOf(arg10))

    @override
    @overload
    def getShader(self) -> 'glutils.ShaderProgram':
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g2d.SpriteBatch.getShader()"""
        return 'glutils.ShaderProgram'.__wrap(super(SpriteBatch, self).getShader())

    @override
    @overload
    def getBlendDstFuncAlpha(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.SpriteBatch.getBlendDstFuncAlpha()"""
        return int.__wrap(super(SpriteBatch, self).getBlendDstFuncAlpha())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.SpriteBatch()"""
        val = __SpriteBatch()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setBlendFunctionSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setBlendFunctionSeparate(int,int,int,int)"""
        super(__SpriteBatch, self).setBlendFunctionSeparate(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setColor(float,float,float,float)"""
        super(__SpriteBatch, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.begin()"""
        super(SpriteBatch, self).begin()

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float)"""
        super(__SpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def setProjectionMatrix(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setProjectionMatrix(com.badlogic.gdx.math.Matrix4)"""
        super(__SpriteBatch, self).setProjectionMatrix(arg0)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.dispose()"""
        super(SpriteBatch, self).dispose()

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float[],int,int)"""
        super(__SpriteBatch, self).draw(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def __init__(self, arg0: int, arg1: 'ShaderProgram'):
        """public com.badlogic.gdx.graphics.g2d.SpriteBatch(int,com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        val = __SpriteBatch(__int.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.SpriteBatch()"""
        val = __SpriteBatch()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: int, arg11: int, arg12: int, arg13: int, arg14: bool, arg15: bool):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float,float,int,int,int,int,boolean,boolean)"""
        super(__SpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __boolean.valueOf(arg14), __boolean.valueOf(arg15)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEmitter$Particle
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
from typing import List
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_Particle
__Particle = __ParticleEmitter_Particle.Particle
import com.badlogic.gdx.math.Rectangle as __Rectangle
__Rectangle = __Rectangle
import com.badlogic.gdx.graphics.g2d.TextureRegion as __TextureRegion
__TextureRegion = __TextureRegion
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g2d.Sprite as __Sprite
__Sprite = __Sprite
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Texture as __Texture
__Texture = __Texture
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class Particle():
    """com.badlogic.gdx.graphics.g2d.ParticleEmitter.Particle"""
 
    @staticmethod
    def __wrap(java_value: __Particle) -> 'Particle':
        return Particle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Particle):
        """
        Dynamic initializer for Particle.
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
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setY(float)"""
        super(__Sprite, self).setY(__float.valueOf(arg0))

    @override
    @overload
    def translateX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.translateX(float)"""
        super(__Sprite, self).translateX(__float.valueOf(arg0))

    @override
    @overload
    def getV2(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getV2()"""
        return float.__wrap(super(TextureRegion, self).getV2())

    @override
    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getScaleY()"""
        return float.__wrap(super(Sprite, self).getScaleY())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setX(float)"""
        super(__Sprite, self).setX(__float.valueOf(arg0))

    @override
    @overload
    def setCenterX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setCenterX(float)"""
        super(__Sprite, self).setCenterX(__float.valueOf(arg0))

    @override
    @overload
    def setOriginCenter(self):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setOriginCenter()"""
        super(Sprite, self).setOriginCenter()

    @overload
    def split(self, arg0: int, arg1: int) -> List[List['TextureRegion']]:
        """public com.badlogic.gdx.graphics.g2d.TextureRegion[][] com.badlogic.gdx.graphics.g2d.TextureRegion.split(int,int)"""
        return List[List['TextureRegion']].__wrap(super(__TextureRegion, self).split(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setCenter(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setCenter(float,float)"""
        super(__Sprite, self).setCenter(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def setRegionX(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionX(int)"""
        super(__TextureRegion, self).setRegionX(__int.valueOf(arg0))

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.Sprite.getColor()"""
        return 'graphics.Color'.__wrap(super(Sprite, self).getColor())

    @override
    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setScale(float)"""
        super(__Sprite, self).setScale(__float.valueOf(arg0))

    @override
    @overload
    def setRegion(self, arg0: 'Texture'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.Texture)"""
        super(__TextureRegion, self).setRegion(arg0)

    @override
    @overload
    def getRegionX(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionX()"""
        return int.__wrap(super(TextureRegion, self).getRegionX())

    @override
    @overload
    def setFlip(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setFlip(boolean,boolean)"""
        super(__Sprite, self).setFlip(__boolean.valueOf(arg0), __boolean.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setU2(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setU2(float)"""
        super(__Sprite, self).setU2(__float.valueOf(arg0))

    @override
    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getX()"""
        return float.__wrap(super(Sprite, self).getX())

    @override
    @overload
    def draw(self, arg0: 'Batch'):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.draw(com.badlogic.gdx.graphics.g2d.Batch)"""
        super(__Sprite, self).draw(arg0)

    @override
    @overload
    def setV(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setV(float)"""
        super(__Sprite, self).setV(__float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setRotation(float)"""
        super(__Sprite, self).setRotation(__float.valueOf(arg0))

    @override
    @overload
    def getRegionWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionWidth()"""
        return int.__wrap(super(TextureRegion, self).getRegionWidth())

    @override
    @overload
    def getRegionY(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionY()"""
        return int.__wrap(super(TextureRegion, self).getRegionY())

    @override
    @overload
    def translate(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.translate(float,float)"""
        super(__Sprite, self).translate(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getOriginY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getOriginY()"""
        return float.__wrap(super(Sprite, self).getOriginY())

    @override
    @overload
    def setRegionWidth(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionWidth(int)"""
        super(__TextureRegion, self).setRegionWidth(__int.valueOf(arg0))

    @override
    @overload
    def setV2(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setV2(float)"""
        super(__Sprite, self).setV2(__float.valueOf(arg0))

    @override
    @overload
    def setRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(__TextureRegion, self).setRegion(arg0)

    @override
    @overload
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getRotation()"""
        return float.__wrap(super(Sprite, self).getRotation())

    @override
    @overload
    def setRegion(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setRegion(float,float,float,float)"""
        super(__Sprite, self).setRegion(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setScale(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setScale(float,float)"""
        super(__Sprite, self).setScale(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def set(self, arg0: 'Sprite'):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.set(com.badlogic.gdx.graphics.g2d.Sprite)"""
        super(__Sprite, self).set(arg0)

    @override
    @overload
    def flip(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.flip(boolean,boolean)"""
        super(__Sprite, self).flip(__boolean.valueOf(arg0), __boolean.valueOf(arg1))

    @override
    @overload
    def getHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getHeight()"""
        return float.__wrap(super(Sprite, self).getHeight())

    @override
    @overload
    def getRegionHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionHeight()"""
        return int.__wrap(super(TextureRegion, self).getRegionHeight())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setPosition(float,float)"""
        super(__Sprite, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def setOriginBasedPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setOriginBasedPosition(float,float)"""
        super(__Sprite, self).setOriginBasedPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getV(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getV()"""
        return float.__wrap(super(TextureRegion, self).getV())

    @override
    @overload
    def translateY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.translateY(float)"""
        super(__Sprite, self).translateY(__float.valueOf(arg0))

    @override
    @overload
    def setRegionHeight(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionHeight(int)"""
        super(__TextureRegion, self).setRegionHeight(__int.valueOf(arg0))

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setColor(float,float,float,float)"""
        super(__Sprite, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def rotate90(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.rotate90(boolean)"""
        super(__Sprite, self).rotate90(__boolean.valueOf(arg0))

    @override
    @overload
    def setCenterY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setCenterY(float)"""
        super(__Sprite, self).setCenterY(__float.valueOf(arg0))

    @override
    @overload
    def isFlipY(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.TextureRegion.isFlipY()"""
        return bool.__wrap(super(TextureRegion, self).isFlipY())

    @staticmethod
    @overload
    def split(arg0: 'Texture', arg1: int, arg2: int) -> List[List['TextureRegion']]:
        """public static com.badlogic.gdx.graphics.g2d.TextureRegion[][] com.badlogic.gdx.graphics.g2d.TextureRegion.split(com.badlogic.gdx.graphics.Texture,int,int)"""
        return List[List[TextureRegion]].__wrap(__TextureRegion.split(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def __init__(self, arg0: 'Sprite'):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$Particle(com.badlogic.gdx.graphics.g2d.Sprite)"""
        val = __Particle(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setPackedColor(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setPackedColor(float)"""
        super(__Sprite, self).setPackedColor(__float.valueOf(arg0))

    @override
    @overload
    def setU(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setU(float)"""
        super(__Sprite, self).setU(__float.valueOf(arg0))

    @override
    @overload
    def getOriginX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getOriginX()"""
        return float.__wrap(super(Sprite, self).getOriginX())

    @override
    @overload
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.graphics.g2d.TextureRegion.getTexture()"""
        return 'graphics.Texture'.__wrap(super(TextureRegion, self).getTexture())

    @override
    @overload
    def getBoundingRectangle(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.graphics.g2d.Sprite.getBoundingRectangle()"""
        return 'math.Rectangle'.__wrap(super(Sprite, self).getBoundingRectangle())

    @override
    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getY()"""
        return float.__wrap(super(Sprite, self).getY())

    @override
    @overload
    def getVertices(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.Sprite.getVertices()"""
        return List[float].__wrap(super(Sprite, self).getVertices())

    @override
    @overload
    def scale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.scale(float)"""
        super(__Sprite, self).scale(__float.valueOf(arg0))

    @override
    @overload
    def getU(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getU()"""
        return float.__wrap(super(TextureRegion, self).getU())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setTexture(self, arg0: 'Texture'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setTexture(com.badlogic.gdx.graphics.Texture)"""
        super(__TextureRegion, self).setTexture(arg0)

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__Sprite, self).setColor(arg0)

    @override
    @overload
    def getU2(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getU2()"""
        return float.__wrap(super(TextureRegion, self).getU2())

    @override
    @overload
    def setRegion(self, arg0: 'TextureRegion', arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.g2d.TextureRegion,int,int,int,int)"""
        super(__TextureRegion, self).setRegion(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def scroll(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.scroll(float,float)"""
        super(__Sprite, self).scroll(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.draw(com.badlogic.gdx.graphics.g2d.Batch,float)"""
        super(__Sprite, self).draw(arg0, __float.valueOf(arg1))

    @override
    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getScaleX()"""
        return float.__wrap(super(Sprite, self).getScaleX())

    @override
    @overload
    def setOrigin(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setOrigin(float,float)"""
        super(__Sprite, self).setOrigin(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def isFlipX(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.TextureRegion.isFlipX()"""
        return bool.__wrap(super(TextureRegion, self).isFlipX())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setSize(float,float)"""
        super(__Sprite, self).setSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def setBounds(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setBounds(float,float,float,float)"""
        super(__Sprite, self).setBounds(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getWidth()"""
        return float.__wrap(super(Sprite, self).getWidth())

    @override
    @overload
    def setRegionY(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionY(int)"""
        super(__TextureRegion, self).setRegionY(__int.valueOf(arg0))

    @override
    @overload
    def setAlpha(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setAlpha(float)"""
        super(__Sprite, self).setAlpha(__float.valueOf(arg0))

    @override
    @overload
    def rotate(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.rotate(float)"""
        super(__Sprite, self).rotate(__float.valueOf(arg0))

    @override
    @overload
    def setRegion(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(int,int,int,int)"""
        super(__TextureRegion, self).setRegion(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PolygonSprite
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.graphics.g2d.PolygonRegion as __PolygonRegion
__PolygonRegion = __PolygonRegion
import com.badlogic.gdx.graphics.g2d.PolygonSprite as __PolygonSprite
__PolygonSprite = __PolygonSprite
from typing import List
import com.badlogic.gdx.math.Rectangle as __Rectangle
__Rectangle = __Rectangle
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class PolygonSprite():
    """com.badlogic.gdx.graphics.g2d.PolygonSprite"""
 
    @staticmethod
    def __wrap(java_value: __PolygonSprite) -> 'PolygonSprite':
        return PolygonSprite(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PolygonSprite):
        """
        Dynamic initializer for PolygonSprite.
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
    def scale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.scale(float)"""
        super(__PolygonSprite, self).scale(__float.valueOf(arg0))

    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.PolygonSprite.getScaleX()"""
        return float.__wrap(super(PolygonSprite, self).getScaleX())

    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.setScale(float)"""
        super(__PolygonSprite, self).setScale(__float.valueOf(arg0))

    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.setX(float)"""
        super(__PolygonSprite, self).setX(__float.valueOf(arg0))

    @overload
    def getOriginX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.PolygonSprite.getOriginX()"""
        return float.__wrap(super(PolygonSprite, self).getOriginX())

    @overload
    def draw(self, arg0: 'PolygonSpriteBatch'):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.draw(com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch)"""
        super(__PolygonSprite, self).draw(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def translateY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.translateY(float)"""
        super(__PolygonSprite, self).translateY(__float.valueOf(arg0))

    @overload
    def setOrigin(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.setOrigin(float,float)"""
        super(__PolygonSprite, self).setOrigin(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def set(self, arg0: 'PolygonSprite'):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.set(com.badlogic.gdx.graphics.g2d.PolygonSprite)"""
        super(__PolygonSprite, self).set(arg0)

    @overload
    def __init__(self, arg0: 'PolygonSprite'):
        """public com.badlogic.gdx.graphics.g2d.PolygonSprite(com.badlogic.gdx.graphics.g2d.PolygonSprite)"""
        val = __PolygonSprite(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getRegion(self) -> 'PolygonRegion':
        """public com.badlogic.gdx.graphics.g2d.PolygonRegion com.badlogic.gdx.graphics.g2d.PolygonSprite.getRegion()"""
        return 'PolygonRegion'.__wrap(super(PolygonSprite, self).getRegion())

    @overload
    def getOriginY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.PolygonSprite.getOriginY()"""
        return float.__wrap(super(PolygonSprite, self).getOriginY())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.setRotation(float)"""
        super(__PolygonSprite, self).setRotation(__float.valueOf(arg0))

    @overload
    def setBounds(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.setBounds(float,float,float,float)"""
        super(__PolygonSprite, self).setBounds(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.PolygonSprite.getScaleY()"""
        return float.__wrap(super(PolygonSprite, self).getScaleY())

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.setColor(float,float,float,float)"""
        super(__PolygonSprite, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getBoundingRectangle(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.graphics.g2d.PolygonSprite.getBoundingRectangle()"""
        return 'math.Rectangle'.__wrap(super(PolygonSprite, self).getBoundingRectangle())

    @overload
    def draw(self, arg0: 'PolygonSpriteBatch', arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.draw(com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch,float)"""
        super(__PolygonSprite, self).draw(arg0, __float.valueOf(arg1))

    @overload
    def getPackedColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.PolygonSprite.getPackedColor()"""
        return 'graphics.Color'.__wrap(super(PolygonSprite, self).getPackedColor())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.PolygonSprite.getX()"""
        return float.__wrap(super(PolygonSprite, self).getX())

    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.PolygonSprite.getWidth()"""
        return float.__wrap(super(PolygonSprite, self).getWidth())

    @overload
    def setSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.setSize(float,float)"""
        super(__PolygonSprite, self).setSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def getVertices(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.PolygonSprite.getVertices()"""
        return List[float].__wrap(super(PolygonSprite, self).getVertices())

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.PolygonSprite.getColor()"""
        return 'graphics.Color'.__wrap(super(PolygonSprite, self).getColor())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'PolygonRegion'):
        """public com.badlogic.gdx.graphics.g2d.PolygonSprite(com.badlogic.gdx.graphics.g2d.PolygonRegion)"""
        val = __PolygonSprite(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.setPosition(float,float)"""
        super(__PolygonSprite, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.PolygonSprite.getRotation()"""
        return float.__wrap(super(PolygonSprite, self).getRotation())

    @overload
    def translateX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.translateX(float)"""
        super(__PolygonSprite, self).translateX(__float.valueOf(arg0))

    @overload
    def setRegion(self, arg0: 'PolygonRegion'):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.setRegion(com.badlogic.gdx.graphics.g2d.PolygonRegion)"""
        super(__PolygonSprite, self).setRegion(arg0)

    @overload
    def setScale(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.setScale(float,float)"""
        super(__PolygonSprite, self).setScale(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.setY(float)"""
        super(__PolygonSprite, self).setY(__float.valueOf(arg0))

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
    def rotate(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.rotate(float)"""
        super(__PolygonSprite, self).rotate(__float.valueOf(arg0))

    @overload
    def getHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.PolygonSprite.getHeight()"""
        return float.__wrap(super(PolygonSprite, self).getHeight())

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__PolygonSprite, self).setColor(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.PolygonSprite.getY()"""
        return float.__wrap(super(PolygonSprite, self).getY())

    @overload
    def translate(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSprite.translate(float,float)"""
        super(__PolygonSprite, self).translate(__float.valueOf(arg0), __float.valueOf(arg1)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PixmapPackerIO
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.graphics.g2d.PixmapPackerIO as __PixmapPackerIO
__PixmapPackerIO = __PixmapPackerIO
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PixmapPackerIO():
    """com.badlogic.gdx.graphics.g2d.PixmapPackerIO"""
 
    @staticmethod
    def __wrap(java_value: __PixmapPackerIO) -> 'PixmapPackerIO':
        return PixmapPackerIO(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PixmapPackerIO):
        """
        Dynamic initializer for PixmapPackerIO.
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

    @overload
    def save(self, arg0: 'FileHandle', arg1: 'PixmapPacker', arg2: 'SaveParameters'):
        """public void com.badlogic.gdx.graphics.g2d.PixmapPackerIO.save(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g2d.PixmapPacker,com.badlogic.gdx.graphics.g2d.PixmapPackerIO$SaveParameters) throws java.io.IOException"""
        super(__PixmapPackerIO, self).save(arg0, arg1, arg2)

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
    def save(self, arg0: 'FileHandle', arg1: 'PixmapPacker'):
        """public void com.badlogic.gdx.graphics.g2d.PixmapPackerIO.save(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g2d.PixmapPacker) throws java.io.IOException"""
        super(__PixmapPackerIO, self).save(arg0, arg1)

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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.PixmapPackerIO()"""
        val = __PixmapPackerIO()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.PixmapPackerIO()"""
        val = __PixmapPackerIO()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.Gdx2DPixmap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.nio.ByteBuffer as __ByteBuffer
__ByteBuffer = __ByteBuffer
import com.badlogic.gdx.graphics.g2d.Gdx2DPixmap as __Gdx2DPixmap
__Gdx2DPixmap = __Gdx2DPixmap
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.nio.ByteBuffer as ByteBuffer
from builtins import bool
from builtins import int
 
class Gdx2DPixmap():
    """com.badlogic.gdx.graphics.g2d.Gdx2DPixmap"""
 
    @staticmethod
    def __wrap(java_value: __Gdx2DPixmap) -> 'Gdx2DPixmap':
        return Gdx2DPixmap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Gdx2DPixmap):
        """
        Dynamic initializer for Gdx2DPixmap.
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
    def newPixmap(arg0: 'InputStream', arg1: int) -> 'Gdx2DPixmap':
        """public static com.badlogic.gdx.graphics.g2d.Gdx2DPixmap com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.newPixmap(java.io.InputStream,int)"""
        return Gdx2DPixmap.__wrap(__Gdx2DPixmap.newPixmap(arg0, __int.valueOf(arg1)))

    @overload
    def drawCircle(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.drawCircle(int,int,int,int)"""
        super(__Gdx2DPixmap, self).drawCircle(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @staticmethod
    @overload
    def toGlType(arg0: int) -> int:
        """public static int com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.toGlType(int)"""
        return int.__wrap(__Gdx2DPixmap.toGlType(__int.valueOf(arg0)))

    @overload
    def fillTriangle(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.fillTriangle(int,int,int,int,int,int,int)"""
        super(__Gdx2DPixmap, self).fillTriangle(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getFormatString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.getFormatString()"""
        return str.__wrap(super(Gdx2DPixmap, self).getFormatString())

    @overload
    def drawLine(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.drawLine(int,int,int,int,int)"""
        super(__Gdx2DPixmap, self).drawLine(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @overload
    def getGLInternalFormat(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.getGLInternalFormat()"""
        return int.__wrap(super(Gdx2DPixmap, self).getGLInternalFormat())

    @overload
    def setPixel(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.setPixel(int,int,int)"""
        super(__Gdx2DPixmap, self).setPixel(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def __init__(self, arg0: 'ByteBuffer', arg1: int, arg2: int, arg3: int):
        """public com.badlogic.gdx.graphics.g2d.Gdx2DPixmap(java.nio.ByteBuffer,int,int,int) throws java.io.IOException"""
        val = __Gdx2DPixmap(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def getWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.getWidth()"""
        return int.__wrap(super(Gdx2DPixmap, self).getWidth())

    @staticmethod
    @overload
    def toGlFormat(arg0: int) -> int:
        """public static int com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.toGlFormat(int)"""
        return int.__wrap(__Gdx2DPixmap.toGlFormat(__int.valueOf(arg0)))

    @staticmethod
    @overload
    def newPixmap(arg0: int, arg1: int, arg2: int) -> 'Gdx2DPixmap':
        """public static com.badlogic.gdx.graphics.g2d.Gdx2DPixmap com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.newPixmap(int,int,int)"""
        return Gdx2DPixmap.__wrap(__Gdx2DPixmap.newPixmap(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def fillRect(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.fillRect(int,int,int,int,int)"""
        super(__Gdx2DPixmap, self).fillRect(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def drawPixmap(self, arg0: 'Gdx2DPixmap', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int, arg7: int, arg8: int):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.drawPixmap(com.badlogic.gdx.graphics.g2d.Gdx2DPixmap,int,int,int,int,int,int,int,int)"""
        super(__Gdx2DPixmap, self).drawPixmap(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int):
        """public com.badlogic.gdx.graphics.g2d.Gdx2DPixmap(int,int,int) throws com.badlogic.gdx.utils.GdxRuntimeException"""
        val = __Gdx2DPixmap(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getGLType(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.getGLType()"""
        return int.__wrap(super(Gdx2DPixmap, self).getGLType())

    @overload
    def setScale(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.setScale(int)"""
        super(__Gdx2DPixmap, self).setScale(__int.valueOf(arg0))

    @staticmethod
    @overload
    def getFailureReason() -> str:
        """public static native java.lang.String com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.getFailureReason()"""
        return str.__wrap(__Gdx2DPixmap.getFailureReason())

    @overload
    def __init__(self, arg0: bytes, arg1: int, arg2: int, arg3: int):
        """public com.badlogic.gdx.graphics.g2d.Gdx2DPixmap(byte[],int,int,int) throws java.io.IOException"""
        val = __Gdx2DPixmap(bytes, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setBlend(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.setBlend(int)"""
        super(__Gdx2DPixmap, self).setBlend(__int.valueOf(arg0))

    @overload
    def getPixels(self) -> 'ByteBuffer':
        """public java.nio.ByteBuffer com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.getPixels()"""
        return 'ByteBuffer'.__wrap(super(Gdx2DPixmap, self).getPixels())

    @overload
    def getFormat(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.getFormat()"""
        return int.__wrap(super(Gdx2DPixmap, self).getFormat())

    @overload
    def __init__(self, arg0: 'InputStream', arg1: int):
        """public com.badlogic.gdx.graphics.g2d.Gdx2DPixmap(java.io.InputStream,int) throws java.io.IOException"""
        val = __Gdx2DPixmap(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def clear(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.clear(int)"""
        super(__Gdx2DPixmap, self).clear(__int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def fillCircle(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.fillCircle(int,int,int,int)"""
        super(__Gdx2DPixmap, self).fillCircle(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def drawPixmap(self, arg0: 'Gdx2DPixmap', arg1: int, arg2: int, arg3: int, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.drawPixmap(com.badlogic.gdx.graphics.g2d.Gdx2DPixmap,int,int,int,int,int,int)"""
        super(__Gdx2DPixmap, self).drawPixmap(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6))

    @overload
    def getGLFormat(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.getGLFormat()"""
        return int.__wrap(super(Gdx2DPixmap, self).getGLFormat())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.dispose()"""
        super(Gdx2DPixmap, self).dispose()

    @overload
    def getHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.getHeight()"""
        return int.__wrap(super(Gdx2DPixmap, self).getHeight())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def drawRect(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.drawRect(int,int,int,int,int)"""
        super(__Gdx2DPixmap, self).drawRect(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @overload
    def __init__(self, arg0: 'ByteBuffer', arg1: 'long'):
        """public com.badlogic.gdx.graphics.g2d.Gdx2DPixmap(java.nio.ByteBuffer,long[])"""
        val = __Gdx2DPixmap(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getPixel(self, arg0: int, arg1: int) -> int:
        """public int com.badlogic.gdx.graphics.g2d.Gdx2DPixmap.getPixel(int,int)"""
        return int.__wrap(super(__Gdx2DPixmap, self).getPixel(__int.valueOf(arg0), __int.valueOf(arg1))) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.Sprite
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
from typing import List
import com.badlogic.gdx.math.Rectangle as __Rectangle
__Rectangle = __Rectangle
import com.badlogic.gdx.graphics.g2d.TextureRegion as __TextureRegion
__TextureRegion = __TextureRegion
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g2d.Sprite as __Sprite
__Sprite = __Sprite
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Texture as __Texture
__Texture = __Texture
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class Sprite():
    """com.badlogic.gdx.graphics.g2d.Sprite"""
 
    @staticmethod
    def __wrap(java_value: __Sprite) -> 'Sprite':
        return Sprite(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Sprite):
        """
        Dynamic initializer for Sprite.
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
    def setPackedColor(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setPackedColor(float)"""
        super(__Sprite, self).setPackedColor(__float.valueOf(arg0))

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getX()"""
        return float.__wrap(super(Sprite, self).getX())

    @override
    @overload
    def getV2(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getV2()"""
        return float.__wrap(super(TextureRegion, self).getV2())

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.Sprite.getColor()"""
        return 'graphics.Color'.__wrap(super(Sprite, self).getColor())

    @overload
    def getOriginY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getOriginY()"""
        return float.__wrap(super(Sprite, self).getOriginY())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'TextureRegion', arg1: int, arg2: int, arg3: int, arg4: int):
        """public com.badlogic.gdx.graphics.g2d.Sprite(com.badlogic.gdx.graphics.g2d.TextureRegion,int,int,int,int)"""
        val = __Sprite(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setScale(float)"""
        super(__Sprite, self).setScale(__float.valueOf(arg0))

    @overload
    def draw(self, arg0: 'Batch'):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.draw(com.badlogic.gdx.graphics.g2d.Batch)"""
        super(__Sprite, self).draw(arg0)

    @overload
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setRotation(float)"""
        super(__Sprite, self).setRotation(__float.valueOf(arg0))

    @overload
    def setOriginCenter(self):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setOriginCenter()"""
        super(Sprite, self).setOriginCenter()

    @overload
    def split(self, arg0: int, arg1: int) -> List[List['TextureRegion']]:
        """public com.badlogic.gdx.graphics.g2d.TextureRegion[][] com.badlogic.gdx.graphics.g2d.TextureRegion.split(int,int)"""
        return List[List['TextureRegion']].__wrap(super(__TextureRegion, self).split(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setRegionX(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionX(int)"""
        super(__TextureRegion, self).setRegionX(__int.valueOf(arg0))

    @overload
    def setCenter(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setCenter(float,float)"""
        super(__Sprite, self).setCenter(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def translateX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.translateX(float)"""
        super(__Sprite, self).translateX(__float.valueOf(arg0))

    @overload
    def setFlip(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setFlip(boolean,boolean)"""
        super(__Sprite, self).setFlip(__boolean.valueOf(arg0), __boolean.valueOf(arg1))

    @overload
    def getHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getHeight()"""
        return float.__wrap(super(Sprite, self).getHeight())

    @overload
    def __init__(self, arg0: 'TextureRegion'):
        """public com.badlogic.gdx.graphics.g2d.Sprite(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = __Sprite(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setRegion(self, arg0: 'Texture'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.Texture)"""
        super(__TextureRegion, self).setRegion(arg0)

    @override
    @overload
    def getRegionX(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionX()"""
        return int.__wrap(super(TextureRegion, self).getRegionX())

    @overload
    def scale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.scale(float)"""
        super(__Sprite, self).scale(__float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setU2(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setU2(float)"""
        super(__Sprite, self).setU2(__float.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Sprite'):
        """public com.badlogic.gdx.graphics.g2d.Sprite(com.badlogic.gdx.graphics.g2d.Sprite)"""
        val = __Sprite(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Texture', arg1: int, arg2: int, arg3: int, arg4: int):
        """public com.badlogic.gdx.graphics.g2d.Sprite(com.badlogic.gdx.graphics.Texture,int,int,int,int)"""
        val = __Sprite(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setV(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setV(float)"""
        super(__Sprite, self).setV(__float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Texture'):
        """public com.badlogic.gdx.graphics.g2d.Sprite(com.badlogic.gdx.graphics.Texture)"""
        val = __Sprite(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getRegionWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionWidth()"""
        return int.__wrap(super(TextureRegion, self).getRegionWidth())

    @override
    @overload
    def getRegionY(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionY()"""
        return int.__wrap(super(TextureRegion, self).getRegionY())

    @overload
    def translate(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.translate(float,float)"""
        super(__Sprite, self).translate(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getRotation()"""
        return float.__wrap(super(Sprite, self).getRotation())

    @override
    @overload
    def setRegionWidth(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionWidth(int)"""
        super(__TextureRegion, self).setRegionWidth(__int.valueOf(arg0))

    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getScaleY()"""
        return float.__wrap(super(Sprite, self).getScaleY())

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getY()"""
        return float.__wrap(super(Sprite, self).getY())

    @override
    @overload
    def setV2(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setV2(float)"""
        super(__Sprite, self).setV2(__float.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Texture', arg1: int, arg2: int):
        """public com.badlogic.gdx.graphics.g2d.Sprite(com.badlogic.gdx.graphics.Texture,int,int)"""
        val = __Sprite(arg0, __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(__TextureRegion, self).setRegion(arg0)

    @overload
    def setScale(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setScale(float,float)"""
        super(__Sprite, self).setScale(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def setRegion(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setRegion(float,float,float,float)"""
        super(__Sprite, self).setRegion(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def flip(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.flip(boolean,boolean)"""
        super(__Sprite, self).flip(__boolean.valueOf(arg0), __boolean.valueOf(arg1))

    @overload
    def getOriginX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getOriginX()"""
        return float.__wrap(super(Sprite, self).getOriginX())

    @overload
    def rotate(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.rotate(float)"""
        super(__Sprite, self).rotate(__float.valueOf(arg0))

    @override
    @overload
    def getRegionHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionHeight()"""
        return int.__wrap(super(TextureRegion, self).getRegionHeight())

    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getScaleX()"""
        return float.__wrap(super(Sprite, self).getScaleX())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getV(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getV()"""
        return float.__wrap(super(TextureRegion, self).getV())

    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setX(float)"""
        super(__Sprite, self).setX(__float.valueOf(arg0))

    @override
    @overload
    def setRegionHeight(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionHeight(int)"""
        super(__TextureRegion, self).setRegionHeight(__int.valueOf(arg0))

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__Sprite, self).setColor(arg0)

    @overload
    def setAlpha(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setAlpha(float)"""
        super(__Sprite, self).setAlpha(__float.valueOf(arg0))

    @override
    @overload
    def isFlipY(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.TextureRegion.isFlipY()"""
        return bool.__wrap(super(TextureRegion, self).isFlipY())

    @staticmethod
    @overload
    def split(arg0: 'Texture', arg1: int, arg2: int) -> List[List['TextureRegion']]:
        """public static com.badlogic.gdx.graphics.g2d.TextureRegion[][] com.badlogic.gdx.graphics.g2d.TextureRegion.split(com.badlogic.gdx.graphics.Texture,int,int)"""
        return List[List[TextureRegion]].__wrap(__TextureRegion.split(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def setSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setSize(float,float)"""
        super(__Sprite, self).setSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def setBounds(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setBounds(float,float,float,float)"""
        super(__Sprite, self).setBounds(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def setU(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setU(float)"""
        super(__Sprite, self).setU(__float.valueOf(arg0))

    @overload
    def setOriginBasedPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setOriginBasedPosition(float,float)"""
        super(__Sprite, self).setOriginBasedPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.graphics.g2d.TextureRegion.getTexture()"""
        return 'graphics.Texture'.__wrap(super(TextureRegion, self).getTexture())

    @overload
    def rotate90(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.rotate90(boolean)"""
        super(__Sprite, self).rotate90(__boolean.valueOf(arg0))

    @overload
    def getBoundingRectangle(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.graphics.g2d.Sprite.getBoundingRectangle()"""
        return 'math.Rectangle'.__wrap(super(Sprite, self).getBoundingRectangle())

    @override
    @overload
    def getU(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getU()"""
        return float.__wrap(super(TextureRegion, self).getU())

    @overload
    def translateY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.translateY(float)"""
        super(__Sprite, self).translateY(__float.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setTexture(self, arg0: 'Texture'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setTexture(com.badlogic.gdx.graphics.Texture)"""
        super(__TextureRegion, self).setTexture(arg0)

    @override
    @overload
    def getU2(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getU2()"""
        return float.__wrap(super(TextureRegion, self).getU2())

    @override
    @overload
    def setRegion(self, arg0: 'TextureRegion', arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.g2d.TextureRegion,int,int,int,int)"""
        super(__TextureRegion, self).setRegion(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def scroll(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.scroll(float,float)"""
        super(__Sprite, self).scroll(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def draw(self, arg0: 'Batch', arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.draw(com.badlogic.gdx.graphics.g2d.Batch,float)"""
        super(__Sprite, self).draw(arg0, __float.valueOf(arg1))

    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getWidth()"""
        return float.__wrap(super(Sprite, self).getWidth())

    @overload
    def getVertices(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.Sprite.getVertices()"""
        return List[float].__wrap(super(Sprite, self).getVertices())

    @overload
    def setOrigin(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setOrigin(float,float)"""
        super(__Sprite, self).setOrigin(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.Sprite()"""
        val = __Sprite()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setColor(float,float,float,float)"""
        super(__Sprite, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def isFlipX(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.TextureRegion.isFlipX()"""
        return bool.__wrap(super(TextureRegion, self).isFlipX())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.Sprite()"""
        val = __Sprite()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: 'Sprite'):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.set(com.badlogic.gdx.graphics.g2d.Sprite)"""
        super(__Sprite, self).set(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setY(float)"""
        super(__Sprite, self).setY(__float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def setRegionY(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionY(int)"""
        super(__TextureRegion, self).setRegionY(__int.valueOf(arg0))

    @overload
    def setCenterX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setCenterX(float)"""
        super(__Sprite, self).setCenterX(__float.valueOf(arg0))

    @overload
    def setCenterY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setCenterY(float)"""
        super(__Sprite, self).setCenterY(__float.valueOf(arg0))

    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setPosition(float,float)"""
        super(__Sprite, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def setRegion(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(int,int,int,int)"""
        super(__TextureRegion, self).setRegion(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PixmapPacker
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from builtins import str
import com.badlogic.gdx.graphics.g2d.PixmapPacker as __PixmapPacker
__PixmapPacker = __PixmapPacker
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import com.badlogic.gdx.graphics.g2d.TextureAtlas as __TextureAtlas
__TextureAtlas = __TextureAtlas
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Rectangle as __Rectangle
__Rectangle = __Rectangle
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Pixmap as __Pixmap_Format
__Format = __Pixmap_Format.Format
import com.badlogic.gdx.graphics.g2d.PixmapPacker as __PixmapPacker_Page
__Page = __PixmapPacker_Page.Page
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class PixmapPacker():
    """com.badlogic.gdx.graphics.g2d.PixmapPacker"""
 
    @staticmethod
    def __wrap(java_value: __PixmapPacker) -> 'PixmapPacker':
        return PixmapPacker(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PixmapPacker):
        """
        Dynamic initializer for PixmapPacker.
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
    def updateTextureAtlas(self, arg0: 'TextureAtlas', arg1: 'TextureFilter', arg2: 'TextureFilter', arg3: bool):
        """public synchronized void com.badlogic.gdx.graphics.g2d.PixmapPacker.updateTextureAtlas(com.badlogic.gdx.graphics.g2d.TextureAtlas,com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,boolean)"""
        super(__PixmapPacker, self).updateTextureAtlas(arg0, arg1, arg2, __boolean.valueOf(arg3))

    @overload
    def setPadding(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.PixmapPacker.setPadding(int)"""
        super(__PixmapPacker, self).setPadding(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'Format', arg3: int, arg4: bool, arg5: 'PackStrategy'):
        """public com.badlogic.gdx.graphics.g2d.PixmapPacker(int,int,com.badlogic.gdx.graphics.Pixmap$Format,int,boolean,com.badlogic.gdx.graphics.g2d.PixmapPacker$PackStrategy)"""
        val = __PixmapPacker(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __boolean.valueOf(arg4), arg5)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getPackToTexture(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.PixmapPacker.getPackToTexture()"""
        return bool.__wrap(super(PixmapPacker, self).getPackToTexture())

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
    def pack(self, arg0: str, arg1: 'Pixmap') -> 'math.Rectangle':
        """public synchronized com.badlogic.gdx.math.Rectangle com.badlogic.gdx.graphics.g2d.PixmapPacker.pack(java.lang.String,com.badlogic.gdx.graphics.Pixmap)"""
        return 'math.Rectangle'.__wrap(super(__PixmapPacker, self).pack(arg0, arg1))

    @overload
    def updateTextureRegions(self, arg0: 'Array', arg1: 'TextureFilter', arg2: 'TextureFilter', arg3: bool):
        """public synchronized void com.badlogic.gdx.graphics.g2d.PixmapPacker.updateTextureRegions(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.TextureRegion>,com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,boolean)"""
        super(__PixmapPacker, self).updateTextureRegions(arg0, arg1, arg2, __boolean.valueOf(arg3))

    @overload
    def setPageFormat(self, arg0: 'Format'):
        """public void com.badlogic.gdx.graphics.g2d.PixmapPacker.setPageFormat(com.badlogic.gdx.graphics.Pixmap$Format)"""
        super(__PixmapPacker, self).setPageFormat(arg0)

    @overload
    def setDuplicateBorder(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.PixmapPacker.setDuplicateBorder(boolean)"""
        super(__PixmapPacker, self).setDuplicateBorder(__boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'Format', arg3: int, arg4: bool, arg5: bool, arg6: bool, arg7: 'PackStrategy'):
        """public com.badlogic.gdx.graphics.g2d.PixmapPacker(int,int,com.badlogic.gdx.graphics.Pixmap$Format,int,boolean,boolean,boolean,com.badlogic.gdx.graphics.g2d.PixmapPacker$PackStrategy)"""
        val = __PixmapPacker(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __boolean.valueOf(arg4), __boolean.valueOf(arg5), __boolean.valueOf(arg6), arg7)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getPageHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.PixmapPacker.getPageHeight()"""
        return int.__wrap(super(PixmapPacker, self).getPageHeight())

    @overload
    def getPageFormat(self) -> 'graphics.Pixmap$Format':
        """public com.badlogic.gdx.graphics.Pixmap$Format com.badlogic.gdx.graphics.g2d.PixmapPacker.getPageFormat()"""
        return 'graphics.Pixmap$Format'.__wrap(super(PixmapPacker, self).getPageFormat())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getRect(self, arg0: str) -> 'math.Rectangle':
        """public synchronized com.badlogic.gdx.math.Rectangle com.badlogic.gdx.graphics.g2d.PixmapPacker.getRect(java.lang.String)"""
        return 'math.Rectangle'.__wrap(super(__PixmapPacker, self).getRect(arg0))

    @overload
    def getPadding(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.PixmapPacker.getPadding()"""
        return int.__wrap(super(PixmapPacker, self).getPadding())

    @overload
    def getDuplicateBorder(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.PixmapPacker.getDuplicateBorder()"""
        return bool.__wrap(super(PixmapPacker, self).getDuplicateBorder())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getPages(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.PixmapPacker$Page> com.badlogic.gdx.graphics.g2d.PixmapPacker.getPages()"""
        return 'utils.Array'.__wrap(super(PixmapPacker, self).getPages())

    @overload
    def setPageHeight(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.PixmapPacker.setPageHeight(int)"""
        super(__PixmapPacker, self).setPageHeight(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'Format', arg3: int, arg4: bool):
        """public com.badlogic.gdx.graphics.g2d.PixmapPacker(int,int,com.badlogic.gdx.graphics.Pixmap$Format,int,boolean)"""
        val = __PixmapPacker(__int.valueOf(arg0), __int.valueOf(arg1), arg2, __int.valueOf(arg3), __boolean.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def sort(self, arg0: 'Array'):
        """public void com.badlogic.gdx.graphics.g2d.PixmapPacker.sort(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.Pixmap>)"""
        super(__PixmapPacker, self).sort(arg0)

    @override
    @overload
    def dispose(self):
        """public synchronized void com.badlogic.gdx.graphics.g2d.PixmapPacker.dispose()"""
        super(PixmapPacker, self).dispose()

    @overload
    def setPageWidth(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.PixmapPacker.setPageWidth(int)"""
        super(__PixmapPacker, self).setPageWidth(__int.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getPageWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.PixmapPacker.getPageWidth()"""
        return int.__wrap(super(PixmapPacker, self).getPageWidth())

    @overload
    def pack(self, arg0: 'Pixmap') -> 'math.Rectangle':
        """public synchronized com.badlogic.gdx.math.Rectangle com.badlogic.gdx.graphics.g2d.PixmapPacker.pack(com.badlogic.gdx.graphics.Pixmap)"""
        return 'math.Rectangle'.__wrap(super(__PixmapPacker, self).pack(arg0))

    @overload
    def getTransparentColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.PixmapPacker.getTransparentColor()"""
        return 'graphics.Color'.__wrap(super(PixmapPacker, self).getTransparentColor())

    @overload
    def getPageIndex(self, arg0: str) -> int:
        """public synchronized int com.badlogic.gdx.graphics.g2d.PixmapPacker.getPageIndex(java.lang.String)"""
        return int.__wrap(super(__PixmapPacker, self).getPageIndex(arg0))

    @overload
    def getPage(self, arg0: str) -> 'Page':
        """public synchronized com.badlogic.gdx.graphics.g2d.PixmapPacker$Page com.badlogic.gdx.graphics.g2d.PixmapPacker.getPage(java.lang.String)"""
        return 'Page'.__wrap(super(__PixmapPacker, self).getPage(arg0))

    @overload
    def setTransparentColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.PixmapPacker.setTransparentColor(com.badlogic.gdx.graphics.Color)"""
        super(__PixmapPacker, self).setTransparentColor(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def generateTextureAtlas(self, arg0: 'TextureFilter', arg1: 'TextureFilter', arg2: bool) -> 'TextureAtlas':
        """public synchronized com.badlogic.gdx.graphics.g2d.TextureAtlas com.badlogic.gdx.graphics.g2d.PixmapPacker.generateTextureAtlas(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,boolean)"""
        return 'TextureAtlas'.__wrap(super(__PixmapPacker, self).generateTextureAtlas(arg0, arg1, __boolean.valueOf(arg2)))

    @overload
    def setPackToTexture(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.PixmapPacker.setPackToTexture(boolean)"""
        super(__PixmapPacker, self).setPackToTexture(__boolean.valueOf(arg0))

    @overload
    def updateTextureAtlas(self, arg0: 'TextureAtlas', arg1: 'TextureFilter', arg2: 'TextureFilter', arg3: bool, arg4: bool):
        """public synchronized void com.badlogic.gdx.graphics.g2d.PixmapPacker.updateTextureAtlas(com.badlogic.gdx.graphics.g2d.TextureAtlas,com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,boolean,boolean)"""
        super(__PixmapPacker, self).updateTextureAtlas(arg0, arg1, arg2, __boolean.valueOf(arg3), __boolean.valueOf(arg4))

    @overload
    def updatePageTextures(self, arg0: 'TextureFilter', arg1: 'TextureFilter', arg2: bool):
        """public synchronized void com.badlogic.gdx.graphics.g2d.PixmapPacker.updatePageTextures(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,boolean)"""
        super(__PixmapPacker, self).updatePageTextures(arg0, arg1, __boolean.valueOf(arg2)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PixmapPacker$PackStrategy
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import com.badlogic.gdx.graphics.g2d.PixmapPacker as __PixmapPacker_PackStrategy
__PackStrategy = __PixmapPacker_PackStrategy.PackStrategy
from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

 
class PackStrategy(ABC):
    """com.badlogic.gdx.graphics.g2d.PixmapPacker.PackStrategy"""
 
    @staticmethod
    def __wrap(java_value: __PackStrategy) -> 'PackStrategy':
        return PackStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PackStrategy):
        """
        Dynamic initializer for PackStrategy.
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
 
    @abstractmethod
    def sort(self, arg0: 'Array'):
        """public abstract void com.badlogic.gdx.graphics.g2d.PixmapPacker$PackStrategy.sort(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.Pixmap>)"""
        pass

    @abstractmethod
    def pack(self, arg0: 'PixmapPacker', arg1: str, arg2: 'Rectangle'):
        """public abstract com.badlogic.gdx.graphics.g2d.PixmapPacker$Page com.badlogic.gdx.graphics.g2d.PixmapPacker$PackStrategy.pack(com.badlogic.gdx.graphics.g2d.PixmapPacker,java.lang.String,com.badlogic.gdx.math.Rectangle)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.files.FileHandle as __FileHandle
__FileHandle = __FileHandle
import java.lang.Character as __char
import java.lang.CharSequence as CharSequence
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from typing import List
import com.badlogic.gdx.graphics.g2d.BitmapFont as __BitmapFont_Glyph
__Glyph = __BitmapFont_Glyph.Glyph
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.g2d.BitmapFont as __BitmapFont_BitmapFontData
__BitmapFontData = __BitmapFont_BitmapFontData.BitmapFontData
from builtins import int
 
class BitmapFontData():
    """com.badlogic.gdx.graphics.g2d.BitmapFont.BitmapFontData"""
 
    @staticmethod
    def __wrap(java_value: __BitmapFontData) -> 'BitmapFontData':
        return BitmapFontData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BitmapFontData):
        """
        Dynamic initializer for BitmapFontData.
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
    def isWhitespace(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.isWhitespace(char)"""
        return bool.__wrap(super(__BitmapFontData, self).isWhitespace(__char.valueOf(arg0)))

    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.setScale(float)"""
        super(__BitmapFontData, self).setScale(__float.valueOf(arg0))

    @overload
    def setLineHeight(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.setLineHeight(float)"""
        super(__BitmapFontData, self).setLineHeight(__float.valueOf(arg0))

    @overload
    def load(self, arg0: 'FileHandle', arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.load(com.badlogic.gdx.files.FileHandle,boolean)"""
        super(__BitmapFontData, self).load(arg0, __boolean.valueOf(arg1))

    @overload
    def setGlyph(self, arg0: int, arg1: 'Glyph'):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.setGlyph(int,com.badlogic.gdx.graphics.g2d.BitmapFont$Glyph)"""
        super(__BitmapFontData, self).setGlyph(__int.valueOf(arg0), arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getImagePath(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.getImagePath(int)"""
        return str.__wrap(super(__BitmapFontData, self).getImagePath(__int.valueOf(arg0)))

    @overload
    def hasGlyph(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.hasGlyph(char)"""
        return bool.__wrap(super(__BitmapFontData, self).hasGlyph(__char.valueOf(arg0)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData()"""
        val = __BitmapFontData()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def scale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.scale(float)"""
        super(__BitmapFontData, self).scale(__float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getImagePaths(self) -> List[str]:
        """public java.lang.String[] com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.getImagePaths()"""
        return List[str].__wrap(super(BitmapFontData, self).getImagePaths())

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: bool):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData(com.badlogic.gdx.files.FileHandle,boolean)"""
        val = __BitmapFontData(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getGlyphs(self, arg0: 'GlyphRun', arg1: 'CharSequence', arg2: int, arg3: int, arg4: 'Glyph'):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.getGlyphs(com.badlogic.gdx.graphics.g2d.GlyphLayout$GlyphRun,java.lang.CharSequence,int,int,com.badlogic.gdx.graphics.g2d.BitmapFont$Glyph)"""
        super(__BitmapFontData, self).getGlyphs(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), arg4)

    @overload
    def setScale(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.setScale(float,float)"""
        super(__BitmapFontData, self).setScale(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def getGlyph(self, arg0: str) -> 'Glyph':
        """public com.badlogic.gdx.graphics.g2d.BitmapFont$Glyph com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.getGlyph(char)"""
        return 'Glyph'.__wrap(super(__BitmapFontData, self).getGlyph(__char.valueOf(arg0)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData()"""
        val = __BitmapFontData()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getWrapIndex(self, arg0: 'Array', arg1: int) -> int:
        """public int com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.getWrapIndex(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.BitmapFont$Glyph>,int)"""
        return int.__wrap(super(__BitmapFontData, self).getWrapIndex(arg0, __int.valueOf(arg1)))

    @overload
    def setGlyphRegion(self, arg0: 'Glyph', arg1: 'TextureRegion'):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.setGlyphRegion(com.badlogic.gdx.graphics.g2d.BitmapFont$Glyph,com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(__BitmapFontData, self).setGlyphRegion(arg0, arg1)

    @overload
    def isBreakChar(self, arg0: str) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.isBreakChar(char)"""
        return bool.__wrap(super(__BitmapFontData, self).isBreakChar(__char.valueOf(arg0)))

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
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.toString()"""
        return str.__wrap(super(BitmapFontData, self).toString())

    @overload
    def getFontFile(self) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.getFontFile()"""
        return 'files.FileHandle'.__wrap(super(BitmapFontData, self).getFontFile())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getFirstGlyph(self) -> 'Glyph':
        """public com.badlogic.gdx.graphics.g2d.BitmapFont$Glyph com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData.getFirstGlyph()"""
        return 'Glyph'.__wrap(super(BitmapFontData, self).getFirstGlyph()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PolygonRegionLoader
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.files.FileHandle as __FileHandle
__FileHandle = __FileHandle
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g2d.PolygonRegion as __PolygonRegion
__PolygonRegion = __PolygonRegion
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g2d.PolygonRegionLoader as __PolygonRegionLoader
__PolygonRegionLoader = __PolygonRegionLoader
try:
    from pygdx.assets import loaders
except ImportError:
    loaders = __import_once__("pygdx.assets.loaders")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.assets.loaders.AssetLoader as __AssetLoader
__AssetLoader = __AssetLoader
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PolygonRegionLoader():
    """com.badlogic.gdx.graphics.g2d.PolygonRegionLoader"""
 
    @staticmethod
    def __wrap(java_value: __PolygonRegionLoader) -> 'PolygonRegionLoader':
        return PolygonRegionLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PolygonRegionLoader):
        """
        Dynamic initializer for PolygonRegionLoader.
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
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'.__wrap(super(__loaders.AssetLoader, self).resolve(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.PolygonRegionLoader()"""
        val = __PolygonRegionLoader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def load(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'PolygonRegionParameters') -> 'PolygonRegion':
        """public com.badlogic.gdx.graphics.g2d.PolygonRegion com.badlogic.gdx.graphics.g2d.PolygonRegionLoader.load(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g2d.PolygonRegionLoader$PolygonRegionParameters)"""
        return 'PolygonRegion'.__wrap(super(__PolygonRegionLoader, self).load(arg0, arg1, arg2, arg3))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.PolygonRegionLoader()"""
        val = __PolygonRegionLoader()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def load(self, arg0: 'TextureRegion', arg1: 'FileHandle') -> 'PolygonRegion':
        """public com.badlogic.gdx.graphics.g2d.PolygonRegion com.badlogic.gdx.graphics.g2d.PolygonRegionLoader.load(com.badlogic.gdx.graphics.g2d.TextureRegion,com.badlogic.gdx.files.FileHandle)"""
        return 'PolygonRegion'.__wrap(super(__PolygonRegionLoader, self).load(arg0, arg1))

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
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'PolygonRegionParameters') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.graphics.g2d.PolygonRegionLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g2d.PolygonRegionLoader$PolygonRegionParameters)"""
        return 'utils.Array'.__wrap(super(__PolygonRegionLoader, self).getDependencies(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.graphics.g2d.PolygonRegionLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = __PolygonRegionLoader(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEffectPool$PooledEffect
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter
__ParticleEmitter = __ParticleEmitter
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
try:
    from pygdx.math import collision
except ImportError:
    collision = __import_once__("pygdx.math.collision")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g2d.ParticleEffectPool as __ParticleEffectPool_PooledEffect
__PooledEffect = __ParticleEffectPool_PooledEffect.PooledEffect
import com.badlogic.gdx.graphics.g2d.ParticleEffect as __ParticleEffect
__ParticleEffect = __ParticleEffect
import com.badlogic.gdx.math.collision.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PooledEffect():
    """com.badlogic.gdx.graphics.g2d.ParticleEffectPool.PooledEffect"""
 
    @staticmethod
    def __wrap(java_value: __PooledEffect) -> 'PooledEffect':
        return PooledEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PooledEffect):
        """
        Dynamic initializer for PooledEffect.
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
    def start(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.start()"""
        super(ParticleEffect, self).start()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.dispose()"""
        super(ParticleEffect, self).dispose()

    @override
    @overload
    def save(self, arg0: 'Writer'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.save(java.io.Writer) throws java.io.IOException"""
        super(__ParticleEffect, self).save(arg0)

    @override
    @overload
    def scaleEffect(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.scaleEffect(float,float,float)"""
        super(__ParticleEffect, self).scaleEffect(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def scaleEffect(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.scaleEffect(float)"""
        super(__ParticleEffect, self).scaleEffect(__float.valueOf(arg0))

    @override
    @overload
    def flipY(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.flipY()"""
        super(ParticleEffect, self).flipY()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def draw(self, arg0: 'Batch'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.draw(com.badlogic.gdx.graphics.g2d.Batch)"""
        super(__ParticleEffect, self).draw(arg0)

    @override
    @overload
    def setFlip(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.setFlip(boolean,boolean)"""
        super(__ParticleEffect, self).setFlip(__boolean.valueOf(arg0), __boolean.valueOf(arg1))

    @override
    @overload
    def loadEmitterImages(self, arg0: 'TextureAtlas', arg1: str):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.loadEmitterImages(com.badlogic.gdx.graphics.g2d.TextureAtlas,java.lang.String)"""
        super(__ParticleEffect, self).loadEmitterImages(arg0, arg1)

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
    def update(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.update(float)"""
        super(__ParticleEffect, self).update(__float.valueOf(arg0))

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEffect.isComplete()"""
        return bool.__wrap(super(ParticleEffect, self).isComplete())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def loadEmitterImages(self, arg0: 'TextureAtlas'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.loadEmitterImages(com.badlogic.gdx.graphics.g2d.TextureAtlas)"""
        super(__ParticleEffect, self).loadEmitterImages(arg0)

    @override
    @overload
    def loadEmitterImages(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.loadEmitterImages(com.badlogic.gdx.files.FileHandle)"""
        super(__ParticleEffect, self).loadEmitterImages(arg0)

    @override
    @overload
    def allowCompletion(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.allowCompletion()"""
        super(ParticleEffect, self).allowCompletion()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def findEmitter(self, arg0: str) -> 'ParticleEmitter':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter com.badlogic.gdx.graphics.g2d.ParticleEffect.findEmitter(java.lang.String)"""
        return 'ParticleEmitter'.__wrap(super(__ParticleEffect, self).findEmitter(arg0))

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.draw(com.badlogic.gdx.graphics.g2d.Batch,float)"""
        super(__ParticleEffect, self).draw(arg0, __float.valueOf(arg1))

    @override
    @overload
    def setDuration(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.setDuration(int)"""
        super(__ParticleEffect, self).setDuration(__int.valueOf(arg0))

    @override
    @overload
    def loadEmitters(self, arg0: 'FileHandle'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.loadEmitters(com.badlogic.gdx.files.FileHandle)"""
        super(__ParticleEffect, self).loadEmitters(arg0)

    @override
    @overload
    def load(self, arg0: 'FileHandle', arg1: 'TextureAtlas'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.load(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g2d.TextureAtlas)"""
        super(__ParticleEffect, self).load(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def free(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffectPool$PooledEffect.free()"""
        super(PooledEffect, self).free()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def scaleEffect(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.scaleEffect(float,float)"""
        super(__ParticleEffect, self).scaleEffect(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def setEmittersCleanUpBlendFunction(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.setEmittersCleanUpBlendFunction(boolean)"""
        super(__ParticleEffect, self).setEmittersCleanUpBlendFunction(__boolean.valueOf(arg0))

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.setPosition(float,float)"""
        super(__ParticleEffect, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getBoundingBox(self) -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g2d.ParticleEffect.getBoundingBox()"""
        return 'collision.BoundingBox'.__wrap(super(ParticleEffect, self).getBoundingBox())

    @override
    @overload
    def load(self, arg0: 'FileHandle', arg1: 'TextureAtlas', arg2: str):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.load(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g2d.TextureAtlas,java.lang.String)"""
        super(__ParticleEffect, self).load(arg0, arg1, arg2)

    @override
    @overload
    def getEmitters(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.ParticleEmitter> com.badlogic.gdx.graphics.g2d.ParticleEffect.getEmitters()"""
        return 'utils.Array'.__wrap(super(ParticleEffect, self).getEmitters())

    @override
    @overload
    def load(self, arg0: 'FileHandle', arg1: 'FileHandle'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.load(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        super(__ParticleEffect, self).load(arg0, arg1)

    @override
    @overload
    def preAllocateParticles(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.preAllocateParticles()"""
        super(ParticleEffect, self).preAllocateParticles()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.reset()"""
        super(ParticleEffect, self).reset()

    @override
    @overload
    def reset(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffect.reset(boolean)"""
        super(__ParticleEffect, self).reset(__boolean.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.BitmapFont
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
import java.lang.Boolean as __boolean
from builtins import type
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __string
import com.badlogic.gdx.graphics.g2d.BitmapFontCache as __BitmapFontCache
__BitmapFontCache = __BitmapFontCache
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

from builtins import bool
import com.badlogic.gdx.graphics.g2d.GlyphLayout as __GlyphLayout
__GlyphLayout = __GlyphLayout
from builtins import str
import java.lang.CharSequence as CharSequence
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
import com.badlogic.gdx.graphics.g2d.TextureRegion as __TextureRegion
__TextureRegion = __TextureRegion
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

import com.badlogic.gdx.graphics.g2d.BitmapFont as __BitmapFont_BitmapFontData
__BitmapFontData = __BitmapFont_BitmapFontData.BitmapFontData
import com.badlogic.gdx.graphics.g2d.BitmapFont as __BitmapFont
__BitmapFont = __BitmapFont
from builtins import int
 
class BitmapFont():
    """com.badlogic.gdx.graphics.g2d.BitmapFont"""
 
    @staticmethod
    def __wrap(java_value: __BitmapFont) -> 'BitmapFont':
        return BitmapFont(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BitmapFont):
        """
        Dynamic initializer for BitmapFont.
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
    def __init__(self, arg0: 'BitmapFontData', arg1: 'Array', arg2: bool):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont(com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.TextureRegion>,boolean)"""
        val = __BitmapFont(arg0, arg1, __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont()"""
        val = __BitmapFont()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle', arg2: bool):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,boolean)"""
        val = __BitmapFont(arg0, arg1, __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle', arg2: bool, arg3: bool):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,boolean,boolean)"""
        val = __BitmapFont(arg0, arg1, __boolean.valueOf(arg2), __boolean.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getRegion(self, arg0: int) -> 'TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.graphics.g2d.BitmapFont.getRegion(int)"""
        return 'TextureRegion'.__wrap(super(__BitmapFont, self).getRegion(__int.valueOf(arg0)))

    @overload
    def isFlipped(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.BitmapFont.isFlipped()"""
        return bool.__wrap(super(BitmapFont, self).isFlipped())

    @overload
    def getSpaceXadvance(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getSpaceXadvance()"""
        return float.__wrap(super(BitmapFont, self).getSpaceXadvance())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getScaleY()"""
        return float.__wrap(super(BitmapFont, self).getScaleY())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def draw(self, arg0: 'Batch', arg1: 'CharSequence', arg2: float, arg3: float, arg4: int, arg5: int, arg6: float, arg7: int, arg8: bool) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFont.draw(com.badlogic.gdx.graphics.g2d.Batch,java.lang.CharSequence,float,float,int,int,float,int,boolean)"""
        return 'GlyphLayout'.__wrap(super(__BitmapFont, self).draw(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __float.valueOf(arg6), __int.valueOf(arg7), __boolean.valueOf(arg8)))

    @overload
    def getCache(self) -> 'BitmapFontCache':
        """public com.badlogic.gdx.graphics.g2d.BitmapFontCache com.badlogic.gdx.graphics.g2d.BitmapFont.getCache()"""
        return 'BitmapFontCache'.__wrap(super(BitmapFont, self).getCache())

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__BitmapFont, self).setColor(arg0)

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'TextureRegion', arg2: bool):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g2d.TextureRegion,boolean)"""
        val = __BitmapFont(arg0, arg1, __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getRegion(self) -> 'TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.graphics.g2d.BitmapFont.getRegion()"""
        return 'TextureRegion'.__wrap(super(BitmapFont, self).getRegion())

    @overload
    def __init__(self, arg0: bool):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont(boolean)"""
        val = __BitmapFont(__boolean.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def draw(self, arg0: 'Batch', arg1: 'GlyphLayout', arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.draw(com.badlogic.gdx.graphics.g2d.Batch,com.badlogic.gdx.graphics.g2d.GlyphLayout,float,float)"""
        super(__BitmapFont, self).draw(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def __init__(self, arg0: 'BitmapFontData', arg1: 'TextureRegion', arg2: bool):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont(com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData,com.badlogic.gdx.graphics.g2d.TextureRegion,boolean)"""
        val = __BitmapFont(arg0, arg1, __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont()"""
        val = __BitmapFont()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def draw(self, arg0: 'Batch', arg1: 'CharSequence', arg2: float, arg3: float) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFont.draw(com.badlogic.gdx.graphics.g2d.Batch,java.lang.CharSequence,float,float)"""
        return 'GlyphLayout'.__wrap(super(__BitmapFont, self).draw(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: bool):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont(com.badlogic.gdx.files.FileHandle,boolean)"""
        val = __BitmapFont(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getScaleX()"""
        return float.__wrap(super(BitmapFont, self).getScaleX())

    @overload
    def getDescent(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getDescent()"""
        return float.__wrap(super(BitmapFont, self).getDescent())

    @overload
    def getXHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getXHeight()"""
        return float.__wrap(super(BitmapFont, self).getXHeight())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getCapHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getCapHeight()"""
        return float.__wrap(super(BitmapFont, self).getCapHeight())

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.setColor(float,float,float,float)"""
        super(__BitmapFont, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def setUseIntegerPositions(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.setUseIntegerPositions(boolean)"""
        super(__BitmapFont, self).setUseIntegerPositions(__boolean.valueOf(arg0))

    @overload
    def getRegions(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.TextureRegion> com.badlogic.gdx.graphics.g2d.BitmapFont.getRegions()"""
        return 'utils.Array'.__wrap(super(BitmapFont, self).getRegions())

    @overload
    def setOwnsTexture(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.setOwnsTexture(boolean)"""
        super(__BitmapFont, self).setOwnsTexture(__boolean.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g2d.BitmapFont.toString()"""
        return str.__wrap(super(BitmapFont, self).toString())

    @overload
    def draw(self, arg0: 'Batch', arg1: 'CharSequence', arg2: float, arg3: float, arg4: float, arg5: int, arg6: bool) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFont.draw(com.badlogic.gdx.graphics.g2d.Batch,java.lang.CharSequence,float,float,float,int,boolean)"""
        return 'GlyphLayout'.__wrap(super(__BitmapFont, self).draw(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5), __boolean.valueOf(arg6)))

    @overload
    def getAscent(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getAscent()"""
        return float.__wrap(super(BitmapFont, self).getAscent())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def usesIntegerPositions(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.BitmapFont.usesIntegerPositions()"""
        return bool.__wrap(super(BitmapFont, self).usesIntegerPositions())

    @overload
    def getData(self) -> 'BitmapFontData':
        """public com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData com.badlogic.gdx.graphics.g2d.BitmapFont.getData()"""
        return 'BitmapFontData'.__wrap(super(BitmapFont, self).getData())

    @overload
    def getLineHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getLineHeight()"""
        return float.__wrap(super(BitmapFont, self).getLineHeight())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.dispose()"""
        super(BitmapFont, self).dispose()

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.BitmapFont.getColor()"""
        return 'graphics.Color'.__wrap(super(BitmapFont, self).getColor())

    @overload
    def draw(self, arg0: 'Batch', arg1: 'CharSequence', arg2: float, arg3: float, arg4: int, arg5: int, arg6: float, arg7: int, arg8: bool, arg9: str) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFont.draw(com.badlogic.gdx.graphics.g2d.Batch,java.lang.CharSequence,float,float,int,int,float,int,boolean,java.lang.String)"""
        return 'GlyphLayout'.__wrap(super(__BitmapFont, self).draw(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __float.valueOf(arg6), __int.valueOf(arg7), __boolean.valueOf(arg8), arg9))

    @overload
    def ownsTexture(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.BitmapFont.ownsTexture()"""
        return bool.__wrap(super(BitmapFont, self).ownsTexture())

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
    def setFixedWidthGlyphs(self, arg0: 'CharSequence'):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.setFixedWidthGlyphs(java.lang.CharSequence)"""
        super(__BitmapFont, self).setFixedWidthGlyphs(arg0)

    @overload
    def newFontCache(self) -> 'BitmapFontCache':
        """public com.badlogic.gdx.graphics.g2d.BitmapFontCache com.badlogic.gdx.graphics.g2d.BitmapFont.newFontCache()"""
        return 'BitmapFontCache'.__wrap(super(BitmapFont, self).newFontCache())

    @overload
    def __init__(self, arg0: 'FileHandle'):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont(com.badlogic.gdx.files.FileHandle)"""
        val = __BitmapFont(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'TextureRegion'):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = __BitmapFont(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEffectPool
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import com.badlogic.gdx.graphics.g2d.ParticleEffectPool as __ParticleEffectPool
__ParticleEffectPool = __ParticleEffectPool
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Pool as __Pool
__Pool = __Pool
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ParticleEffectPool():
    """com.badlogic.gdx.graphics.g2d.ParticleEffectPool"""
 
    @staticmethod
    def __wrap(java_value: __ParticleEffectPool) -> 'ParticleEffectPool':
        return ParticleEffectPool(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleEffectPool):
        """
        Dynamic initializer for ParticleEffectPool.
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
    def clear(self):
        """public void com.badlogic.gdx.utils.Pool.clear()"""
        super(utils.Pool, self).clear()

    @overload
    def free(self, arg0: 'PooledEffect'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEffectPool.free(com.badlogic.gdx.graphics.g2d.ParticleEffectPool$PooledEffect)"""
        super(__ParticleEffectPool, self).free(arg0)

    @override
    @overload
    def freeAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.utils.Pool.freeAll(com.badlogic.gdx.utils.Array<T>)"""
        super(__utils.Pool, self).freeAll(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def fill(self, arg0: int):
        """public void com.badlogic.gdx.utils.Pool.fill(int)"""
        super(__utils.Pool, self).fill(__int.valueOf(arg0))

    @override
    @overload
    def getFree(self) -> int:
        """public int com.badlogic.gdx.utils.Pool.getFree()"""
        return int.__wrap(super(utils.Pool, self).getFree())

    @overload
    def __init__(self, arg0: 'ParticleEffect', arg1: int, arg2: int):
        """public com.badlogic.gdx.graphics.g2d.ParticleEffectPool(com.badlogic.gdx.graphics.g2d.ParticleEffect,int,int)"""
        val = __ParticleEffectPool(arg0, __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def obtain(self) -> object:
        """public T com.badlogic.gdx.utils.Pool.obtain()"""
        return object.__wrap(super(utils.Pool, self).obtain())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_ParticleValue
__ParticleValue = __ParticleEmitter_ParticleValue.ParticleValue
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_SpawnShapeValue
__SpawnShapeValue = __ParticleEmitter_SpawnShapeValue.SpawnShapeValue
import java.io.BufferedReader as BufferedReader
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_SpawnShape
__SpawnShape = __ParticleEmitter_SpawnShape.SpawnShape
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_SpawnEllipseSide
__SpawnEllipseSide = __ParticleEmitter_SpawnEllipseSide.SpawnEllipseSide
from builtins import int
 
class SpawnShapeValue():
    """com.badlogic.gdx.graphics.g2d.ParticleEmitter.SpawnShapeValue"""
 
    @staticmethod
    def __wrap(java_value: __SpawnShapeValue) -> 'SpawnShapeValue':
        return SpawnShapeValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SpawnShapeValue):
        """
        Dynamic initializer for SpawnShapeValue.
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
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isActive()"""
        return bool.__wrap(super(ParticleValue, self).isActive())

    @overload
    def load(self, arg0: 'SpawnShapeValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue)"""
        super(__SpawnShapeValue, self).load(arg0)

    @overload
    def getShape(self) -> 'SpawnShape':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShape com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue.getShape()"""
        return 'SpawnShape'.__wrap(super(SpawnShapeValue, self).getShape())

    @overload
    def isEdges(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue.isEdges()"""
        return bool.__wrap(super(SpawnShapeValue, self).isEdges())

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue)"""
        super(__ParticleValue, self).load(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getSide(self) -> 'SpawnEllipseSide':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnEllipseSide com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue.getSide()"""
        return 'SpawnEllipseSide'.__wrap(super(SpawnShapeValue, self).getSide())

    @overload
    def setEdges(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue.setEdges(boolean)"""
        super(__SpawnShapeValue, self).setEdges(__boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue()"""
        val = __SpawnShapeValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setAlwaysActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setAlwaysActive(boolean)"""
        super(__ParticleValue, self).setAlwaysActive(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setSide(self, arg0: 'SpawnEllipseSide'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue.setSide(com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnEllipseSide)"""
        super(__SpawnShapeValue, self).setSide(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setActive(boolean)"""
        super(__ParticleValue, self).setActive(__boolean.valueOf(arg0))

    @override
    @overload
    def load(self, arg0: 'BufferedReader'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue.load(java.io.BufferedReader) throws java.io.IOException"""
        super(__SpawnShapeValue, self).load(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue()"""
        val = __SpawnShapeValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setShape(self, arg0: 'SpawnShape'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue.setShape(com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShape)"""
        super(__SpawnShapeValue, self).setShape(arg0)

    @override
    @overload
    def isAlwaysActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isAlwaysActive()"""
        return bool.__wrap(super(ParticleValue, self).isAlwaysActive())

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
    def save(self, arg0: 'Writer'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue.save(java.io.Writer) throws java.io.IOException"""
        super(__SpawnShapeValue, self).save(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import com.badlogic.gdx.graphics.glutils.ShaderProgram as __ShaderProgram
__ShaderProgram = __ShaderProgram
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch as __PolygonSpriteBatch
__PolygonSpriteBatch = __PolygonSpriteBatch
from builtins import float
import com.badlogic.gdx.math.Matrix4 as __Matrix4
__Matrix4 = __Matrix4
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class PolygonSpriteBatch():
    """com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch"""
 
    @staticmethod
    def __wrap(java_value: __PolygonSpriteBatch) -> 'PolygonSpriteBatch':
        return PolygonSpriteBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PolygonSpriteBatch):
        """
        Dynamic initializer for PolygonSpriteBatch.
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
    def begin(self):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.begin()"""
        super(PolygonSpriteBatch, self).begin()

    @override
    @overload
    def enableBlending(self):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.enableBlending()"""
        super(PolygonSpriteBatch, self).enableBlending()

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: 'ShaderProgram'):
        """public com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch(int,int,com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        val = __PolygonSpriteBatch(__int.valueOf(arg0), __int.valueOf(arg1), arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isDrawing(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.isDrawing()"""
        return bool.__wrap(super(PolygonSpriteBatch, self).isDrawing())

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: 'Affine2'):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,com.badlogic.gdx.math.Affine2)"""
        super(__PolygonSpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: 'float', arg2: int, arg3: int, arg4: 'short', arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float[],int,int,short[],int,int)"""
        super(__PolygonSpriteBatch, self).draw(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), arg4, __int.valueOf(arg5), __int.valueOf(arg6))

    @override
    @overload
    def setBlendFunctionSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.setBlendFunctionSeparate(int,int,int,int)"""
        super(__PolygonSpriteBatch, self).setBlendFunctionSeparate(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def flush(self):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.flush()"""
        super(PolygonSpriteBatch, self).flush()

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float)"""
        super(__PolygonSpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def disableBlending(self):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.disableBlending()"""
        super(PolygonSpriteBatch, self).disableBlending()

    @override
    @overload
    def isBlendingEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.isBlendingEnabled()"""
        return bool.__wrap(super(PolygonSpriteBatch, self).isBlendingEnabled())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch(int)"""
        val = __PolygonSpriteBatch(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float)"""
        super(__PolygonSpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: bool):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,float,float,float,float,boolean)"""
        super(__PolygonSpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __boolean.valueOf(arg10))

    @override
    @overload
    def getBlendDstFuncAlpha(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getBlendDstFuncAlpha()"""
        return int.__wrap(super(PolygonSpriteBatch, self).getBlendDstFuncAlpha())

    @override
    @overload
    def setShader(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.setShader(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(__PolygonSpriteBatch, self).setShader(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getProjectionMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getProjectionMatrix()"""
        return 'math.Matrix4'.__wrap(super(PolygonSpriteBatch, self).getProjectionMatrix())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setPackedColor(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.setPackedColor(float)"""
        super(__PolygonSpriteBatch, self).setPackedColor(__float.valueOf(arg0))

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float)"""
        super(__PolygonSpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.dispose()"""
        super(PolygonSpriteBatch, self).dispose()

    @override
    @overload
    def draw(self, arg0: 'PolygonRegion', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.PolygonRegion,float,float,float,float)"""
        super(__PolygonSpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.setColor(float,float,float,float)"""
        super(__PolygonSpriteBatch, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def draw(self, arg0: 'PolygonRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.PolygonRegion,float,float,float,float,float,float,float,float,float)"""
        super(__PolygonSpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9))

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getColor()"""
        return 'graphics.Color'.__wrap(super(PolygonSpriteBatch, self).getColor())

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,int,int,int,int)"""
        super(__PolygonSpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getShader(self) -> 'glutils.ShaderProgram':
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getShader()"""
        return 'glutils.ShaderProgram'.__wrap(super(PolygonSpriteBatch, self).getShader())

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,float,float,float,float)"""
        super(__PolygonSpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float)"""
        super(__PolygonSpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8))

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: int, arg11: int, arg12: int, arg13: int, arg14: bool, arg15: bool):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float,float,int,int,int,int,boolean,boolean)"""
        super(__PolygonSpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __boolean.valueOf(arg14), __boolean.valueOf(arg15))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch()"""
        val = __PolygonSpriteBatch()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setTransformMatrix(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.setTransformMatrix(com.badlogic.gdx.math.Matrix4)"""
        super(__PolygonSpriteBatch, self).setTransformMatrix(arg0)

    @override
    @overload
    def draw(self, arg0: 'PolygonRegion', arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.PolygonRegion,float,float)"""
        super(__PolygonSpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__PolygonSpriteBatch, self).setColor(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setProjectionMatrix(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.setProjectionMatrix(com.badlogic.gdx.math.Matrix4)"""
        super(__PolygonSpriteBatch, self).setProjectionMatrix(arg0)

    @override
    @overload
    def setBlendFunction(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.setBlendFunction(int,int)"""
        super(__PolygonSpriteBatch, self).setBlendFunction(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getBlendSrcFunc(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getBlendSrcFunc()"""
        return int.__wrap(super(PolygonSpriteBatch, self).getBlendSrcFunc())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch()"""
        val = __PolygonSpriteBatch()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: bool):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,int,int,int,int,boolean,boolean)"""
        super(__PolygonSpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __boolean.valueOf(arg9), __boolean.valueOf(arg10))

    @override
    @overload
    def getTransformMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getTransformMatrix()"""
        return 'math.Matrix4'.__wrap(super(PolygonSpriteBatch, self).getTransformMatrix())

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float[],int,int)"""
        super(__PolygonSpriteBatch, self).draw(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: 'ShaderProgram'):
        """public com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch(int,com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        val = __PolygonSpriteBatch(__int.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def getPackedColor(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getPackedColor()"""
        return float.__wrap(super(PolygonSpriteBatch, self).getPackedColor())

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float)"""
        super(__PolygonSpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def getBlendSrcFuncAlpha(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getBlendSrcFuncAlpha()"""
        return int.__wrap(super(PolygonSpriteBatch, self).getBlendSrcFuncAlpha())

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.end()"""
        super(PolygonSpriteBatch, self).end()

    @override
    @overload
    def getBlendDstFunc(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch.getBlendDstFunc()"""
        return int.__wrap(super(PolygonSpriteBatch, self).getBlendDstFunc()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PixmapPacker$GuillotineStrategy
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
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g2d.PixmapPacker as __PixmapPacker_GuillotineStrategy
__GuillotineStrategy = __PixmapPacker_GuillotineStrategy.GuillotineStrategy
import com.badlogic.gdx.graphics.g2d.PixmapPacker as __PixmapPacker_Page
__Page = __PixmapPacker_Page.Page
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GuillotineStrategy():
    """com.badlogic.gdx.graphics.g2d.PixmapPacker.GuillotineStrategy"""
 
    @staticmethod
    def __wrap(java_value: __GuillotineStrategy) -> 'GuillotineStrategy':
        return GuillotineStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GuillotineStrategy):
        """
        Dynamic initializer for GuillotineStrategy.
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
    def sort(self, arg0: 'Array'):
        """public void com.badlogic.gdx.graphics.g2d.PixmapPacker$GuillotineStrategy.sort(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.Pixmap>)"""
        super(__GuillotineStrategy, self).sort(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.PixmapPacker$GuillotineStrategy()"""
        val = __GuillotineStrategy()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def pack(self, arg0: 'PixmapPacker', arg1: str, arg2: 'Rectangle') -> 'Page':
        """public com.badlogic.gdx.graphics.g2d.PixmapPacker$Page com.badlogic.gdx.graphics.g2d.PixmapPacker$GuillotineStrategy.pack(com.badlogic.gdx.graphics.g2d.PixmapPacker,java.lang.String,com.badlogic.gdx.math.Rectangle)"""
        return 'Page'.__wrap(super(__GuillotineStrategy, self).pack(arg0, arg1, arg2))

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.PixmapPacker$GuillotineStrategy()"""
        val = __GuillotineStrategy()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PixmapPacker$SkylineStrategy
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
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g2d.PixmapPacker as __PixmapPacker_Page
__Page = __PixmapPacker_Page.Page
import com.badlogic.gdx.graphics.g2d.PixmapPacker as __PixmapPacker_SkylineStrategy
__SkylineStrategy = __PixmapPacker_SkylineStrategy.SkylineStrategy
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SkylineStrategy():
    """com.badlogic.gdx.graphics.g2d.PixmapPacker.SkylineStrategy"""
 
    @staticmethod
    def __wrap(java_value: __SkylineStrategy) -> 'SkylineStrategy':
        return SkylineStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SkylineStrategy):
        """
        Dynamic initializer for SkylineStrategy.
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
    def pack(self, arg0: 'PixmapPacker', arg1: str, arg2: 'Rectangle') -> 'Page':
        """public com.badlogic.gdx.graphics.g2d.PixmapPacker$Page com.badlogic.gdx.graphics.g2d.PixmapPacker$SkylineStrategy.pack(com.badlogic.gdx.graphics.g2d.PixmapPacker,java.lang.String,com.badlogic.gdx.math.Rectangle)"""
        return 'Page'.__wrap(super(__SkylineStrategy, self).pack(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def sort(self, arg0: 'Array'):
        """public void com.badlogic.gdx.graphics.g2d.PixmapPacker$SkylineStrategy.sort(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.Pixmap>)"""
        super(__SkylineStrategy, self).sort(arg0)

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.PixmapPacker$SkylineStrategy()"""
        val = __SkylineStrategy()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
        """public com.badlogic.gdx.graphics.g2d.PixmapPacker$SkylineStrategy()"""
        val = __SkylineStrategy()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.Animation
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.graphics.g2d.Animation as __Animation
__Animation = __Animation
import com.badlogic.gdx.graphics.g2d.Animation as __Animation_PlayMode
__PlayMode = __Animation_PlayMode.PlayMode
from builtins import object
from typing import List
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Animation():
    """com.badlogic.gdx.graphics.g2d.Animation"""
 
    @staticmethod
    def __wrap(java_value: __Animation) -> 'Animation':
        return Animation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Animation):
        """
        Dynamic initializer for Animation.
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
    def getKeyFrames(self) -> List[object]:
        """public T[] com.badlogic.gdx.graphics.g2d.Animation.getKeyFrames()"""
        return List[object].__wrap(super(Animation, self).getKeyFrames())

    @overload
    def getPlayMode(self) -> 'PlayMode':
        """public com.badlogic.gdx.graphics.g2d.Animation$PlayMode com.badlogic.gdx.graphics.g2d.Animation.getPlayMode()"""
        return 'PlayMode'.__wrap(super(Animation, self).getPlayMode())

    @overload
    def getAnimationDuration(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Animation.getAnimationDuration()"""
        return float.__wrap(super(Animation, self).getAnimationDuration())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: float, *arg1: object):
        """public com.badlogic.gdx.graphics.g2d.Animation(float,T...)"""
        val = __Animation(__float.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isAnimationFinished(self, arg0: float) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.Animation.isAnimationFinished(float)"""
        return bool.__wrap(super(__Animation, self).isAnimationFinished(__float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: float, arg1: 'Array'):
        """public com.badlogic.gdx.graphics.g2d.Animation(float,com.badlogic.gdx.utils.Array<? extends T>)"""
        val = __Animation(__float.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: float, arg1: 'Array', arg2: 'PlayMode'):
        """public com.badlogic.gdx.graphics.g2d.Animation(float,com.badlogic.gdx.utils.Array<? extends T>,com.badlogic.gdx.graphics.g2d.Animation$PlayMode)"""
        val = __Animation(__float.valueOf(arg0), arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getKeyFrame(self, arg0: float, arg1: bool) -> object:
        """public T com.badlogic.gdx.graphics.g2d.Animation.getKeyFrame(float,boolean)"""
        return object.__wrap(super(__Animation, self).getKeyFrame(__float.valueOf(arg0), __boolean.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getKeyFrame(self, arg0: float) -> object:
        """public T com.badlogic.gdx.graphics.g2d.Animation.getKeyFrame(float)"""
        return object.__wrap(super(__Animation, self).getKeyFrame(__float.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setFrameDuration(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Animation.setFrameDuration(float)"""
        super(__Animation, self).setFrameDuration(__float.valueOf(arg0))

    @overload
    def getFrameDuration(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Animation.getFrameDuration()"""
        return float.__wrap(super(Animation, self).getFrameDuration())

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
    def getKeyFrameIndex(self, arg0: float) -> int:
        """public int com.badlogic.gdx.graphics.g2d.Animation.getKeyFrameIndex(float)"""
        return int.__wrap(super(__Animation, self).getKeyFrameIndex(__float.valueOf(arg0)))

    @overload
    def setPlayMode(self, arg0: 'PlayMode'):
        """public void com.badlogic.gdx.graphics.g2d.Animation.setPlayMode(com.badlogic.gdx.graphics.g2d.Animation$PlayMode)"""
        super(__Animation, self).setPlayMode(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShape
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
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_SpawnShape
__SpawnShape = __ParticleEmitter_SpawnShape.SpawnShape
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class SpawnShape():
    """com.badlogic.gdx.graphics.g2d.ParticleEmitter.SpawnShape"""
 
    @staticmethod
    def __wrap(java_value: __SpawnShape) -> 'SpawnShape':
        return SpawnShape(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SpawnShape):
        """
        Dynamic initializer for SpawnShape.
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
    def values() -> List['SpawnShape']:
        """public static com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShape[] com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShape.values()"""
        return List[SpawnShape].__wrap(__SpawnShape.values())

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
    def valueOf(arg0: str) -> 'SpawnShape':
        """public static com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShape com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShape.valueOf(java.lang.String)"""
        return SpawnShape.__wrap(__SpawnShape.valueOf(arg0))

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
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.GlyphLayout
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.g2d.GlyphLayout as __GlyphLayout
__GlyphLayout = __GlyphLayout
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
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
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class GlyphLayout():
    """com.badlogic.gdx.graphics.g2d.GlyphLayout"""
 
    @staticmethod
    def __wrap(java_value: __GlyphLayout) -> 'GlyphLayout':
        return GlyphLayout(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GlyphLayout):
        """
        Dynamic initializer for GlyphLayout.
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
        """public java.lang.String com.badlogic.gdx.graphics.g2d.GlyphLayout.toString()"""
        return str.__wrap(super(GlyphLayout, self).toString())

    @overload
    def setText(self, arg0: 'BitmapFont', arg1: 'CharSequence', arg2: int, arg3: int, arg4: 'Color', arg5: float, arg6: int, arg7: bool, arg8: str):
        """public void com.badlogic.gdx.graphics.g2d.GlyphLayout.setText(com.badlogic.gdx.graphics.g2d.BitmapFont,java.lang.CharSequence,int,int,com.badlogic.gdx.graphics.Color,float,int,boolean,java.lang.String)"""
        super(__GlyphLayout, self).setText(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), arg4, __float.valueOf(arg5), __int.valueOf(arg6), __boolean.valueOf(arg7), arg8)

    @overload
    def __init__(self, arg0: 'BitmapFont', arg1: 'CharSequence'):
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout(com.badlogic.gdx.graphics.g2d.BitmapFont,java.lang.CharSequence)"""
        val = __GlyphLayout(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout()"""
        val = __GlyphLayout()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setText(self, arg0: 'BitmapFont', arg1: 'CharSequence', arg2: 'Color', arg3: float, arg4: int, arg5: bool):
        """public void com.badlogic.gdx.graphics.g2d.GlyphLayout.setText(com.badlogic.gdx.graphics.g2d.BitmapFont,java.lang.CharSequence,com.badlogic.gdx.graphics.Color,float,int,boolean)"""
        super(__GlyphLayout, self).setText(arg0, arg1, arg2, __float.valueOf(arg3), __int.valueOf(arg4), __boolean.valueOf(arg5))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'BitmapFont', arg1: 'CharSequence', arg2: 'Color', arg3: float, arg4: int, arg5: bool):
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout(com.badlogic.gdx.graphics.g2d.BitmapFont,java.lang.CharSequence,com.badlogic.gdx.graphics.Color,float,int,boolean)"""
        val = __GlyphLayout(arg0, arg1, arg2, __float.valueOf(arg3), __int.valueOf(arg4), __boolean.valueOf(arg5))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self, arg0: 'BitmapFont', arg1: 'CharSequence', arg2: int, arg3: int, arg4: 'Color', arg5: float, arg6: int, arg7: bool, arg8: str):
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout(com.badlogic.gdx.graphics.g2d.BitmapFont,java.lang.CharSequence,int,int,com.badlogic.gdx.graphics.Color,float,int,boolean,java.lang.String)"""
        val = __GlyphLayout(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), arg4, __float.valueOf(arg5), __int.valueOf(arg6), __boolean.valueOf(arg7), arg8)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def setText(self, arg0: 'BitmapFont', arg1: 'CharSequence'):
        """public void com.badlogic.gdx.graphics.g2d.GlyphLayout.setText(com.badlogic.gdx.graphics.g2d.BitmapFont,java.lang.CharSequence)"""
        super(__GlyphLayout, self).setText(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout()"""
        val = __GlyphLayout()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.g2d.GlyphLayout.reset()"""
        super(GlyphLayout, self).reset() 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.BitmapFont$Glyph
from builtins import str
import java.lang.Character as __char
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g2d.BitmapFont as __BitmapFont_Glyph
__Glyph = __BitmapFont_Glyph.Glyph
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
 
class Glyph():
    """com.badlogic.gdx.graphics.g2d.BitmapFont.Glyph"""
 
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g2d.BitmapFont$Glyph.toString()"""
        return str.__wrap(super(Glyph, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setKerning(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont$Glyph.setKerning(int,int)"""
        super(__Glyph, self).setKerning(__int.valueOf(arg0), __int.valueOf(arg1))

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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont$Glyph()"""
        val = __Glyph()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.BitmapFont$Glyph()"""
        val = __Glyph()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getKerning(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.g2d.BitmapFont$Glyph.getKerning(char)"""
        return int.__wrap(super(__Glyph, self).getKerning(__char.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEmitter
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
from builtins import type
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_ScaledNumericValue
__ScaledNumericValue = __ParticleEmitter_ScaledNumericValue.ScaledNumericValue
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __string
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_RangedNumericValue
__RangedNumericValue = __ParticleEmitter_RangedNumericValue.RangedNumericValue
import com.badlogic.gdx.math.collision.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
from builtins import bool
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_SpriteMode
__SpriteMode = __ParticleEmitter_SpriteMode.SpriteMode
from builtins import str
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter
__ParticleEmitter = __ParticleEmitter
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_GradientColorValue
__GradientColorValue = __ParticleEmitter_GradientColorValue.GradientColorValue
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_SpawnShapeValue
__SpawnShapeValue = __ParticleEmitter_SpawnShapeValue.SpawnShapeValue
import java.io.BufferedReader as BufferedReader
try:
    from pygdx.math import collision
except ImportError:
    collision = __import_once__("pygdx.math.collision")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import int
 
class ParticleEmitter():
    """com.badlogic.gdx.graphics.g2d.ParticleEmitter"""
 
    @staticmethod
    def __wrap(java_value: __ParticleEmitter) -> 'ParticleEmitter':
        return ParticleEmitter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleEmitter):
        """
        Dynamic initializer for ParticleEmitter.
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
    def getSpawnWidth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getSpawnWidth()"""
        return 'ScaledNumericValue'.__wrap(super(ParticleEmitter, self).getSpawnWidth())

    @overload
    def setBehind(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setBehind(boolean)"""
        super(__ParticleEmitter, self).setBehind(__boolean.valueOf(arg0))

    @overload
    def setMinParticleCount(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setMinParticleCount(int)"""
        super(__ParticleEmitter, self).setMinParticleCount(__int.valueOf(arg0))

    @overload
    def cleansUpBlendFunction(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.cleansUpBlendFunction()"""
        return bool.__wrap(super(ParticleEmitter, self).cleansUpBlendFunction())

    @overload
    def getVelocity(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getVelocity()"""
        return 'ScaledNumericValue'.__wrap(super(ParticleEmitter, self).getVelocity())

    @overload
    def getLife(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getLife()"""
        return 'ScaledNumericValue'.__wrap(super(ParticleEmitter, self).getLife())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isAttached(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isAttached()"""
        return bool.__wrap(super(ParticleEmitter, self).isAttached())

    @overload
    def __init__(self, arg0: 'BufferedReader'):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter(java.io.BufferedReader) throws java.io.IOException"""
        val = __ParticleEmitter(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getWind(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getWind()"""
        return 'ScaledNumericValue'.__wrap(super(ParticleEmitter, self).getWind())

    @overload
    def setAdditive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setAdditive(boolean)"""
        super(__ParticleEmitter, self).setAdditive(__boolean.valueOf(arg0))

    @overload
    def getDelay(self) -> 'RangedNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getDelay()"""
        return 'RangedNumericValue'.__wrap(super(ParticleEmitter, self).getDelay())

    @overload
    def setCleansUpBlendFunction(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setCleansUpBlendFunction(boolean)"""
        super(__ParticleEmitter, self).setCleansUpBlendFunction(__boolean.valueOf(arg0))

    @overload
    def update(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.update(float)"""
        super(__ParticleEmitter, self).update(__float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getTint(self) -> 'GradientColorValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getTint()"""
        return 'GradientColorValue'.__wrap(super(ParticleEmitter, self).getTint())

    @overload
    def save(self, arg0: 'Writer'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.save(java.io.Writer) throws java.io.IOException"""
        super(__ParticleEmitter, self).save(arg0)

    @overload
    def setFlip(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setFlip(boolean,boolean)"""
        super(__ParticleEmitter, self).setFlip(__boolean.valueOf(arg0), __boolean.valueOf(arg1))

    @overload
    def getBoundingBox(self) -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g2d.ParticleEmitter.getBoundingBox()"""
        return 'collision.BoundingBox'.__wrap(super(ParticleEmitter, self).getBoundingBox())

    @overload
    def getLifeOffset(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getLifeOffset()"""
        return 'ScaledNumericValue'.__wrap(super(ParticleEmitter, self).getLifeOffset())

    @overload
    def getTransparency(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getTransparency()"""
        return 'ScaledNumericValue'.__wrap(super(ParticleEmitter, self).getTransparency())

    @overload
    def getMaxParticleCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.ParticleEmitter.getMaxParticleCount()"""
        return int.__wrap(super(ParticleEmitter, self).getMaxParticleCount())

    @overload
    def getSpriteMode(self) -> 'SpriteMode':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpriteMode com.badlogic.gdx.graphics.g2d.ParticleEmitter.getSpriteMode()"""
        return 'SpriteMode'.__wrap(super(ParticleEmitter, self).getSpriteMode())

    @overload
    def matchXSize(self, arg0: 'ParticleEmitter'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.matchXSize(com.badlogic.gdx.graphics.g2d.ParticleEmitter)"""
        super(__ParticleEmitter, self).matchXSize(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter()"""
        val = __ParticleEmitter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getXScale(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getXScale()"""
        return 'ScaledNumericValue'.__wrap(super(ParticleEmitter, self).getXScale())

    @overload
    def load(self, arg0: 'BufferedReader'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.load(java.io.BufferedReader) throws java.io.IOException"""
        super(__ParticleEmitter, self).load(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getEmission(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getEmission()"""
        return 'ScaledNumericValue'.__wrap(super(ParticleEmitter, self).getEmission())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def matchMotion(self, arg0: 'ParticleEmitter'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.matchMotion(com.badlogic.gdx.graphics.g2d.ParticleEmitter)"""
        super(__ParticleEmitter, self).matchMotion(arg0)

    @overload
    def setMaxParticleCount(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setMaxParticleCount(int)"""
        super(__ParticleEmitter, self).setMaxParticleCount(__int.valueOf(arg0))

    @overload
    def flipY(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.flipY()"""
        super(ParticleEmitter, self).flipY()

    @overload
    def isAligned(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isAligned()"""
        return bool.__wrap(super(ParticleEmitter, self).isAligned())

    @overload
    def matchYSize(self, arg0: 'ParticleEmitter'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.matchYSize(com.badlogic.gdx.graphics.g2d.ParticleEmitter)"""
        super(__ParticleEmitter, self).matchYSize(arg0)

    @overload
    def draw(self, arg0: 'Batch'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.draw(com.badlogic.gdx.graphics.g2d.Batch)"""
        super(__ParticleEmitter, self).draw(arg0)

    @overload
    def getRotation(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getRotation()"""
        return 'ScaledNumericValue'.__wrap(super(ParticleEmitter, self).getRotation())

    @overload
    def setSprites(self, arg0: 'Array'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setSprites(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.Sprite>)"""
        super(__ParticleEmitter, self).setSprites(arg0)

    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setName(java.lang.String)"""
        super(__ParticleEmitter, self).setName(arg0)

    @overload
    def matchSize(self, arg0: 'ParticleEmitter'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.matchSize(com.badlogic.gdx.graphics.g2d.ParticleEmitter)"""
        super(__ParticleEmitter, self).matchSize(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setAttached(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setAttached(boolean)"""
        super(__ParticleEmitter, self).setAttached(__boolean.valueOf(arg0))

    @overload
    def getYScale(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getYScale()"""
        return 'ScaledNumericValue'.__wrap(super(ParticleEmitter, self).getYScale())

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter.getX()"""
        return float.__wrap(super(ParticleEmitter, self).getX())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setImagePaths(self, arg0: 'Array'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setImagePaths(com.badlogic.gdx.utils.Array<java.lang.String>)"""
        super(__ParticleEmitter, self).setImagePaths(arg0)

    @overload
    def allowCompletion(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.allowCompletion()"""
        super(ParticleEmitter, self).allowCompletion()

    @overload
    def getSpawnHeight(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getSpawnHeight()"""
        return 'ScaledNumericValue'.__wrap(super(ParticleEmitter, self).getSpawnHeight())

    @overload
    def getPercentComplete(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter.getPercentComplete()"""
        return float.__wrap(super(ParticleEmitter, self).getPercentComplete())

    @overload
    def isAdditive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isAdditive()"""
        return bool.__wrap(super(ParticleEmitter, self).isAdditive())

    @overload
    def getGravity(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getGravity()"""
        return 'ScaledNumericValue'.__wrap(super(ParticleEmitter, self).getGravity())

    @overload
    def isPremultipliedAlpha(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isPremultipliedAlpha()"""
        return bool.__wrap(super(ParticleEmitter, self).isPremultipliedAlpha())

    @overload
    def preAllocateParticles(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.preAllocateParticles()"""
        super(ParticleEmitter, self).preAllocateParticles()

    @overload
    def draw(self, arg0: 'Batch', arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.draw(com.badlogic.gdx.graphics.g2d.Batch,float)"""
        super(__ParticleEmitter, self).draw(arg0, __float.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getXOffsetValue(self) -> 'RangedNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getXOffsetValue()"""
        return 'RangedNumericValue'.__wrap(super(ParticleEmitter, self).getXOffsetValue())

    @overload
    def isBehind(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isBehind()"""
        return bool.__wrap(super(ParticleEmitter, self).isBehind())

    @overload
    def setPremultipliedAlpha(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setPremultipliedAlpha(boolean)"""
        super(__ParticleEmitter, self).setPremultipliedAlpha(__boolean.valueOf(arg0))

    @overload
    def setContinuous(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setContinuous(boolean)"""
        super(__ParticleEmitter, self).setContinuous(__boolean.valueOf(arg0))

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter.getY()"""
        return float.__wrap(super(ParticleEmitter, self).getY())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter()"""
        val = __ParticleEmitter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def addParticles(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.addParticles(int)"""
        super(__ParticleEmitter, self).addParticles(__int.valueOf(arg0))

    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.reset()"""
        super(ParticleEmitter, self).reset()

    @overload
    def getSprites(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.Sprite> com.badlogic.gdx.graphics.g2d.ParticleEmitter.getSprites()"""
        return 'utils.Array'.__wrap(super(ParticleEmitter, self).getSprites())

    @overload
    def getActiveCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.ParticleEmitter.getActiveCount()"""
        return int.__wrap(super(ParticleEmitter, self).getActiveCount())

    @overload
    def setSpriteMode(self, arg0: 'SpriteMode'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setSpriteMode(com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpriteMode)"""
        super(__ParticleEmitter, self).setSpriteMode(arg0)

    @overload
    def getSpawnShape(self) -> 'SpawnShapeValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getSpawnShape()"""
        return 'SpawnShapeValue'.__wrap(super(ParticleEmitter, self).getSpawnShape())

    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setPosition(float,float)"""
        super(__ParticleEmitter, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getImagePaths(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<java.lang.String> com.badlogic.gdx.graphics.g2d.ParticleEmitter.getImagePaths()"""
        return 'utils.Array'.__wrap(super(ParticleEmitter, self).getImagePaths())

    @overload
    def scaleMotion(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.scaleMotion(float)"""
        super(__ParticleEmitter, self).scaleMotion(__float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.start()"""
        super(ParticleEmitter, self).start()

    @overload
    def getMinParticleCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.ParticleEmitter.getMinParticleCount()"""
        return int.__wrap(super(ParticleEmitter, self).getMinParticleCount())

    @overload
    def scaleSize(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.scaleSize(float)"""
        super(__ParticleEmitter, self).scaleSize(__float.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'ParticleEmitter'):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter(com.badlogic.gdx.graphics.g2d.ParticleEmitter)"""
        val = __ParticleEmitter(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g2d.ParticleEmitter.getName()"""
        return str.__wrap(super(ParticleEmitter, self).getName())

    @overload
    def getDuration(self) -> 'RangedNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getDuration()"""
        return 'RangedNumericValue'.__wrap(super(ParticleEmitter, self).getDuration())

    @overload
    def getAngle(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getAngle()"""
        return 'ScaledNumericValue'.__wrap(super(ParticleEmitter, self).getAngle())

    @overload
    def addParticle(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.addParticle()"""
        super(ParticleEmitter, self).addParticle()

    @overload
    def isContinuous(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isContinuous()"""
        return bool.__wrap(super(ParticleEmitter, self).isContinuous())

    @overload
    def getYOffsetValue(self) -> 'RangedNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getYOffsetValue()"""
        return 'RangedNumericValue'.__wrap(super(ParticleEmitter, self).getYOffsetValue())

    @overload
    def setAligned(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setAligned(boolean)"""
        super(__ParticleEmitter, self).setAligned(__boolean.valueOf(arg0))

    @overload
    def scaleSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.scaleSize(float,float)"""
        super(__ParticleEmitter, self).scaleSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isComplete()"""
        return bool.__wrap(super(ParticleEmitter, self).isComplete()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PolygonRegionLoader$PolygonRegionParameters
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import com.badlogic.gdx.graphics.g2d.PolygonRegionLoader as __PolygonRegionLoader_PolygonRegionParameters
__PolygonRegionParameters = __PolygonRegionLoader_PolygonRegionParameters.PolygonRegionParameters
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PolygonRegionParameters():
    """com.badlogic.gdx.graphics.g2d.PolygonRegionLoader.PolygonRegionParameters"""
 
    @staticmethod
    def __wrap(java_value: __PolygonRegionParameters) -> 'PolygonRegionParameters':
        return PolygonRegionParameters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PolygonRegionParameters):
        """
        Dynamic initializer for PolygonRegionParameters.
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.PolygonRegionLoader$PolygonRegionParameters()"""
        val = __PolygonRegionParameters()
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.PolygonRegionLoader$PolygonRegionParameters()"""
        val = __PolygonRegionParameters()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnEllipseSide
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
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_SpawnEllipseSide
__SpawnEllipseSide = __ParticleEmitter_SpawnEllipseSide.SpawnEllipseSide
from builtins import int
 
class SpawnEllipseSide():
    """com.badlogic.gdx.graphics.g2d.ParticleEmitter.SpawnEllipseSide"""
 
    @staticmethod
    def __wrap(java_value: __SpawnEllipseSide) -> 'SpawnEllipseSide':
        return SpawnEllipseSide(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SpawnEllipseSide):
        """
        Dynamic initializer for SpawnEllipseSide.
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'SpawnEllipseSide':
        """public static com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnEllipseSide com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnEllipseSide.valueOf(java.lang.String)"""
        return SpawnEllipseSide.__wrap(__SpawnEllipseSide.valueOf(arg0))

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
    def values() -> List['SpawnEllipseSide']:
        """public static com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnEllipseSide[] com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnEllipseSide.values()"""
        return List[SpawnEllipseSide].__wrap(__SpawnEllipseSide.values()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.graphics.g2d.TextureAtlas as __TextureAtlas_AtlasRegion
__AtlasRegion = __TextureAtlas_AtlasRegion.AtlasRegion
from typing import List
import com.badlogic.gdx.math.Rectangle as __Rectangle
__Rectangle = __Rectangle
import com.badlogic.gdx.graphics.g2d.TextureRegion as __TextureRegion
__TextureRegion = __TextureRegion
import java.lang.Long as __long
import com.badlogic.gdx.graphics.g2d.TextureAtlas as __TextureAtlas_AtlasSprite
__AtlasSprite = __TextureAtlas_AtlasSprite.AtlasSprite
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g2d.Sprite as __Sprite
__Sprite = __Sprite
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Texture as __Texture
__Texture = __Texture
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class AtlasSprite():
    """com.badlogic.gdx.graphics.g2d.TextureAtlas.AtlasSprite"""
 
    @staticmethod
    def __wrap(java_value: __AtlasSprite) -> 'AtlasSprite':
        return AtlasSprite(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AtlasSprite):
        """
        Dynamic initializer for AtlasSprite.
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
    def translateX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.translateX(float)"""
        super(__Sprite, self).translateX(__float.valueOf(arg0))

    @override
    @overload
    def getV2(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getV2()"""
        return float.__wrap(super(TextureRegion, self).getV2())

    @override
    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.getX()"""
        return float.__wrap(super(AtlasSprite, self).getX())

    @overload
    def getAtlasRegion(self) -> 'AtlasRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.getAtlasRegion()"""
        return 'AtlasRegion'.__wrap(super(AtlasSprite, self).getAtlasRegion())

    @override
    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getScaleY()"""
        return float.__wrap(super(Sprite, self).getScaleY())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setCenterX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setCenterX(float)"""
        super(__Sprite, self).setCenterX(__float.valueOf(arg0))

    @overload
    def split(self, arg0: int, arg1: int) -> List[List['TextureRegion']]:
        """public com.badlogic.gdx.graphics.g2d.TextureRegion[][] com.badlogic.gdx.graphics.g2d.TextureRegion.split(int,int)"""
        return List[List['TextureRegion']].__wrap(super(__TextureRegion, self).split(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getOriginX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.getOriginX()"""
        return float.__wrap(super(AtlasSprite, self).getOriginX())

    @override
    @overload
    def setCenter(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setCenter(float,float)"""
        super(__Sprite, self).setCenter(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def setRegionX(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionX(int)"""
        super(__TextureRegion, self).setRegionX(__int.valueOf(arg0))

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.Sprite.getColor()"""
        return 'graphics.Color'.__wrap(super(Sprite, self).getColor())

    @override
    @overload
    def flip(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.flip(boolean,boolean)"""
        super(__AtlasSprite, self).flip(__boolean.valueOf(arg0), __boolean.valueOf(arg1))

    @override
    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setScale(float)"""
        super(__Sprite, self).setScale(__float.valueOf(arg0))

    @override
    @overload
    def setRegion(self, arg0: 'Texture'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.Texture)"""
        super(__TextureRegion, self).setRegion(arg0)

    @override
    @overload
    def getRegionX(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionX()"""
        return int.__wrap(super(TextureRegion, self).getRegionX())

    @override
    @overload
    def setOrigin(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.setOrigin(float,float)"""
        super(__AtlasSprite, self).setOrigin(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def setFlip(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setFlip(boolean,boolean)"""
        super(__Sprite, self).setFlip(__boolean.valueOf(arg0), __boolean.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setU2(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setU2(float)"""
        super(__Sprite, self).setU2(__float.valueOf(arg0))

    @override
    @overload
    def draw(self, arg0: 'Batch'):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.draw(com.badlogic.gdx.graphics.g2d.Batch)"""
        super(__Sprite, self).draw(arg0)

    @override
    @overload
    def setV(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setV(float)"""
        super(__Sprite, self).setV(__float.valueOf(arg0))

    @override
    @overload
    def setRotation(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setRotation(float)"""
        super(__Sprite, self).setRotation(__float.valueOf(arg0))

    @override
    @overload
    def getRegionWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionWidth()"""
        return int.__wrap(super(TextureRegion, self).getRegionWidth())

    @override
    @overload
    def getRegionY(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionY()"""
        return int.__wrap(super(TextureRegion, self).getRegionY())

    @override
    @overload
    def translate(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.translate(float,float)"""
        super(__Sprite, self).translate(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def setRegionWidth(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionWidth(int)"""
        super(__TextureRegion, self).setRegionWidth(__int.valueOf(arg0))

    @override
    @overload
    def setBounds(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.setBounds(float,float,float,float)"""
        super(__AtlasSprite, self).setBounds(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def setV2(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setV2(float)"""
        super(__Sprite, self).setV2(__float.valueOf(arg0))

    @override
    @overload
    def setRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(__TextureRegion, self).setRegion(arg0)

    @override
    @overload
    def getOriginY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.getOriginY()"""
        return float.__wrap(super(AtlasSprite, self).getOriginY())

    @override
    @overload
    def getRotation(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getRotation()"""
        return float.__wrap(super(Sprite, self).getRotation())

    @override
    @overload
    def setRegion(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setRegion(float,float,float,float)"""
        super(__Sprite, self).setRegion(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setScale(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setScale(float,float)"""
        super(__Sprite, self).setScale(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def set(self, arg0: 'Sprite'):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.set(com.badlogic.gdx.graphics.g2d.Sprite)"""
        super(__Sprite, self).set(arg0)

    @override
    @overload
    def getRegionHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionHeight()"""
        return int.__wrap(super(TextureRegion, self).getRegionHeight())

    @override
    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.getY()"""
        return float.__wrap(super(AtlasSprite, self).getY())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def setOriginBasedPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setOriginBasedPosition(float,float)"""
        super(__Sprite, self).setOriginBasedPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getV(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getV()"""
        return float.__wrap(super(TextureRegion, self).getV())

    @override
    @overload
    def translateY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.translateY(float)"""
        super(__Sprite, self).translateY(__float.valueOf(arg0))

    @override
    @overload
    def setRegionHeight(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionHeight(int)"""
        super(__TextureRegion, self).setRegionHeight(__int.valueOf(arg0))

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setColor(float,float,float,float)"""
        super(__Sprite, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def setCenterY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setCenterY(float)"""
        super(__Sprite, self).setCenterY(__float.valueOf(arg0))

    @override
    @overload
    def isFlipY(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.TextureRegion.isFlipY()"""
        return bool.__wrap(super(TextureRegion, self).isFlipY())

    @staticmethod
    @overload
    def split(arg0: 'Texture', arg1: int, arg2: int) -> List[List['TextureRegion']]:
        """public static com.badlogic.gdx.graphics.g2d.TextureRegion[][] com.badlogic.gdx.graphics.g2d.TextureRegion.split(com.badlogic.gdx.graphics.Texture,int,int)"""
        return List[List[TextureRegion]].__wrap(__TextureRegion.split(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def setOriginCenter(self):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.setOriginCenter()"""
        super(AtlasSprite, self).setOriginCenter()

    @override
    @overload
    def setPackedColor(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setPackedColor(float)"""
        super(__Sprite, self).setPackedColor(__float.valueOf(arg0))

    @override
    @overload
    def setU(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setU(float)"""
        super(__Sprite, self).setU(__float.valueOf(arg0))

    @override
    @overload
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.graphics.g2d.TextureRegion.getTexture()"""
        return 'graphics.Texture'.__wrap(super(TextureRegion, self).getTexture())

    @override
    @overload
    def getBoundingRectangle(self) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.graphics.g2d.Sprite.getBoundingRectangle()"""
        return 'math.Rectangle'.__wrap(super(Sprite, self).getBoundingRectangle())

    @override
    @overload
    def getVertices(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.Sprite.getVertices()"""
        return List[float].__wrap(super(Sprite, self).getVertices())

    @overload
    def __init__(self, arg0: 'AtlasRegion'):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite(com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion)"""
        val = __AtlasSprite(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def scale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.scale(float)"""
        super(__Sprite, self).scale(__float.valueOf(arg0))

    @override
    @overload
    def getU(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getU()"""
        return float.__wrap(super(TextureRegion, self).getU())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setTexture(self, arg0: 'Texture'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setTexture(com.badlogic.gdx.graphics.Texture)"""
        super(__TextureRegion, self).setTexture(arg0)

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__Sprite, self).setColor(arg0)

    @override
    @overload
    def getU2(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getU2()"""
        return float.__wrap(super(TextureRegion, self).getU2())

    @override
    @overload
    def setRegion(self, arg0: 'TextureRegion', arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.g2d.TextureRegion,int,int,int,int)"""
        super(__TextureRegion, self).setRegion(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @overload
    def getHeightRatio(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.getHeightRatio()"""
        return float.__wrap(super(AtlasSprite, self).getHeightRatio())

    @override
    @overload
    def scroll(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.scroll(float,float)"""
        super(__Sprite, self).scroll(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.draw(com.badlogic.gdx.graphics.g2d.Batch,float)"""
        super(__Sprite, self).draw(arg0, __float.valueOf(arg1))

    @override
    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.Sprite.getScaleX()"""
        return float.__wrap(super(Sprite, self).getScaleX())

    @override
    @overload
    def isFlipX(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.TextureRegion.isFlipX()"""
        return bool.__wrap(super(TextureRegion, self).isFlipX())

    @override
    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.setX(float)"""
        super(__AtlasSprite, self).setX(__float.valueOf(arg0))

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.setPosition(float,float)"""
        super(__AtlasSprite, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def rotate90(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.rotate90(boolean)"""
        super(__AtlasSprite, self).rotate90(__boolean.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'AtlasSprite'):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite(com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite)"""
        val = __AtlasSprite(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getWidthRatio(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.getWidthRatio()"""
        return float.__wrap(super(AtlasSprite, self).getWidthRatio())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.toString()"""
        return str.__wrap(super(AtlasSprite, self).toString())

    @override
    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.getWidth()"""
        return float.__wrap(super(AtlasSprite, self).getWidth())

    @override
    @overload
    def setSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.setSize(float,float)"""
        super(__AtlasSprite, self).setSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.getHeight()"""
        return float.__wrap(super(AtlasSprite, self).getHeight())

    @override
    @overload
    def setRegionY(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionY(int)"""
        super(__TextureRegion, self).setRegionY(__int.valueOf(arg0))

    @override
    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasSprite.setY(float)"""
        super(__AtlasSprite, self).setY(__float.valueOf(arg0))

    @override
    @overload
    def setAlpha(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.setAlpha(float)"""
        super(__Sprite, self).setAlpha(__float.valueOf(arg0))

    @override
    @overload
    def rotate(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.Sprite.rotate(float)"""
        super(__Sprite, self).rotate(__float.valueOf(arg0))

    @override
    @overload
    def setRegion(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(int,int,int,int)"""
        super(__TextureRegion, self).setRegion(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.BitmapFontCache
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.g2d.GlyphLayout as __GlyphLayout
__GlyphLayout = __GlyphLayout
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from builtins import str
import java.lang.CharSequence as CharSequence
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
from typing import List
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g2d.BitmapFontCache as __BitmapFontCache
__BitmapFontCache = __BitmapFontCache
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
import com.badlogic.gdx.graphics.g2d.BitmapFont as __BitmapFont
__BitmapFont = __BitmapFont
from builtins import int
 
class BitmapFontCache():
    """com.badlogic.gdx.graphics.g2d.BitmapFontCache"""
 
    @staticmethod
    def __wrap(java_value: __BitmapFontCache) -> 'BitmapFontCache':
        return BitmapFontCache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BitmapFontCache):
        """
        Dynamic initializer for BitmapFontCache.
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
    def setColors(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.setColors(float,float,float,float)"""
        super(__BitmapFontCache, self).setColors(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def getVertices(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.BitmapFontCache.getVertices()"""
        return List[float].__wrap(super(BitmapFontCache, self).getVertices())

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFontCache.getY()"""
        return float.__wrap(super(BitmapFontCache, self).getY())

    @overload
    def setText(self, arg0: 'CharSequence', arg1: float, arg2: float, arg3: int, arg4: int, arg5: float, arg6: int, arg7: bool, arg8: str) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFontCache.setText(java.lang.CharSequence,float,float,int,int,float,int,boolean,java.lang.String)"""
        return 'GlyphLayout'.__wrap(super(__BitmapFontCache, self).setText(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __int.valueOf(arg6), __boolean.valueOf(arg7), arg8))

    @overload
    def setColors(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.setColors(float)"""
        super(__BitmapFontCache, self).setColors(__float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setText(self, arg0: 'CharSequence', arg1: float, arg2: float, arg3: float, arg4: int, arg5: bool) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFontCache.setText(java.lang.CharSequence,float,float,float,int,boolean)"""
        return 'GlyphLayout'.__wrap(super(__BitmapFontCache, self).setText(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4), __boolean.valueOf(arg5)))

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.setColor(float,float,float,float)"""
        super(__BitmapFontCache, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def setText(self, arg0: 'GlyphLayout', arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.setText(com.badlogic.gdx.graphics.g2d.GlyphLayout,float,float)"""
        super(__BitmapFontCache, self).setText(arg0, __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def addText(self, arg0: 'CharSequence', arg1: float, arg2: float, arg3: int, arg4: int, arg5: float, arg6: int, arg7: bool, arg8: str) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFontCache.addText(java.lang.CharSequence,float,float,int,int,float,int,boolean,java.lang.String)"""
        return 'GlyphLayout'.__wrap(super(__BitmapFontCache, self).addText(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __int.valueOf(arg6), __boolean.valueOf(arg7), arg8))

    @overload
    def setAlphas(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.setAlphas(float)"""
        super(__BitmapFontCache, self).setAlphas(__float.valueOf(arg0))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.clear()"""
        super(BitmapFontCache, self).clear()

    @overload
    def setText(self, arg0: 'CharSequence', arg1: float, arg2: float) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFontCache.setText(java.lang.CharSequence,float,float)"""
        return 'GlyphLayout'.__wrap(super(__BitmapFontCache, self).setText(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def translate(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.translate(float,float)"""
        super(__BitmapFontCache, self).translate(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def draw(self, arg0: 'Batch'):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.draw(com.badlogic.gdx.graphics.g2d.Batch)"""
        super(__BitmapFontCache, self).draw(arg0)

    @overload
    def draw(self, arg0: 'Batch', arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.draw(com.badlogic.gdx.graphics.g2d.Batch,float)"""
        super(__BitmapFontCache, self).draw(arg0, __float.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'BitmapFont', arg1: bool):
        """public com.badlogic.gdx.graphics.g2d.BitmapFontCache(com.badlogic.gdx.graphics.g2d.BitmapFont,boolean)"""
        val = __BitmapFontCache(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setColors(self, arg0: float, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.setColors(float,int,int)"""
        super(__BitmapFontCache, self).setColors(__float.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setText(self, arg0: 'CharSequence', arg1: float, arg2: float, arg3: int, arg4: int, arg5: float, arg6: int, arg7: bool) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFontCache.setText(java.lang.CharSequence,float,float,int,int,float,int,boolean)"""
        return 'GlyphLayout'.__wrap(super(__BitmapFontCache, self).setText(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __int.valueOf(arg6), __boolean.valueOf(arg7)))

    @overload
    def getLayouts(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.GlyphLayout> com.badlogic.gdx.graphics.g2d.BitmapFontCache.getLayouts()"""
        return 'utils.Array'.__wrap(super(BitmapFontCache, self).getLayouts())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFontCache.getX()"""
        return float.__wrap(super(BitmapFontCache, self).getX())

    @overload
    def setColors(self, arg0: 'Color', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.setColors(com.badlogic.gdx.graphics.Color,int,int)"""
        super(__BitmapFontCache, self).setColors(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def usesIntegerPositions(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.BitmapFontCache.usesIntegerPositions()"""
        return bool.__wrap(super(BitmapFontCache, self).usesIntegerPositions())

    @overload
    def getVertices(self, arg0: int) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.BitmapFontCache.getVertices(int)"""
        return List[float].__wrap(super(__BitmapFontCache, self).getVertices(__int.valueOf(arg0)))

    @overload
    def setColors(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.setColors(com.badlogic.gdx.graphics.Color)"""
        super(__BitmapFontCache, self).setColors(arg0)

    @overload
    def addText(self, arg0: 'CharSequence', arg1: float, arg2: float, arg3: float, arg4: int, arg5: bool) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFontCache.addText(java.lang.CharSequence,float,float,float,int,boolean)"""
        return 'GlyphLayout'.__wrap(super(__BitmapFontCache, self).addText(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4), __boolean.valueOf(arg5)))

    @overload
    def getVertexCount(self, arg0: int) -> int:
        """public int com.badlogic.gdx.graphics.g2d.BitmapFontCache.getVertexCount(int)"""
        return int.__wrap(super(__BitmapFontCache, self).getVertexCount(__int.valueOf(arg0)))

    @overload
    def tint(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.tint(com.badlogic.gdx.graphics.Color)"""
        super(__BitmapFontCache, self).tint(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.BitmapFontCache.getColor()"""
        return 'graphics.Color'.__wrap(super(BitmapFontCache, self).getColor())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def addText(self, arg0: 'CharSequence', arg1: float, arg2: float, arg3: int, arg4: int, arg5: float, arg6: int, arg7: bool) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFontCache.addText(java.lang.CharSequence,float,float,int,int,float,int,boolean)"""
        return 'GlyphLayout'.__wrap(super(__BitmapFontCache, self).addText(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __int.valueOf(arg6), __boolean.valueOf(arg7)))

    @overload
    def addText(self, arg0: 'CharSequence', arg1: float, arg2: float) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFontCache.addText(java.lang.CharSequence,float,float)"""
        return 'GlyphLayout'.__wrap(super(__BitmapFontCache, self).addText(arg0, __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__BitmapFontCache, self).setColor(arg0)

    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.setPosition(float,float)"""
        super(__BitmapFontCache, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def addText(self, arg0: 'GlyphLayout', arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.addText(com.badlogic.gdx.graphics.g2d.GlyphLayout,float,float)"""
        super(__BitmapFontCache, self).addText(arg0, __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def draw(self, arg0: 'Batch', arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.draw(com.badlogic.gdx.graphics.g2d.Batch,int,int)"""
        super(__BitmapFontCache, self).draw(arg0, __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def setUseIntegerPositions(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFontCache.setUseIntegerPositions(boolean)"""
        super(__BitmapFontCache, self).setUseIntegerPositions(__boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'BitmapFont'):
        """public com.badlogic.gdx.graphics.g2d.BitmapFontCache(com.badlogic.gdx.graphics.g2d.BitmapFont)"""
        val = __BitmapFontCache(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getFont(self) -> 'BitmapFont':
        """public com.badlogic.gdx.graphics.g2d.BitmapFont com.badlogic.gdx.graphics.g2d.BitmapFontCache.getFont()"""
        return 'BitmapFont'.__wrap(super(BitmapFontCache, self).getFont()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData$Region
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g2d.TextureAtlas as __TextureAtlas_TextureAtlasData_Region
__Region = __TextureAtlas_TextureAtlasData_Region.TextureAtlasData.Region
from typing import List
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
 
class Region():
    """com.badlogic.gdx.graphics.g2d.TextureAtlas.TextureAtlasData.Region"""
 
    @staticmethod
    def __wrap(java_value: __Region) -> 'Region':
        return Region(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Region):
        """
        Dynamic initializer for Region.
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
    def findValue(self, arg0: str) -> List[int]:
        """public int[] com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData$Region.findValue(java.lang.String)"""
        return List[int].__wrap(super(__Region, self).findValue(arg0))

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData$Region()"""
        val = __Region()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData$Region()"""
        val = __Region()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_ParticleValue
__ParticleValue = __ParticleEmitter_ParticleValue.ParticleValue
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_ScaledNumericValue
__ScaledNumericValue = __ParticleEmitter_ScaledNumericValue.ScaledNumericValue
from typing import List
import java.io.BufferedReader as BufferedReader
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_RangedNumericValue
__RangedNumericValue = __ParticleEmitter_RangedNumericValue.RangedNumericValue
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ScaledNumericValue():
    """com.badlogic.gdx.graphics.g2d.ParticleEmitter.ScaledNumericValue"""
 
    @staticmethod
    def __wrap(java_value: __ScaledNumericValue) -> 'ScaledNumericValue':
        return ScaledNumericValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ScaledNumericValue):
        """
        Dynamic initializer for ScaledNumericValue.
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
    def set(self, arg0: 'RangedNumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.set(com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue)"""
        super(__ScaledNumericValue, self).set(arg0)

    @override
    @overload
    def setLowMax(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.setLowMax(float)"""
        super(__RangedNumericValue, self).setLowMax(__float.valueOf(arg0))

    @overload
    def setHigh(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setHigh(float)"""
        super(__ScaledNumericValue, self).setHigh(__float.valueOf(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isActive()"""
        return bool.__wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue)"""
        super(__ParticleValue, self).load(arg0)

    @overload
    def setHighMax(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setHighMax(float)"""
        super(__ScaledNumericValue, self).setHighMax(__float.valueOf(arg0))

    @override
    @overload
    def getLowMax(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.getLowMax()"""
        return float.__wrap(super(RangedNumericValue, self).getLowMax())

    @override
    @overload
    def load(self, arg0: 'BufferedReader'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.load(java.io.BufferedReader) throws java.io.IOException"""
        super(__ScaledNumericValue, self).load(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getHighMax(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.getHighMax()"""
        return float.__wrap(super(ScaledNumericValue, self).getHighMax())

    @overload
    def setTimeline(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setTimeline(float[])"""
        super(__ScaledNumericValue, self).setTimeline(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def save(self, arg0: 'Writer'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.save(java.io.Writer) throws java.io.IOException"""
        super(__ScaledNumericValue, self).save(arg0)

    @override
    @overload
    def load(self, arg0: 'RangedNumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue)"""
        super(__RangedNumericValue, self).load(arg0)

    @override
    @overload
    def setAlwaysActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setAlwaysActive(boolean)"""
        super(__ParticleValue, self).setAlwaysActive(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getLowMin(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.getLowMin()"""
        return float.__wrap(super(RangedNumericValue, self).getLowMin())

    @overload
    def load(self, arg0: 'ScaledNumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue)"""
        super(__ScaledNumericValue, self).load(arg0)

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setActive(boolean)"""
        super(__ParticleValue, self).setActive(__boolean.valueOf(arg0))

    @overload
    def setScaling(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setScaling(float[])"""
        super(__ScaledNumericValue, self).setScaling(arg0)

    @override
    @overload
    def setLow(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.setLow(float)"""
        super(__RangedNumericValue, self).setLow(__float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue()"""
        val = __ScaledNumericValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setHighMin(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setHighMin(float)"""
        super(__ScaledNumericValue, self).setHighMin(__float.valueOf(arg0))

    @override
    @overload
    def setLow(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.setLow(float,float)"""
        super(__RangedNumericValue, self).setLow(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def getTimeline(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.getTimeline()"""
        return List[float].__wrap(super(ScaledNumericValue, self).getTimeline())

    @override
    @overload
    def newLowValue(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.newLowValue()"""
        return float.__wrap(super(RangedNumericValue, self).newLowValue())

    @override
    @overload
    def isAlwaysActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isAlwaysActive()"""
        return bool.__wrap(super(ParticleValue, self).isAlwaysActive())

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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue()"""
        val = __ScaledNumericValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def scale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.scale(float)"""
        super(__ScaledNumericValue, self).scale(__float.valueOf(arg0))

    @overload
    def getHighMin(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.getHighMin()"""
        return float.__wrap(super(ScaledNumericValue, self).getHighMin())

    @overload
    def set(self, arg0: 'ScaledNumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.set(com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue)"""
        super(__ScaledNumericValue, self).set(arg0)

    @overload
    def isRelative(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.isRelative()"""
        return bool.__wrap(super(ScaledNumericValue, self).isRelative())

    @overload
    def getScale(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.getScale(float)"""
        return float.__wrap(super(__ScaledNumericValue, self).getScale(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def newHighValue(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.newHighValue()"""
        return float.__wrap(super(ScaledNumericValue, self).newHighValue())

    @overload
    def setHigh(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setHigh(float,float)"""
        super(__ScaledNumericValue, self).setHigh(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def getScaling(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.getScaling()"""
        return List[float].__wrap(super(ScaledNumericValue, self).getScaling())

    @overload
    def setRelative(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setRelative(boolean)"""
        super(__ScaledNumericValue, self).setRelative(__boolean.valueOf(arg0))

    @override
    @overload
    def setLowMin(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.setLowMin(float)"""
        super(__RangedNumericValue, self).setLowMin(__float.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEmitter$NumericValue
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_NumericValue
__NumericValue = __ParticleEmitter_NumericValue.NumericValue
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_ParticleValue
__ParticleValue = __ParticleEmitter_ParticleValue.ParticleValue
import java.io.BufferedReader as BufferedReader
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class NumericValue():
    """com.badlogic.gdx.graphics.g2d.ParticleEmitter.NumericValue"""
 
    @staticmethod
    def __wrap(java_value: __NumericValue) -> 'NumericValue':
        return NumericValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __NumericValue):
        """
        Dynamic initializer for NumericValue.
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
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setActive(boolean)"""
        super(__ParticleValue, self).setActive(__boolean.valueOf(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isActive()"""
        return bool.__wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$NumericValue()"""
        val = __NumericValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue)"""
        super(__ParticleValue, self).load(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isAlwaysActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isAlwaysActive()"""
        return bool.__wrap(super(ParticleValue, self).isAlwaysActive())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$NumericValue()"""
        val = __NumericValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def load(self, arg0: 'NumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$NumericValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$NumericValue)"""
        super(__NumericValue, self).load(arg0)

    @overload
    def setValue(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$NumericValue.setValue(float)"""
        super(__NumericValue, self).setValue(__float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def save(self, arg0: 'Writer'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$NumericValue.save(java.io.Writer) throws java.io.IOException"""
        super(__NumericValue, self).save(arg0)

    @override
    @overload
    def setAlwaysActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setAlwaysActive(boolean)"""
        super(__ParticleValue, self).setAlwaysActive(__boolean.valueOf(arg0))

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

    @override
    @overload
    def load(self, arg0: 'BufferedReader'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$NumericValue.load(java.io.BufferedReader) throws java.io.IOException"""
        super(__NumericValue, self).load(arg0)

    @overload
    def getValue(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$NumericValue.getValue()"""
        return float.__wrap(super(NumericValue, self).getValue())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_ParticleValue
__ParticleValue = __ParticleEmitter_ParticleValue.ParticleValue
import java.io.BufferedReader as BufferedReader
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_RangedNumericValue
__RangedNumericValue = __ParticleEmitter_RangedNumericValue.RangedNumericValue
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RangedNumericValue():
    """com.badlogic.gdx.graphics.g2d.ParticleEmitter.RangedNumericValue"""
 
    @staticmethod
    def __wrap(java_value: __RangedNumericValue) -> 'RangedNumericValue':
        return RangedNumericValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RangedNumericValue):
        """
        Dynamic initializer for RangedNumericValue.
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
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isActive()"""
        return bool.__wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue)"""
        super(__ParticleValue, self).load(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setLow(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.setLow(float)"""
        super(__RangedNumericValue, self).setLow(__float.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue()"""
        val = __RangedNumericValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def newLowValue(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.newLowValue()"""
        return float.__wrap(super(RangedNumericValue, self).newLowValue())

    @overload
    def set(self, arg0: 'RangedNumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.set(com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue)"""
        super(__RangedNumericValue, self).set(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setAlwaysActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setAlwaysActive(boolean)"""
        super(__ParticleValue, self).setAlwaysActive(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getLowMin(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.getLowMin()"""
        return float.__wrap(super(RangedNumericValue, self).getLowMin())

    @overload
    def setLowMax(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.setLowMax(float)"""
        super(__RangedNumericValue, self).setLowMax(__float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getLowMax(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.getLowMax()"""
        return float.__wrap(super(RangedNumericValue, self).getLowMax())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue()"""
        val = __RangedNumericValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setActive(boolean)"""
        super(__ParticleValue, self).setActive(__boolean.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def load(self, arg0: 'RangedNumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue)"""
        super(__RangedNumericValue, self).load(arg0)

    @overload
    def scale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.scale(float)"""
        super(__RangedNumericValue, self).scale(__float.valueOf(arg0))

    @override
    @overload
    def isAlwaysActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isAlwaysActive()"""
        return bool.__wrap(super(ParticleValue, self).isAlwaysActive())

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
    def setLowMin(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.setLowMin(float)"""
        super(__RangedNumericValue, self).setLowMin(__float.valueOf(arg0))

    @override
    @overload
    def save(self, arg0: 'Writer'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.save(java.io.Writer) throws java.io.IOException"""
        super(__RangedNumericValue, self).save(arg0)

    @override
    @overload
    def load(self, arg0: 'BufferedReader'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.load(java.io.BufferedReader) throws java.io.IOException"""
        super(__RangedNumericValue, self).load(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setLow(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.setLow(float,float)"""
        super(__RangedNumericValue, self).setLow(__float.valueOf(arg0), __float.valueOf(arg1)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PixmapPackerIO$ImageFormat
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g2d.PixmapPackerIO as __PixmapPackerIO_ImageFormat
__ImageFormat = __PixmapPackerIO_ImageFormat.ImageFormat
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
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class ImageFormat():
    """com.badlogic.gdx.graphics.g2d.PixmapPackerIO.ImageFormat"""
 
    @staticmethod
    def __wrap(java_value: __ImageFormat) -> 'ImageFormat':
        return ImageFormat(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ImageFormat):
        """
        Dynamic initializer for ImageFormat.
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

    @staticmethod
    @overload
    def values() -> List['ImageFormat']:
        """public static com.badlogic.gdx.graphics.g2d.PixmapPackerIO$ImageFormat[] com.badlogic.gdx.graphics.g2d.PixmapPackerIO$ImageFormat.values()"""
        return List[ImageFormat].__wrap(__ImageFormat.values())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ImageFormat':
        """public static com.badlogic.gdx.graphics.g2d.PixmapPackerIO$ImageFormat com.badlogic.gdx.graphics.g2d.PixmapPackerIO$ImageFormat.valueOf(java.lang.String)"""
        return ImageFormat.__wrap(__ImageFormat.valueOf(arg0))

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

    @overload
    def getExtension(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g2d.PixmapPackerIO$ImageFormat.getExtension()"""
        return str.__wrap(super(ImageFormat, self).getExtension())

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
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_ParticleValue
__ParticleValue = __ParticleEmitter_ParticleValue.ParticleValue
import java.io.BufferedReader as BufferedReader
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ParticleValue():
    """com.badlogic.gdx.graphics.g2d.ParticleEmitter.ParticleValue"""
 
    @staticmethod
    def __wrap(java_value: __ParticleValue) -> 'ParticleValue':
        return ParticleValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleValue):
        """
        Dynamic initializer for ParticleValue.
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

    @overload
    def save(self, arg0: 'Writer'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.save(java.io.Writer) throws java.io.IOException"""
        super(__ParticleValue, self).save(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setAlwaysActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setAlwaysActive(boolean)"""
        super(__ParticleValue, self).setAlwaysActive(__boolean.valueOf(arg0))

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
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setActive(boolean)"""
        super(__ParticleValue, self).setActive(__boolean.valueOf(arg0))

    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue)"""
        super(__ParticleValue, self).load(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue()"""
        val = __ParticleValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue()"""
        val = __ParticleValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def load(self, arg0: 'BufferedReader'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.load(java.io.BufferedReader) throws java.io.IOException"""
        super(__ParticleValue, self).load(arg0)

    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isActive()"""
        return bool.__wrap(super(ParticleValue, self).isActive())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def isAlwaysActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isAlwaysActive()"""
        return bool.__wrap(super(ParticleValue, self).isAlwaysActive()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.CpuSpriteBatch
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.g2d.CpuSpriteBatch as __CpuSpriteBatch
__CpuSpriteBatch = __CpuSpriteBatch
import com.badlogic.gdx.graphics.g2d.SpriteBatch as __SpriteBatch
__SpriteBatch = __SpriteBatch
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import com.badlogic.gdx.graphics.glutils.ShaderProgram as __ShaderProgram
__ShaderProgram = __ShaderProgram
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Matrix4 as __Matrix4
__Matrix4 = __Matrix4
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class CpuSpriteBatch():
    """com.badlogic.gdx.graphics.g2d.CpuSpriteBatch"""
 
    @staticmethod
    def __wrap(java_value: __CpuSpriteBatch) -> 'CpuSpriteBatch':
        return CpuSpriteBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CpuSpriteBatch):
        """
        Dynamic initializer for CpuSpriteBatch.
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
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: bool):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,float,float,float,float,boolean)"""
        super(__CpuSpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __boolean.valueOf(arg10))

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: int, arg11: int, arg12: int, arg13: int, arg14: bool, arg15: bool):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float,float,int,int,int,int,boolean,boolean)"""
        super(__CpuSpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __boolean.valueOf(arg14), __boolean.valueOf(arg15))

    @override
    @overload
    def getBlendDstFunc(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.SpriteBatch.getBlendDstFunc()"""
        return int.__wrap(super(SpriteBatch, self).getBlendDstFunc())

    @override
    @overload
    def getBlendSrcFuncAlpha(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.SpriteBatch.getBlendSrcFuncAlpha()"""
        return int.__wrap(super(SpriteBatch, self).getBlendSrcFuncAlpha())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.CpuSpriteBatch()"""
        val = __CpuSpriteBatch()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float)"""
        super(__CpuSpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setTransformMatrix(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.setTransformMatrix(com.badlogic.gdx.math.Matrix4)"""
        super(__CpuSpriteBatch, self).setTransformMatrix(arg0)

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__SpriteBatch, self).setColor(arg0)

    @override
    @overload
    def isDrawing(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.SpriteBatch.isDrawing()"""
        return bool.__wrap(super(SpriteBatch, self).isDrawing())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def createDefaultShader() -> 'glutils.ShaderProgram':
        """public static com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g2d.SpriteBatch.createDefaultShader()"""
        return glutils.ShaderProgram.__wrap(__SpriteBatch.createDefaultShader())

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.end()"""
        super(SpriteBatch, self).end()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,float,float,float,float)"""
        super(__CpuSpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9))

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: 'Affine2'):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,com.badlogic.gdx.math.Affine2)"""
        super(__CpuSpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), arg3)

    @override
    @overload
    def disableBlending(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.disableBlending()"""
        super(SpriteBatch, self).disableBlending()

    @override
    @overload
    def getBlendSrcFunc(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.SpriteBatch.getBlendSrcFunc()"""
        return int.__wrap(super(SpriteBatch, self).getBlendSrcFunc())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,int,int,int,int)"""
        super(__CpuSpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6))

    @override
    @overload
    def getTransformMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.getTransformMatrix()"""
        return 'math.Matrix4'.__wrap(super(CpuSpriteBatch, self).getTransformMatrix())

    @override
    @overload
    def setBlendFunction(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setBlendFunction(int,int)"""
        super(__SpriteBatch, self).setBlendFunction(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float)"""
        super(__CpuSpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float)"""
        super(__CpuSpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))

    @overload
    def flushAndSyncTransformMatrix(self):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.flushAndSyncTransformMatrix()"""
        super(CpuSpriteBatch, self).flushAndSyncTransformMatrix()

    @override
    @overload
    def isBlendingEnabled(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.SpriteBatch.isBlendingEnabled()"""
        return bool.__wrap(super(SpriteBatch, self).isBlendingEnabled())

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float)"""
        super(__CpuSpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8))

    @override
    @overload
    def setPackedColor(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setPackedColor(float)"""
        super(__SpriteBatch, self).setPackedColor(__float.valueOf(arg0))

    @override
    @overload
    def setShader(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setShader(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(__SpriteBatch, self).setShader(arg0)

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

    @override
    @overload
    def flush(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.flush()"""
        super(SpriteBatch, self).flush()

    @override
    @overload
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float)"""
        super(__CpuSpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.CpuSpriteBatch()"""
        val = __CpuSpriteBatch()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float[],int,int)"""
        super(__CpuSpriteBatch, self).draw(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g2d.CpuSpriteBatch(int)"""
        val = __CpuSpriteBatch(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def enableBlending(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.enableBlending()"""
        super(SpriteBatch, self).enableBlending()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getPackedColor(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.SpriteBatch.getPackedColor()"""
        return float.__wrap(super(SpriteBatch, self).getPackedColor())

    @override
    @overload
    def getProjectionMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.SpriteBatch.getProjectionMatrix()"""
        return 'math.Matrix4'.__wrap(super(SpriteBatch, self).getProjectionMatrix())

    @override
    @overload
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: bool):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,int,int,int,int,boolean,boolean)"""
        super(__CpuSpriteBatch, self).draw(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __boolean.valueOf(arg9), __boolean.valueOf(arg10))

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.SpriteBatch.getColor()"""
        return 'graphics.Color'.__wrap(super(SpriteBatch, self).getColor())

    @override
    @overload
    def getShader(self) -> 'glutils.ShaderProgram':
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g2d.SpriteBatch.getShader()"""
        return 'glutils.ShaderProgram'.__wrap(super(SpriteBatch, self).getShader())

    @override
    @overload
    def getBlendDstFuncAlpha(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.SpriteBatch.getBlendDstFuncAlpha()"""
        return int.__wrap(super(SpriteBatch, self).getBlendDstFuncAlpha())

    @overload
    def __init__(self, arg0: int, arg1: 'ShaderProgram'):
        """public com.badlogic.gdx.graphics.g2d.CpuSpriteBatch(int,com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        val = __CpuSpriteBatch(__int.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setBlendFunctionSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setBlendFunctionSeparate(int,int,int,int)"""
        super(__SpriteBatch, self).setBlendFunctionSeparate(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setTransformMatrix(self, arg0: 'Affine2'):
        """public void com.badlogic.gdx.graphics.g2d.CpuSpriteBatch.setTransformMatrix(com.badlogic.gdx.math.Affine2)"""
        super(__CpuSpriteBatch, self).setTransformMatrix(arg0)

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setColor(float,float,float,float)"""
        super(__SpriteBatch, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.begin()"""
        super(SpriteBatch, self).begin()

    @override
    @overload
    def setProjectionMatrix(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.setProjectionMatrix(com.badlogic.gdx.math.Matrix4)"""
        super(__SpriteBatch, self).setProjectionMatrix(arg0)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteBatch.dispose()"""
        super(SpriteBatch, self).dispose() 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_ParticleValue
__ParticleValue = __ParticleEmitter_ParticleValue.ParticleValue
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_ScaledNumericValue
__ScaledNumericValue = __ParticleEmitter_ScaledNumericValue.ScaledNumericValue
from typing import List
import java.io.BufferedReader as BufferedReader
import java.lang.Long as __long
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_IndependentScaledNumericValue
__IndependentScaledNumericValue = __ParticleEmitter_IndependentScaledNumericValue.IndependentScaledNumericValue
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.io.Writer as Writer
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_RangedNumericValue
__RangedNumericValue = __ParticleEmitter_RangedNumericValue.RangedNumericValue
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class IndependentScaledNumericValue():
    """com.badlogic.gdx.graphics.g2d.ParticleEmitter.IndependentScaledNumericValue"""
 
    @staticmethod
    def __wrap(java_value: __IndependentScaledNumericValue) -> 'IndependentScaledNumericValue':
        return IndependentScaledNumericValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IndependentScaledNumericValue):
        """
        Dynamic initializer for IndependentScaledNumericValue.
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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue()"""
        val = __IndependentScaledNumericValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setHighMin(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setHighMin(float)"""
        super(__ScaledNumericValue, self).setHighMin(__float.valueOf(arg0))

    @override
    @overload
    def setLowMax(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.setLowMax(float)"""
        super(__RangedNumericValue, self).setLowMax(__float.valueOf(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isActive()"""
        return bool.__wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue)"""
        super(__ParticleValue, self).load(arg0)

    @override
    @overload
    def setScaling(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setScaling(float[])"""
        super(__ScaledNumericValue, self).setScaling(arg0)

    @overload
    def set(self, arg0: 'IndependentScaledNumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue.set(com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue)"""
        super(__IndependentScaledNumericValue, self).set(arg0)

    @override
    @overload
    def getLowMax(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.getLowMax()"""
        return float.__wrap(super(RangedNumericValue, self).getLowMax())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def set(self, arg0: 'ScaledNumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue.set(com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue)"""
        super(__IndependentScaledNumericValue, self).set(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setHigh(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setHigh(float)"""
        super(__ScaledNumericValue, self).setHigh(__float.valueOf(arg0))

    @override
    @overload
    def load(self, arg0: 'ScaledNumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue)"""
        super(__ScaledNumericValue, self).load(arg0)

    @override
    @overload
    def load(self, arg0: 'RangedNumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue)"""
        super(__RangedNumericValue, self).load(arg0)

    @override
    @overload
    def setAlwaysActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setAlwaysActive(boolean)"""
        super(__ParticleValue, self).setAlwaysActive(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def save(self, arg0: 'Writer'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue.save(java.io.Writer) throws java.io.IOException"""
        super(__IndependentScaledNumericValue, self).save(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue()"""
        val = __IndependentScaledNumericValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def set(self, arg0: 'RangedNumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue.set(com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue)"""
        super(__IndependentScaledNumericValue, self).set(arg0)

    @override
    @overload
    def getTimeline(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.getTimeline()"""
        return List[float].__wrap(super(ScaledNumericValue, self).getTimeline())

    @override
    @overload
    def getScaling(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.getScaling()"""
        return List[float].__wrap(super(ScaledNumericValue, self).getScaling())

    @override
    @overload
    def setTimeline(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setTimeline(float[])"""
        super(__ScaledNumericValue, self).setTimeline(arg0)

    @override
    @overload
    def getHighMax(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.getHighMax()"""
        return float.__wrap(super(ScaledNumericValue, self).getHighMax())

    @override
    @overload
    def setHighMax(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setHighMax(float)"""
        super(__ScaledNumericValue, self).setHighMax(__float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getLowMin(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.getLowMin()"""
        return float.__wrap(super(RangedNumericValue, self).getLowMin())

    @override
    @overload
    def load(self, arg0: 'BufferedReader'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue.load(java.io.BufferedReader) throws java.io.IOException"""
        super(__IndependentScaledNumericValue, self).load(arg0)

    @overload
    def isIndependent(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue.isIndependent()"""
        return bool.__wrap(super(IndependentScaledNumericValue, self).isIndependent())

    @overload
    def setIndependent(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue.setIndependent(boolean)"""
        super(__IndependentScaledNumericValue, self).setIndependent(__boolean.valueOf(arg0))

    @override
    @overload
    def getHighMin(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.getHighMin()"""
        return float.__wrap(super(ScaledNumericValue, self).getHighMin())

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.setActive(boolean)"""
        super(__ParticleValue, self).setActive(__boolean.valueOf(arg0))

    @override
    @overload
    def setLow(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.setLow(float)"""
        super(__RangedNumericValue, self).setLow(__float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def load(self, arg0: 'IndependentScaledNumericValue'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue.load(com.badlogic.gdx.graphics.g2d.ParticleEmitter$IndependentScaledNumericValue)"""
        super(__IndependentScaledNumericValue, self).load(arg0)

    @override
    @overload
    def setLow(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.setLow(float,float)"""
        super(__RangedNumericValue, self).setLow(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def newLowValue(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.newLowValue()"""
        return float.__wrap(super(RangedNumericValue, self).newLowValue())

    @override
    @overload
    def setHigh(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setHigh(float,float)"""
        super(__ScaledNumericValue, self).setHigh(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def isAlwaysActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ParticleValue.isAlwaysActive()"""
        return bool.__wrap(super(ParticleValue, self).isAlwaysActive())

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
    def scale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.scale(float)"""
        super(__ScaledNumericValue, self).scale(__float.valueOf(arg0))

    @override
    @overload
    def isRelative(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.isRelative()"""
        return bool.__wrap(super(ScaledNumericValue, self).isRelative())

    @override
    @overload
    def newHighValue(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.newHighValue()"""
        return float.__wrap(super(ScaledNumericValue, self).newHighValue())

    @overload
    def getScale(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.getScale(float)"""
        return float.__wrap(super(__ScaledNumericValue, self).getScale(__float.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setRelative(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue.setRelative(boolean)"""
        super(__ScaledNumericValue, self).setRelative(__boolean.valueOf(arg0))

    @override
    @overload
    def setLowMin(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue.setLowMin(float)"""
        super(__RangedNumericValue, self).setLowMin(__float.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PixmapPackerIO$SaveParameters
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import com.badlogic.gdx.graphics.g2d.PixmapPackerIO as __PixmapPackerIO_SaveParameters
__SaveParameters = __PixmapPackerIO_SaveParameters.SaveParameters
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SaveParameters():
    """com.badlogic.gdx.graphics.g2d.PixmapPackerIO.SaveParameters"""
 
    @staticmethod
    def __wrap(java_value: __SaveParameters) -> 'SaveParameters':
        return SaveParameters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SaveParameters):
        """
        Dynamic initializer for SaveParameters.
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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.PixmapPackerIO$SaveParameters()"""
        val = __SaveParameters()
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.PixmapPackerIO$SaveParameters()"""
        val = __SaveParameters()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g2d.TextureAtlas as __TextureAtlas_TextureAtlasData
__TextureAtlasData = __TextureAtlas_TextureAtlasData.TextureAtlasData
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TextureAtlasData():
    """com.badlogic.gdx.graphics.g2d.TextureAtlas.TextureAtlasData"""
 
    @staticmethod
    def __wrap(java_value: __TextureAtlasData) -> 'TextureAtlasData':
        return TextureAtlasData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextureAtlasData):
        """
        Dynamic initializer for TextureAtlasData.
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
    def getRegions(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData$Region> com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData.getRegions()"""
        return 'utils.Array'.__wrap(super(TextureAtlasData, self).getRegions())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle', arg2: bool):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,boolean)"""
        val = __TextureAtlasData(arg0, arg1, __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getPages(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData$Page> com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData.getPages()"""
        return 'utils.Array'.__wrap(super(TextureAtlasData, self).getPages())

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData()"""
        val = __TextureAtlasData()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def load(self, arg0: 'FileHandle', arg1: 'FileHandle', arg2: bool):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData.load(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,boolean)"""
        super(__TextureAtlasData, self).load(arg0, arg1, __boolean.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData()"""
        val = __TextureAtlasData()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.GlyphLayout$GlyphRun
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import com.badlogic.gdx.graphics.g2d.GlyphLayout as __GlyphLayout_GlyphRun
__GlyphRun = __GlyphLayout_GlyphRun.GlyphRun
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GlyphRun():
    """com.badlogic.gdx.graphics.g2d.GlyphLayout.GlyphRun"""
 
    @staticmethod
    def __wrap(java_value: __GlyphRun) -> 'GlyphRun':
        return GlyphRun(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GlyphRun):
        """
        Dynamic initializer for GlyphRun.
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
    def reset(self):
        """public void com.badlogic.gdx.graphics.g2d.GlyphLayout$GlyphRun.reset()"""
        super(GlyphRun, self).reset()

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
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g2d.GlyphLayout$GlyphRun.toString()"""
        return str.__wrap(super(GlyphRun, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout$GlyphRun()"""
        val = __GlyphRun()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout$GlyphRun()"""
        val = __GlyphRun()
        self.__dict__ = val.__dict__
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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData$Page
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g2d.TextureAtlas as __TextureAtlas_TextureAtlasData_Page
__Page = __TextureAtlas_TextureAtlasData_Page.TextureAtlasData.Page
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Page():
    """com.badlogic.gdx.graphics.g2d.TextureAtlas.TextureAtlasData.Page"""
 
    @staticmethod
    def __wrap(java_value: __Page) -> 'Page':
        return Page(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Page):
        """
        Dynamic initializer for Page.
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData$Page()"""
        val = __Page()
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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData$Page()"""
        val = __Page()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.TextureAtlas
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import com.badlogic.gdx.graphics.g2d.TextureAtlas as __TextureAtlas
__TextureAtlas = __TextureAtlas
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g2d.TextureAtlas as __TextureAtlas_AtlasRegion
__AtlasRegion = __TextureAtlas_AtlasRegion.AtlasRegion
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __string
import com.badlogic.gdx.graphics.g2d.NinePatch as __NinePatch
__NinePatch = __NinePatch
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g2d.Sprite as __Sprite
__Sprite = __Sprite
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.ObjectSet as __ObjectSet
__ObjectSet = __ObjectSet
import java.lang.Integer as __int
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class TextureAtlas():
    """com.badlogic.gdx.graphics.g2d.TextureAtlas"""
 
    @staticmethod
    def __wrap(java_value: __TextureAtlas) -> 'TextureAtlas':
        return TextureAtlas(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextureAtlas):
        """
        Dynamic initializer for TextureAtlas.
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
    def addRegion(self, arg0: str, arg1: 'TextureRegion') -> 'AtlasRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion com.badlogic.gdx.graphics.g2d.TextureAtlas.addRegion(java.lang.String,com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return 'AtlasRegion'.__wrap(super(__TextureAtlas, self).addRegion(arg0, arg1))

    @overload
    def getRegions(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion> com.badlogic.gdx.graphics.g2d.TextureAtlas.getRegions()"""
        return 'utils.Array'.__wrap(super(TextureAtlas, self).getRegions())

    @overload
    def createSprite(self, arg0: str, arg1: int) -> 'Sprite':
        """public com.badlogic.gdx.graphics.g2d.Sprite com.badlogic.gdx.graphics.g2d.TextureAtlas.createSprite(java.lang.String,int)"""
        return 'Sprite'.__wrap(super(__TextureAtlas, self).createSprite(arg0, __int.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def createSprite(self, arg0: str) -> 'Sprite':
        """public com.badlogic.gdx.graphics.g2d.Sprite com.badlogic.gdx.graphics.g2d.TextureAtlas.createSprite(java.lang.String)"""
        return 'Sprite'.__wrap(super(__TextureAtlas, self).createSprite(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas()"""
        val = __TextureAtlas()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'FileHandle'):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas(com.badlogic.gdx.files.FileHandle)"""
        val = __TextureAtlas(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas()"""
        val = __TextureAtlas()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def createSprites(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.Sprite> com.badlogic.gdx.graphics.g2d.TextureAtlas.createSprites()"""
        return 'utils.Array'.__wrap(super(TextureAtlas, self).createSprites())

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle', arg2: bool):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,boolean)"""
        val = __TextureAtlas(arg0, arg1, __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle'):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle)"""
        val = __TextureAtlas(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def createSprites(self, arg0: str) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.Sprite> com.badlogic.gdx.graphics.g2d.TextureAtlas.createSprites(java.lang.String)"""
        return 'utils.Array'.__wrap(super(__TextureAtlas, self).createSprites(arg0))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas.dispose()"""
        super(TextureAtlas, self).dispose()

    @overload
    def addRegion(self, arg0: str, arg1: 'Texture', arg2: int, arg3: int, arg4: int, arg5: int) -> 'AtlasRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion com.badlogic.gdx.graphics.g2d.TextureAtlas.addRegion(java.lang.String,com.badlogic.gdx.graphics.Texture,int,int,int,int)"""
        return 'AtlasRegion'.__wrap(super(__TextureAtlas, self).addRegion(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def load(self, arg0: 'TextureAtlasData'):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas.load(com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData)"""
        super(__TextureAtlas, self).load(arg0)

    @overload
    def findRegion(self, arg0: str) -> 'AtlasRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion com.badlogic.gdx.graphics.g2d.TextureAtlas.findRegion(java.lang.String)"""
        return 'AtlasRegion'.__wrap(super(__TextureAtlas, self).findRegion(arg0))

    @overload
    def createPatch(self, arg0: str) -> 'NinePatch':
        """public com.badlogic.gdx.graphics.g2d.NinePatch com.badlogic.gdx.graphics.g2d.TextureAtlas.createPatch(java.lang.String)"""
        return 'NinePatch'.__wrap(super(__TextureAtlas, self).createPatch(arg0))

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas(java.lang.String)"""
        val = __TextureAtlas(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: bool):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas(com.badlogic.gdx.files.FileHandle,boolean)"""
        val = __TextureAtlas(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def findRegion(self, arg0: str, arg1: int) -> 'AtlasRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion com.badlogic.gdx.graphics.g2d.TextureAtlas.findRegion(java.lang.String,int)"""
        return 'AtlasRegion'.__wrap(super(__TextureAtlas, self).findRegion(arg0, __int.valueOf(arg1)))

    @overload
    def __init__(self, arg0: 'TextureAtlasData'):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas(com.badlogic.gdx.graphics.g2d.TextureAtlas$TextureAtlasData)"""
        val = __TextureAtlas(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def findRegions(self, arg0: str) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion> com.badlogic.gdx.graphics.g2d.TextureAtlas.findRegions(java.lang.String)"""
        return 'utils.Array'.__wrap(super(__TextureAtlas, self).findRegions(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getTextures(self) -> 'utils.ObjectSet':
        """public com.badlogic.gdx.utils.ObjectSet<com.badlogic.gdx.graphics.Texture> com.badlogic.gdx.graphics.g2d.TextureAtlas.getTextures()"""
        return 'utils.ObjectSet'.__wrap(super(TextureAtlas, self).getTextures()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.RepeatablePolygonSprite
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g2d.RepeatablePolygonSprite as __RepeatablePolygonSprite
__RepeatablePolygonSprite = __RepeatablePolygonSprite
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class RepeatablePolygonSprite():
    """com.badlogic.gdx.graphics.g2d.RepeatablePolygonSprite"""
 
    @staticmethod
    def __wrap(java_value: __RepeatablePolygonSprite) -> 'RepeatablePolygonSprite':
        return RepeatablePolygonSprite(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RepeatablePolygonSprite):
        """
        Dynamic initializer for RepeatablePolygonSprite.
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
    def draw(self, arg0: 'PolygonSpriteBatch'):
        """public void com.badlogic.gdx.graphics.g2d.RepeatablePolygonSprite.draw(com.badlogic.gdx.graphics.g2d.PolygonSpriteBatch)"""
        super(__RepeatablePolygonSprite, self).draw(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.RepeatablePolygonSprite.setPosition(float,float)"""
        super(__RepeatablePolygonSprite, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1))

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

    @overload
    def setPolygon(self, arg0: 'TextureRegion', arg1: 'float', arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.RepeatablePolygonSprite.setPolygon(com.badlogic.gdx.graphics.g2d.TextureRegion,float[],float)"""
        super(__RepeatablePolygonSprite, self).setPolygon(arg0, arg1, __float.valueOf(arg2))

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.RepeatablePolygonSprite()"""
        val = __RepeatablePolygonSprite()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setPolygon(self, arg0: 'TextureRegion', arg1: 'float'):
        """public void com.badlogic.gdx.graphics.g2d.RepeatablePolygonSprite.setPolygon(com.badlogic.gdx.graphics.g2d.TextureRegion,float[])"""
        super(__RepeatablePolygonSprite, self).setPolygon(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.RepeatablePolygonSprite()"""
        val = __RepeatablePolygonSprite()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.RepeatablePolygonSprite.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__RepeatablePolygonSprite, self).setColor(arg0) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PolygonRegion
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g2d.PolygonRegion as __PolygonRegion
__PolygonRegion = __PolygonRegion
from builtins import float
from typing import List
import com.badlogic.gdx.graphics.g2d.TextureRegion as __TextureRegion
__TextureRegion = __TextureRegion
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
 
class PolygonRegion():
    """com.badlogic.gdx.graphics.g2d.PolygonRegion"""
 
    @staticmethod
    def __wrap(java_value: __PolygonRegion) -> 'PolygonRegion':
        return PolygonRegion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PolygonRegion):
        """
        Dynamic initializer for PolygonRegion.
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
    def getTextureCoords(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.PolygonRegion.getTextureCoords()"""
        return List[float].__wrap(super(PolygonRegion, self).getTextureCoords())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getVertices(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g2d.PolygonRegion.getVertices()"""
        return List[float].__wrap(super(PolygonRegion, self).getVertices())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'TextureRegion', arg1: 'float', arg2: 'short'):
        """public com.badlogic.gdx.graphics.g2d.PolygonRegion(com.badlogic.gdx.graphics.g2d.TextureRegion,float[],short[])"""
        val = __PolygonRegion(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def getRegion(self) -> 'TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.graphics.g2d.PolygonRegion.getRegion()"""
        return 'TextureRegion'.__wrap(super(PolygonRegion, self).getRegion())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getTriangles(self) -> List[int]:
        """public short[] com.badlogic.gdx.graphics.g2d.PolygonRegion.getTriangles()"""
        return List[int].__wrap(super(PolygonRegion, self).getTriangles())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.SpriteCache
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import com.badlogic.gdx.graphics.glutils.ShaderProgram as __ShaderProgram
__ShaderProgram = __ShaderProgram
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.graphics.g2d.SpriteCache as __SpriteCache
__SpriteCache = __SpriteCache
import com.badlogic.gdx.math.Matrix4 as __Matrix4
__Matrix4 = __Matrix4
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class SpriteCache():
    """com.badlogic.gdx.graphics.g2d.SpriteCache"""
 
    @staticmethod
    def __wrap(java_value: __SpriteCache) -> 'SpriteCache':
        return SpriteCache(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SpriteCache):
        """
        Dynamic initializer for SpriteCache.
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
    def add(self, arg0: 'Texture', arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.add(com.badlogic.gdx.graphics.Texture,float,float,int,int,int,int)"""
        super(__SpriteCache, self).add(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6))

    @overload
    def beginCache(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.beginCache(int)"""
        super(__SpriteCache, self).beginCache(__int.valueOf(arg0))

    @overload
    def draw(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.draw(int)"""
        super(__SpriteCache, self).draw(__int.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: 'TextureRegion', arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.add(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float)"""
        super(__SpriteCache, self).add(arg0, __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def add(self, arg0: 'Texture', arg1: 'float', arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.add(com.badlogic.gdx.graphics.Texture,float[],int,int)"""
        super(__SpriteCache, self).add(arg0, arg1, __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__SpriteCache, self).setColor(arg0)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.dispose()"""
        super(SpriteCache, self).dispose()

    @overload
    def getProjectionMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.SpriteCache.getProjectionMatrix()"""
        return 'math.Matrix4'.__wrap(super(SpriteCache, self).getProjectionMatrix())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setProjectionMatrix(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.setProjectionMatrix(com.badlogic.gdx.math.Matrix4)"""
        super(__SpriteCache, self).setProjectionMatrix(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: int, arg1: 'ShaderProgram', arg2: bool):
        """public com.badlogic.gdx.graphics.g2d.SpriteCache(int,com.badlogic.gdx.graphics.glutils.ShaderProgram,boolean)"""
        val = __SpriteCache(__int.valueOf(arg0), arg1, __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.begin()"""
        super(SpriteCache, self).begin()

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.SpriteCache.getColor()"""
        return 'graphics.Color'.__wrap(super(SpriteCache, self).getColor())

    @overload
    def setShader(self, arg0: 'ShaderProgram'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.setShader(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        super(__SpriteCache, self).setShader(arg0)

    @overload
    def __init__(self, arg0: int, arg1: bool):
        """public com.badlogic.gdx.graphics.g2d.SpriteCache(int,boolean)"""
        val = __SpriteCache(__int.valueOf(arg0), __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getPackedColor(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.SpriteCache.getPackedColor()"""
        return float.__wrap(super(SpriteCache, self).getPackedColor())

    @overload
    def getTransformMatrix(self) -> 'math.Matrix4':
        """public com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.SpriteCache.getTransformMatrix()"""
        return 'math.Matrix4'.__wrap(super(SpriteCache, self).getTransformMatrix())

    @overload
    def isDrawing(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.SpriteCache.isDrawing()"""
        return bool.__wrap(super(SpriteCache, self).isDrawing())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def add(self, arg0: 'Texture', arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.add(com.badlogic.gdx.graphics.Texture,float,float)"""
        super(__SpriteCache, self).add(arg0, __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def add(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: bool):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.add(com.badlogic.gdx.graphics.Texture,float,float,float,float,int,int,int,int,boolean,boolean)"""
        super(__SpriteCache, self).add(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __boolean.valueOf(arg9), __boolean.valueOf(arg10))

    @overload
    def setTransformMatrix(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.setTransformMatrix(com.badlogic.gdx.math.Matrix4)"""
        super(__SpriteCache, self).setTransformMatrix(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.SpriteCache()"""
        val = __SpriteCache()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def beginCache(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.beginCache()"""
        super(SpriteCache, self).beginCache()

    @overload
    def clear(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.clear()"""
        super(SpriteCache, self).clear()

    @overload
    def add(self, arg0: 'Texture', arg1: float, arg2: float, arg3: int, arg4: int, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.add(com.badlogic.gdx.graphics.Texture,float,float,int,int,float,float,float,float,float)"""
        super(__SpriteCache, self).add(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9))

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.setColor(float,float,float,float)"""
        super(__SpriteCache, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def setPackedColor(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.setPackedColor(float)"""
        super(__SpriteCache, self).setPackedColor(__float.valueOf(arg0))

    @overload
    def add(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.add(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,float,float,float,float)"""
        super(__SpriteCache, self).add(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9))

    @overload
    def draw(self, arg0: int, arg1: int, arg2: int):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.draw(int,int,int)"""
        super(__SpriteCache, self).draw(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2))

    @overload
    def endCache(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.SpriteCache.endCache()"""
        return int.__wrap(super(SpriteCache, self).endCache())

    @overload
    def add(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: int, arg11: int, arg12: int, arg13: int, arg14: bool, arg15: bool):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.add(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float,float,int,int,int,int,boolean,boolean)"""
        super(__SpriteCache, self).add(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), __float.valueOf(arg9), __int.valueOf(arg10), __int.valueOf(arg11), __int.valueOf(arg12), __int.valueOf(arg13), __boolean.valueOf(arg14), __boolean.valueOf(arg15))

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.SpriteCache()"""
        val = __SpriteCache()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getCustomShader(self) -> 'glutils.ShaderProgram':
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g2d.SpriteCache.getCustomShader()"""
        return 'glutils.ShaderProgram'.__wrap(super(SpriteCache, self).getCustomShader())

    @overload
    def add(self, arg0: 'Sprite'):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.add(com.badlogic.gdx.graphics.g2d.Sprite)"""
        super(__SpriteCache, self).add(arg0)

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.end()"""
        super(SpriteCache, self).end()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def add(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float):
        """public void com.badlogic.gdx.graphics.g2d.SpriteCache.add(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float)"""
        super(__SpriteCache, self).add(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PixmapPacker$Page
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.utils.OrderedMap as __OrderedMap
__OrderedMap = __OrderedMap
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Texture as __Texture
__Texture = __Texture
import com.badlogic.gdx.graphics.g2d.PixmapPacker as __PixmapPacker_Page
__Page = __PixmapPacker_Page.Page
import com.badlogic.gdx.graphics.Pixmap as __Pixmap
__Pixmap = __Pixmap
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class Page():
    """com.badlogic.gdx.graphics.g2d.PixmapPacker.Page"""
 
    @staticmethod
    def __wrap(java_value: __Page) -> 'Page':
        return Page(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Page):
        """
        Dynamic initializer for Page.
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
    def __init__(self, arg0: 'PixmapPacker'):
        """public com.badlogic.gdx.graphics.g2d.PixmapPacker$Page(com.badlogic.gdx.graphics.g2d.PixmapPacker)"""
        val = __Page(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def updateTexture(self, arg0: 'TextureFilter', arg1: 'TextureFilter', arg2: bool) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.PixmapPacker$Page.updateTexture(com.badlogic.gdx.graphics.Texture$TextureFilter,com.badlogic.gdx.graphics.Texture$TextureFilter,boolean)"""
        return bool.__wrap(super(__Page, self).updateTexture(arg0, arg1, __boolean.valueOf(arg2)))

    @overload
    def getRects(self) -> 'utils.OrderedMap':
        """public com.badlogic.gdx.utils.OrderedMap<java.lang.String, com.badlogic.gdx.graphics.g2d.PixmapPacker$PixmapPackerRectangle> com.badlogic.gdx.graphics.g2d.PixmapPacker$Page.getRects()"""
        return 'utils.OrderedMap'.__wrap(super(Page, self).getRects())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.graphics.g2d.PixmapPacker$Page.getTexture()"""
        return 'graphics.Texture'.__wrap(super(Page, self).getTexture())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getPixmap(self) -> 'graphics.Pixmap':
        """public com.badlogic.gdx.graphics.Pixmap com.badlogic.gdx.graphics.g2d.PixmapPacker$Page.getPixmap()"""
        return 'graphics.Pixmap'.__wrap(super(Page, self).getPixmap())

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.TextureRegion
from pyquantum_helper import import_once as __import_once__
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
from typing import List
import com.badlogic.gdx.graphics.g2d.TextureRegion as __TextureRegion
__TextureRegion = __TextureRegion
import java.lang.Long as __long
import java.lang.Float as __float
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
from builtins import int
 
class TextureRegion():
    """com.badlogic.gdx.graphics.g2d.TextureRegion"""
 
    @staticmethod
    def __wrap(java_value: __TextureRegion) -> 'TextureRegion':
        return TextureRegion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextureRegion):
        """
        Dynamic initializer for TextureRegion.
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
    def setRegion(self, arg0: 'Texture'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.Texture)"""
        super(__TextureRegion, self).setRegion(arg0)

    @overload
    def setV2(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setV2(float)"""
        super(__TextureRegion, self).setV2(__float.valueOf(arg0))

    @overload
    def getRegionHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionHeight()"""
        return int.__wrap(super(TextureRegion, self).getRegionHeight())

    @overload
    def getRegionX(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionX()"""
        return int.__wrap(super(TextureRegion, self).getRegionX())

    @overload
    def getV(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getV()"""
        return float.__wrap(super(TextureRegion, self).getV())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g2d.TextureRegion()"""
        val = __TextureRegion()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isFlipY(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.TextureRegion.isFlipY()"""
        return bool.__wrap(super(TextureRegion, self).isFlipY())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'TextureRegion'):
        """public com.badlogic.gdx.graphics.g2d.TextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = __TextureRegion(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def split(arg0: 'Texture', arg1: int, arg2: int) -> List[List['TextureRegion']]:
        """public static com.badlogic.gdx.graphics.g2d.TextureRegion[][] com.badlogic.gdx.graphics.g2d.TextureRegion.split(com.badlogic.gdx.graphics.Texture,int,int)"""
        return List[List[TextureRegion]].__wrap(__TextureRegion.split(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @overload
    def getU(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getU()"""
        return float.__wrap(super(TextureRegion, self).getU())

    @overload
    def getRegionWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionWidth()"""
        return int.__wrap(super(TextureRegion, self).getRegionWidth())

    @overload
    def __init__(self, arg0: 'Texture'):
        """public com.badlogic.gdx.graphics.g2d.TextureRegion(com.badlogic.gdx.graphics.Texture)"""
        val = __TextureRegion(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setRegion(self, arg0: 'TextureRegion', arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.g2d.TextureRegion,int,int,int,int)"""
        super(__TextureRegion, self).setRegion(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @overload
    def __init__(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float):
        """public com.badlogic.gdx.graphics.g2d.TextureRegion(com.badlogic.gdx.graphics.Texture,float,float,float,float)"""
        val = __TextureRegion(arg0, __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def split(self, arg0: int, arg1: int) -> List[List['TextureRegion']]:
        """public com.badlogic.gdx.graphics.g2d.TextureRegion[][] com.badlogic.gdx.graphics.g2d.TextureRegion.split(int,int)"""
        return List[List['TextureRegion']].__wrap(super(__TextureRegion, self).split(__int.valueOf(arg0), __int.valueOf(arg1)))

    @overload
    def setRegion(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(float,float,float,float)"""
        super(__TextureRegion, self).setRegion(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def getRegionY(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionY()"""
        return int.__wrap(super(TextureRegion, self).getRegionY())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.graphics.g2d.TextureRegion.getTexture()"""
        return 'graphics.Texture'.__wrap(super(TextureRegion, self).getTexture())

    @overload
    def setTexture(self, arg0: 'Texture'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setTexture(com.badlogic.gdx.graphics.Texture)"""
        super(__TextureRegion, self).setTexture(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setRegionHeight(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionHeight(int)"""
        super(__TextureRegion, self).setRegionHeight(__int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setRegionX(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionX(int)"""
        super(__TextureRegion, self).setRegionX(__int.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g2d.TextureRegion()"""
        val = __TextureRegion()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setV(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setV(float)"""
        super(__TextureRegion, self).setV(__float.valueOf(arg0))

    @overload
    def setU2(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setU2(float)"""
        super(__TextureRegion, self).setU2(__float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setRegionY(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionY(int)"""
        super(__TextureRegion, self).setRegionY(__int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setU(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setU(float)"""
        super(__TextureRegion, self).setU(__float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'Texture', arg1: int, arg2: int, arg3: int, arg4: int):
        """public com.badlogic.gdx.graphics.g2d.TextureRegion(com.badlogic.gdx.graphics.Texture,int,int,int,int)"""
        val = __TextureRegion(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(__TextureRegion, self).setRegion(arg0)

    @overload
    def __init__(self, arg0: 'Texture', arg1: int, arg2: int):
        """public com.badlogic.gdx.graphics.g2d.TextureRegion(com.badlogic.gdx.graphics.Texture,int,int)"""
        val = __TextureRegion(arg0, __int.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def scroll(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.scroll(float,float)"""
        super(__TextureRegion, self).scroll(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def setRegion(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(int,int,int,int)"""
        super(__TextureRegion, self).setRegion(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @overload
    def isFlipX(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.TextureRegion.isFlipX()"""
        return bool.__wrap(super(TextureRegion, self).isFlipX())

    @overload
    def flip(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.flip(boolean,boolean)"""
        super(__TextureRegion, self).flip(__boolean.valueOf(arg0), __boolean.valueOf(arg1))

    @overload
    def getU2(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getU2()"""
        return float.__wrap(super(TextureRegion, self).getU2())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setRegionWidth(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionWidth(int)"""
        super(__TextureRegion, self).setRegionWidth(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'TextureRegion', arg1: int, arg2: int, arg3: int, arg4: int):
        """public com.badlogic.gdx.graphics.g2d.TextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion,int,int,int,int)"""
        val = __TextureRegion(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getV2(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getV2()"""
        return float.__wrap(super(TextureRegion, self).getV2()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.Animation$PlayMode
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import com.badlogic.gdx.graphics.g2d.Animation as __Animation_PlayMode
__PlayMode = __Animation_PlayMode.PlayMode
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
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
 
class PlayMode():
    """com.badlogic.gdx.graphics.g2d.Animation.PlayMode"""
 
    @staticmethod
    def __wrap(java_value: __PlayMode) -> 'PlayMode':
        return PlayMode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PlayMode):
        """
        Dynamic initializer for PlayMode.
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

    @staticmethod
    @overload
    def values() -> List['PlayMode']:
        """public static com.badlogic.gdx.graphics.g2d.Animation$PlayMode[] com.badlogic.gdx.graphics.g2d.Animation$PlayMode.values()"""
        return List[PlayMode].__wrap(__PlayMode.values())

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
    def valueOf(arg0: str) -> 'PlayMode':
        """public static com.badlogic.gdx.graphics.g2d.Animation$PlayMode com.badlogic.gdx.graphics.g2d.Animation$PlayMode.valueOf(java.lang.String)"""
        return PlayMode.__wrap(__PlayMode.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.graphics.g2d.TextureAtlas as __TextureAtlas_AtlasRegion
__AtlasRegion = __TextureAtlas_AtlasRegion.AtlasRegion
from typing import List
import com.badlogic.gdx.graphics.g2d.TextureRegion as __TextureRegion
__TextureRegion = __TextureRegion
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
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
 
class AtlasRegion():
    """com.badlogic.gdx.graphics.g2d.TextureAtlas.AtlasRegion"""
 
    @staticmethod
    def __wrap(java_value: __AtlasRegion) -> 'AtlasRegion':
        return AtlasRegion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AtlasRegion):
        """
        Dynamic initializer for AtlasRegion.
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
    def setU(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setU(float)"""
        super(__TextureRegion, self).setU(__float.valueOf(arg0))

    @override
    @overload
    def getV(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getV()"""
        return float.__wrap(super(TextureRegion, self).getV())

    @override
    @overload
    def getV2(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getV2()"""
        return float.__wrap(super(TextureRegion, self).getV2())

    @override
    @overload
    def setU2(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setU2(float)"""
        super(__TextureRegion, self).setU2(__float.valueOf(arg0))

    @overload
    def getRotatedPackedHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion.getRotatedPackedHeight()"""
        return float.__wrap(super(AtlasRegion, self).getRotatedPackedHeight())

    @override
    @overload
    def setRegionHeight(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionHeight(int)"""
        super(__TextureRegion, self).setRegionHeight(__int.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def findValue(self, arg0: str) -> List[int]:
        """public int[] com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion.findValue(java.lang.String)"""
        return List[int].__wrap(super(__AtlasRegion, self).findValue(arg0))

    @override
    @overload
    def isFlipY(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.TextureRegion.isFlipY()"""
        return bool.__wrap(super(TextureRegion, self).isFlipY())

    @staticmethod
    @overload
    def split(arg0: 'Texture', arg1: int, arg2: int) -> List[List['TextureRegion']]:
        """public static com.badlogic.gdx.graphics.g2d.TextureRegion[][] com.badlogic.gdx.graphics.g2d.TextureRegion.split(com.badlogic.gdx.graphics.Texture,int,int)"""
        return List[List[TextureRegion]].__wrap(__TextureRegion.split(arg0, __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.graphics.g2d.TextureRegion.getTexture()"""
        return 'graphics.Texture'.__wrap(super(TextureRegion, self).getTexture())

    @overload
    def split(self, arg0: int, arg1: int) -> List[List['TextureRegion']]:
        """public com.badlogic.gdx.graphics.g2d.TextureRegion[][] com.badlogic.gdx.graphics.g2d.TextureRegion.split(int,int)"""
        return List[List['TextureRegion']].__wrap(super(__TextureRegion, self).split(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setRegionX(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionX(int)"""
        super(__TextureRegion, self).setRegionX(__int.valueOf(arg0))

    @override
    @overload
    def getU(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getU()"""
        return float.__wrap(super(TextureRegion, self).getU())

    @override
    @overload
    def setRegion(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(float,float,float,float)"""
        super(__TextureRegion, self).setRegion(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def setTexture(self, arg0: 'Texture'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setTexture(com.badlogic.gdx.graphics.Texture)"""
        super(__TextureRegion, self).setTexture(arg0)

    @override
    @overload
    def getU2(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureRegion.getU2()"""
        return float.__wrap(super(TextureRegion, self).getU2())

    @overload
    def __init__(self, arg0: 'TextureRegion'):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = __AtlasRegion(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setRegion(self, arg0: 'Texture'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.Texture)"""
        super(__TextureRegion, self).setRegion(arg0)

    @override
    @overload
    def setRegion(self, arg0: 'TextureRegion', arg1: int, arg2: int, arg3: int, arg4: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.g2d.TextureRegion,int,int,int,int)"""
        super(__TextureRegion, self).setRegion(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))

    @override
    @overload
    def getRegionX(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionX()"""
        return int.__wrap(super(TextureRegion, self).getRegionX())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def flip(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion.flip(boolean,boolean)"""
        super(__AtlasRegion, self).flip(__boolean.valueOf(arg0), __boolean.valueOf(arg1))

    @override
    @overload
    def getRegionWidth(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionWidth()"""
        return int.__wrap(super(TextureRegion, self).getRegionWidth())

    @override
    @overload
    def getRegionY(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionY()"""
        return int.__wrap(super(TextureRegion, self).getRegionY())

    @override
    @overload
    def isFlipX(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.TextureRegion.isFlipX()"""
        return bool.__wrap(super(TextureRegion, self).isFlipX())

    @override
    @overload
    def scroll(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.scroll(float,float)"""
        super(__TextureRegion, self).scroll(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def getRotatedPackedWidth(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion.getRotatedPackedWidth()"""
        return float.__wrap(super(AtlasRegion, self).getRotatedPackedWidth())

    @override
    @overload
    def setRegionWidth(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionWidth(int)"""
        super(__TextureRegion, self).setRegionWidth(__int.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Texture', arg1: int, arg2: int, arg3: int, arg4: int):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion(com.badlogic.gdx.graphics.Texture,int,int,int,int)"""
        val = __AtlasRegion(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion.toString()"""
        return str.__wrap(super(AtlasRegion, self).toString())

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
    def setRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(__TextureRegion, self).setRegion(arg0)

    @overload
    def __init__(self, arg0: 'AtlasRegion'):
        """public com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion(com.badlogic.gdx.graphics.g2d.TextureAtlas$AtlasRegion)"""
        val = __AtlasRegion(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setV(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setV(float)"""
        super(__TextureRegion, self).setV(__float.valueOf(arg0))

    @override
    @overload
    def setRegionY(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegionY(int)"""
        super(__TextureRegion, self).setRegionY(__int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setV2(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setV2(float)"""
        super(__TextureRegion, self).setV2(__float.valueOf(arg0))

    @override
    @overload
    def setRegion(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public void com.badlogic.gdx.graphics.g2d.TextureRegion.setRegion(int,int,int,int)"""
        super(__TextureRegion, self).setRegion(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))

    @override
    @overload
    def getRegionHeight(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.TextureRegion.getRegionHeight()"""
        return int.__wrap(super(TextureRegion, self).getRegionHeight()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.Batch
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.g2d.Batch as __Batch
__Batch = __Batch
from builtins import float
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

import com.badlogic.gdx.utils.Disposable as __Disposable
__Disposable = __Disposable
 
class Batch(ABC):
    """com.badlogic.gdx.graphics.g2d.Batch"""
 
    @staticmethod
    def __wrap(java_value: __Batch) -> 'Batch':
        return Batch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Batch):
        """
        Dynamic initializer for Batch.
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
 
    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: bool):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,int,int,int,int,boolean,boolean)"""
        pass

    @abstractmethod
    def enableBlending(self, ):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.enableBlending()"""
        pass

    @abstractmethod
    def setColor(self, arg0: 'Color'):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setColor(com.badlogic.gdx.graphics.Color)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float,float)"""
        pass

    @abstractmethod
    def getTransformMatrix(self, ):
        """public abstract com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.Batch.getTransformMatrix()"""
        pass

    @abstractmethod
    def begin(self, ):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.begin()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: bool):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,float,float,float,float,boolean)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float)"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.utils.Disposable.dispose()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float)"""
        pass

    @abstractmethod
    def getShader(self, ):
        """public abstract com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g2d.Batch.getShader()"""
        pass

    @abstractmethod
    def getBlendDstFunc(self, ):
        """public abstract int com.badlogic.gdx.graphics.g2d.Batch.getBlendDstFunc()"""
        pass

    @abstractmethod
    def getColor(self, ):
        """public abstract com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.Batch.getColor()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: 'Affine2'):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,com.badlogic.gdx.math.Affine2)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,float,float,float,float)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float,float,int,int,int,int)"""
        pass

    @abstractmethod
    def getProjectionMatrix(self, ):
        """public abstract com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.Batch.getProjectionMatrix()"""
        pass

    @abstractmethod
    def isDrawing(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.g2d.Batch.isDrawing()"""
        pass

    @abstractmethod
    def getBlendSrcFuncAlpha(self, ):
        """public abstract int com.badlogic.gdx.graphics.g2d.Batch.getBlendSrcFuncAlpha()"""
        pass

    @abstractmethod
    def setBlendFunctionSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setBlendFunctionSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def setProjectionMatrix(self, arg0: 'Matrix4'):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setProjectionMatrix(com.badlogic.gdx.math.Matrix4)"""
        pass

    @abstractmethod
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setColor(float,float,float,float)"""
        pass

    @abstractmethod
    def setPackedColor(self, arg0: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setPackedColor(float)"""
        pass

    @abstractmethod
    def getBlendSrcFunc(self, ):
        """public abstract int com.badlogic.gdx.graphics.g2d.Batch.getBlendSrcFunc()"""
        pass

    @abstractmethod
    def disableBlending(self, ):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.disableBlending()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: int, arg11: int, arg12: int, arg13: int, arg14: bool, arg15: bool):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float,float,int,int,int,int,boolean,boolean)"""
        pass

    @abstractmethod
    def setShader(self, arg0: 'ShaderProgram'):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setShader(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float)"""
        pass

    @abstractmethod
    def flush(self, ):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.flush()"""
        pass

    @abstractmethod
    def setTransformMatrix(self, arg0: 'Matrix4'):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setTransformMatrix(com.badlogic.gdx.math.Matrix4)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: 'float', arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float[],int,int)"""
        pass

    @abstractmethod
    def isBlendingEnabled(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.g2d.Batch.isBlendingEnabled()"""
        pass

    @abstractmethod
    def setBlendFunction(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setBlendFunction(int,int)"""
        pass

    @abstractmethod
    def getBlendDstFuncAlpha(self, ):
        """public abstract int com.badlogic.gdx.graphics.g2d.Batch.getBlendDstFuncAlpha()"""
        pass

    @abstractmethod
    def getPackedColor(self, ):
        """public abstract float com.badlogic.gdx.graphics.g2d.Batch.getPackedColor()"""
        pass

    @abstractmethod
    def end(self, ):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.end()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PolygonBatch
from pyquantum_helper import import_once as __import_once__
from builtins import float
import com.badlogic.gdx.graphics.g2d.Batch as __Batch
__Batch = __Batch
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import com.badlogic.gdx.graphics.g2d.PolygonBatch as __PolygonBatch
__PolygonBatch = __PolygonBatch
from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

import com.badlogic.gdx.utils.Disposable as __Disposable
__Disposable = __Disposable
from builtins import int
 
class PolygonBatch(ABC):
    """com.badlogic.gdx.graphics.g2d.PolygonBatch"""
 
    @staticmethod
    def __wrap(java_value: __PolygonBatch) -> 'PolygonBatch':
        return PolygonBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PolygonBatch):
        """
        Dynamic initializer for PolygonBatch.
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
 
    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: int, arg7: int, arg8: int, arg9: bool, arg10: bool):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,int,int,int,int,boolean,boolean)"""
        pass

    @abstractmethod
    def enableBlending(self, ):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.enableBlending()"""
        pass

    @abstractmethod
    def setColor(self, arg0: 'Color'):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setColor(com.badlogic.gdx.graphics.Color)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float,float)"""
        pass

    @abstractmethod
    def getTransformMatrix(self, ):
        """public abstract com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.Batch.getTransformMatrix()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'PolygonRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.PolygonBatch.draw(com.badlogic.gdx.graphics.g2d.PolygonRegion,float,float,float,float,float,float,float,float,float)"""
        pass

    @abstractmethod
    def begin(self, ):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.begin()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: bool):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,float,float,float,float,boolean)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float)"""
        pass

    @abstractmethod
    def dispose(self, ):
        """public abstract void com.badlogic.gdx.utils.Disposable.dispose()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float)"""
        pass

    @abstractmethod
    def getShader(self, ):
        """public abstract com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g2d.Batch.getShader()"""
        pass

    @abstractmethod
    def getBlendDstFunc(self, ):
        """public abstract int com.badlogic.gdx.graphics.g2d.Batch.getBlendDstFunc()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'PolygonRegion', arg1: float, arg2: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.PolygonBatch.draw(com.badlogic.gdx.graphics.g2d.PolygonRegion,float,float)"""
        pass

    @abstractmethod
    def getColor(self, ):
        """public abstract com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.Batch.getColor()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: 'Affine2'):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,com.badlogic.gdx.math.Affine2)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'TextureRegion', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.g2d.TextureRegion,float,float,float,float,float,float,float,float,float)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: int, arg4: int, arg5: int, arg6: int):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float,float,int,int,int,int)"""
        pass

    @abstractmethod
    def getProjectionMatrix(self, ):
        """public abstract com.badlogic.gdx.math.Matrix4 com.badlogic.gdx.graphics.g2d.Batch.getProjectionMatrix()"""
        pass

    @abstractmethod
    def isDrawing(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.g2d.Batch.isDrawing()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'PolygonRegion', arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.PolygonBatch.draw(com.badlogic.gdx.graphics.g2d.PolygonRegion,float,float,float,float)"""
        pass

    @abstractmethod
    def getBlendSrcFuncAlpha(self, ):
        """public abstract int com.badlogic.gdx.graphics.g2d.Batch.getBlendSrcFuncAlpha()"""
        pass

    @abstractmethod
    def setBlendFunctionSeparate(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setBlendFunctionSeparate(int,int,int,int)"""
        pass

    @abstractmethod
    def setProjectionMatrix(self, arg0: 'Matrix4'):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setProjectionMatrix(com.badlogic.gdx.math.Matrix4)"""
        pass

    @abstractmethod
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setColor(float,float,float,float)"""
        pass

    @abstractmethod
    def setPackedColor(self, arg0: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setPackedColor(float)"""
        pass

    @abstractmethod
    def getBlendSrcFunc(self, ):
        """public abstract int com.badlogic.gdx.graphics.g2d.Batch.getBlendSrcFunc()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: 'float', arg2: int, arg3: int, arg4: 'short', arg5: int, arg6: int):
        """public abstract void com.badlogic.gdx.graphics.g2d.PolygonBatch.draw(com.badlogic.gdx.graphics.Texture,float[],int,int,short[],int,int)"""
        pass

    @abstractmethod
    def disableBlending(self, ):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.disableBlending()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: int, arg11: int, arg12: int, arg13: int, arg14: bool, arg15: bool):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float,float,float,float,float,float,int,int,int,int,boolean,boolean)"""
        pass

    @abstractmethod
    def setShader(self, arg0: 'ShaderProgram'):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setShader(com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: float, arg2: float, arg3: float, arg4: float):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float,float,float,float)"""
        pass

    @abstractmethod
    def flush(self, ):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.flush()"""
        pass

    @abstractmethod
    def setTransformMatrix(self, arg0: 'Matrix4'):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setTransformMatrix(com.badlogic.gdx.math.Matrix4)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'Texture', arg1: 'float', arg2: int, arg3: int):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.draw(com.badlogic.gdx.graphics.Texture,float[],int,int)"""
        pass

    @abstractmethod
    def isBlendingEnabled(self, ):
        """public abstract boolean com.badlogic.gdx.graphics.g2d.Batch.isBlendingEnabled()"""
        pass

    @abstractmethod
    def setBlendFunction(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.setBlendFunction(int,int)"""
        pass

    @abstractmethod
    def getBlendDstFuncAlpha(self, ):
        """public abstract int com.badlogic.gdx.graphics.g2d.Batch.getBlendDstFuncAlpha()"""
        pass

    @abstractmethod
    def getPackedColor(self, ):
        """public abstract float com.badlogic.gdx.graphics.g2d.Batch.getPackedColor()"""
        pass

    @abstractmethod
    def end(self, ):
        """public abstract void com.badlogic.gdx.graphics.g2d.Batch.end()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpriteMode
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
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_SpriteMode
__SpriteMode = __ParticleEmitter_SpriteMode.SpriteMode
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class SpriteMode():
    """com.badlogic.gdx.graphics.g2d.ParticleEmitter.SpriteMode"""
 
    @staticmethod
    def __wrap(java_value: __SpriteMode) -> 'SpriteMode':
        return SpriteMode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SpriteMode):
        """
        Dynamic initializer for SpriteMode.
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
    def values() -> List['SpriteMode']:
        """public static com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpriteMode[] com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpriteMode.values()"""
        return List[SpriteMode].__wrap(__SpriteMode.values())

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'SpriteMode':
        """public static com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpriteMode com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpriteMode.valueOf(java.lang.String)"""
        return SpriteMode.__wrap(__SpriteMode.valueOf(arg0))

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
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.DistanceFieldFont
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
import com.badlogic.gdx.graphics.g2d.DistanceFieldFont as __DistanceFieldFont
__DistanceFieldFont = __DistanceFieldFont
import com.badlogic.gdx.graphics.glutils.ShaderProgram as __ShaderProgram
__ShaderProgram = __ShaderProgram
import java.lang.Boolean as __boolean
from builtins import type
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __string
import com.badlogic.gdx.graphics.g2d.BitmapFontCache as __BitmapFontCache
__BitmapFontCache = __BitmapFontCache
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

from builtins import bool
import com.badlogic.gdx.graphics.g2d.GlyphLayout as __GlyphLayout
__GlyphLayout = __GlyphLayout
from builtins import str
import java.lang.CharSequence as CharSequence
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import float
import com.badlogic.gdx.graphics.g2d.TextureRegion as __TextureRegion
__TextureRegion = __TextureRegion
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

import com.badlogic.gdx.graphics.g2d.BitmapFont as __BitmapFont_BitmapFontData
__BitmapFontData = __BitmapFont_BitmapFontData.BitmapFontData
import com.badlogic.gdx.graphics.g2d.BitmapFont as __BitmapFont
__BitmapFont = __BitmapFont
from builtins import int
 
class DistanceFieldFont():
    """com.badlogic.gdx.graphics.g2d.DistanceFieldFont"""
 
    @staticmethod
    def __wrap(java_value: __DistanceFieldFont) -> 'DistanceFieldFont':
        return DistanceFieldFont(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DistanceFieldFont):
        """
        Dynamic initializer for DistanceFieldFont.
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
    def draw(self, arg0: 'Batch', arg1: 'GlyphLayout', arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.draw(com.badlogic.gdx.graphics.g2d.Batch,com.badlogic.gdx.graphics.g2d.GlyphLayout,float,float)"""
        super(__BitmapFont, self).draw(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g2d.BitmapFont.getColor()"""
        return 'graphics.Color'.__wrap(super(BitmapFont, self).getColor())

    @override
    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.setColor(float,float,float,float)"""
        super(__BitmapFont, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def getRegion(self, arg0: int) -> 'TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.graphics.g2d.BitmapFont.getRegion(int)"""
        return 'TextureRegion'.__wrap(super(__BitmapFont, self).getRegion(__int.valueOf(arg0)))

    @override
    @overload
    def isFlipped(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.BitmapFont.isFlipped()"""
        return bool.__wrap(super(BitmapFont, self).isFlipped())

    @override
    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getScaleY()"""
        return float.__wrap(super(BitmapFont, self).getScaleY())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'TextureRegion', arg2: bool):
        """public com.badlogic.gdx.graphics.g2d.DistanceFieldFont(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g2d.TextureRegion,boolean)"""
        val = __DistanceFieldFont(arg0, arg1, __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'TextureRegion'):
        """public com.badlogic.gdx.graphics.g2d.DistanceFieldFont(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = __DistanceFieldFont(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def draw(self, arg0: 'Batch', arg1: 'CharSequence', arg2: float, arg3: float, arg4: int, arg5: int, arg6: float, arg7: int, arg8: bool) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFont.draw(com.badlogic.gdx.graphics.g2d.Batch,java.lang.CharSequence,float,float,int,int,float,int,boolean)"""
        return 'GlyphLayout'.__wrap(super(__BitmapFont, self).draw(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __float.valueOf(arg6), __int.valueOf(arg7), __boolean.valueOf(arg8)))

    @override
    @overload
    def getLineHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getLineHeight()"""
        return float.__wrap(super(BitmapFont, self).getLineHeight())

    @override
    @overload
    def setOwnsTexture(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.setOwnsTexture(boolean)"""
        super(__BitmapFont, self).setOwnsTexture(__boolean.valueOf(arg0))

    @override
    @overload
    def usesIntegerPositions(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.BitmapFont.usesIntegerPositions()"""
        return bool.__wrap(super(BitmapFont, self).usesIntegerPositions())

    @override
    @overload
    def newFontCache(self) -> 'BitmapFontCache':
        """public com.badlogic.gdx.graphics.g2d.BitmapFontCache com.badlogic.gdx.graphics.g2d.DistanceFieldFont.newFontCache()"""
        return 'BitmapFontCache'.__wrap(super(DistanceFieldFont, self).newFontCache())

    @override
    @overload
    def getCapHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getCapHeight()"""
        return float.__wrap(super(BitmapFont, self).getCapHeight())

    @override
    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getScaleX()"""
        return float.__wrap(super(BitmapFont, self).getScaleX())

    @override
    @overload
    def getRegion(self) -> 'TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.graphics.g2d.BitmapFont.getRegion()"""
        return 'TextureRegion'.__wrap(super(BitmapFont, self).getRegion())

    @overload
    def draw(self, arg0: 'Batch', arg1: 'CharSequence', arg2: float, arg3: float) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFont.draw(com.badlogic.gdx.graphics.g2d.Batch,java.lang.CharSequence,float,float)"""
        return 'GlyphLayout'.__wrap(super(__BitmapFont, self).draw(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3)))

    @override
    @overload
    def getCache(self) -> 'BitmapFontCache':
        """public com.badlogic.gdx.graphics.g2d.BitmapFontCache com.badlogic.gdx.graphics.g2d.BitmapFont.getCache()"""
        return 'BitmapFontCache'.__wrap(super(BitmapFont, self).getCache())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setUseIntegerPositions(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.setUseIntegerPositions(boolean)"""
        super(__BitmapFont, self).setUseIntegerPositions(__boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle', arg2: bool, arg3: bool):
        """public com.badlogic.gdx.graphics.g2d.DistanceFieldFont(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,boolean,boolean)"""
        val = __DistanceFieldFont(arg0, arg1, __boolean.valueOf(arg2), __boolean.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'BitmapFontData', arg1: 'Array', arg2: bool):
        """public com.badlogic.gdx.graphics.g2d.DistanceFieldFont(com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.TextureRegion>,boolean)"""
        val = __DistanceFieldFont(arg0, arg1, __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'FileHandle', arg2: bool):
        """public com.badlogic.gdx.graphics.g2d.DistanceFieldFont(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.files.FileHandle,boolean)"""
        val = __DistanceFieldFont(arg0, arg1, __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def createDistanceFieldShader() -> 'glutils.ShaderProgram':
        """public static com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g2d.DistanceFieldFont.createDistanceFieldShader()"""
        return glutils.ShaderProgram.__wrap(__DistanceFieldFont.createDistanceFieldShader())

    @overload
    def __init__(self, arg0: 'BitmapFontData', arg1: 'TextureRegion', arg2: bool):
        """public com.badlogic.gdx.graphics.g2d.DistanceFieldFont(com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData,com.badlogic.gdx.graphics.g2d.TextureRegion,boolean)"""
        val = __DistanceFieldFont(arg0, arg1, __boolean.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getAscent(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getAscent()"""
        return float.__wrap(super(BitmapFont, self).getAscent())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g2d.BitmapFont.toString()"""
        return str.__wrap(super(BitmapFont, self).toString())

    @override
    @overload
    def getRegions(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.TextureRegion> com.badlogic.gdx.graphics.g2d.BitmapFont.getRegions()"""
        return 'utils.Array'.__wrap(super(BitmapFont, self).getRegions())

    @overload
    def draw(self, arg0: 'Batch', arg1: 'CharSequence', arg2: float, arg3: float, arg4: float, arg5: int, arg6: bool) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFont.draw(com.badlogic.gdx.graphics.g2d.Batch,java.lang.CharSequence,float,float,float,int,boolean)"""
        return 'GlyphLayout'.__wrap(super(__BitmapFont, self).draw(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __int.valueOf(arg5), __boolean.valueOf(arg6)))

    @override
    @overload
    def setFixedWidthGlyphs(self, arg0: 'CharSequence'):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.setFixedWidthGlyphs(java.lang.CharSequence)"""
        super(__BitmapFont, self).setFixedWidthGlyphs(arg0)

    @override
    @overload
    def getSpaceXadvance(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getSpaceXadvance()"""
        return float.__wrap(super(BitmapFont, self).getSpaceXadvance())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getData(self) -> 'BitmapFontData':
        """public com.badlogic.gdx.graphics.g2d.BitmapFont$BitmapFontData com.badlogic.gdx.graphics.g2d.BitmapFont.getData()"""
        return 'BitmapFontData'.__wrap(super(BitmapFont, self).getData())

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: bool):
        """public com.badlogic.gdx.graphics.g2d.DistanceFieldFont(com.badlogic.gdx.files.FileHandle,boolean)"""
        val = __DistanceFieldFont(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setDistanceFieldSmoothing(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.DistanceFieldFont.setDistanceFieldSmoothing(float)"""
        super(__DistanceFieldFont, self).setDistanceFieldSmoothing(__float.valueOf(arg0))

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__BitmapFont, self).setColor(arg0)

    @override
    @overload
    def ownsTexture(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.BitmapFont.ownsTexture()"""
        return bool.__wrap(super(BitmapFont, self).ownsTexture())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g2d.BitmapFont.dispose()"""
        super(BitmapFont, self).dispose()

    @overload
    def draw(self, arg0: 'Batch', arg1: 'CharSequence', arg2: float, arg3: float, arg4: int, arg5: int, arg6: float, arg7: int, arg8: bool, arg9: str) -> 'GlyphLayout':
        """public com.badlogic.gdx.graphics.g2d.GlyphLayout com.badlogic.gdx.graphics.g2d.BitmapFont.draw(com.badlogic.gdx.graphics.g2d.Batch,java.lang.CharSequence,float,float,int,int,float,int,boolean,java.lang.String)"""
        return 'GlyphLayout'.__wrap(super(__BitmapFont, self).draw(arg0, arg1, __float.valueOf(arg2), __float.valueOf(arg3), __int.valueOf(arg4), __int.valueOf(arg5), __float.valueOf(arg6), __int.valueOf(arg7), __boolean.valueOf(arg8), arg9))

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
    def getXHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getXHeight()"""
        return float.__wrap(super(BitmapFont, self).getXHeight())

    @override
    @overload
    def getDescent(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.BitmapFont.getDescent()"""
        return float.__wrap(super(BitmapFont, self).getDescent())

    @overload
    def __init__(self, arg0: 'FileHandle'):
        """public com.badlogic.gdx.graphics.g2d.DistanceFieldFont(com.badlogic.gdx.files.FileHandle)"""
        val = __DistanceFieldFont(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getDistanceFieldSmoothing(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.DistanceFieldFont.getDistanceFieldSmoothing()"""
        return float.__wrap(super(DistanceFieldFont, self).getDistanceFieldSmoothing()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g2d.PixmapPacker$PixmapPackerRectangle
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.math.Vector2 as __Vector2
__Vector2 = __Vector2
import com.badlogic.gdx.math.Rectangle as __Rectangle
__Rectangle = __Rectangle
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import com.badlogic.gdx.graphics.g2d.PixmapPacker as __PixmapPacker_PixmapPackerRectangle
__PixmapPackerRectangle = __PixmapPacker_PixmapPackerRectangle.PixmapPackerRectangle
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PixmapPackerRectangle():
    """com.badlogic.gdx.graphics.g2d.PixmapPacker.PixmapPackerRectangle"""
 
    @staticmethod
    def __wrap(java_value: __PixmapPackerRectangle) -> 'PixmapPackerRectangle':
        return PixmapPackerRectangle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PixmapPackerRectangle):
        """
        Dynamic initializer for PixmapPackerRectangle.
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
    def fromString(self, arg0: str) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.fromString(java.lang.String)"""
        return 'math.Rectangle'.__wrap(super(__math.Rectangle, self).fromString(arg0))

    @overload
    def contains(self, arg0: 'Rectangle') -> bool:
        """public boolean com.badlogic.gdx.math.Rectangle.contains(com.badlogic.gdx.math.Rectangle)"""
        return bool.__wrap(super(__math.Rectangle, self).contains(arg0))

    @overload
    def merge(self, arg0: 'Rectangle') -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.merge(com.badlogic.gdx.math.Rectangle)"""
        return 'math.Rectangle'.__wrap(super(__math.Rectangle, self).merge(arg0))

    @override
    @overload
    def getAspectRatio(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.getAspectRatio()"""
        return float.__wrap(super(math.Rectangle, self).getAspectRatio())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def contains(self, arg0: float, arg1: float) -> bool:
        """public boolean com.badlogic.gdx.math.Rectangle.contains(float,float)"""
        return bool.__wrap(super(__math.Rectangle, self).contains(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.getY()"""
        return float.__wrap(super(math.Rectangle, self).getY())

    @overload
    def setHeight(self, arg0: float) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setHeight(float)"""
        return 'math.Rectangle'.__wrap(super(__math.Rectangle, self).setHeight(__float.valueOf(arg0)))

    @overload
    def overlaps(self, arg0: 'Rectangle') -> bool:
        """public boolean com.badlogic.gdx.math.Rectangle.overlaps(com.badlogic.gdx.math.Rectangle)"""
        return bool.__wrap(super(__math.Rectangle, self).overlaps(arg0))

    @overload
    def merge(self, arg0: float, arg1: float) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.merge(float,float)"""
        return 'math.Rectangle'.__wrap(super(__math.Rectangle, self).merge(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def setX(self, arg0: float) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setX(float)"""
        return 'math.Rectangle'.__wrap(super(__math.Rectangle, self).setX(__float.valueOf(arg0)))

    @override
    @overload
    def area(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.area()"""
        return float.__wrap(super(math.Rectangle, self).area())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setY(self, arg0: float) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setY(float)"""
        return 'math.Rectangle'.__wrap(super(__math.Rectangle, self).setY(__float.valueOf(arg0)))

    @overload
    def merge(self, arg0: 'Vector2') -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.merge(com.badlogic.gdx.math.Vector2[])"""
        return 'math.Rectangle'.__wrap(super(__math.Rectangle, self).merge(arg0))

    @override
    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.getX()"""
        return float.__wrap(super(math.Rectangle, self).getX())

    @overload
    def getCenter(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Rectangle.getCenter(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__math.Rectangle, self).getCenter(arg0))

    @overload
    def fitOutside(self, arg0: 'Rectangle') -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.fitOutside(com.badlogic.gdx.math.Rectangle)"""
        return 'math.Rectangle'.__wrap(super(__math.Rectangle, self).fitOutside(arg0))

    @overload
    def setWidth(self, arg0: float) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setWidth(float)"""
        return 'math.Rectangle'.__wrap(super(__math.Rectangle, self).setWidth(__float.valueOf(arg0)))

    @overload
    def getPosition(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Rectangle.getPosition(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__math.Rectangle, self).getPosition(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.math.Rectangle.equals(java.lang.Object)"""
        return bool.__wrap(super(__math.Rectangle, self).equals(arg0))

    @overload
    def getSize(self, arg0: 'Vector2') -> 'math.Vector2':
        """public com.badlogic.gdx.math.Vector2 com.badlogic.gdx.math.Rectangle.getSize(com.badlogic.gdx.math.Vector2)"""
        return 'math.Vector2'.__wrap(super(__math.Rectangle, self).getSize(arg0))

    @overload
    def set(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.set(float,float,float,float)"""
        return 'math.Rectangle'.__wrap(super(__math.Rectangle, self).set(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @overload
    def set(self, arg0: 'Rectangle') -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.set(com.badlogic.gdx.math.Rectangle)"""
        return 'math.Rectangle'.__wrap(super(__math.Rectangle, self).set(arg0))

    @overload
    def contains(self, arg0: 'Vector2') -> bool:
        """public boolean com.badlogic.gdx.math.Rectangle.contains(com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__math.Rectangle, self).contains(arg0))

    @overload
    def merge(self, arg0: 'Vector2') -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.merge(com.badlogic.gdx.math.Vector2)"""
        return 'math.Rectangle'.__wrap(super(__math.Rectangle, self).merge(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.math.Rectangle.hashCode()"""
        return int.__wrap(super(math.Rectangle, self).hashCode())

    @overload
    def setCenter(self, arg0: 'Vector2') -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setCenter(com.badlogic.gdx.math.Vector2)"""
        return 'math.Rectangle'.__wrap(super(__math.Rectangle, self).setCenter(arg0))

    @override
    @overload
    def getHeight(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.getHeight()"""
        return float.__wrap(super(math.Rectangle, self).getHeight())

    @override
    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.getWidth()"""
        return float.__wrap(super(math.Rectangle, self).getWidth())

    @overload
    def setPosition(self, arg0: float, arg1: float) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setPosition(float,float)"""
        return 'math.Rectangle'.__wrap(super(__math.Rectangle, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def fitInside(self, arg0: 'Rectangle') -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.fitInside(com.badlogic.gdx.math.Rectangle)"""
        return 'math.Rectangle'.__wrap(super(__math.Rectangle, self).fitInside(arg0))

    @override
    @overload
    def perimeter(self) -> float:
        """public float com.badlogic.gdx.math.Rectangle.perimeter()"""
        return float.__wrap(super(math.Rectangle, self).perimeter())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setSize(self, arg0: float) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setSize(float)"""
        return 'math.Rectangle'.__wrap(super(__math.Rectangle, self).setSize(__float.valueOf(arg0)))

    @overload
    def setCenter(self, arg0: float, arg1: float) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setCenter(float,float)"""
        return 'math.Rectangle'.__wrap(super(__math.Rectangle, self).setCenter(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def contains(self, arg0: 'Circle') -> bool:
        """public boolean com.badlogic.gdx.math.Rectangle.contains(com.badlogic.gdx.math.Circle)"""
        return bool.__wrap(super(__math.Rectangle, self).contains(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setSize(self, arg0: float, arg1: float) -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setSize(float,float)"""
        return 'math.Rectangle'.__wrap(super(__math.Rectangle, self).setSize(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def setPosition(self, arg0: 'Vector2') -> 'math.Rectangle':
        """public com.badlogic.gdx.math.Rectangle com.badlogic.gdx.math.Rectangle.setPosition(com.badlogic.gdx.math.Vector2)"""
        return 'math.Rectangle'.__wrap(super(__math.Rectangle, self).setPosition(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.math.Rectangle.toString()"""
        return str.__wrap(super(math.Rectangle, self).toString())