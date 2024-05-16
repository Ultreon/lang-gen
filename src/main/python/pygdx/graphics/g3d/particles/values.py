from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = __import_once__("pygdx.graphics.g3d.particles")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue as __SpawnShapeValue
__SpawnShapeValue = __SpawnShapeValue
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as __ParticleValue
__ParticleValue = __ParticleValue
import com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue as __RectangleSpawnShapeValue
__RectangleSpawnShapeValue = __RectangleSpawnShapeValue
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

import com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue as __ScaledNumericValue
__ScaledNumericValue = __ScaledNumericValue
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue as __PrimitiveSpawnShapeValue
__PrimitiveSpawnShapeValue = __PrimitiveSpawnShapeValue
from builtins import int
 
class RectangleSpawnShapeValue(__PrimitiveSpawnShapeValue, PrimitiveSpawnShapeValue):
    """com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue"""
 
    @staticmethod
    def __wrap(java_value: __RectangleSpawnShapeValue) -> 'RectangleSpawnShapeValue':
        return RectangleSpawnShapeValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RectangleSpawnShapeValue):
        """
        Dynamic initializer for RectangleSpawnShapeValue.
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
    def spawn(self, arg0: 'Vector3', arg1: float) -> 'math.Vector3':
        """public final com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawn(com.badlogic.gdx.math.Vector3,float)"""
        return 'math.Vector3'.__wrap(super(__SpawnShapeValue, self).spawn(arg0, __float.valueOf(arg1)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue()"""
        val = __RectangleSpawnShapeValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'RectangleSpawnShapeValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue(com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue)"""
        val = __RectangleSpawnShapeValue(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def copy(self) -> 'SpawnShapeValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue.copy()"""
        return 'SpawnShapeValue'.__wrap(super(RectangleSpawnShapeValue, self).copy())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setEdges(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setEdges(boolean)"""
        super(__PrimitiveSpawnShapeValue, self).setEdges(__boolean.valueOf(arg0))

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__PrimitiveSpawnShapeValue, self).read(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def spawnAux(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue.spawnAux(com.badlogic.gdx.math.Vector3,float)"""
        super(__RectangleSpawnShapeValue, self).spawnAux(arg0, __float.valueOf(arg1))

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__SpawnShapeValue, self).load(arg0, arg1)

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
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool.__wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setActive(boolean)"""
        super(__PrimitiveSpawnShapeValue, self).setActive(__boolean.valueOf(arg0))

    @override
    @overload
    def getSpawnWidth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnWidth()"""
        return 'ScaledNumericValue'.__wrap(super(PrimitiveSpawnShapeValue, self).getSpawnWidth())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def isEdges(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.isEdges()"""
        return bool.__wrap(super(PrimitiveSpawnShapeValue, self).isEdges())

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__SpawnShapeValue, self).save(arg0, arg1)

    @override
    @overload
    def getSpawnHeight(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnHeight()"""
        return 'ScaledNumericValue'.__wrap(super(PrimitiveSpawnShapeValue, self).getSpawnHeight())

    @override
    @overload
    def setDimensions(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setDimensions(float,float,float)"""
        super(__PrimitiveSpawnShapeValue, self).setDimensions(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

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
        """public com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue()"""
        val = __RectangleSpawnShapeValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(__PrimitiveSpawnShapeValue, self).load(arg0)

    @override
    @overload
    def getSpawnDepth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnDepth()"""
        return 'ScaledNumericValue'.__wrap(super(PrimitiveSpawnShapeValue, self).getSpawnDepth())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.init()"""
        super(SpawnShapeValue, self).init()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.write(com.badlogic.gdx.utils.Json)"""
        super(__PrimitiveSpawnShapeValue, self).write(arg0)

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.start()"""
        super(PrimitiveSpawnShapeValue, self).start()

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = __import_once__("pygdx.graphics.g3d.particles")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue as __SpawnShapeValue
__SpawnShapeValue = __SpawnShapeValue
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as __ParticleValue
__ParticleValue = __ParticleValue
import com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue as __RectangleSpawnShapeValue
__RectangleSpawnShapeValue = __RectangleSpawnShapeValue
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

import com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue as __ScaledNumericValue
__ScaledNumericValue = __ScaledNumericValue
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue as __PrimitiveSpawnShapeValue
__PrimitiveSpawnShapeValue = __PrimitiveSpawnShapeValue
from builtins import int
 
class RectangleSpawnShapeValue(__PrimitiveSpawnShapeValue, PrimitiveSpawnShapeValue):
    """com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue"""
 
    @staticmethod
    def __wrap(java_value: __RectangleSpawnShapeValue) -> 'RectangleSpawnShapeValue':
        return RectangleSpawnShapeValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RectangleSpawnShapeValue):
        """
        Dynamic initializer for RectangleSpawnShapeValue.
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
    def spawn(self, arg0: 'Vector3', arg1: float) -> 'math.Vector3':
        """public final com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawn(com.badlogic.gdx.math.Vector3,float)"""
        return 'math.Vector3'.__wrap(super(__SpawnShapeValue, self).spawn(arg0, __float.valueOf(arg1)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue()"""
        val = __RectangleSpawnShapeValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'RectangleSpawnShapeValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue(com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue)"""
        val = __RectangleSpawnShapeValue(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def copy(self) -> 'SpawnShapeValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue.copy()"""
        return 'SpawnShapeValue'.__wrap(super(RectangleSpawnShapeValue, self).copy())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setEdges(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setEdges(boolean)"""
        super(__PrimitiveSpawnShapeValue, self).setEdges(__boolean.valueOf(arg0))

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__PrimitiveSpawnShapeValue, self).read(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def spawnAux(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue.spawnAux(com.badlogic.gdx.math.Vector3,float)"""
        super(__RectangleSpawnShapeValue, self).spawnAux(arg0, __float.valueOf(arg1))

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__SpawnShapeValue, self).load(arg0, arg1)

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
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool.__wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setActive(boolean)"""
        super(__PrimitiveSpawnShapeValue, self).setActive(__boolean.valueOf(arg0))

    @override
    @overload
    def getSpawnWidth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnWidth()"""
        return 'ScaledNumericValue'.__wrap(super(PrimitiveSpawnShapeValue, self).getSpawnWidth())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def isEdges(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.isEdges()"""
        return bool.__wrap(super(PrimitiveSpawnShapeValue, self).isEdges())

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__SpawnShapeValue, self).save(arg0, arg1)

    @override
    @overload
    def getSpawnHeight(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnHeight()"""
        return 'ScaledNumericValue'.__wrap(super(PrimitiveSpawnShapeValue, self).getSpawnHeight())

    @override
    @overload
    def setDimensions(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setDimensions(float,float,float)"""
        super(__PrimitiveSpawnShapeValue, self).setDimensions(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

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
        """public com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue()"""
        val = __RectangleSpawnShapeValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(__PrimitiveSpawnShapeValue, self).load(arg0)

    @override
    @overload
    def getSpawnDepth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnDepth()"""
        return 'ScaledNumericValue'.__wrap(super(PrimitiveSpawnShapeValue, self).getSpawnDepth())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.init()"""
        super(SpawnShapeValue, self).init()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.write(com.badlogic.gdx.utils.Json)"""
        super(__PrimitiveSpawnShapeValue, self).write(arg0)

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.start()"""
        super(PrimitiveSpawnShapeValue, self).start()

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.UnweightedMeshSpawnShapeValue
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = __import_once__("pygdx.graphics.g3d.particles")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.values.UnweightedMeshSpawnShapeValue as __UnweightedMeshSpawnShapeValue
__UnweightedMeshSpawnShapeValue = __UnweightedMeshSpawnShapeValue
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue as __SpawnShapeValue
__SpawnShapeValue = __SpawnShapeValue
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as __ParticleValue
__ParticleValue = __ParticleValue
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue as __MeshSpawnShapeValue
__MeshSpawnShapeValue = __MeshSpawnShapeValue
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
 
class UnweightedMeshSpawnShapeValue(__MeshSpawnShapeValue, MeshSpawnShapeValue):
    """com.badlogic.gdx.graphics.g3d.particles.values.UnweightedMeshSpawnShapeValue"""
 
    @staticmethod
    def __wrap(java_value: __UnweightedMeshSpawnShapeValue) -> 'UnweightedMeshSpawnShapeValue':
        return UnweightedMeshSpawnShapeValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UnweightedMeshSpawnShapeValue):
        """
        Dynamic initializer for UnweightedMeshSpawnShapeValue.
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
    def spawn(self, arg0: 'Vector3', arg1: float) -> 'math.Vector3':
        """public final com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawn(com.badlogic.gdx.math.Vector3,float)"""
        return 'math.Vector3'.__wrap(super(__SpawnShapeValue, self).spawn(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setMesh(self, arg0: 'Mesh', arg1: 'Model'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.UnweightedMeshSpawnShapeValue.setMesh(com.badlogic.gdx.graphics.Mesh,com.badlogic.gdx.graphics.g3d.Model)"""
        super(__UnweightedMeshSpawnShapeValue, self).setMesh(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setMesh(self, arg0: 'Mesh'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.setMesh(com.badlogic.gdx.graphics.Mesh)"""
        super(__MeshSpawnShapeValue, self).setMesh(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__MeshSpawnShapeValue, self).save(arg0, arg1)

    @override
    @overload
    def spawnAux(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.UnweightedMeshSpawnShapeValue.spawnAux(com.badlogic.gdx.math.Vector3,float)"""
        super(__UnweightedMeshSpawnShapeValue, self).spawnAux(arg0, __float.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool.__wrap(super(ParticleValue, self).isActive())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.UnweightedMeshSpawnShapeValue()"""
        val = __UnweightedMeshSpawnShapeValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.setActive(boolean)"""
        super(__ParticleValue, self).setActive(__boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'UnweightedMeshSpawnShapeValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.values.UnweightedMeshSpawnShapeValue(com.badlogic.gdx.graphics.g3d.particles.values.UnweightedMeshSpawnShapeValue)"""
        val = __UnweightedMeshSpawnShapeValue(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__MeshSpawnShapeValue, self).load(arg0, arg1)

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
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.start()"""
        super(SpawnShapeValue, self).start()

    @override
    @overload
    def copy(self) -> 'SpawnShapeValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue com.badlogic.gdx.graphics.g3d.particles.values.UnweightedMeshSpawnShapeValue.copy()"""
        return 'SpawnShapeValue'.__wrap(super(UnweightedMeshSpawnShapeValue, self).copy())

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.write(com.badlogic.gdx.utils.Json)"""
        super(__SpawnShapeValue, self).write(arg0)

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(__MeshSpawnShapeValue, self).load(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.init()"""
        super(SpawnShapeValue, self).init()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.UnweightedMeshSpawnShapeValue()"""
        val = __UnweightedMeshSpawnShapeValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__SpawnShapeValue, self).read(arg0, arg1) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.NumericValue
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as __ParticleValue
__ParticleValue = __ParticleValue
import com.badlogic.gdx.graphics.g3d.particles.values.NumericValue as __NumericValue
__NumericValue = __NumericValue
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
 
class NumericValue(__ParticleValue, ParticleValue):
    """com.badlogic.gdx.graphics.g3d.particles.values.NumericValue"""
 
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
 
    @overload
    def getValue(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.values.NumericValue.getValue()"""
        return float.__wrap(super(NumericValue, self).getValue())

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
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.NumericValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__NumericValue, self).read(arg0, arg1)

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.setActive(boolean)"""
        super(__ParticleValue, self).setActive(__boolean.valueOf(arg0))

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
        """public com.badlogic.gdx.graphics.g3d.particles.values.NumericValue()"""
        val = __NumericValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.NumericValue()"""
        val = __NumericValue()
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
    def load(self, arg0: 'NumericValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.NumericValue.load(com.badlogic.gdx.graphics.g3d.particles.values.NumericValue)"""
        super(__NumericValue, self).load(arg0)

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(__ParticleValue, self).load(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setValue(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.NumericValue.setValue(float)"""
        super(__NumericValue, self).setValue(__float.valueOf(arg0))

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.NumericValue.write(com.badlogic.gdx.utils.Json)"""
        super(__NumericValue, self).write(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool.__wrap(super(ParticleValue, self).isActive()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = __import_once__("pygdx.graphics.g3d.particles")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue as __SpawnShapeValue
__SpawnShapeValue = __SpawnShapeValue
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as __ParticleValue
__ParticleValue = __ParticleValue
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue as __ScaledNumericValue
__ScaledNumericValue = __ScaledNumericValue
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue as __PrimitiveSpawnShapeValue
__PrimitiveSpawnShapeValue = __PrimitiveSpawnShapeValue
from builtins import int
 
class PrimitiveSpawnShapeValue(ABC, __SpawnShapeValue, SpawnShapeValue):
    """com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue"""
 
    @staticmethod
    def __wrap(java_value: __PrimitiveSpawnShapeValue) -> 'PrimitiveSpawnShapeValue':
        return PrimitiveSpawnShapeValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PrimitiveSpawnShapeValue):
        """
        Dynamic initializer for PrimitiveSpawnShapeValue.
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
    def getSpawnHeight(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnHeight()"""
        return 'ScaledNumericValue'.__wrap(super(PrimitiveSpawnShapeValue, self).getSpawnHeight())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def spawn(self, arg0: 'Vector3', arg1: float) -> 'math.Vector3':
        """public final com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawn(com.badlogic.gdx.math.Vector3,float)"""
        return 'math.Vector3'.__wrap(super(__SpawnShapeValue, self).spawn(arg0, __float.valueOf(arg1)))

    @overload
    def setEdges(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setEdges(boolean)"""
        super(__PrimitiveSpawnShapeValue, self).setEdges(__boolean.valueOf(arg0))

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.copy()"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__PrimitiveSpawnShapeValue, self).read(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def spawnAux(self, arg0: 'Vector3', arg1: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawnAux(com.badlogic.gdx.math.Vector3,float)"""
        pass

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__SpawnShapeValue, self).load(arg0, arg1)

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
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool.__wrap(super(ParticleValue, self).isActive())

    @overload
    def getSpawnWidth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnWidth()"""
        return 'ScaledNumericValue'.__wrap(super(PrimitiveSpawnShapeValue, self).getSpawnWidth())

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setActive(boolean)"""
        super(__PrimitiveSpawnShapeValue, self).setActive(__boolean.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def isEdges(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.isEdges()"""
        return bool.__wrap(super(PrimitiveSpawnShapeValue, self).isEdges())

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__SpawnShapeValue, self).save(arg0, arg1)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue()"""
        val = __PrimitiveSpawnShapeValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setDimensions(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setDimensions(float,float,float)"""
        super(__PrimitiveSpawnShapeValue, self).setDimensions(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def __init__(self, arg0: 'PrimitiveSpawnShapeValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue(com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue)"""
        val = __PrimitiveSpawnShapeValue(arg0)
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
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(__PrimitiveSpawnShapeValue, self).load(arg0)

    @overload
    def getSpawnDepth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnDepth()"""
        return 'ScaledNumericValue'.__wrap(super(PrimitiveSpawnShapeValue, self).getSpawnDepth())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.init()"""
        super(SpawnShapeValue, self).init()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue()"""
        val = __PrimitiveSpawnShapeValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.write(com.badlogic.gdx.utils.Json)"""
        super(__PrimitiveSpawnShapeValue, self).write(arg0)

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.start()"""
        super(PrimitiveSpawnShapeValue, self).start() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = __import_once__("pygdx.graphics.g3d.particles")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue as __SpawnShapeValue
__SpawnShapeValue = __SpawnShapeValue
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as __ParticleValue
__ParticleValue = __ParticleValue
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue as __MeshSpawnShapeValue
__MeshSpawnShapeValue = __MeshSpawnShapeValue
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
 
class MeshSpawnShapeValue(ABC, __SpawnShapeValue, SpawnShapeValue):
    """com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue"""
 
    @staticmethod
    def __wrap(java_value: __MeshSpawnShapeValue) -> 'MeshSpawnShapeValue':
        return MeshSpawnShapeValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MeshSpawnShapeValue):
        """
        Dynamic initializer for MeshSpawnShapeValue.
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
    def spawn(self, arg0: 'Vector3', arg1: float) -> 'math.Vector3':
        """public final com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawn(com.badlogic.gdx.math.Vector3,float)"""
        return 'math.Vector3'.__wrap(super(__SpawnShapeValue, self).spawn(arg0, __float.valueOf(arg1)))

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.copy()"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue()"""
        val = __MeshSpawnShapeValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def spawnAux(self, arg0: 'Vector3', arg1: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawnAux(com.badlogic.gdx.math.Vector3,float)"""
        pass

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__MeshSpawnShapeValue, self).save(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool.__wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.setActive(boolean)"""
        super(__ParticleValue, self).setActive(__boolean.valueOf(arg0))

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__MeshSpawnShapeValue, self).load(arg0, arg1)

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
        """public com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue()"""
        val = __MeshSpawnShapeValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.start()"""
        super(SpawnShapeValue, self).start()

    @overload
    def setMesh(self, arg0: 'Mesh'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.setMesh(com.badlogic.gdx.graphics.Mesh)"""
        super(__MeshSpawnShapeValue, self).setMesh(arg0)

    @overload
    def __init__(self, arg0: 'MeshSpawnShapeValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue(com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue)"""
        val = __MeshSpawnShapeValue(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.write(com.badlogic.gdx.utils.Json)"""
        super(__SpawnShapeValue, self).write(arg0)

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(__MeshSpawnShapeValue, self).load(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.init()"""
        super(SpawnShapeValue, self).init()

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__SpawnShapeValue, self).read(arg0, arg1)

    @overload
    def setMesh(self, arg0: 'Mesh', arg1: 'Model'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.setMesh(com.badlogic.gdx.graphics.Mesh,com.badlogic.gdx.graphics.g3d.Model)"""
        super(__MeshSpawnShapeValue, self).setMesh(arg0, arg1) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.LineSpawnShapeValue
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = __import_once__("pygdx.graphics.g3d.particles")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import com.badlogic.gdx.graphics.g3d.particles.values.LineSpawnShapeValue as __LineSpawnShapeValue
__LineSpawnShapeValue = __LineSpawnShapeValue
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue as __SpawnShapeValue
__SpawnShapeValue = __SpawnShapeValue
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as __ParticleValue
__ParticleValue = __ParticleValue
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

import com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue as __ScaledNumericValue
__ScaledNumericValue = __ScaledNumericValue
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue as __PrimitiveSpawnShapeValue
__PrimitiveSpawnShapeValue = __PrimitiveSpawnShapeValue
from builtins import int
 
class LineSpawnShapeValue(__PrimitiveSpawnShapeValue, PrimitiveSpawnShapeValue):
    """com.badlogic.gdx.graphics.g3d.particles.values.LineSpawnShapeValue"""
 
    @staticmethod
    def __wrap(java_value: __LineSpawnShapeValue) -> 'LineSpawnShapeValue':
        return LineSpawnShapeValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LineSpawnShapeValue):
        """
        Dynamic initializer for LineSpawnShapeValue.
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
    def spawn(self, arg0: 'Vector3', arg1: float) -> 'math.Vector3':
        """public final com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawn(com.badlogic.gdx.math.Vector3,float)"""
        return 'math.Vector3'.__wrap(super(__SpawnShapeValue, self).spawn(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def copy(self) -> 'SpawnShapeValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue com.badlogic.gdx.graphics.g3d.particles.values.LineSpawnShapeValue.copy()"""
        return 'SpawnShapeValue'.__wrap(super(LineSpawnShapeValue, self).copy())

    @override
    @overload
    def setEdges(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setEdges(boolean)"""
        super(__PrimitiveSpawnShapeValue, self).setEdges(__boolean.valueOf(arg0))

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__PrimitiveSpawnShapeValue, self).read(arg0, arg1)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.LineSpawnShapeValue()"""
        val = __LineSpawnShapeValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__SpawnShapeValue, self).load(arg0, arg1)

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
    def __init__(self, arg0: 'LineSpawnShapeValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.values.LineSpawnShapeValue(com.badlogic.gdx.graphics.g3d.particles.values.LineSpawnShapeValue)"""
        val = __LineSpawnShapeValue(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool.__wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setActive(boolean)"""
        super(__PrimitiveSpawnShapeValue, self).setActive(__boolean.valueOf(arg0))

    @override
    @overload
    def getSpawnWidth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnWidth()"""
        return 'ScaledNumericValue'.__wrap(super(PrimitiveSpawnShapeValue, self).getSpawnWidth())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def isEdges(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.isEdges()"""
        return bool.__wrap(super(PrimitiveSpawnShapeValue, self).isEdges())

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__SpawnShapeValue, self).save(arg0, arg1)

    @override
    @overload
    def spawnAux(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.LineSpawnShapeValue.spawnAux(com.badlogic.gdx.math.Vector3,float)"""
        super(__LineSpawnShapeValue, self).spawnAux(arg0, __float.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.LineSpawnShapeValue()"""
        val = __LineSpawnShapeValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getSpawnHeight(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnHeight()"""
        return 'ScaledNumericValue'.__wrap(super(PrimitiveSpawnShapeValue, self).getSpawnHeight())

    @override
    @overload
    def setDimensions(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setDimensions(float,float,float)"""
        super(__PrimitiveSpawnShapeValue, self).setDimensions(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

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
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(__PrimitiveSpawnShapeValue, self).load(arg0)

    @override
    @overload
    def getSpawnDepth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnDepth()"""
        return 'ScaledNumericValue'.__wrap(super(PrimitiveSpawnShapeValue, self).getSpawnDepth())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.init()"""
        super(SpawnShapeValue, self).init()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.write(com.badlogic.gdx.utils.Json)"""
        super(__PrimitiveSpawnShapeValue, self).write(arg0)

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.start()"""
        super(PrimitiveSpawnShapeValue, self).start() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as __ParticleValue
__ParticleValue = __ParticleValue
import com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue as __RangedNumericValue
__RangedNumericValue = __RangedNumericValue
from typing import List
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue as __ScaledNumericValue
__ScaledNumericValue = __ScaledNumericValue
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ScaledNumericValue(__RangedNumericValue, RangedNumericValue):
    """com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue"""
 
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

    @overload
    def getHighMax(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.getHighMax()"""
        return float.__wrap(super(ScaledNumericValue, self).getHighMax())

    @overload
    def getHighMin(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.getHighMin()"""
        return float.__wrap(super(ScaledNumericValue, self).getHighMin())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setScaling(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.setScaling(float[])"""
        super(__ScaledNumericValue, self).setScaling(arg0)

    @override
    @overload
    def getLowMax(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.getLowMax()"""
        return float.__wrap(super(RangedNumericValue, self).getLowMax())

    @overload
    def isRelative(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.isRelative()"""
        return bool.__wrap(super(ScaledNumericValue, self).isRelative())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def newLowValue(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.newLowValue()"""
        return float.__wrap(super(RangedNumericValue, self).newLowValue())

    @override
    @overload
    def setLow(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.setLow(float,float)"""
        super(__RangedNumericValue, self).setLow(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setTimeline(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.setTimeline(float[])"""
        super(__ScaledNumericValue, self).setTimeline(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool.__wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def load(self, arg0: 'RangedNumericValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.load(com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue)"""
        super(__RangedNumericValue, self).load(arg0)

    @override
    @overload
    def getLowMin(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.getLowMin()"""
        return float.__wrap(super(RangedNumericValue, self).getLowMin())

    @overload
    def getScale(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.getScale(float)"""
        return float.__wrap(super(__ScaledNumericValue, self).getScale(__float.valueOf(arg0)))

    @overload
    def getScaling(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.getScaling()"""
        return List[float].__wrap(super(ScaledNumericValue, self).getScaling())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setLow(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.setLow(float)"""
        super(__RangedNumericValue, self).setLow(__float.valueOf(arg0))

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.setActive(boolean)"""
        super(__ParticleValue, self).setActive(__boolean.valueOf(arg0))

    @overload
    def load(self, arg0: 'ScaledNumericValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue)"""
        super(__ScaledNumericValue, self).load(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue()"""
        val = __ScaledNumericValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue()"""
        val = __ScaledNumericValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.write(com.badlogic.gdx.utils.Json)"""
        super(__ScaledNumericValue, self).write(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__ScaledNumericValue, self).read(arg0, arg1)

    @overload
    def setHigh(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.setHigh(float)"""
        super(__ScaledNumericValue, self).setHigh(__float.valueOf(arg0))

    @overload
    def setHigh(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.setHigh(float,float)"""
        super(__ScaledNumericValue, self).setHigh(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setHighMax(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.setHighMax(float)"""
        super(__ScaledNumericValue, self).setHighMax(__float.valueOf(arg0))

    @override
    @overload
    def setLowMin(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.setLowMin(float)"""
        super(__RangedNumericValue, self).setLowMin(__float.valueOf(arg0))

    @overload
    def newHighValue(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.newHighValue()"""
        return float.__wrap(super(ScaledNumericValue, self).newHighValue())

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(__ParticleValue, self).load(arg0)

    @overload
    def setHighMin(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.setHighMin(float)"""
        super(__ScaledNumericValue, self).setHighMin(__float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getTimeline(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.getTimeline()"""
        return List[float].__wrap(super(ScaledNumericValue, self).getTimeline())

    @override
    @overload
    def setLowMax(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.setLowMax(float)"""
        super(__RangedNumericValue, self).setLowMax(__float.valueOf(arg0))

    @overload
    def setRelative(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.setRelative(boolean)"""
        super(__ScaledNumericValue, self).setRelative(__boolean.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.PointSpawnShapeValue
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.graphics.g3d.particles.values.PointSpawnShapeValue as __PointSpawnShapeValue
__PointSpawnShapeValue = __PointSpawnShapeValue
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = __import_once__("pygdx.graphics.g3d.particles")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue as __SpawnShapeValue
__SpawnShapeValue = __SpawnShapeValue
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as __ParticleValue
__ParticleValue = __ParticleValue
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

import com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue as __ScaledNumericValue
__ScaledNumericValue = __ScaledNumericValue
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue as __PrimitiveSpawnShapeValue
__PrimitiveSpawnShapeValue = __PrimitiveSpawnShapeValue
from builtins import int
 
class PointSpawnShapeValue(__PrimitiveSpawnShapeValue, PrimitiveSpawnShapeValue):
    """com.badlogic.gdx.graphics.g3d.particles.values.PointSpawnShapeValue"""
 
    @staticmethod
    def __wrap(java_value: __PointSpawnShapeValue) -> 'PointSpawnShapeValue':
        return PointSpawnShapeValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PointSpawnShapeValue):
        """
        Dynamic initializer for PointSpawnShapeValue.
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
    def spawn(self, arg0: 'Vector3', arg1: float) -> 'math.Vector3':
        """public final com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawn(com.badlogic.gdx.math.Vector3,float)"""
        return 'math.Vector3'.__wrap(super(__SpawnShapeValue, self).spawn(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setEdges(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setEdges(boolean)"""
        super(__PrimitiveSpawnShapeValue, self).setEdges(__boolean.valueOf(arg0))

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__PrimitiveSpawnShapeValue, self).read(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__SpawnShapeValue, self).load(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'PointSpawnShapeValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.values.PointSpawnShapeValue(com.badlogic.gdx.graphics.g3d.particles.values.PointSpawnShapeValue)"""
        val = __PointSpawnShapeValue(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def copy(self) -> 'SpawnShapeValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue com.badlogic.gdx.graphics.g3d.particles.values.PointSpawnShapeValue.copy()"""
        return 'SpawnShapeValue'.__wrap(super(PointSpawnShapeValue, self).copy())

    @override
    @overload
    def spawnAux(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PointSpawnShapeValue.spawnAux(com.badlogic.gdx.math.Vector3,float)"""
        super(__PointSpawnShapeValue, self).spawnAux(arg0, __float.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool.__wrap(super(ParticleValue, self).isActive())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.PointSpawnShapeValue()"""
        val = __PointSpawnShapeValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setActive(boolean)"""
        super(__PrimitiveSpawnShapeValue, self).setActive(__boolean.valueOf(arg0))

    @override
    @overload
    def getSpawnWidth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnWidth()"""
        return 'ScaledNumericValue'.__wrap(super(PrimitiveSpawnShapeValue, self).getSpawnWidth())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def isEdges(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.isEdges()"""
        return bool.__wrap(super(PrimitiveSpawnShapeValue, self).isEdges())

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__SpawnShapeValue, self).save(arg0, arg1)

    @override
    @overload
    def getSpawnHeight(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnHeight()"""
        return 'ScaledNumericValue'.__wrap(super(PrimitiveSpawnShapeValue, self).getSpawnHeight())

    @override
    @overload
    def setDimensions(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setDimensions(float,float,float)"""
        super(__PrimitiveSpawnShapeValue, self).setDimensions(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

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
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(__PrimitiveSpawnShapeValue, self).load(arg0)

    @override
    @overload
    def getSpawnDepth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnDepth()"""
        return 'ScaledNumericValue'.__wrap(super(PrimitiveSpawnShapeValue, self).getSpawnDepth())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.init()"""
        super(SpawnShapeValue, self).init()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.write(com.badlogic.gdx.utils.Json)"""
        super(__PrimitiveSpawnShapeValue, self).write(arg0)

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.start()"""
        super(PrimitiveSpawnShapeValue, self).start()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.PointSpawnShapeValue()"""
        val = __PointSpawnShapeValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue as __GradientColorValue
__GradientColorValue = __GradientColorValue
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as __ParticleValue
__ParticleValue = __ParticleValue
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
 
class GradientColorValue(__ParticleValue, ParticleValue):
    """com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue"""
 
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
    def getTimeline(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue.getTimeline()"""
        return List[float].__wrap(super(GradientColorValue, self).getTimeline())

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue.write(com.badlogic.gdx.utils.Json)"""
        super(__GradientColorValue, self).write(arg0)

    @overload
    def getColor(self, arg0: float, arg1: 'float', arg2: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue.getColor(float,float[],int)"""
        super(__GradientColorValue, self).getColor(__float.valueOf(arg0), arg1, __int.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.setActive(boolean)"""
        super(__ParticleValue, self).setActive(__boolean.valueOf(arg0))

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__GradientColorValue, self).read(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue()"""
        val = __GradientColorValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setColors(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue.setColors(float[])"""
        super(__GradientColorValue, self).setColors(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue()"""
        val = __GradientColorValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setTimeline(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue.setTimeline(float[])"""
        super(__GradientColorValue, self).setTimeline(arg0)

    @overload
    def getColor(self, arg0: float) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue.getColor(float)"""
        return List[float].__wrap(super(__GradientColorValue, self).getColor(__float.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(__ParticleValue, self).load(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getColors(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue.getColors()"""
        return List[float].__wrap(super(GradientColorValue, self).getColors())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def load(self, arg0: 'GradientColorValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue.load(com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue)"""
        super(__GradientColorValue, self).load(arg0)

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool.__wrap(super(ParticleValue, self).isActive()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as __ParticleValue
__ParticleValue = __ParticleValue
import com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue as __RangedNumericValue
__RangedNumericValue = __RangedNumericValue
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
 
class RangedNumericValue(__ParticleValue, ParticleValue):
    """com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue"""
 
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

    @overload
    def getLowMax(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.getLowMax()"""
        return float.__wrap(super(RangedNumericValue, self).getLowMax())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setLow(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.setLow(float)"""
        super(__RangedNumericValue, self).setLow(__float.valueOf(arg0))

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.setActive(boolean)"""
        super(__ParticleValue, self).setActive(__boolean.valueOf(arg0))

    @overload
    def load(self, arg0: 'RangedNumericValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.load(com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue)"""
        super(__RangedNumericValue, self).load(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__RangedNumericValue, self).read(arg0, arg1)

    @overload
    def setLowMax(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.setLowMax(float)"""
        super(__RangedNumericValue, self).setLowMax(__float.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue()"""
        val = __RangedNumericValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setLowMin(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.setLowMin(float)"""
        super(__RangedNumericValue, self).setLowMin(__float.valueOf(arg0))

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
        """public com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue()"""
        val = __RangedNumericValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(__ParticleValue, self).load(arg0)

    @overload
    def setLow(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.setLow(float,float)"""
        super(__RangedNumericValue, self).setLow(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.write(com.badlogic.gdx.utils.Json)"""
        super(__RangedNumericValue, self).write(arg0)

    @overload
    def getLowMin(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.getLowMin()"""
        return float.__wrap(super(RangedNumericValue, self).getLowMin())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def newLowValue(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.newLowValue()"""
        return float.__wrap(super(RangedNumericValue, self).newLowValue())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool.__wrap(super(ParticleValue, self).isActive()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.CylinderSpawnShapeValue
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = __import_once__("pygdx.graphics.g3d.particles")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue as __SpawnShapeValue
__SpawnShapeValue = __SpawnShapeValue
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as __ParticleValue
__ParticleValue = __ParticleValue
import com.badlogic.gdx.graphics.g3d.particles.values.CylinderSpawnShapeValue as __CylinderSpawnShapeValue
__CylinderSpawnShapeValue = __CylinderSpawnShapeValue
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

import com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue as __ScaledNumericValue
__ScaledNumericValue = __ScaledNumericValue
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue as __PrimitiveSpawnShapeValue
__PrimitiveSpawnShapeValue = __PrimitiveSpawnShapeValue
from builtins import int
 
class CylinderSpawnShapeValue(__PrimitiveSpawnShapeValue, PrimitiveSpawnShapeValue):
    """com.badlogic.gdx.graphics.g3d.particles.values.CylinderSpawnShapeValue"""
 
    @staticmethod
    def __wrap(java_value: __CylinderSpawnShapeValue) -> 'CylinderSpawnShapeValue':
        return CylinderSpawnShapeValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CylinderSpawnShapeValue):
        """
        Dynamic initializer for CylinderSpawnShapeValue.
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
    def spawnAux(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.CylinderSpawnShapeValue.spawnAux(com.badlogic.gdx.math.Vector3,float)"""
        super(__CylinderSpawnShapeValue, self).spawnAux(arg0, __float.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def spawn(self, arg0: 'Vector3', arg1: float) -> 'math.Vector3':
        """public final com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawn(com.badlogic.gdx.math.Vector3,float)"""
        return 'math.Vector3'.__wrap(super(__SpawnShapeValue, self).spawn(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def copy(self) -> 'SpawnShapeValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue com.badlogic.gdx.graphics.g3d.particles.values.CylinderSpawnShapeValue.copy()"""
        return 'SpawnShapeValue'.__wrap(super(CylinderSpawnShapeValue, self).copy())

    @override
    @overload
    def setEdges(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setEdges(boolean)"""
        super(__PrimitiveSpawnShapeValue, self).setEdges(__boolean.valueOf(arg0))

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__PrimitiveSpawnShapeValue, self).read(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__SpawnShapeValue, self).load(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.CylinderSpawnShapeValue()"""
        val = __CylinderSpawnShapeValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool.__wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setActive(boolean)"""
        super(__PrimitiveSpawnShapeValue, self).setActive(__boolean.valueOf(arg0))

    @override
    @overload
    def getSpawnWidth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnWidth()"""
        return 'ScaledNumericValue'.__wrap(super(PrimitiveSpawnShapeValue, self).getSpawnWidth())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.CylinderSpawnShapeValue()"""
        val = __CylinderSpawnShapeValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def isEdges(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.isEdges()"""
        return bool.__wrap(super(PrimitiveSpawnShapeValue, self).isEdges())

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__SpawnShapeValue, self).save(arg0, arg1)

    @override
    @overload
    def getSpawnHeight(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnHeight()"""
        return 'ScaledNumericValue'.__wrap(super(PrimitiveSpawnShapeValue, self).getSpawnHeight())

    @override
    @overload
    def setDimensions(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setDimensions(float,float,float)"""
        super(__PrimitiveSpawnShapeValue, self).setDimensions(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

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
    def __init__(self, arg0: 'CylinderSpawnShapeValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.values.CylinderSpawnShapeValue(com.badlogic.gdx.graphics.g3d.particles.values.CylinderSpawnShapeValue)"""
        val = __CylinderSpawnShapeValue(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(__PrimitiveSpawnShapeValue, self).load(arg0)

    @override
    @overload
    def getSpawnDepth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnDepth()"""
        return 'ScaledNumericValue'.__wrap(super(PrimitiveSpawnShapeValue, self).getSpawnDepth())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.init()"""
        super(SpawnShapeValue, self).init()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.write(com.badlogic.gdx.utils.Json)"""
        super(__PrimitiveSpawnShapeValue, self).write(arg0)

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.start()"""
        super(PrimitiveSpawnShapeValue, self).start() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue
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
import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as __ParticleValue
__ParticleValue = __ParticleValue
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
 
class ParticleValue(pygdx.__Json_Serializable, utils.Json$Serializable):
    """com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue"""
 
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
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.write(com.badlogic.gdx.utils.Json)"""
        super(__ParticleValue, self).write(arg0)

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
        """public com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue()"""
        val = __ParticleValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'ParticleValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        val = __ParticleValue(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(__ParticleValue, self).load(arg0)

    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.setActive(boolean)"""
        super(__ParticleValue, self).setActive(__boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__ParticleValue, self).read(arg0, arg1)

    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool.__wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue()"""
        val = __ParticleValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue$Triangle
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue as __MeshSpawnShapeValue_Triangle
__Triangle = __MeshSpawnShapeValue_Triangle.Triangle
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
from builtins import bool
from builtins import int
 
class Triangle():
    """com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.Triangle"""
 
    @staticmethod
    def __wrap(java_value: __Triangle) -> 'Triangle':
        return Triangle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Triangle):
        """
        Dynamic initializer for Triangle.
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
 
    @staticmethod
    @overload
    def pick(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: 'Vector3') -> 'math.Vector3':
        """public static com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue$Triangle.pick(float,float,float,float,float,float,float,float,float,com.badlogic.gdx.math.Vector3)"""
        return math.Vector3.__wrap(__Triangle.pick(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8), arg9))

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
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue$Triangle(float,float,float,float,float,float,float,float,float)"""
        val = __Triangle(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7), __float.valueOf(arg8))
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
    def pick(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue$Triangle.pick(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'.__wrap(super(__Triangle, self).pick(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.WeightMeshSpawnShapeValue
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.g3d.particles.values.WeightMeshSpawnShapeValue as __WeightMeshSpawnShapeValue
__WeightMeshSpawnShapeValue = __WeightMeshSpawnShapeValue
from builtins import str
try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = __import_once__("pygdx.graphics.g3d.particles")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue as __SpawnShapeValue
__SpawnShapeValue = __SpawnShapeValue
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as __ParticleValue
__ParticleValue = __ParticleValue
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue as __MeshSpawnShapeValue
__MeshSpawnShapeValue = __MeshSpawnShapeValue
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
 
class WeightMeshSpawnShapeValue(__MeshSpawnShapeValue, MeshSpawnShapeValue):
    """com.badlogic.gdx.graphics.g3d.particles.values.WeightMeshSpawnShapeValue"""
 
    @staticmethod
    def __wrap(java_value: __WeightMeshSpawnShapeValue) -> 'WeightMeshSpawnShapeValue':
        return WeightMeshSpawnShapeValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WeightMeshSpawnShapeValue):
        """
        Dynamic initializer for WeightMeshSpawnShapeValue.
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
    def spawn(self, arg0: 'Vector3', arg1: float) -> 'math.Vector3':
        """public final com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawn(com.badlogic.gdx.math.Vector3,float)"""
        return 'math.Vector3'.__wrap(super(__SpawnShapeValue, self).spawn(arg0, __float.valueOf(arg1)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.WeightMeshSpawnShapeValue()"""
        val = __WeightMeshSpawnShapeValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.WeightMeshSpawnShapeValue.init()"""
        super(WeightMeshSpawnShapeValue, self).init()

    @overload
    def calculateWeights(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.WeightMeshSpawnShapeValue.calculateWeights()"""
        super(WeightMeshSpawnShapeValue, self).calculateWeights()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setMesh(self, arg0: 'Mesh'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.setMesh(com.badlogic.gdx.graphics.Mesh)"""
        super(__MeshSpawnShapeValue, self).setMesh(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__MeshSpawnShapeValue, self).save(arg0, arg1)

    @override
    @overload
    def setMesh(self, arg0: 'Mesh', arg1: 'Model'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.setMesh(com.badlogic.gdx.graphics.Mesh,com.badlogic.gdx.graphics.g3d.Model)"""
        super(__MeshSpawnShapeValue, self).setMesh(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool.__wrap(super(ParticleValue, self).isActive())

    @overload
    def __init__(self, arg0: 'WeightMeshSpawnShapeValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.values.WeightMeshSpawnShapeValue(com.badlogic.gdx.graphics.g3d.particles.values.WeightMeshSpawnShapeValue)"""
        val = __WeightMeshSpawnShapeValue(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def spawnAux(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.WeightMeshSpawnShapeValue.spawnAux(com.badlogic.gdx.math.Vector3,float)"""
        super(__WeightMeshSpawnShapeValue, self).spawnAux(arg0, __float.valueOf(arg1))

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.setActive(boolean)"""
        super(__ParticleValue, self).setActive(__boolean.valueOf(arg0))

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__MeshSpawnShapeValue, self).load(arg0, arg1)

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
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.start()"""
        super(SpawnShapeValue, self).start()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.write(com.badlogic.gdx.utils.Json)"""
        super(__SpawnShapeValue, self).write(arg0)

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(__MeshSpawnShapeValue, self).load(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def copy(self) -> 'SpawnShapeValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue com.badlogic.gdx.graphics.g3d.particles.values.WeightMeshSpawnShapeValue.copy()"""
        return 'SpawnShapeValue'.__wrap(super(WeightMeshSpawnShapeValue, self).copy())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.WeightMeshSpawnShapeValue()"""
        val = __WeightMeshSpawnShapeValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__SpawnShapeValue, self).read(arg0, arg1) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue$SpawnSide
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue as __PrimitiveSpawnShapeValue_SpawnSide
__SpawnSide = __PrimitiveSpawnShapeValue_SpawnSide.SpawnSide
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
 
class SpawnSide(__Enum, Enum):
    """com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.SpawnSide"""
 
    @staticmethod
    def __wrap(java_value: __SpawnSide) -> 'SpawnSide':
        return SpawnSide(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SpawnSide):
        """
        Dynamic initializer for SpawnSide.
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

    @staticmethod
    @overload
    def values() -> List['SpawnSide']:
        """public static com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue$SpawnSide[] com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue$SpawnSide.values()"""
        return List[SpawnSide].__wrap(__SpawnSide.values())

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
    def valueOf(arg0: str) -> 'SpawnSide':
        """public static com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue$SpawnSide com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue$SpawnSide.valueOf(java.lang.String)"""
        return SpawnSide.__wrap(__SpawnSide.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = __import_once__("pygdx.graphics.g3d.particles")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue as __SpawnShapeValue
__SpawnShapeValue = __SpawnShapeValue
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as __ParticleValue
__ParticleValue = __ParticleValue
import com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue as __PrimitiveSpawnShapeValue_SpawnSide
__SpawnSide = __PrimitiveSpawnShapeValue_SpawnSide.SpawnSide
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue as __EllipseSpawnShapeValue
__EllipseSpawnShapeValue = __EllipseSpawnShapeValue
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue as __ScaledNumericValue
__ScaledNumericValue = __ScaledNumericValue
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue as __PrimitiveSpawnShapeValue
__PrimitiveSpawnShapeValue = __PrimitiveSpawnShapeValue
from builtins import int
 
class EllipseSpawnShapeValue(__PrimitiveSpawnShapeValue, PrimitiveSpawnShapeValue):
    """com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue"""
 
    @staticmethod
    def __wrap(java_value: __EllipseSpawnShapeValue) -> 'EllipseSpawnShapeValue':
        return EllipseSpawnShapeValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EllipseSpawnShapeValue):
        """
        Dynamic initializer for EllipseSpawnShapeValue.
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
    def spawn(self, arg0: 'Vector3', arg1: float) -> 'math.Vector3':
        """public final com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawn(com.badlogic.gdx.math.Vector3,float)"""
        return 'math.Vector3'.__wrap(super(__SpawnShapeValue, self).spawn(arg0, __float.valueOf(arg1)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue()"""
        val = __EllipseSpawnShapeValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue.write(com.badlogic.gdx.utils.Json)"""
        super(__EllipseSpawnShapeValue, self).write(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(__EllipseSpawnShapeValue, self).load(arg0)

    @override
    @overload
    def setEdges(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setEdges(boolean)"""
        super(__PrimitiveSpawnShapeValue, self).setEdges(__boolean.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__SpawnShapeValue, self).load(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'EllipseSpawnShapeValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue(com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue)"""
        val = __EllipseSpawnShapeValue(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue()"""
        val = __EllipseSpawnShapeValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool.__wrap(super(ParticleValue, self).isActive())

    @overload
    def getSide(self) -> 'SpawnSide':
        """public com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue$SpawnSide com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue.getSide()"""
        return 'SpawnSide'.__wrap(super(EllipseSpawnShapeValue, self).getSide())

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setActive(boolean)"""
        super(__PrimitiveSpawnShapeValue, self).setActive(__boolean.valueOf(arg0))

    @override
    @overload
    def getSpawnWidth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnWidth()"""
        return 'ScaledNumericValue'.__wrap(super(PrimitiveSpawnShapeValue, self).getSpawnWidth())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def isEdges(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.isEdges()"""
        return bool.__wrap(super(PrimitiveSpawnShapeValue, self).isEdges())

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__SpawnShapeValue, self).save(arg0, arg1)

    @override
    @overload
    def spawnAux(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue.spawnAux(com.badlogic.gdx.math.Vector3,float)"""
        super(__EllipseSpawnShapeValue, self).spawnAux(arg0, __float.valueOf(arg1))

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__EllipseSpawnShapeValue, self).read(arg0, arg1)

    @overload
    def setSide(self, arg0: 'SpawnSide'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue.setSide(com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue$SpawnSide)"""
        super(__EllipseSpawnShapeValue, self).setSide(arg0)

    @override
    @overload
    def getSpawnHeight(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnHeight()"""
        return 'ScaledNumericValue'.__wrap(super(PrimitiveSpawnShapeValue, self).getSpawnHeight())

    @override
    @overload
    def setDimensions(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setDimensions(float,float,float)"""
        super(__PrimitiveSpawnShapeValue, self).setDimensions(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

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
    def copy(self) -> 'SpawnShapeValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue.copy()"""
        return 'SpawnShapeValue'.__wrap(super(EllipseSpawnShapeValue, self).copy())

    @override
    @overload
    def getSpawnDepth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnDepth()"""
        return 'ScaledNumericValue'.__wrap(super(PrimitiveSpawnShapeValue, self).getSpawnDepth())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.init()"""
        super(SpawnShapeValue, self).init()

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.start()"""
        super(PrimitiveSpawnShapeValue, self).start() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = __import_once__("pygdx.graphics.g3d.particles")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
import com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue as __SpawnShapeValue
__SpawnShapeValue = __SpawnShapeValue
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as __ParticleValue
__ParticleValue = __ParticleValue
from abc import abstractmethod, ABC
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
from builtins import bool
from builtins import int
 
class SpawnShapeValue(ABC, __ParticleValue, ParticleValue, g3d.__ResourceData_Configurable, particles.ResourceData$Configurable, pygdx.__Json_Serializable, utils.Json$Serializable):
    """com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue"""
 
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

    @overload
    def spawn(self, arg0: 'Vector3', arg1: float) -> 'math.Vector3':
        """public final com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawn(com.badlogic.gdx.math.Vector3,float)"""
        return 'math.Vector3'.__wrap(super(__SpawnShapeValue, self).spawn(arg0, __float.valueOf(arg1)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__SpawnShapeValue, self).save(arg0, arg1)

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.setActive(boolean)"""
        super(__ParticleValue, self).setActive(__boolean.valueOf(arg0))

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(__SpawnShapeValue, self).load(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue()"""
        val = __SpawnShapeValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.copy()"""
        pass

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

    @overload
    def __init__(self, arg0: 'SpawnShapeValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue(com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue)"""
        val = __SpawnShapeValue(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue()"""
        val = __SpawnShapeValue()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.init()"""
        super(SpawnShapeValue, self).init()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def spawnAux(self, arg0: 'Vector3', arg1: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawnAux(com.badlogic.gdx.math.Vector3,float)"""
        pass

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__SpawnShapeValue, self).load(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.write(com.badlogic.gdx.utils.Json)"""
        super(__SpawnShapeValue, self).write(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.start()"""
        super(SpawnShapeValue, self).start()

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__SpawnShapeValue, self).read(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool.__wrap(super(ParticleValue, self).isActive())