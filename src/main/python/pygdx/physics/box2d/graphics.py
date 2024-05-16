from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

from builtins import type
import com.badlogic.gdx.physics.box2d.graphics.ParticleEmitterBox2D as __ParticleEmitterBox2D
__ParticleEmitterBox2D = __ParticleEmitterBox2D
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

from pyquantum_helper import override
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_GradientColorValue
__GradientColorValue = __ParticleEmitter_GradientColorValue.GradientColorValue
import java.lang.Object as __object
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

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
 
class ParticleEmitterBox2D():
    """com.badlogic.gdx.physics.box2d.graphics.ParticleEmitterBox2D"""
 
    @staticmethod
    def __wrap(java_value: __ParticleEmitterBox2D) -> 'ParticleEmitterBox2D':
        return ParticleEmitterBox2D(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleEmitterBox2D):
        """
        Dynamic initializer for ParticleEmitterBox2D.
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
    def getMinParticleCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.ParticleEmitter.getMinParticleCount()"""
        return int.__wrap(super(g2d.ParticleEmitter, self).getMinParticleCount())

    @override
    @overload
    def getPercentComplete(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter.getPercentComplete()"""
        return float.__wrap(super(g2d.ParticleEmitter, self).getPercentComplete())

    @overload
    def __init__(self, arg0: 'World'):
        """public com.badlogic.gdx.physics.box2d.graphics.ParticleEmitterBox2D(com.badlogic.gdx.physics.box2d.World)"""
        val = __ParticleEmitterBox2D(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getRotation(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getRotation()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getRotation())

    @override
    @overload
    def cleansUpBlendFunction(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.cleansUpBlendFunction()"""
        return bool.__wrap(super(g2d.ParticleEmitter, self).cleansUpBlendFunction())

    @overload
    def __init__(self, arg0: 'World', arg1: 'BufferedReader'):
        """public com.badlogic.gdx.physics.box2d.graphics.ParticleEmitterBox2D(com.badlogic.gdx.physics.box2d.World,java.io.BufferedReader) throws java.io.IOException"""
        val = __ParticleEmitterBox2D(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setBehind(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setBehind(boolean)"""
        super(__g2d.ParticleEmitter, self).setBehind(__boolean.valueOf(arg0))

    @override
    @overload
    def matchYSize(self, arg0: 'ParticleEmitter'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.matchYSize(com.badlogic.gdx.graphics.g2d.ParticleEmitter)"""
        super(__g2d.ParticleEmitter, self).matchYSize(arg0)

    @override
    @overload
    def save(self, arg0: 'Writer'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.save(java.io.Writer) throws java.io.IOException"""
        super(__g2d.ParticleEmitter, self).save(arg0)

    @override
    @overload
    def getWind(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getWind()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getWind())

    @override
    @overload
    def addParticles(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.addParticles(int)"""
        super(__g2d.ParticleEmitter, self).addParticles(__int.valueOf(arg0))

    @override
    @overload
    def getYOffsetValue(self) -> 'g2d.ParticleEmitter$RangedNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getYOffsetValue()"""
        return 'g2d.ParticleEmitter$RangedNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getYOffsetValue())

    @override
    @overload
    def preAllocateParticles(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.preAllocateParticles()"""
        super(g2d.ParticleEmitter, self).preAllocateParticles()

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g2d.ParticleEmitter.getName()"""
        return str.__wrap(super(g2d.ParticleEmitter, self).getName())

    @override
    @overload
    def getXScale(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getXScale()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getXScale())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isPremultipliedAlpha(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isPremultipliedAlpha()"""
        return bool.__wrap(super(g2d.ParticleEmitter, self).isPremultipliedAlpha())

    @override
    @overload
    def getMaxParticleCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.ParticleEmitter.getMaxParticleCount()"""
        return int.__wrap(super(g2d.ParticleEmitter, self).getMaxParticleCount())

    @override
    @overload
    def getTransparency(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getTransparency()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getTransparency())

    @override
    @overload
    def matchSize(self, arg0: 'ParticleEmitter'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.matchSize(com.badlogic.gdx.graphics.g2d.ParticleEmitter)"""
        super(__g2d.ParticleEmitter, self).matchSize(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setSprites(self, arg0: 'Array'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setSprites(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.Sprite>)"""
        super(__g2d.ParticleEmitter, self).setSprites(arg0)

    @override
    @overload
    def getBoundingBox(self) -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g2d.ParticleEmitter.getBoundingBox()"""
        return 'collision.BoundingBox'.__wrap(super(g2d.ParticleEmitter, self).getBoundingBox())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getSprites(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.Sprite> com.badlogic.gdx.graphics.g2d.ParticleEmitter.getSprites()"""
        return 'utils.Array'.__wrap(super(g2d.ParticleEmitter, self).getSprites())

    @override
    @overload
    def update(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.update(float)"""
        super(__g2d.ParticleEmitter, self).update(__float.valueOf(arg0))

    @override
    @overload
    def draw(self, arg0: 'Batch'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.draw(com.badlogic.gdx.graphics.g2d.Batch)"""
        super(__g2d.ParticleEmitter, self).draw(arg0)

    @override
    @overload
    def getLifeOffset(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getLifeOffset()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getLifeOffset())

    @override
    @overload
    def getDuration(self) -> 'g2d.ParticleEmitter$RangedNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getDuration()"""
        return 'g2d.ParticleEmitter$RangedNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getDuration())

    @override
    @overload
    def setMaxParticleCount(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setMaxParticleCount(int)"""
        super(__g2d.ParticleEmitter, self).setMaxParticleCount(__int.valueOf(arg0))

    @override
    @overload
    def setAligned(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setAligned(boolean)"""
        super(__g2d.ParticleEmitter, self).setAligned(__boolean.valueOf(arg0))

    @override
    @overload
    def getSpriteMode(self) -> 'g2d.ParticleEmitter$SpriteMode':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpriteMode com.badlogic.gdx.graphics.g2d.ParticleEmitter.getSpriteMode()"""
        return 'g2d.ParticleEmitter$SpriteMode'.__wrap(super(g2d.ParticleEmitter, self).getSpriteMode())

    @override
    @overload
    def scaleSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.scaleSize(float,float)"""
        super(__g2d.ParticleEmitter, self).scaleSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def addParticle(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.addParticle()"""
        super(g2d.ParticleEmitter, self).addParticle()

    @override
    @overload
    def getDelay(self) -> 'g2d.ParticleEmitter$RangedNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getDelay()"""
        return 'g2d.ParticleEmitter$RangedNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getDelay())

    @override
    @overload
    def setImagePaths(self, arg0: 'Array'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setImagePaths(com.badlogic.gdx.utils.Array<java.lang.String>)"""
        super(__g2d.ParticleEmitter, self).setImagePaths(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.reset()"""
        super(g2d.ParticleEmitter, self).reset()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def flipY(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.flipY()"""
        super(g2d.ParticleEmitter, self).flipY()

    @override
    @overload
    def getXOffsetValue(self) -> 'g2d.ParticleEmitter$RangedNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getXOffsetValue()"""
        return 'g2d.ParticleEmitter$RangedNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getXOffsetValue())

    @override
    @overload
    def matchXSize(self, arg0: 'ParticleEmitter'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.matchXSize(com.badlogic.gdx.graphics.g2d.ParticleEmitter)"""
        super(__g2d.ParticleEmitter, self).matchXSize(arg0)

    @override
    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter.getY()"""
        return float.__wrap(super(g2d.ParticleEmitter, self).getY())

    @override
    @overload
    def isAdditive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isAdditive()"""
        return bool.__wrap(super(g2d.ParticleEmitter, self).isAdditive())

    @override
    @overload
    def setPremultipliedAlpha(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setPremultipliedAlpha(boolean)"""
        super(__g2d.ParticleEmitter, self).setPremultipliedAlpha(__boolean.valueOf(arg0))

    @override
    @overload
    def isAligned(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isAligned()"""
        return bool.__wrap(super(g2d.ParticleEmitter, self).isAligned())

    @override
    @overload
    def getTint(self) -> 'g2d.ParticleEmitter$GradientColorValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getTint()"""
        return 'g2d.ParticleEmitter$GradientColorValue'.__wrap(super(g2d.ParticleEmitter, self).getTint())

    @override
    @overload
    def getGravity(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getGravity()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getGravity())

    @override
    @overload
    def isAttached(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isAttached()"""
        return bool.__wrap(super(g2d.ParticleEmitter, self).isAttached())

    @override
    @overload
    def setFlip(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setFlip(boolean,boolean)"""
        super(__g2d.ParticleEmitter, self).setFlip(__boolean.valueOf(arg0), __boolean.valueOf(arg1))

    @override
    @overload
    def setAttached(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setAttached(boolean)"""
        super(__g2d.ParticleEmitter, self).setAttached(__boolean.valueOf(arg0))

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setPosition(float,float)"""
        super(__g2d.ParticleEmitter, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def setMinParticleCount(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setMinParticleCount(int)"""
        super(__g2d.ParticleEmitter, self).setMinParticleCount(__int.valueOf(arg0))

    @override
    @overload
    def load(self, arg0: 'BufferedReader'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.load(java.io.BufferedReader) throws java.io.IOException"""
        super(__g2d.ParticleEmitter, self).load(arg0)

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isComplete()"""
        return bool.__wrap(super(g2d.ParticleEmitter, self).isComplete())

    @override
    @overload
    def setContinuous(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setContinuous(boolean)"""
        super(__g2d.ParticleEmitter, self).setContinuous(__boolean.valueOf(arg0))

    @override
    @overload
    def allowCompletion(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.allowCompletion()"""
        super(g2d.ParticleEmitter, self).allowCompletion()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getYScale(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getYScale()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getYScale())

    @override
    @overload
    def getSpawnHeight(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getSpawnHeight()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getSpawnHeight())

    @override
    @overload
    def getSpawnShape(self) -> 'g2d.ParticleEmitter$SpawnShapeValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getSpawnShape()"""
        return 'g2d.ParticleEmitter$SpawnShapeValue'.__wrap(super(g2d.ParticleEmitter, self).getSpawnShape())

    @override
    @overload
    def getAngle(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getAngle()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getAngle())

    @override
    @overload
    def getLife(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getLife()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getLife())

    @override
    @overload
    def scaleMotion(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.scaleMotion(float)"""
        super(__g2d.ParticleEmitter, self).scaleMotion(__float.valueOf(arg0))

    @override
    @overload
    def matchMotion(self, arg0: 'ParticleEmitter'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.matchMotion(com.badlogic.gdx.graphics.g2d.ParticleEmitter)"""
        super(__g2d.ParticleEmitter, self).matchMotion(arg0)

    @overload
    def __init__(self, arg0: 'World', arg1: 'ParticleEmitter'):
        """public com.badlogic.gdx.physics.box2d.graphics.ParticleEmitterBox2D(com.badlogic.gdx.physics.box2d.World,com.badlogic.gdx.graphics.g2d.ParticleEmitter)"""
        val = __ParticleEmitterBox2D(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setAdditive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setAdditive(boolean)"""
        super(__g2d.ParticleEmitter, self).setAdditive(__boolean.valueOf(arg0))

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.draw(com.badlogic.gdx.graphics.g2d.Batch,float)"""
        super(__g2d.ParticleEmitter, self).draw(arg0, __float.valueOf(arg1))

    @override
    @overload
    def getVelocity(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getVelocity()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getVelocity())

    @override
    @overload
    def isBehind(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isBehind()"""
        return bool.__wrap(super(g2d.ParticleEmitter, self).isBehind())

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
    def start(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.start()"""
        super(g2d.ParticleEmitter, self).start()

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setName(java.lang.String)"""
        super(__g2d.ParticleEmitter, self).setName(arg0)

    @override
    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter.getX()"""
        return float.__wrap(super(g2d.ParticleEmitter, self).getX())

    @override
    @overload
    def getSpawnWidth(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getSpawnWidth()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getSpawnWidth())

    @override
    @overload
    def getEmission(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getEmission()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getEmission())

    @override
    @overload
    def isContinuous(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isContinuous()"""
        return bool.__wrap(super(g2d.ParticleEmitter, self).isContinuous())

    @override
    @overload
    def getImagePaths(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<java.lang.String> com.badlogic.gdx.graphics.g2d.ParticleEmitter.getImagePaths()"""
        return 'utils.Array'.__wrap(super(g2d.ParticleEmitter, self).getImagePaths())

    @override
    @overload
    def getActiveCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.ParticleEmitter.getActiveCount()"""
        return int.__wrap(super(g2d.ParticleEmitter, self).getActiveCount())

    @override
    @overload
    def setSpriteMode(self, arg0: 'SpriteMode'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setSpriteMode(com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpriteMode)"""
        super(__g2d.ParticleEmitter, self).setSpriteMode(arg0)

    @override
    @overload
    def scaleSize(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.scaleSize(float)"""
        super(__g2d.ParticleEmitter, self).scaleSize(__float.valueOf(arg0))

    @override
    @overload
    def setCleansUpBlendFunction(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setCleansUpBlendFunction(boolean)"""
        super(__g2d.ParticleEmitter, self).setCleansUpBlendFunction(__boolean.valueOf(arg0))

 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.graphics.ParticleEmitterBox2D
from pyquantum_helper import import_once as __import_once__
import java.lang.Boolean as __boolean
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

from builtins import type
import com.badlogic.gdx.physics.box2d.graphics.ParticleEmitterBox2D as __ParticleEmitterBox2D
__ParticleEmitterBox2D = __ParticleEmitterBox2D
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

from pyquantum_helper import override
import com.badlogic.gdx.graphics.g2d.ParticleEmitter as __ParticleEmitter_GradientColorValue
__GradientColorValue = __ParticleEmitter_GradientColorValue.GradientColorValue
import java.lang.Object as __object
try:
    from pygdx.physics import box2d
except ImportError:
    box2d = __import_once__("pygdx.physics.box2d")

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
 
class ParticleEmitterBox2D():
    """com.badlogic.gdx.physics.box2d.graphics.ParticleEmitterBox2D"""
 
    @staticmethod
    def __wrap(java_value: __ParticleEmitterBox2D) -> 'ParticleEmitterBox2D':
        return ParticleEmitterBox2D(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleEmitterBox2D):
        """
        Dynamic initializer for ParticleEmitterBox2D.
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
    def getMinParticleCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.ParticleEmitter.getMinParticleCount()"""
        return int.__wrap(super(g2d.ParticleEmitter, self).getMinParticleCount())

    @override
    @overload
    def getPercentComplete(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter.getPercentComplete()"""
        return float.__wrap(super(g2d.ParticleEmitter, self).getPercentComplete())

    @overload
    def __init__(self, arg0: 'World'):
        """public com.badlogic.gdx.physics.box2d.graphics.ParticleEmitterBox2D(com.badlogic.gdx.physics.box2d.World)"""
        val = __ParticleEmitterBox2D(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getRotation(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getRotation()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getRotation())

    @override
    @overload
    def cleansUpBlendFunction(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.cleansUpBlendFunction()"""
        return bool.__wrap(super(g2d.ParticleEmitter, self).cleansUpBlendFunction())

    @overload
    def __init__(self, arg0: 'World', arg1: 'BufferedReader'):
        """public com.badlogic.gdx.physics.box2d.graphics.ParticleEmitterBox2D(com.badlogic.gdx.physics.box2d.World,java.io.BufferedReader) throws java.io.IOException"""
        val = __ParticleEmitterBox2D(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setBehind(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setBehind(boolean)"""
        super(__g2d.ParticleEmitter, self).setBehind(__boolean.valueOf(arg0))

    @override
    @overload
    def matchYSize(self, arg0: 'ParticleEmitter'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.matchYSize(com.badlogic.gdx.graphics.g2d.ParticleEmitter)"""
        super(__g2d.ParticleEmitter, self).matchYSize(arg0)

    @override
    @overload
    def save(self, arg0: 'Writer'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.save(java.io.Writer) throws java.io.IOException"""
        super(__g2d.ParticleEmitter, self).save(arg0)

    @override
    @overload
    def getWind(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getWind()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getWind())

    @override
    @overload
    def addParticles(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.addParticles(int)"""
        super(__g2d.ParticleEmitter, self).addParticles(__int.valueOf(arg0))

    @override
    @overload
    def getYOffsetValue(self) -> 'g2d.ParticleEmitter$RangedNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getYOffsetValue()"""
        return 'g2d.ParticleEmitter$RangedNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getYOffsetValue())

    @override
    @overload
    def preAllocateParticles(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.preAllocateParticles()"""
        super(g2d.ParticleEmitter, self).preAllocateParticles()

    @override
    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g2d.ParticleEmitter.getName()"""
        return str.__wrap(super(g2d.ParticleEmitter, self).getName())

    @override
    @overload
    def getXScale(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getXScale()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getXScale())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def isPremultipliedAlpha(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isPremultipliedAlpha()"""
        return bool.__wrap(super(g2d.ParticleEmitter, self).isPremultipliedAlpha())

    @override
    @overload
    def getMaxParticleCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.ParticleEmitter.getMaxParticleCount()"""
        return int.__wrap(super(g2d.ParticleEmitter, self).getMaxParticleCount())

    @override
    @overload
    def getTransparency(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getTransparency()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getTransparency())

    @override
    @overload
    def matchSize(self, arg0: 'ParticleEmitter'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.matchSize(com.badlogic.gdx.graphics.g2d.ParticleEmitter)"""
        super(__g2d.ParticleEmitter, self).matchSize(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def setSprites(self, arg0: 'Array'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setSprites(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.Sprite>)"""
        super(__g2d.ParticleEmitter, self).setSprites(arg0)

    @override
    @overload
    def getBoundingBox(self) -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g2d.ParticleEmitter.getBoundingBox()"""
        return 'collision.BoundingBox'.__wrap(super(g2d.ParticleEmitter, self).getBoundingBox())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getSprites(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g2d.Sprite> com.badlogic.gdx.graphics.g2d.ParticleEmitter.getSprites()"""
        return 'utils.Array'.__wrap(super(g2d.ParticleEmitter, self).getSprites())

    @override
    @overload
    def update(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.update(float)"""
        super(__g2d.ParticleEmitter, self).update(__float.valueOf(arg0))

    @override
    @overload
    def draw(self, arg0: 'Batch'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.draw(com.badlogic.gdx.graphics.g2d.Batch)"""
        super(__g2d.ParticleEmitter, self).draw(arg0)

    @override
    @overload
    def getLifeOffset(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getLifeOffset()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getLifeOffset())

    @override
    @overload
    def getDuration(self) -> 'g2d.ParticleEmitter$RangedNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getDuration()"""
        return 'g2d.ParticleEmitter$RangedNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getDuration())

    @override
    @overload
    def setMaxParticleCount(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setMaxParticleCount(int)"""
        super(__g2d.ParticleEmitter, self).setMaxParticleCount(__int.valueOf(arg0))

    @override
    @overload
    def setAligned(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setAligned(boolean)"""
        super(__g2d.ParticleEmitter, self).setAligned(__boolean.valueOf(arg0))

    @override
    @overload
    def getSpriteMode(self) -> 'g2d.ParticleEmitter$SpriteMode':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpriteMode com.badlogic.gdx.graphics.g2d.ParticleEmitter.getSpriteMode()"""
        return 'g2d.ParticleEmitter$SpriteMode'.__wrap(super(g2d.ParticleEmitter, self).getSpriteMode())

    @override
    @overload
    def scaleSize(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.scaleSize(float,float)"""
        super(__g2d.ParticleEmitter, self).scaleSize(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def addParticle(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.addParticle()"""
        super(g2d.ParticleEmitter, self).addParticle()

    @override
    @overload
    def getDelay(self) -> 'g2d.ParticleEmitter$RangedNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getDelay()"""
        return 'g2d.ParticleEmitter$RangedNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getDelay())

    @override
    @overload
    def setImagePaths(self, arg0: 'Array'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setImagePaths(com.badlogic.gdx.utils.Array<java.lang.String>)"""
        super(__g2d.ParticleEmitter, self).setImagePaths(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.reset()"""
        super(g2d.ParticleEmitter, self).reset()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def flipY(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.flipY()"""
        super(g2d.ParticleEmitter, self).flipY()

    @override
    @overload
    def getXOffsetValue(self) -> 'g2d.ParticleEmitter$RangedNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$RangedNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getXOffsetValue()"""
        return 'g2d.ParticleEmitter$RangedNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getXOffsetValue())

    @override
    @overload
    def matchXSize(self, arg0: 'ParticleEmitter'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.matchXSize(com.badlogic.gdx.graphics.g2d.ParticleEmitter)"""
        super(__g2d.ParticleEmitter, self).matchXSize(arg0)

    @override
    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter.getY()"""
        return float.__wrap(super(g2d.ParticleEmitter, self).getY())

    @override
    @overload
    def isAdditive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isAdditive()"""
        return bool.__wrap(super(g2d.ParticleEmitter, self).isAdditive())

    @override
    @overload
    def setPremultipliedAlpha(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setPremultipliedAlpha(boolean)"""
        super(__g2d.ParticleEmitter, self).setPremultipliedAlpha(__boolean.valueOf(arg0))

    @override
    @overload
    def isAligned(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isAligned()"""
        return bool.__wrap(super(g2d.ParticleEmitter, self).isAligned())

    @override
    @overload
    def getTint(self) -> 'g2d.ParticleEmitter$GradientColorValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$GradientColorValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getTint()"""
        return 'g2d.ParticleEmitter$GradientColorValue'.__wrap(super(g2d.ParticleEmitter, self).getTint())

    @override
    @overload
    def getGravity(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getGravity()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getGravity())

    @override
    @overload
    def isAttached(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isAttached()"""
        return bool.__wrap(super(g2d.ParticleEmitter, self).isAttached())

    @override
    @overload
    def setFlip(self, arg0: bool, arg1: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setFlip(boolean,boolean)"""
        super(__g2d.ParticleEmitter, self).setFlip(__boolean.valueOf(arg0), __boolean.valueOf(arg1))

    @override
    @overload
    def setAttached(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setAttached(boolean)"""
        super(__g2d.ParticleEmitter, self).setAttached(__boolean.valueOf(arg0))

    @override
    @overload
    def setPosition(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setPosition(float,float)"""
        super(__g2d.ParticleEmitter, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def setMinParticleCount(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setMinParticleCount(int)"""
        super(__g2d.ParticleEmitter, self).setMinParticleCount(__int.valueOf(arg0))

    @override
    @overload
    def load(self, arg0: 'BufferedReader'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.load(java.io.BufferedReader) throws java.io.IOException"""
        super(__g2d.ParticleEmitter, self).load(arg0)

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isComplete()"""
        return bool.__wrap(super(g2d.ParticleEmitter, self).isComplete())

    @override
    @overload
    def setContinuous(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setContinuous(boolean)"""
        super(__g2d.ParticleEmitter, self).setContinuous(__boolean.valueOf(arg0))

    @override
    @overload
    def allowCompletion(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.allowCompletion()"""
        super(g2d.ParticleEmitter, self).allowCompletion()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getYScale(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getYScale()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getYScale())

    @override
    @overload
    def getSpawnHeight(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getSpawnHeight()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getSpawnHeight())

    @override
    @overload
    def getSpawnShape(self) -> 'g2d.ParticleEmitter$SpawnShapeValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpawnShapeValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getSpawnShape()"""
        return 'g2d.ParticleEmitter$SpawnShapeValue'.__wrap(super(g2d.ParticleEmitter, self).getSpawnShape())

    @override
    @overload
    def getAngle(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getAngle()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getAngle())

    @override
    @overload
    def getLife(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getLife()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getLife())

    @override
    @overload
    def scaleMotion(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.scaleMotion(float)"""
        super(__g2d.ParticleEmitter, self).scaleMotion(__float.valueOf(arg0))

    @override
    @overload
    def matchMotion(self, arg0: 'ParticleEmitter'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.matchMotion(com.badlogic.gdx.graphics.g2d.ParticleEmitter)"""
        super(__g2d.ParticleEmitter, self).matchMotion(arg0)

    @overload
    def __init__(self, arg0: 'World', arg1: 'ParticleEmitter'):
        """public com.badlogic.gdx.physics.box2d.graphics.ParticleEmitterBox2D(com.badlogic.gdx.physics.box2d.World,com.badlogic.gdx.graphics.g2d.ParticleEmitter)"""
        val = __ParticleEmitterBox2D(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setAdditive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setAdditive(boolean)"""
        super(__g2d.ParticleEmitter, self).setAdditive(__boolean.valueOf(arg0))

    @override
    @overload
    def draw(self, arg0: 'Batch', arg1: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.draw(com.badlogic.gdx.graphics.g2d.Batch,float)"""
        super(__g2d.ParticleEmitter, self).draw(arg0, __float.valueOf(arg1))

    @override
    @overload
    def getVelocity(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getVelocity()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getVelocity())

    @override
    @overload
    def isBehind(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isBehind()"""
        return bool.__wrap(super(g2d.ParticleEmitter, self).isBehind())

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
    def start(self):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.start()"""
        super(g2d.ParticleEmitter, self).start()

    @override
    @overload
    def setName(self, arg0: str):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setName(java.lang.String)"""
        super(__g2d.ParticleEmitter, self).setName(arg0)

    @override
    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.graphics.g2d.ParticleEmitter.getX()"""
        return float.__wrap(super(g2d.ParticleEmitter, self).getX())

    @override
    @overload
    def getSpawnWidth(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getSpawnWidth()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getSpawnWidth())

    @override
    @overload
    def getEmission(self) -> 'g2d.ParticleEmitter$ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g2d.ParticleEmitter$ScaledNumericValue com.badlogic.gdx.graphics.g2d.ParticleEmitter.getEmission()"""
        return 'g2d.ParticleEmitter$ScaledNumericValue'.__wrap(super(g2d.ParticleEmitter, self).getEmission())

    @override
    @overload
    def isContinuous(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g2d.ParticleEmitter.isContinuous()"""
        return bool.__wrap(super(g2d.ParticleEmitter, self).isContinuous())

    @override
    @overload
    def getImagePaths(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<java.lang.String> com.badlogic.gdx.graphics.g2d.ParticleEmitter.getImagePaths()"""
        return 'utils.Array'.__wrap(super(g2d.ParticleEmitter, self).getImagePaths())

    @override
    @overload
    def getActiveCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g2d.ParticleEmitter.getActiveCount()"""
        return int.__wrap(super(g2d.ParticleEmitter, self).getActiveCount())

    @override
    @overload
    def setSpriteMode(self, arg0: 'SpriteMode'):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setSpriteMode(com.badlogic.gdx.graphics.g2d.ParticleEmitter$SpriteMode)"""
        super(__g2d.ParticleEmitter, self).setSpriteMode(arg0)

    @override
    @overload
    def scaleSize(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.scaleSize(float)"""
        super(__g2d.ParticleEmitter, self).scaleSize(__float.valueOf(arg0))

    @override
    @overload
    def setCleansUpBlendFunction(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g2d.ParticleEmitter.setCleansUpBlendFunction(boolean)"""
        super(__g2d.ParticleEmitter, self).setCleansUpBlendFunction(__boolean.valueOf(arg0))

 
 
 
# CLASS: com.badlogic.gdx.physics.box2d.graphics.ParticleEmitterBox2D