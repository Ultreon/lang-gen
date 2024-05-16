from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.render.meshing.GreedyMesher as __GreedyMesher_LightLevelData
__LightLevelData = __GreedyMesher_LightLevelData.LightLevelData
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LightLevelData():
    """dev.ultreon.quantum.client.render.meshing.GreedyMesher.LightLevelData"""
 
    @staticmethod
    def __wrap(java_value: __LightLevelData) -> 'LightLevelData':
        return LightLevelData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LightLevelData):
        """
        Dynamic initializer for LightLevelData.
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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData.equals(java.lang.Object)"""
        return bool.__wrap(super(__LightLevelData, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

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
    def lightLevel(self) -> float:
        """public float dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData.lightLevel()"""
        return float.__wrap(super(LightLevelData, self).lightLevel())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def blockBrightness(self) -> float:
        """public float dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData.blockBrightness()"""
        return float.__wrap(super(LightLevelData, self).blockBrightness())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData.toString()"""
        return str.__wrap(super(LightLevelData, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData.hashCode()"""
        return int.__wrap(super(LightLevelData, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData(float,float)"""
        val = __LightLevelData(__float.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def sunBrightness(self) -> float:
        """public float dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData.sunBrightness()"""
        return float.__wrap(super(LightLevelData, self).sunBrightness())

 
 
 
# CLASS: dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.render.meshing.GreedyMesher as __GreedyMesher_LightLevelData
__LightLevelData = __GreedyMesher_LightLevelData.LightLevelData
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class LightLevelData():
    """dev.ultreon.quantum.client.render.meshing.GreedyMesher.LightLevelData"""
 
    @staticmethod
    def __wrap(java_value: __LightLevelData) -> 'LightLevelData':
        return LightLevelData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LightLevelData):
        """
        Dynamic initializer for LightLevelData.
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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData.equals(java.lang.Object)"""
        return bool.__wrap(super(__LightLevelData, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

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
    def lightLevel(self) -> float:
        """public float dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData.lightLevel()"""
        return float.__wrap(super(LightLevelData, self).lightLevel())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def blockBrightness(self) -> float:
        """public float dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData.blockBrightness()"""
        return float.__wrap(super(LightLevelData, self).blockBrightness())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData.toString()"""
        return str.__wrap(super(LightLevelData, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData.hashCode()"""
        return int.__wrap(super(LightLevelData, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData(float,float)"""
        val = __LightLevelData(__float.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def sunBrightness(self) -> float:
        """public float dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData.sunBrightness()"""
        return float.__wrap(super(LightLevelData, self).sunBrightness())

 
 
 
# CLASS: dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData 
 
 
# CLASS: dev.ultreon.quantum.client.render.meshing.GreedyMesher$MergeCondition
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import dev.ultreon.quantum.client.render.meshing.GreedyMesher as __GreedyMesher_MergeCondition
__MergeCondition = __GreedyMesher_MergeCondition.MergeCondition
from abc import abstractmethod, ABC
 
class MergeCondition(ABC):
    """dev.ultreon.quantum.client.render.meshing.GreedyMesher.MergeCondition"""
 
    @staticmethod
    def __wrap(java_value: __MergeCondition) -> 'MergeCondition':
        return MergeCondition(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MergeCondition):
        """
        Dynamic initializer for MergeCondition.
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
    def shouldMerge(self, arg0: 'BlockProperties', arg1: float, arg2: 'PerCornerLightData', arg3: 'BlockProperties', arg4: float, arg5: 'PerCornerLightData'):
        """public abstract boolean dev.ultreon.quantum.client.render.meshing.GreedyMesher$MergeCondition.shouldMerge(dev.ultreon.quantum.block.state.BlockProperties,float,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,dev.ultreon.quantum.block.state.BlockProperties,float,dev.ultreon.quantum.client.render.meshing.PerCornerLightData)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.render.meshing.Mesher$UseCondition
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

import dev.ultreon.quantum.client.render.meshing.Mesher as __Mesher_UseCondition
__UseCondition = __Mesher_UseCondition.UseCondition
from abc import abstractmethod, ABC
 
class UseCondition(ABC):
    """dev.ultreon.quantum.client.render.meshing.Mesher.UseCondition"""
 
    @staticmethod
    def __wrap(java_value: __UseCondition) -> 'UseCondition':
        return UseCondition(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __UseCondition):
        """
        Dynamic initializer for UseCondition.
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
    def shouldUse(self, arg0: 'Block'):
        """public abstract boolean dev.ultreon.quantum.client.render.meshing.Mesher$UseCondition.shouldUse(dev.ultreon.quantum.block.Block)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.render.meshing.Mesher
from pyquantum_helper import import_once as __import_once__
from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.render.meshing.Mesher as __Mesher
__Mesher = __Mesher
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

 
class Mesher(ABC):
    """dev.ultreon.quantum.client.render.meshing.Mesher"""
 
    @staticmethod
    def __wrap(java_value: __Mesher) -> 'Mesher':
        return Mesher(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Mesher):
        """
        Dynamic initializer for Mesher.
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
    def meshVoxels(self, arg0: 'ModelBuilder', arg1: 'MeshPartBuilder', arg2: 'UseCondition'):
        """public abstract void dev.ultreon.quantum.client.render.meshing.Mesher.meshVoxels(com.badlogic.gdx.graphics.g3d.utils.ModelBuilder,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,dev.ultreon.quantum.client.render.meshing.Mesher$UseCondition)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo as __AdvancedVertexInfo
__AdvancedVertexInfo = __AdvancedVertexInfo
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder as __MeshPartBuilder_VertexInfo
__VertexInfo = __MeshPartBuilder_VertexInfo.VertexInfo
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.client.render.meshing.GreedyMesher as __GreedyMesher_LightLevelData
__LightLevelData = __GreedyMesher_LightLevelData.LightLevelData
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
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class AdvancedVertexInfo():
    """dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo"""
 
    @staticmethod
    def __wrap(java_value: __AdvancedVertexInfo) -> 'AdvancedVertexInfo':
        return AdvancedVertexInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AdvancedVertexInfo):
        """
        Dynamic initializer for AdvancedVertexInfo.
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
    def setPos(self, arg0: 'Vector3') -> 'AdvancedVertexInfo':
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.setPos(com.badlogic.gdx.math.Vector3)"""
        return 'AdvancedVertexInfo'.__wrap(super(__AdvancedVertexInfo, self).setPos(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def hasLLD(self) -> bool:
        """public boolean dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.hasLLD()"""
        return bool.__wrap(super(AdvancedVertexInfo, self).hasLLD())

    @property
    def lightLevelData(self, value: 'LightLevelData'):
        super(__AdvancedVertexInfo).lightLevelData(value)

    @overload
    def setLLD(self, arg0: 'LightLevelData') -> 'AdvancedVertexInfo':
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.setLLD(dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData)"""
        return 'AdvancedVertexInfo'.__wrap(super(__AdvancedVertexInfo, self).setLLD(arg0))

    @overload
    def set(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Color', arg3: 'Vector2') -> 'AdvancedVertexInfo':
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.set(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector2)"""
        return 'AdvancedVertexInfo'.__wrap(super(__AdvancedVertexInfo, self).set(arg0, arg1, arg2, arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def lerp(self, arg0: 'VertexInfo', arg1: float) -> 'AdvancedVertexInfo':
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.lerp(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,float)"""
        return 'AdvancedVertexInfo'.__wrap(super(__AdvancedVertexInfo, self).lerp(arg0, __float.valueOf(arg1)))

    @overload
    def setPos(self, arg0: float, arg1: float, arg2: float) -> 'AdvancedVertexInfo':
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.setPos(float,float,float)"""
        return 'AdvancedVertexInfo'.__wrap(super(__AdvancedVertexInfo, self).setPos(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @property
    def lightLevelData(self) -> LightLevelData:
        return LightLevelData.__wrap(super(__AdvancedVertexInfo).lightLevelData())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def set(self, arg0: 'VertexInfo') -> 'AdvancedVertexInfo':
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.set(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo)"""
        return 'AdvancedVertexInfo'.__wrap(super(__AdvancedVertexInfo, self).set(arg0))

    @overload
    def setUV(self, arg0: 'Vector2') -> 'AdvancedVertexInfo':
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.setUV(com.badlogic.gdx.math.Vector2)"""
        return 'AdvancedVertexInfo'.__wrap(super(__AdvancedVertexInfo, self).setUV(arg0))

    @overload
    def setNor(self, arg0: 'Vector3') -> 'AdvancedVertexInfo':
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.setNor(com.badlogic.gdx.math.Vector3)"""
        return 'AdvancedVertexInfo'.__wrap(super(__AdvancedVertexInfo, self).setNor(arg0))

    @overload
    def setCol(self, arg0: 'Color') -> 'AdvancedVertexInfo':
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.setCol(com.badlogic.gdx.graphics.Color)"""
        return 'AdvancedVertexInfo'.__wrap(super(__AdvancedVertexInfo, self).setCol(arg0))

    @overload
    def getLLD(self) -> 'LightLevelData':
        """public dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.getLLD()"""
        return 'LightLevelData'.__wrap(super(AdvancedVertexInfo, self).getLLD())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo()"""
        val = __AdvancedVertexInfo()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.reset()"""
        super(utils.MeshPartBuilder$VertexInfo, self).reset()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo()"""
        val = __AdvancedVertexInfo()
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

    @overload
    def setNor(self, arg0: float, arg1: float, arg2: float) -> 'AdvancedVertexInfo':
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.setNor(float,float,float)"""
        return 'AdvancedVertexInfo'.__wrap(super(__AdvancedVertexInfo, self).setNor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setUV(self, arg0: float, arg1: float) -> 'AdvancedVertexInfo':
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.setUV(float,float)"""
        return 'AdvancedVertexInfo'.__wrap(super(__AdvancedVertexInfo, self).setUV(__float.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def setCol(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'AdvancedVertexInfo':
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.setCol(float,float,float,float)"""
        return 'AdvancedVertexInfo'.__wrap(super(__AdvancedVertexInfo, self).setCol(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))) 
 
 
# CLASS: dev.ultreon.quantum.client.render.meshing.GreedyMesher$OccludeCondition
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import block
except ImportError:
    block = __import_once__("pyquantum.block")

from abc import abstractmethod, ABC
import dev.ultreon.quantum.client.render.meshing.GreedyMesher as __GreedyMesher_OccludeCondition
__OccludeCondition = __GreedyMesher_OccludeCondition.OccludeCondition
 
class OccludeCondition(ABC):
    """dev.ultreon.quantum.client.render.meshing.GreedyMesher.OccludeCondition"""
 
    @staticmethod
    def __wrap(java_value: __OccludeCondition) -> 'OccludeCondition':
        return OccludeCondition(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __OccludeCondition):
        """
        Dynamic initializer for OccludeCondition.
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
    def shouldOcclude(self, arg0: 'Block', arg1: 'Block'):
        """public abstract boolean dev.ultreon.quantum.client.render.meshing.GreedyMesher$OccludeCondition.shouldOcclude(dev.ultreon.quantum.block.Block,dev.ultreon.quantum.block.Block)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.render.meshing.GreedyMesher$Face
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import world
except ImportError:
    world = __import_once__("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import dev.ultreon.quantum.client.render.meshing.GreedyMesher as __GreedyMesher_Face
__Face = __GreedyMesher_Face.Face
import java.lang.String as __String
__String = __String
try:
    from pyquantum.block import state
except ImportError:
    state = __import_once__("pyquantum.block.state")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class Face():
    """dev.ultreon.quantum.client.render.meshing.GreedyMesher.Face"""
 
    @staticmethod
    def __wrap(java_value: __Face) -> 'Face':
        return Face(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Face):
        """
        Dynamic initializer for Face.
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

    @overload
    def __init__(self, arg0: 'CubicDirection', arg1: 'BlockProperties', arg2: float, arg3: 'PerCornerLightData', arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: float):
        """public dev.ultreon.quantum.client.render.meshing.GreedyMesher$Face(dev.ultreon.quantum.world.CubicDirection,dev.ultreon.quantum.block.state.BlockProperties,float,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,int,int,int,int,int,float)"""
        val = __Face(arg0, arg1, __float.valueOf(arg2), arg3, __int.valueOf(arg4), __int.valueOf(arg5), __int.valueOf(arg6), __int.valueOf(arg7), __int.valueOf(arg8), __float.valueOf(arg9))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def render(self, arg0: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.meshing.GreedyMesher$Face.render(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(__Face, self).render(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.client.render.meshing.GreedyMesher
from pyquantum_helper import import_once as __import_once__
from builtins import str
import dev.ultreon.quantum.client.render.meshing.GreedyMesher as __GreedyMesher
__GreedyMesher = __GreedyMesher
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum.client import world
except ImportError:
    world = __import_once__("pyquantum.client.world")

import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

import java.util.List as List
from builtins import int
 
class GreedyMesher():
    """dev.ultreon.quantum.client.render.meshing.GreedyMesher"""
 
    @staticmethod
    def __wrap(java_value: __GreedyMesher) -> 'GreedyMesher':
        return GreedyMesher(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GreedyMesher):
        """
        Dynamic initializer for GreedyMesher.
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
    def getFaces(self, arg0: 'ModelBuilder', arg1: 'UseCondition') -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.render.meshing.GreedyMesher$Face> dev.ultreon.quantum.client.render.meshing.GreedyMesher.getFaces(com.badlogic.gdx.graphics.g3d.utils.ModelBuilder,dev.ultreon.quantum.client.render.meshing.Mesher$UseCondition)"""
        return 'List'.__wrap(super(__GreedyMesher, self).getFaces(arg0, arg1))

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

    @override
    @overload
    def meshVoxels(self, arg0: 'ModelBuilder', arg1: 'MeshPartBuilder', arg2: 'UseCondition'):
        """public void dev.ultreon.quantum.client.render.meshing.GreedyMesher.meshVoxels(com.badlogic.gdx.graphics.g3d.utils.ModelBuilder,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,dev.ultreon.quantum.client.render.meshing.Mesher$UseCondition)"""
        super(__GreedyMesher, self).meshVoxels(arg0, arg1, arg2)

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
    def getFaces(self, arg0: 'ModelBuilder', arg1: 'UseCondition', arg2: 'OccludeCondition', arg3: 'MergeCondition') -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.render.meshing.GreedyMesher$Face> dev.ultreon.quantum.client.render.meshing.GreedyMesher.getFaces(com.badlogic.gdx.graphics.g3d.utils.ModelBuilder,dev.ultreon.quantum.client.render.meshing.Mesher$UseCondition,dev.ultreon.quantum.client.render.meshing.GreedyMesher$OccludeCondition,dev.ultreon.quantum.client.render.meshing.GreedyMesher$MergeCondition)"""
        return 'List'.__wrap(super(__GreedyMesher, self).getFaces(arg0, arg1, arg2, arg3))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def meshFaces(self, arg0: 'List', arg1: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.meshing.GreedyMesher.meshFaces(java.util.List<dev.ultreon.quantum.client.render.meshing.GreedyMesher$Face>,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(__GreedyMesher, self).meshFaces(arg0, arg1)

    @overload
    def __init__(self, arg0: 'ClientChunk', arg1: bool):
        """public dev.ultreon.quantum.client.render.meshing.GreedyMesher(dev.ultreon.quantum.client.world.ClientChunk,boolean)"""
        val = __GreedyMesher(arg0, __boolean.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.render.meshing.PerCornerLightData
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import dev.ultreon.quantum.client.render.meshing.PerCornerLightData as __PerCornerLightData
__PerCornerLightData = __PerCornerLightData
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PerCornerLightData():
    """dev.ultreon.quantum.client.render.meshing.PerCornerLightData"""
 
    @staticmethod
    def __wrap(java_value: __PerCornerLightData) -> 'PerCornerLightData':
        return PerCornerLightData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PerCornerLightData):
        """
        Dynamic initializer for PerCornerLightData.
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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.render.meshing.PerCornerLightData.equals(java.lang.Object)"""
        return bool.__wrap(super(__PerCornerLightData, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.meshing.PerCornerLightData()"""
        val = __PerCornerLightData()
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
    def __init__(self):
        """public dev.ultreon.quantum.client.render.meshing.PerCornerLightData()"""
        val = __PerCornerLightData()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))