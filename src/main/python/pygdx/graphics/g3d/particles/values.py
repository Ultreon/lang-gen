from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue as _PrimitiveSpawnShapeValue
_PrimitiveSpawnShapeValue = _PrimitiveSpawnShapeValue
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = _import_once("pygdx.graphics.g3d.particles")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as _ParticleValue
_ParticleValue = _ParticleValue
import java.lang.Boolean as _boolean
import com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue as _ScaledNumericValue
_ScaledNumericValue = _ScaledNumericValue
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue as _SpawnShapeValue
_SpawnShapeValue = _SpawnShapeValue
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PrimitiveSpawnShapeValue():
    """com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue"""
 
    @staticmethod
    def _wrap(java_value: _PrimitiveSpawnShapeValue) -> 'PrimitiveSpawnShapeValue':
        return PrimitiveSpawnShapeValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PrimitiveSpawnShapeValue):
        """
        Dynamic initializer for PrimitiveSpawnShapeValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PrimitiveSpawnShapeValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PrimitiveSpawnShapeValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue()"""
        val = _PrimitiveSpawnShapeValue()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'PrimitiveSpawnShapeValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue(com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue)"""
        val = _PrimitiveSpawnShapeValue(arg0)
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
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_PrimitiveSpawnShapeValue, self).read(arg0, arg1)

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

    @abstractmethod
    def spawnAux(self, arg0: 'Vector3', arg1: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawnAux(com.badlogic.gdx.math.Vector3,float)"""
        pass

    @overload
    def spawn(self, arg0: 'Vector3', arg1: float) -> 'math.Vector3':
        """public final com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawn(com.badlogic.gdx.math.Vector3,float)"""
        return 'math.Vector3'._wrap(super(_SpawnShapeValue, self).spawn(arg0, _float.valueOf(arg1)))

    @overload
    def isEdges(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.isEdges()"""
        return bool._wrap(super(PrimitiveSpawnShapeValue, self).isEdges())

    @overload
    def getSpawnWidth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnWidth()"""
        return 'ScaledNumericValue'._wrap(super(PrimitiveSpawnShapeValue, self).getSpawnWidth())

    @overload
    def setEdges(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setEdges(boolean)"""
        super(_PrimitiveSpawnShapeValue, self).setEdges(_boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue()"""
        val = _PrimitiveSpawnShapeValue()
        self.__wrapper = val

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setActive(boolean)"""
        super(_PrimitiveSpawnShapeValue, self).setActive(_boolean.valueOf(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool._wrap(super(ParticleValue, self).isActive())

    @overload
    def getSpawnHeight(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnHeight()"""
        return 'ScaledNumericValue'._wrap(super(PrimitiveSpawnShapeValue, self).getSpawnHeight())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setDimensions(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setDimensions(float,float,float)"""
        super(_PrimitiveSpawnShapeValue, self).setDimensions(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(_PrimitiveSpawnShapeValue, self).load(arg0)

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.write(com.badlogic.gdx.utils.Json)"""
        super(_PrimitiveSpawnShapeValue, self).write(arg0)

    @overload
    def getSpawnDepth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnDepth()"""
        return 'ScaledNumericValue'._wrap(super(PrimitiveSpawnShapeValue, self).getSpawnDepth())

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_SpawnShapeValue, self).load(arg0, arg1)

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

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_SpawnShapeValue, self).save(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue as _PrimitiveSpawnShapeValue
_PrimitiveSpawnShapeValue = _PrimitiveSpawnShapeValue
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = _import_once("pygdx.graphics.g3d.particles")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as _ParticleValue
_ParticleValue = _ParticleValue
import java.lang.Boolean as _boolean
import com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue as _ScaledNumericValue
_ScaledNumericValue = _ScaledNumericValue
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue as _SpawnShapeValue
_SpawnShapeValue = _SpawnShapeValue
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PrimitiveSpawnShapeValue():
    """com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue"""
 
    @staticmethod
    def _wrap(java_value: _PrimitiveSpawnShapeValue) -> 'PrimitiveSpawnShapeValue':
        return PrimitiveSpawnShapeValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PrimitiveSpawnShapeValue):
        """
        Dynamic initializer for PrimitiveSpawnShapeValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PrimitiveSpawnShapeValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PrimitiveSpawnShapeValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue()"""
        val = _PrimitiveSpawnShapeValue()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'PrimitiveSpawnShapeValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue(com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue)"""
        val = _PrimitiveSpawnShapeValue(arg0)
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
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_PrimitiveSpawnShapeValue, self).read(arg0, arg1)

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

    @abstractmethod
    def spawnAux(self, arg0: 'Vector3', arg1: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawnAux(com.badlogic.gdx.math.Vector3,float)"""
        pass

    @overload
    def spawn(self, arg0: 'Vector3', arg1: float) -> 'math.Vector3':
        """public final com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawn(com.badlogic.gdx.math.Vector3,float)"""
        return 'math.Vector3'._wrap(super(_SpawnShapeValue, self).spawn(arg0, _float.valueOf(arg1)))

    @overload
    def isEdges(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.isEdges()"""
        return bool._wrap(super(PrimitiveSpawnShapeValue, self).isEdges())

    @overload
    def getSpawnWidth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnWidth()"""
        return 'ScaledNumericValue'._wrap(super(PrimitiveSpawnShapeValue, self).getSpawnWidth())

    @overload
    def setEdges(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setEdges(boolean)"""
        super(_PrimitiveSpawnShapeValue, self).setEdges(_boolean.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue()"""
        val = _PrimitiveSpawnShapeValue()
        self.__wrapper = val

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setActive(boolean)"""
        super(_PrimitiveSpawnShapeValue, self).setActive(_boolean.valueOf(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool._wrap(super(ParticleValue, self).isActive())

    @overload
    def getSpawnHeight(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnHeight()"""
        return 'ScaledNumericValue'._wrap(super(PrimitiveSpawnShapeValue, self).getSpawnHeight())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setDimensions(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setDimensions(float,float,float)"""
        super(_PrimitiveSpawnShapeValue, self).setDimensions(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(_PrimitiveSpawnShapeValue, self).load(arg0)

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.write(com.badlogic.gdx.utils.Json)"""
        super(_PrimitiveSpawnShapeValue, self).write(arg0)

    @overload
    def getSpawnDepth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnDepth()"""
        return 'ScaledNumericValue'._wrap(super(PrimitiveSpawnShapeValue, self).getSpawnDepth())

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_SpawnShapeValue, self).load(arg0, arg1)

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

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_SpawnShapeValue, self).save(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.PointSpawnShapeValue
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue as _PrimitiveSpawnShapeValue
_PrimitiveSpawnShapeValue = _PrimitiveSpawnShapeValue
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = _import_once("pygdx.graphics.g3d.particles")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as _ParticleValue
_ParticleValue = _ParticleValue
import java.lang.Boolean as _boolean
import com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue as _ScaledNumericValue
_ScaledNumericValue = _ScaledNumericValue
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.values.PointSpawnShapeValue as _PointSpawnShapeValue
_PointSpawnShapeValue = _PointSpawnShapeValue
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue as _SpawnShapeValue
_SpawnShapeValue = _SpawnShapeValue
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PointSpawnShapeValue():
    """com.badlogic.gdx.graphics.g3d.particles.values.PointSpawnShapeValue"""
 
    @staticmethod
    def _wrap(java_value: _PointSpawnShapeValue) -> 'PointSpawnShapeValue':
        return PointSpawnShapeValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PointSpawnShapeValue):
        """
        Dynamic initializer for PointSpawnShapeValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PointSpawnShapeValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PointSpawnShapeValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def isEdges(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.isEdges()"""
        return bool._wrap(super(PrimitiveSpawnShapeValue, self).isEdges())

    @override
    @overload
    def copy(self) -> 'SpawnShapeValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue com.badlogic.gdx.graphics.g3d.particles.values.PointSpawnShapeValue.copy()"""
        return 'SpawnShapeValue'._wrap(super(PointSpawnShapeValue, self).copy())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_PrimitiveSpawnShapeValue, self).read(arg0, arg1)

    @override
    @overload
    def getSpawnDepth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnDepth()"""
        return 'ScaledNumericValue'._wrap(super(PrimitiveSpawnShapeValue, self).getSpawnDepth())

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
    def spawn(self, arg0: 'Vector3', arg1: float) -> 'math.Vector3':
        """public final com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawn(com.badlogic.gdx.math.Vector3,float)"""
        return 'math.Vector3'._wrap(super(_SpawnShapeValue, self).spawn(arg0, _float.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'PointSpawnShapeValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.values.PointSpawnShapeValue(com.badlogic.gdx.graphics.g3d.particles.values.PointSpawnShapeValue)"""
        val = _PointSpawnShapeValue(arg0)
        self.__wrapper = val

    @override
    @overload
    def spawnAux(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PointSpawnShapeValue.spawnAux(com.badlogic.gdx.math.Vector3,float)"""
        super(_PointSpawnShapeValue, self).spawnAux(arg0, _float.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setActive(boolean)"""
        super(_PrimitiveSpawnShapeValue, self).setActive(_boolean.valueOf(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool._wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def setDimensions(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setDimensions(float,float,float)"""
        super(_PrimitiveSpawnShapeValue, self).setDimensions(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.PointSpawnShapeValue()"""
        val = _PointSpawnShapeValue()
        self.__wrapper = val

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(_PrimitiveSpawnShapeValue, self).load(arg0)

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.write(com.badlogic.gdx.utils.Json)"""
        super(_PrimitiveSpawnShapeValue, self).write(arg0)

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_SpawnShapeValue, self).load(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getSpawnWidth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnWidth()"""
        return 'ScaledNumericValue'._wrap(super(PrimitiveSpawnShapeValue, self).getSpawnWidth())

    @override
    @overload
    def setEdges(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setEdges(boolean)"""
        super(_PrimitiveSpawnShapeValue, self).setEdges(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getSpawnHeight(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnHeight()"""
        return 'ScaledNumericValue'._wrap(super(PrimitiveSpawnShapeValue, self).getSpawnHeight())

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

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_SpawnShapeValue, self).save(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.PointSpawnShapeValue()"""
        val = _PointSpawnShapeValue()
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.CylinderSpawnShapeValue
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue as _PrimitiveSpawnShapeValue
_PrimitiveSpawnShapeValue = _PrimitiveSpawnShapeValue
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = _import_once("pygdx.graphics.g3d.particles")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.values.CylinderSpawnShapeValue as _CylinderSpawnShapeValue
_CylinderSpawnShapeValue = _CylinderSpawnShapeValue
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as _ParticleValue
_ParticleValue = _ParticleValue
import java.lang.Boolean as _boolean
import com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue as _ScaledNumericValue
_ScaledNumericValue = _ScaledNumericValue
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue as _SpawnShapeValue
_SpawnShapeValue = _SpawnShapeValue
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CylinderSpawnShapeValue():
    """com.badlogic.gdx.graphics.g3d.particles.values.CylinderSpawnShapeValue"""
 
    @staticmethod
    def _wrap(java_value: _CylinderSpawnShapeValue) -> 'CylinderSpawnShapeValue':
        return CylinderSpawnShapeValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CylinderSpawnShapeValue):
        """
        Dynamic initializer for CylinderSpawnShapeValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CylinderSpawnShapeValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CylinderSpawnShapeValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def spawnAux(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.CylinderSpawnShapeValue.spawnAux(com.badlogic.gdx.math.Vector3,float)"""
        super(_CylinderSpawnShapeValue, self).spawnAux(arg0, _float.valueOf(arg1))

    @override
    @overload
    def isEdges(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.isEdges()"""
        return bool._wrap(super(PrimitiveSpawnShapeValue, self).isEdges())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_PrimitiveSpawnShapeValue, self).read(arg0, arg1)

    @override
    @overload
    def getSpawnDepth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnDepth()"""
        return 'ScaledNumericValue'._wrap(super(PrimitiveSpawnShapeValue, self).getSpawnDepth())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.CylinderSpawnShapeValue()"""
        val = _CylinderSpawnShapeValue()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def spawn(self, arg0: 'Vector3', arg1: float) -> 'math.Vector3':
        """public final com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawn(com.badlogic.gdx.math.Vector3,float)"""
        return 'math.Vector3'._wrap(super(_SpawnShapeValue, self).spawn(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def copy(self) -> 'SpawnShapeValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue com.badlogic.gdx.graphics.g3d.particles.values.CylinderSpawnShapeValue.copy()"""
        return 'SpawnShapeValue'._wrap(super(CylinderSpawnShapeValue, self).copy())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.CylinderSpawnShapeValue()"""
        val = _CylinderSpawnShapeValue()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setActive(boolean)"""
        super(_PrimitiveSpawnShapeValue, self).setActive(_boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'CylinderSpawnShapeValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.values.CylinderSpawnShapeValue(com.badlogic.gdx.graphics.g3d.particles.values.CylinderSpawnShapeValue)"""
        val = _CylinderSpawnShapeValue(arg0)
        self.__wrapper = val

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool._wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def setDimensions(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setDimensions(float,float,float)"""
        super(_PrimitiveSpawnShapeValue, self).setDimensions(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(_PrimitiveSpawnShapeValue, self).load(arg0)

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.write(com.badlogic.gdx.utils.Json)"""
        super(_PrimitiveSpawnShapeValue, self).write(arg0)

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_SpawnShapeValue, self).load(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getSpawnWidth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnWidth()"""
        return 'ScaledNumericValue'._wrap(super(PrimitiveSpawnShapeValue, self).getSpawnWidth())

    @override
    @overload
    def setEdges(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setEdges(boolean)"""
        super(_PrimitiveSpawnShapeValue, self).setEdges(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getSpawnHeight(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnHeight()"""
        return 'ScaledNumericValue'._wrap(super(PrimitiveSpawnShapeValue, self).getSpawnHeight())

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

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_SpawnShapeValue, self).save(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue$Triangle
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue as _MeshSpawnShapeValue_Triangle
_Triangle = _MeshSpawnShapeValue_Triangle.Triangle
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
 
class Triangle():
    """com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.Triangle"""
 
    @staticmethod
    def _wrap(java_value: _Triangle) -> 'Triangle':
        return Triangle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Triangle):
        """
        Dynamic initializer for Triangle.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Triangle__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Triangle__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def pick(self, arg0: 'Vector3') -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue$Triangle.pick(com.badlogic.gdx.math.Vector3)"""
        return 'math.Vector3'._wrap(super(_Triangle, self).pick(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue$Triangle(float,float,float,float,float,float,float,float,float)"""
        val = _Triangle(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8))
        self.__wrapper = val

    @staticmethod
    @overload
    def pick(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: 'Vector3') -> 'math.Vector3':
        """public static com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue$Triangle.pick(float,float,float,float,float,float,float,float,float,com.badlogic.gdx.math.Vector3)"""
        return math.Vector3._wrap(_Triangle.pick(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), arg9))

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

import com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue as _RangedNumericValue
_RangedNumericValue = _RangedNumericValue
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Float as _float
import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as _ParticleValue
_ParticleValue = _ParticleValue
import com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue as _ScaledNumericValue
_ScaledNumericValue = _ScaledNumericValue
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ScaledNumericValue():
    """com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue"""
 
    @staticmethod
    def _wrap(java_value: _ScaledNumericValue) -> 'ScaledNumericValue':
        return ScaledNumericValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ScaledNumericValue):
        """
        Dynamic initializer for ScaledNumericValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ScaledNumericValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ScaledNumericValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(_ParticleValue, self).load(arg0)

    @override
    @overload
    def load(self, arg0: 'RangedNumericValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.load(com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue)"""
        super(_RangedNumericValue, self).load(arg0)

    @overload
    def setHigh(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.setHigh(float,float)"""
        super(_ScaledNumericValue, self).setHigh(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def getScale(self, arg0: float) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.getScale(float)"""
        return float._wrap(super(_ScaledNumericValue, self).getScale(_float.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.write(com.badlogic.gdx.utils.Json)"""
        super(_ScaledNumericValue, self).write(arg0)

    @override
    @overload
    def setLow(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.setLow(float,float)"""
        super(_RangedNumericValue, self).setLow(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue()"""
        val = _ScaledNumericValue()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue()"""
        val = _ScaledNumericValue()
        self.__wrapper = val

    @overload
    def load(self, arg0: 'ScaledNumericValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue)"""
        super(_ScaledNumericValue, self).load(arg0)

    @overload
    def getScaling(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.getScaling()"""
        return List[float]._wrap(super(ScaledNumericValue, self).getScaling())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setRelative(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.setRelative(boolean)"""
        super(_ScaledNumericValue, self).setRelative(_boolean.valueOf(arg0))

    @overload
    def setHighMin(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.setHighMin(float)"""
        super(_ScaledNumericValue, self).setHighMin(_float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setTimeline(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.setTimeline(float[])"""
        super(_ScaledNumericValue, self).setTimeline(arg0)

    @override
    @overload
    def setLowMax(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.setLowMax(float)"""
        super(_RangedNumericValue, self).setLowMax(_float.valueOf(arg0))

    @override
    @overload
    def setLowMin(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.setLowMin(float)"""
        super(_RangedNumericValue, self).setLowMin(_float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def isRelative(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.isRelative()"""
        return bool._wrap(super(ScaledNumericValue, self).isRelative())

    @overload
    def setHighMax(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.setHighMax(float)"""
        super(_ScaledNumericValue, self).setHighMax(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool._wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setHigh(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.setHigh(float)"""
        super(_ScaledNumericValue, self).setHigh(_float.valueOf(arg0))

    @overload
    def setScaling(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.setScaling(float[])"""
        super(_ScaledNumericValue, self).setScaling(arg0)

    @overload
    def newHighValue(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.newHighValue()"""
        return float._wrap(super(ScaledNumericValue, self).newHighValue())

    @overload
    def getHighMin(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.getHighMin()"""
        return float._wrap(super(ScaledNumericValue, self).getHighMin())

    @override
    @overload
    def getLowMax(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.getLowMax()"""
        return float._wrap(super(RangedNumericValue, self).getLowMax())

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_ScaledNumericValue, self).read(arg0, arg1)

    @overload
    def getTimeline(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.getTimeline()"""
        return List[float]._wrap(super(ScaledNumericValue, self).getTimeline())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getLowMin(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.getLowMin()"""
        return float._wrap(super(RangedNumericValue, self).getLowMin())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def newLowValue(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.newLowValue()"""
        return float._wrap(super(RangedNumericValue, self).newLowValue())

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.setActive(boolean)"""
        super(_ParticleValue, self).setActive(_boolean.valueOf(arg0))

    @overload
    def getHighMax(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue.getHighMax()"""
        return float._wrap(super(ScaledNumericValue, self).getHighMax())

    @override
    @overload
    def setLow(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.setLow(float)"""
        super(_RangedNumericValue, self).setLow(_float.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = _import_once("pygdx.graphics.g3d.particles")

try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as _ParticleValue
_ParticleValue = _ParticleValue
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue as _SpawnShapeValue
_SpawnShapeValue = _SpawnShapeValue
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SpawnShapeValue():
    """com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue"""
 
    @staticmethod
    def _wrap(java_value: _SpawnShapeValue) -> 'SpawnShapeValue':
        return SpawnShapeValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SpawnShapeValue):
        """
        Dynamic initializer for SpawnShapeValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SpawnShapeValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SpawnShapeValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(_SpawnShapeValue, self).load(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

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
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool._wrap(super(ParticleValue, self).isActive())

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

    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.init()"""
        super(SpawnShapeValue, self).init()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.write(com.badlogic.gdx.utils.Json)"""
        super(_SpawnShapeValue, self).write(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_SpawnShapeValue, self).read(arg0, arg1)

    @abstractmethod
    def spawnAux(self, arg0: 'Vector3', arg1: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawnAux(com.badlogic.gdx.math.Vector3,float)"""
        pass

    @overload
    def spawn(self, arg0: 'Vector3', arg1: float) -> 'math.Vector3':
        """public final com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawn(com.badlogic.gdx.math.Vector3,float)"""
        return 'math.Vector3'._wrap(super(_SpawnShapeValue, self).spawn(arg0, _float.valueOf(arg1)))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue()"""
        val = _SpawnShapeValue()
        self.__wrapper = val

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_SpawnShapeValue, self).load(arg0, arg1)

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
    def __init__(self, arg0: 'SpawnShapeValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue(com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue)"""
        val = _SpawnShapeValue(arg0)
        self.__wrapper = val

    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.start()"""
        super(SpawnShapeValue, self).start()

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.setActive(boolean)"""
        super(_ParticleValue, self).setActive(_boolean.valueOf(arg0))

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_SpawnShapeValue, self).save(arg0, arg1)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue()"""
        val = _SpawnShapeValue()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue
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
import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as _ParticleValue
_ParticleValue = _ParticleValue
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParticleValue():
    """com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue"""
 
    @staticmethod
    def _wrap(java_value: _ParticleValue) -> 'ParticleValue':
        return ParticleValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleValue):
        """
        Dynamic initializer for ParticleValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.setActive(boolean)"""
        super(_ParticleValue, self).setActive(_boolean.valueOf(arg0))

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
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(_ParticleValue, self).load(arg0)

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.write(com.badlogic.gdx.utils.Json)"""
        super(_ParticleValue, self).write(arg0)

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_ParticleValue, self).read(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool._wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue()"""
        val = _ParticleValue()
        self.__wrapper = val

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue()"""
        val = _ParticleValue()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'ParticleValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        val = _ParticleValue(arg0)
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue as _PrimitiveSpawnShapeValue
_PrimitiveSpawnShapeValue = _PrimitiveSpawnShapeValue
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = _import_once("pygdx.graphics.g3d.particles")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue as _EllipseSpawnShapeValue
_EllipseSpawnShapeValue = _EllipseSpawnShapeValue
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as _ParticleValue
_ParticleValue = _ParticleValue
import java.lang.Boolean as _boolean
import com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue as _ScaledNumericValue
_ScaledNumericValue = _ScaledNumericValue
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue as _PrimitiveSpawnShapeValue_SpawnSide
_SpawnSide = _PrimitiveSpawnShapeValue_SpawnSide.SpawnSide
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue as _SpawnShapeValue
_SpawnShapeValue = _SpawnShapeValue
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EllipseSpawnShapeValue():
    """com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue"""
 
    @staticmethod
    def _wrap(java_value: _EllipseSpawnShapeValue) -> 'EllipseSpawnShapeValue':
        return EllipseSpawnShapeValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EllipseSpawnShapeValue):
        """
        Dynamic initializer for EllipseSpawnShapeValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EllipseSpawnShapeValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EllipseSpawnShapeValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_EllipseSpawnShapeValue, self).read(arg0, arg1)

    @override
    @overload
    def isEdges(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.isEdges()"""
        return bool._wrap(super(PrimitiveSpawnShapeValue, self).isEdges())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getSpawnDepth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnDepth()"""
        return 'ScaledNumericValue'._wrap(super(PrimitiveSpawnShapeValue, self).getSpawnDepth())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def spawnAux(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue.spawnAux(com.badlogic.gdx.math.Vector3,float)"""
        super(_EllipseSpawnShapeValue, self).spawnAux(arg0, _float.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def spawn(self, arg0: 'Vector3', arg1: float) -> 'math.Vector3':
        """public final com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawn(com.badlogic.gdx.math.Vector3,float)"""
        return 'math.Vector3'._wrap(super(_SpawnShapeValue, self).spawn(arg0, _float.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(_EllipseSpawnShapeValue, self).load(arg0)

    @override
    @overload
    def copy(self) -> 'SpawnShapeValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue.copy()"""
        return 'SpawnShapeValue'._wrap(super(EllipseSpawnShapeValue, self).copy())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setActive(boolean)"""
        super(_PrimitiveSpawnShapeValue, self).setActive(_boolean.valueOf(arg0))

    @overload
    def getSide(self) -> 'SpawnSide':
        """public com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue$SpawnSide com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue.getSide()"""
        return 'SpawnSide'._wrap(super(EllipseSpawnShapeValue, self).getSide())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool._wrap(super(ParticleValue, self).isActive())

    @overload
    def setSide(self, arg0: 'SpawnSide'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue.setSide(com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue$SpawnSide)"""
        super(_EllipseSpawnShapeValue, self).setSide(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def setDimensions(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setDimensions(float,float,float)"""
        super(_PrimitiveSpawnShapeValue, self).setDimensions(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue()"""
        val = _EllipseSpawnShapeValue()
        self.__wrapper = val

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_SpawnShapeValue, self).load(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue.write(com.badlogic.gdx.utils.Json)"""
        super(_EllipseSpawnShapeValue, self).write(arg0)

    @override
    @overload
    def getSpawnWidth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnWidth()"""
        return 'ScaledNumericValue'._wrap(super(PrimitiveSpawnShapeValue, self).getSpawnWidth())

    @override
    @overload
    def setEdges(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setEdges(boolean)"""
        super(_PrimitiveSpawnShapeValue, self).setEdges(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getSpawnHeight(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnHeight()"""
        return 'ScaledNumericValue'._wrap(super(PrimitiveSpawnShapeValue, self).getSpawnHeight())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue()"""
        val = _EllipseSpawnShapeValue()
        self.__wrapper = val

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

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_SpawnShapeValue, self).save(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'EllipseSpawnShapeValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue(com.badlogic.gdx.graphics.g3d.particles.values.EllipseSpawnShapeValue)"""
        val = _EllipseSpawnShapeValue(arg0)
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = _import_once("pygdx.graphics.g3d.particles")

try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

import com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue as _MeshSpawnShapeValue
_MeshSpawnShapeValue = _MeshSpawnShapeValue
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as _ParticleValue
_ParticleValue = _ParticleValue
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue as _SpawnShapeValue
_SpawnShapeValue = _SpawnShapeValue
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MeshSpawnShapeValue():
    """com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue"""
 
    @staticmethod
    def _wrap(java_value: _MeshSpawnShapeValue) -> 'MeshSpawnShapeValue':
        return MeshSpawnShapeValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MeshSpawnShapeValue):
        """
        Dynamic initializer for MeshSpawnShapeValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MeshSpawnShapeValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MeshSpawnShapeValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue()"""
        val = _MeshSpawnShapeValue()
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
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(_MeshSpawnShapeValue, self).load(arg0)

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

    @abstractmethod
    def spawnAux(self, arg0: 'Vector3', arg1: float):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawnAux(com.badlogic.gdx.math.Vector3,float)"""
        pass

    @overload
    def spawn(self, arg0: 'Vector3', arg1: float) -> 'math.Vector3':
        """public final com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawn(com.badlogic.gdx.math.Vector3,float)"""
        return 'math.Vector3'._wrap(super(_SpawnShapeValue, self).spawn(arg0, _float.valueOf(arg1)))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue()"""
        val = _MeshSpawnShapeValue()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_MeshSpawnShapeValue, self).load(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool._wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.start()"""
        super(SpawnShapeValue, self).start()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.write(com.badlogic.gdx.utils.Json)"""
        super(_SpawnShapeValue, self).write(arg0)

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_SpawnShapeValue, self).read(arg0, arg1)

    @overload
    def __init__(self, arg0: 'MeshSpawnShapeValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue(com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue)"""
        val = _MeshSpawnShapeValue(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setMesh(self, arg0: 'Mesh', arg1: 'Model'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.setMesh(com.badlogic.gdx.graphics.Mesh,com.badlogic.gdx.graphics.g3d.Model)"""
        super(_MeshSpawnShapeValue, self).setMesh(arg0, arg1)

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_MeshSpawnShapeValue, self).save(arg0, arg1)

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
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.setActive(boolean)"""
        super(_ParticleValue, self).setActive(_boolean.valueOf(arg0))

    @overload
    def setMesh(self, arg0: 'Mesh'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.setMesh(com.badlogic.gdx.graphics.Mesh)"""
        super(_MeshSpawnShapeValue, self).setMesh(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.NumericValue
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
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as _ParticleValue
_ParticleValue = _ParticleValue
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.values.NumericValue as _NumericValue
_NumericValue = _NumericValue
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class NumericValue():
    """com.badlogic.gdx.graphics.g3d.particles.values.NumericValue"""
 
    @staticmethod
    def _wrap(java_value: _NumericValue) -> 'NumericValue':
        return NumericValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _NumericValue):
        """
        Dynamic initializer for NumericValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_NumericValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_NumericValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(_ParticleValue, self).load(arg0)

    @overload
    def load(self, arg0: 'NumericValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.NumericValue.load(com.badlogic.gdx.graphics.g3d.particles.values.NumericValue)"""
        super(_NumericValue, self).load(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.NumericValue.write(com.badlogic.gdx.utils.Json)"""
        super(_NumericValue, self).write(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool._wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getValue(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.values.NumericValue.getValue()"""
        return float._wrap(super(NumericValue, self).getValue())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.NumericValue()"""
        val = _NumericValue()
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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setValue(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.NumericValue.setValue(float)"""
        super(_NumericValue, self).setValue(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.setActive(boolean)"""
        super(_ParticleValue, self).setActive(_boolean.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.NumericValue()"""
        val = _NumericValue()
        self.__wrapper = val

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.NumericValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_NumericValue, self).read(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.UnweightedMeshSpawnShapeValue
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = _import_once("pygdx.graphics.g3d.particles")

try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue as _MeshSpawnShapeValue
_MeshSpawnShapeValue = _MeshSpawnShapeValue
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as _ParticleValue
_ParticleValue = _ParticleValue
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.values.UnweightedMeshSpawnShapeValue as _UnweightedMeshSpawnShapeValue
_UnweightedMeshSpawnShapeValue = _UnweightedMeshSpawnShapeValue
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue as _SpawnShapeValue
_SpawnShapeValue = _SpawnShapeValue
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class UnweightedMeshSpawnShapeValue():
    """com.badlogic.gdx.graphics.g3d.particles.values.UnweightedMeshSpawnShapeValue"""
 
    @staticmethod
    def _wrap(java_value: _UnweightedMeshSpawnShapeValue) -> 'UnweightedMeshSpawnShapeValue':
        return UnweightedMeshSpawnShapeValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UnweightedMeshSpawnShapeValue):
        """
        Dynamic initializer for UnweightedMeshSpawnShapeValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UnweightedMeshSpawnShapeValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UnweightedMeshSpawnShapeValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setMesh(self, arg0: 'Mesh'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.setMesh(com.badlogic.gdx.graphics.Mesh)"""
        super(_MeshSpawnShapeValue, self).setMesh(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(_MeshSpawnShapeValue, self).load(arg0)

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
    def __init__(self, arg0: 'UnweightedMeshSpawnShapeValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.values.UnweightedMeshSpawnShapeValue(com.badlogic.gdx.graphics.g3d.particles.values.UnweightedMeshSpawnShapeValue)"""
        val = _UnweightedMeshSpawnShapeValue(arg0)
        self.__wrapper = val

    @overload
    def spawn(self, arg0: 'Vector3', arg1: float) -> 'math.Vector3':
        """public final com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawn(com.badlogic.gdx.math.Vector3,float)"""
        return 'math.Vector3'._wrap(super(_SpawnShapeValue, self).spawn(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def copy(self) -> 'SpawnShapeValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue com.badlogic.gdx.graphics.g3d.particles.values.UnweightedMeshSpawnShapeValue.copy()"""
        return 'SpawnShapeValue'._wrap(super(UnweightedMeshSpawnShapeValue, self).copy())

    @override
    @overload
    def spawnAux(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.UnweightedMeshSpawnShapeValue.spawnAux(com.badlogic.gdx.math.Vector3,float)"""
        super(_UnweightedMeshSpawnShapeValue, self).spawnAux(arg0, _float.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_MeshSpawnShapeValue, self).load(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.UnweightedMeshSpawnShapeValue()"""
        val = _UnweightedMeshSpawnShapeValue()
        self.__wrapper = val

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool._wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def setMesh(self, arg0: 'Mesh', arg1: 'Model'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.UnweightedMeshSpawnShapeValue.setMesh(com.badlogic.gdx.graphics.Mesh,com.badlogic.gdx.graphics.g3d.Model)"""
        super(_UnweightedMeshSpawnShapeValue, self).setMesh(arg0, arg1)

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.start()"""
        super(SpawnShapeValue, self).start()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.write(com.badlogic.gdx.utils.Json)"""
        super(_SpawnShapeValue, self).write(arg0)

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_SpawnShapeValue, self).read(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.UnweightedMeshSpawnShapeValue()"""
        val = _UnweightedMeshSpawnShapeValue()
        self.__wrapper = val

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_MeshSpawnShapeValue, self).save(arg0, arg1)

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
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.setActive(boolean)"""
        super(_ParticleValue, self).setActive(_boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.LineSpawnShapeValue
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue as _PrimitiveSpawnShapeValue
_PrimitiveSpawnShapeValue = _PrimitiveSpawnShapeValue
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = _import_once("pygdx.graphics.g3d.particles")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as _ParticleValue
_ParticleValue = _ParticleValue
import java.lang.Boolean as _boolean
import com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue as _ScaledNumericValue
_ScaledNumericValue = _ScaledNumericValue
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.values.LineSpawnShapeValue as _LineSpawnShapeValue
_LineSpawnShapeValue = _LineSpawnShapeValue
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue as _SpawnShapeValue
_SpawnShapeValue = _SpawnShapeValue
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LineSpawnShapeValue():
    """com.badlogic.gdx.graphics.g3d.particles.values.LineSpawnShapeValue"""
 
    @staticmethod
    def _wrap(java_value: _LineSpawnShapeValue) -> 'LineSpawnShapeValue':
        return LineSpawnShapeValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LineSpawnShapeValue):
        """
        Dynamic initializer for LineSpawnShapeValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LineSpawnShapeValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LineSpawnShapeValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def isEdges(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.isEdges()"""
        return bool._wrap(super(PrimitiveSpawnShapeValue, self).isEdges())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_PrimitiveSpawnShapeValue, self).read(arg0, arg1)

    @override
    @overload
    def getSpawnDepth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnDepth()"""
        return 'ScaledNumericValue'._wrap(super(PrimitiveSpawnShapeValue, self).getSpawnDepth())

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
    def spawn(self, arg0: 'Vector3', arg1: float) -> 'math.Vector3':
        """public final com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawn(com.badlogic.gdx.math.Vector3,float)"""
        return 'math.Vector3'._wrap(super(_SpawnShapeValue, self).spawn(arg0, _float.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def spawnAux(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.LineSpawnShapeValue.spawnAux(com.badlogic.gdx.math.Vector3,float)"""
        super(_LineSpawnShapeValue, self).spawnAux(arg0, _float.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.LineSpawnShapeValue()"""
        val = _LineSpawnShapeValue()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'LineSpawnShapeValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.values.LineSpawnShapeValue(com.badlogic.gdx.graphics.g3d.particles.values.LineSpawnShapeValue)"""
        val = _LineSpawnShapeValue(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setActive(boolean)"""
        super(_PrimitiveSpawnShapeValue, self).setActive(_boolean.valueOf(arg0))

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool._wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def copy(self) -> 'SpawnShapeValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue com.badlogic.gdx.graphics.g3d.particles.values.LineSpawnShapeValue.copy()"""
        return 'SpawnShapeValue'._wrap(super(LineSpawnShapeValue, self).copy())

    @override
    @overload
    def setDimensions(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setDimensions(float,float,float)"""
        super(_PrimitiveSpawnShapeValue, self).setDimensions(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(_PrimitiveSpawnShapeValue, self).load(arg0)

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.write(com.badlogic.gdx.utils.Json)"""
        super(_PrimitiveSpawnShapeValue, self).write(arg0)

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_SpawnShapeValue, self).load(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getSpawnWidth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnWidth()"""
        return 'ScaledNumericValue'._wrap(super(PrimitiveSpawnShapeValue, self).getSpawnWidth())

    @override
    @overload
    def setEdges(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setEdges(boolean)"""
        super(_PrimitiveSpawnShapeValue, self).setEdges(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getSpawnHeight(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnHeight()"""
        return 'ScaledNumericValue'._wrap(super(PrimitiveSpawnShapeValue, self).getSpawnHeight())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.LineSpawnShapeValue()"""
        val = _LineSpawnShapeValue()
        self.__wrapper = val

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

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_SpawnShapeValue, self).save(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue
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
from builtins import float
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Float as _float
import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as _ParticleValue
_ParticleValue = _ParticleValue
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue as _GradientColorValue
_GradientColorValue = _GradientColorValue
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GradientColorValue():
    """com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue"""
 
    @staticmethod
    def _wrap(java_value: _GradientColorValue) -> 'GradientColorValue':
        return GradientColorValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GradientColorValue):
        """
        Dynamic initializer for GradientColorValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GradientColorValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GradientColorValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(_ParticleValue, self).load(arg0)

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue.write(com.badlogic.gdx.utils.Json)"""
        super(_GradientColorValue, self).write(arg0)

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

    @overload
    def setTimeline(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue.setTimeline(float[])"""
        super(_GradientColorValue, self).setTimeline(arg0)

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool._wrap(super(ParticleValue, self).isActive())

    @overload
    def getTimeline(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue.getTimeline()"""
        return List[float]._wrap(super(GradientColorValue, self).getTimeline())

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

    @overload
    def load(self, arg0: 'GradientColorValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue.load(com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue)"""
        super(_GradientColorValue, self).load(arg0)

    @overload
    def getColor(self, arg0: float) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue.getColor(float)"""
        return List[float]._wrap(super(_GradientColorValue, self).getColor(_float.valueOf(arg0)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue()"""
        val = _GradientColorValue()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue()"""
        val = _GradientColorValue()
        self.__wrapper = val

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_GradientColorValue, self).read(arg0, arg1)

    @overload
    def getColor(self, arg0: float, arg1: 'float', arg2: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue.getColor(float,float[],int)"""
        super(_GradientColorValue, self).getColor(_float.valueOf(arg0), arg1, _int.valueOf(arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getColors(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue.getColors()"""
        return List[float]._wrap(super(GradientColorValue, self).getColors())

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.setActive(boolean)"""
        super(_ParticleValue, self).setActive(_boolean.valueOf(arg0))

    @overload
    def setColors(self, arg0: 'float'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.GradientColorValue.setColors(float[])"""
        super(_GradientColorValue, self).setColors(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue$SpawnSide
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
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue as _PrimitiveSpawnShapeValue_SpawnSide
_SpawnSide = _PrimitiveSpawnShapeValue_SpawnSide.SpawnSide
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SpawnSide():
    """com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.SpawnSide"""
 
    @staticmethod
    def _wrap(java_value: _SpawnSide) -> 'SpawnSide':
        return SpawnSide(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SpawnSide):
        """
        Dynamic initializer for SpawnSide.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SpawnSide__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SpawnSide__wrapper":
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

    @staticmethod
    @overload
    def values() -> List['SpawnSide']:
        """public static com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue$SpawnSide[] com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue$SpawnSide.values()"""
        return List[SpawnSide]._wrap(_SpawnSide.values())

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
    def valueOf(arg0: str) -> 'SpawnSide':
        """public static com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue$SpawnSide com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue$SpawnSide.valueOf(java.lang.String)"""
        return SpawnSide._wrap(_SpawnSide.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.WeightMeshSpawnShapeValue
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = _import_once("pygdx.graphics.g3d.particles")

try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue as _MeshSpawnShapeValue
_MeshSpawnShapeValue = _MeshSpawnShapeValue
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.particles.values.WeightMeshSpawnShapeValue as _WeightMeshSpawnShapeValue
_WeightMeshSpawnShapeValue = _WeightMeshSpawnShapeValue
import java.lang.Float as _float
import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as _ParticleValue
_ParticleValue = _ParticleValue
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue as _SpawnShapeValue
_SpawnShapeValue = _SpawnShapeValue
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WeightMeshSpawnShapeValue():
    """com.badlogic.gdx.graphics.g3d.particles.values.WeightMeshSpawnShapeValue"""
 
    @staticmethod
    def _wrap(java_value: _WeightMeshSpawnShapeValue) -> 'WeightMeshSpawnShapeValue':
        return WeightMeshSpawnShapeValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WeightMeshSpawnShapeValue):
        """
        Dynamic initializer for WeightMeshSpawnShapeValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WeightMeshSpawnShapeValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WeightMeshSpawnShapeValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setMesh(self, arg0: 'Mesh'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.setMesh(com.badlogic.gdx.graphics.Mesh)"""
        super(_MeshSpawnShapeValue, self).setMesh(arg0)

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
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(_MeshSpawnShapeValue, self).load(arg0)

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
    def setMesh(self, arg0: 'Mesh', arg1: 'Model'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.setMesh(com.badlogic.gdx.graphics.Mesh,com.badlogic.gdx.graphics.g3d.Model)"""
        super(_MeshSpawnShapeValue, self).setMesh(arg0, arg1)

    @overload
    def spawn(self, arg0: 'Vector3', arg1: float) -> 'math.Vector3':
        """public final com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawn(com.badlogic.gdx.math.Vector3,float)"""
        return 'math.Vector3'._wrap(super(_SpawnShapeValue, self).spawn(arg0, _float.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.WeightMeshSpawnShapeValue()"""
        val = _WeightMeshSpawnShapeValue()
        self.__wrapper = val

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_MeshSpawnShapeValue, self).load(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.WeightMeshSpawnShapeValue()"""
        val = _WeightMeshSpawnShapeValue()
        self.__wrapper = val

    @override
    @overload
    def copy(self) -> 'SpawnShapeValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue com.badlogic.gdx.graphics.g3d.particles.values.WeightMeshSpawnShapeValue.copy()"""
        return 'SpawnShapeValue'._wrap(super(WeightMeshSpawnShapeValue, self).copy())

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool._wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.start()"""
        super(SpawnShapeValue, self).start()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.write(com.badlogic.gdx.utils.Json)"""
        super(_SpawnShapeValue, self).write(arg0)

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_SpawnShapeValue, self).read(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.MeshSpawnShapeValue.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_MeshSpawnShapeValue, self).save(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def spawnAux(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.WeightMeshSpawnShapeValue.spawnAux(com.badlogic.gdx.math.Vector3,float)"""
        super(_WeightMeshSpawnShapeValue, self).spawnAux(arg0, _float.valueOf(arg1))

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.setActive(boolean)"""
        super(_ParticleValue, self).setActive(_boolean.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'WeightMeshSpawnShapeValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.values.WeightMeshSpawnShapeValue(com.badlogic.gdx.graphics.g3d.particles.values.WeightMeshSpawnShapeValue)"""
        val = _WeightMeshSpawnShapeValue(arg0)
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue as _PrimitiveSpawnShapeValue
_PrimitiveSpawnShapeValue = _PrimitiveSpawnShapeValue
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = _import_once("pygdx.graphics.g3d.particles")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue as _RectangleSpawnShapeValue
_RectangleSpawnShapeValue = _RectangleSpawnShapeValue
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as _ParticleValue
_ParticleValue = _ParticleValue
import java.lang.Boolean as _boolean
import com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue as _ScaledNumericValue
_ScaledNumericValue = _ScaledNumericValue
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue as _SpawnShapeValue
_SpawnShapeValue = _SpawnShapeValue
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RectangleSpawnShapeValue():
    """com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue"""
 
    @staticmethod
    def _wrap(java_value: _RectangleSpawnShapeValue) -> 'RectangleSpawnShapeValue':
        return RectangleSpawnShapeValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RectangleSpawnShapeValue):
        """
        Dynamic initializer for RectangleSpawnShapeValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RectangleSpawnShapeValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RectangleSpawnShapeValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def isEdges(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.isEdges()"""
        return bool._wrap(super(PrimitiveSpawnShapeValue, self).isEdges())

    @override
    @overload
    def spawnAux(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue.spawnAux(com.badlogic.gdx.math.Vector3,float)"""
        super(_RectangleSpawnShapeValue, self).spawnAux(arg0, _float.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue()"""
        val = _RectangleSpawnShapeValue()
        self.__wrapper = val

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_PrimitiveSpawnShapeValue, self).read(arg0, arg1)

    @override
    @overload
    def getSpawnDepth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnDepth()"""
        return 'ScaledNumericValue'._wrap(super(PrimitiveSpawnShapeValue, self).getSpawnDepth())

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
    def spawn(self, arg0: 'Vector3', arg1: float) -> 'math.Vector3':
        """public final com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.spawn(com.badlogic.gdx.math.Vector3,float)"""
        return 'math.Vector3'._wrap(super(_SpawnShapeValue, self).spawn(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def copy(self) -> 'SpawnShapeValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue.copy()"""
        return 'SpawnShapeValue'._wrap(super(RectangleSpawnShapeValue, self).copy())

    @overload
    def __init__(self, arg0: 'RectangleSpawnShapeValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue(com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue)"""
        val = _RectangleSpawnShapeValue(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setActive(boolean)"""
        super(_PrimitiveSpawnShapeValue, self).setActive(_boolean.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.RectangleSpawnShapeValue()"""
        val = _RectangleSpawnShapeValue()
        self.__wrapper = val

    @override
    @overload
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool._wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def setDimensions(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setDimensions(float,float,float)"""
        super(_PrimitiveSpawnShapeValue, self).setDimensions(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(_PrimitiveSpawnShapeValue, self).load(arg0)

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.write(com.badlogic.gdx.utils.Json)"""
        super(_PrimitiveSpawnShapeValue, self).write(arg0)

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_SpawnShapeValue, self).load(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getSpawnWidth(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnWidth()"""
        return 'ScaledNumericValue'._wrap(super(PrimitiveSpawnShapeValue, self).getSpawnWidth())

    @override
    @overload
    def setEdges(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.setEdges(boolean)"""
        super(_PrimitiveSpawnShapeValue, self).setEdges(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getSpawnHeight(self) -> 'ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.values.PrimitiveSpawnShapeValue.getSpawnHeight()"""
        return 'ScaledNumericValue'._wrap(super(PrimitiveSpawnShapeValue, self).getSpawnHeight())

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

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_SpawnShapeValue, self).save(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue as _RangedNumericValue
_RangedNumericValue = _RangedNumericValue
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue as _ParticleValue
_ParticleValue = _ParticleValue
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RangedNumericValue():
    """com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue"""
 
    @staticmethod
    def _wrap(java_value: _RangedNumericValue) -> 'RangedNumericValue':
        return RangedNumericValue(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RangedNumericValue):
        """
        Dynamic initializer for RangedNumericValue.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RangedNumericValue__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RangedNumericValue__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getLowMin(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.getLowMin()"""
        return float._wrap(super(RangedNumericValue, self).getLowMin())

    @override
    @overload
    def load(self, arg0: 'ParticleValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.load(com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue)"""
        super(_ParticleValue, self).load(arg0)

    @overload
    def setLow(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.setLow(float)"""
        super(_RangedNumericValue, self).setLow(_float.valueOf(arg0))

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
    def isActive(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.isActive()"""
        return bool._wrap(super(ParticleValue, self).isActive())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def load(self, arg0: 'RangedNumericValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.load(com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue)"""
        super(_RangedNumericValue, self).load(arg0)

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_RangedNumericValue, self).read(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.write(com.badlogic.gdx.utils.Json)"""
        super(_RangedNumericValue, self).write(arg0)

    @overload
    def setLowMax(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.setLowMax(float)"""
        super(_RangedNumericValue, self).setLowMax(_float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setLow(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.setLow(float,float)"""
        super(_RangedNumericValue, self).setLow(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def setLowMin(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.setLowMin(float)"""
        super(_RangedNumericValue, self).setLowMin(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def newLowValue(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.newLowValue()"""
        return float._wrap(super(RangedNumericValue, self).newLowValue())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setActive(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.values.ParticleValue.setActive(boolean)"""
        super(_ParticleValue, self).setActive(_boolean.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue()"""
        val = _RangedNumericValue()
        self.__wrapper = val

    @overload
    def getLowMax(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue.getLowMax()"""
        return float._wrap(super(RangedNumericValue, self).getLowMax())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue()"""
        val = _RangedNumericValue()
        self.__wrapper = val