from __future__ import annotations
from overload import overload


 
import dev.ultreon.quantum.client.render.meshing.GreedyMesher as _GreedyMesher_LightLevelData
_LightLevelData = _GreedyMesher_LightLevelData.LightLevelData
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
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LightLevelData():
    """dev.ultreon.quantum.client.render.meshing.GreedyMesher.LightLevelData"""
 
    @staticmethod
    def _wrap(java_value: _LightLevelData) -> 'LightLevelData':
        return LightLevelData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LightLevelData):
        """
        Dynamic initializer for LightLevelData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LightLevelData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LightLevelData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def blockBrightness(self) -> float:
        """public float dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData.blockBrightness()"""
        return float._wrap(super(LightLevelData, self).blockBrightness())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData.toString()"""
        return str._wrap(super(LightLevelData, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData.equals(java.lang.Object)"""
        return bool._wrap(super(_LightLevelData, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData.hashCode()"""
        return int._wrap(super(LightLevelData, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def lightLevel(self) -> float:
        """public float dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData.lightLevel()"""
        return float._wrap(super(LightLevelData, self).lightLevel())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData(float,float)"""
        val = _LightLevelData(_float.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val

    @overload
    def sunBrightness(self) -> float:
        """public float dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData.sunBrightness()"""
        return float._wrap(super(LightLevelData, self).sunBrightness())

 
 
 
# CLASS: dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData
import dev.ultreon.quantum.client.render.meshing.GreedyMesher as _GreedyMesher_LightLevelData
_LightLevelData = _GreedyMesher_LightLevelData.LightLevelData
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
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LightLevelData():
    """dev.ultreon.quantum.client.render.meshing.GreedyMesher.LightLevelData"""
 
    @staticmethod
    def _wrap(java_value: _LightLevelData) -> 'LightLevelData':
        return LightLevelData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LightLevelData):
        """
        Dynamic initializer for LightLevelData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LightLevelData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LightLevelData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def blockBrightness(self) -> float:
        """public float dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData.blockBrightness()"""
        return float._wrap(super(LightLevelData, self).blockBrightness())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData.toString()"""
        return str._wrap(super(LightLevelData, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData.equals(java.lang.Object)"""
        return bool._wrap(super(_LightLevelData, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData.hashCode()"""
        return int._wrap(super(LightLevelData, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def lightLevel(self) -> float:
        """public float dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData.lightLevel()"""
        return float._wrap(super(LightLevelData, self).lightLevel())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData(float,float)"""
        val = _LightLevelData(_float.valueOf(arg0), _float.valueOf(arg1))
        self.__wrapper = val

    @overload
    def sunBrightness(self) -> float:
        """public float dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData.sunBrightness()"""
        return float._wrap(super(LightLevelData, self).sunBrightness())

 
 
 
# CLASS: dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData 
 
 
# CLASS: dev.ultreon.quantum.client.render.meshing.GreedyMesher$MergeCondition
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.render.meshing.GreedyMesher as _GreedyMesher_MergeCondition
_MergeCondition = _GreedyMesher_MergeCondition.MergeCondition
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

from abc import abstractmethod, ABC
 
class MergeCondition():
    """dev.ultreon.quantum.client.render.meshing.GreedyMesher.MergeCondition"""
 
    @staticmethod
    def _wrap(java_value: _MergeCondition) -> 'MergeCondition':
        return MergeCondition(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MergeCondition):
        """
        Dynamic initializer for MergeCondition.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MergeCondition__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MergeCondition__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def shouldMerge(self, arg0: 'BlockProperties', arg1: float, arg2: 'PerCornerLightData', arg3: 'BlockProperties', arg4: float, arg5: 'PerCornerLightData'):
        """public abstract boolean dev.ultreon.quantum.client.render.meshing.GreedyMesher$MergeCondition.shouldMerge(dev.ultreon.quantum.block.state.BlockProperties,float,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,dev.ultreon.quantum.block.state.BlockProperties,float,dev.ultreon.quantum.client.render.meshing.PerCornerLightData)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.render.meshing.Mesher$UseCondition
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import dev.ultreon.quantum.client.render.meshing.Mesher as _Mesher_UseCondition
_UseCondition = _Mesher_UseCondition.UseCondition
from abc import abstractmethod, ABC
 
class UseCondition():
    """dev.ultreon.quantum.client.render.meshing.Mesher.UseCondition"""
 
    @staticmethod
    def _wrap(java_value: _UseCondition) -> 'UseCondition':
        return UseCondition(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _UseCondition):
        """
        Dynamic initializer for UseCondition.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_UseCondition__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_UseCondition__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def shouldUse(self, arg0: 'Block'):
        """public abstract boolean dev.ultreon.quantum.client.render.meshing.Mesher$UseCondition.shouldUse(dev.ultreon.quantum.block.Block)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.render.meshing.Mesher
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.render.meshing.Mesher as _Mesher
_Mesher = _Mesher
from abc import abstractmethod, ABC
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

 
class Mesher():
    """dev.ultreon.quantum.client.render.meshing.Mesher"""
 
    @staticmethod
    def _wrap(java_value: _Mesher) -> 'Mesher':
        return Mesher(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Mesher):
        """
        Dynamic initializer for Mesher.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Mesher__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Mesher__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def meshVoxels(self, arg0: 'ModelBuilder', arg1: 'MeshPartBuilder', arg2: 'UseCondition'):
        """public abstract void dev.ultreon.quantum.client.render.meshing.Mesher.meshVoxels(com.badlogic.gdx.graphics.g3d.utils.ModelBuilder,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,dev.ultreon.quantum.client.render.meshing.Mesher$UseCondition)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.render.meshing.GreedyMesher as _GreedyMesher_LightLevelData
_LightLevelData = _GreedyMesher_LightLevelData.LightLevelData
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo as _AdvancedVertexInfo
_AdvancedVertexInfo = _AdvancedVertexInfo
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
import com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder as _MeshPartBuilder_VertexInfo
_VertexInfo = _MeshPartBuilder_VertexInfo.VertexInfo
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AdvancedVertexInfo():
    """dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo"""
 
    @staticmethod
    def _wrap(java_value: _AdvancedVertexInfo) -> 'AdvancedVertexInfo':
        return AdvancedVertexInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AdvancedVertexInfo):
        """
        Dynamic initializer for AdvancedVertexInfo.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AdvancedVertexInfo__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AdvancedVertexInfo__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getLLD(self) -> 'LightLevelData':
        """public dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.getLLD()"""
        return 'LightLevelData'._wrap(super(AdvancedVertexInfo, self).getLLD())

    @overload
    def set(self, arg0: 'Vector3', arg1: 'Vector3', arg2: 'Color', arg3: 'Vector2') -> 'AdvancedVertexInfo':
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.set(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.math.Vector2)"""
        return 'AdvancedVertexInfo'._wrap(super(_AdvancedVertexInfo, self).set(arg0, arg1, arg2, arg3))

    @overload
    def lerp(self, arg0: 'VertexInfo', arg1: float) -> 'AdvancedVertexInfo':
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.lerp(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,float)"""
        return 'AdvancedVertexInfo'._wrap(super(_AdvancedVertexInfo, self).lerp(arg0, _float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setUV(self, arg0: float, arg1: float) -> 'AdvancedVertexInfo':
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.setUV(float,float)"""
        return 'AdvancedVertexInfo'._wrap(super(_AdvancedVertexInfo, self).setUV(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def set(self, arg0: 'VertexInfo') -> 'AdvancedVertexInfo':
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.set(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo)"""
        return 'AdvancedVertexInfo'._wrap(super(_AdvancedVertexInfo, self).set(arg0))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo()"""
        val = _AdvancedVertexInfo()
        self.__wrapper = val

    @overload
    def setPos(self, arg0: float, arg1: float, arg2: float) -> 'AdvancedVertexInfo':
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.setPos(float,float,float)"""
        return 'AdvancedVertexInfo'._wrap(super(_AdvancedVertexInfo, self).setPos(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def setCol(self, arg0: 'Color') -> 'AdvancedVertexInfo':
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.setCol(com.badlogic.gdx.graphics.Color)"""
        return 'AdvancedVertexInfo'._wrap(super(_AdvancedVertexInfo, self).setCol(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @property
    def lightLevelData(self, value: 'LightLevelData'):
        super(_AdvancedVertexInfo).lightLevelData(value)

    @overload
    def setPos(self, arg0: 'Vector3') -> 'AdvancedVertexInfo':
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.setPos(com.badlogic.gdx.math.Vector3)"""
        return 'AdvancedVertexInfo'._wrap(super(_AdvancedVertexInfo, self).setPos(arg0))

    @override
    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo.reset()"""
        super(utils.MeshPartBuilder$VertexInfo, self).reset()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setLLD(self, arg0: 'LightLevelData') -> 'AdvancedVertexInfo':
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.setLLD(dev.ultreon.quantum.client.render.meshing.GreedyMesher$LightLevelData)"""
        return 'AdvancedVertexInfo'._wrap(super(_AdvancedVertexInfo, self).setLLD(arg0))

    @overload
    def setUV(self, arg0: 'Vector2') -> 'AdvancedVertexInfo':
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.setUV(com.badlogic.gdx.math.Vector2)"""
        return 'AdvancedVertexInfo'._wrap(super(_AdvancedVertexInfo, self).setUV(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setCol(self, arg0: float, arg1: float, arg2: float, arg3: float) -> 'AdvancedVertexInfo':
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.setCol(float,float,float,float)"""
        return 'AdvancedVertexInfo'._wrap(super(_AdvancedVertexInfo, self).setCol(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @overload
    def hasLLD(self) -> bool:
        """public boolean dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.hasLLD()"""
        return bool._wrap(super(AdvancedVertexInfo, self).hasLLD())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo()"""
        val = _AdvancedVertexInfo()
        self.__wrapper = val

    @overload
    def setNor(self, arg0: 'Vector3') -> 'AdvancedVertexInfo':
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.setNor(com.badlogic.gdx.math.Vector3)"""
        return 'AdvancedVertexInfo'._wrap(super(_AdvancedVertexInfo, self).setNor(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setNor(self, arg0: float, arg1: float, arg2: float) -> 'AdvancedVertexInfo':
        """public dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo dev.ultreon.quantum.client.render.meshing.AdvancedVertexInfo.setNor(float,float,float)"""
        return 'AdvancedVertexInfo'._wrap(super(_AdvancedVertexInfo, self).setNor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @property
    def lightLevelData(self) -> LightLevelData:
        return LightLevelData._wrap(super(_AdvancedVertexInfo).lightLevelData())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.render.meshing.GreedyMesher$OccludeCondition
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import block
except ImportError:
    block = _import_once("pyquantum.block")

import dev.ultreon.quantum.client.render.meshing.GreedyMesher as _GreedyMesher_OccludeCondition
_OccludeCondition = _GreedyMesher_OccludeCondition.OccludeCondition
from abc import abstractmethod, ABC
 
class OccludeCondition():
    """dev.ultreon.quantum.client.render.meshing.GreedyMesher.OccludeCondition"""
 
    @staticmethod
    def _wrap(java_value: _OccludeCondition) -> 'OccludeCondition':
        return OccludeCondition(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OccludeCondition):
        """
        Dynamic initializer for OccludeCondition.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OccludeCondition__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OccludeCondition__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def shouldOcclude(self, arg0: 'Block', arg1: 'Block'):
        """public abstract boolean dev.ultreon.quantum.client.render.meshing.GreedyMesher$OccludeCondition.shouldOcclude(dev.ultreon.quantum.block.Block,dev.ultreon.quantum.block.Block)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.client.render.meshing.GreedyMesher$Face
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import world
except ImportError:
    world = _import_once("pyquantum.world")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.render.meshing.GreedyMesher as _GreedyMesher_Face
_Face = _GreedyMesher_Face.Face
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pyquantum.block import state
except ImportError:
    state = _import_once("pyquantum.block.state")

from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Face():
    """dev.ultreon.quantum.client.render.meshing.GreedyMesher.Face"""
 
    @staticmethod
    def _wrap(java_value: _Face) -> 'Face':
        return Face(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Face):
        """
        Dynamic initializer for Face.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Face__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Face__wrapper":
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

    @overload
    def render(self, arg0: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.meshing.GreedyMesher$Face.render(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(_Face, self).render(arg0)

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
    def __init__(self, arg0: 'CubicDirection', arg1: 'BlockProperties', arg2: float, arg3: 'PerCornerLightData', arg4: int, arg5: int, arg6: int, arg7: int, arg8: int, arg9: float):
        """public dev.ultreon.quantum.client.render.meshing.GreedyMesher$Face(dev.ultreon.quantum.world.CubicDirection,dev.ultreon.quantum.block.state.BlockProperties,float,dev.ultreon.quantum.client.render.meshing.PerCornerLightData,int,int,int,int,int,float)"""
        val = _Face(arg0, arg1, _float.valueOf(arg2), arg3, _int.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _int.valueOf(arg7), _int.valueOf(arg8), _float.valueOf(arg9))
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.client.render.meshing.GreedyMesher
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.render.meshing.GreedyMesher as _GreedyMesher
_GreedyMesher = _GreedyMesher
import java.util.List as _List
_List = _List
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pyquantum.client import world
except ImportError:
    world = _import_once("pyquantum.client.world")

from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GreedyMesher():
    """dev.ultreon.quantum.client.render.meshing.GreedyMesher"""
 
    @staticmethod
    def _wrap(java_value: _GreedyMesher) -> 'GreedyMesher':
        return GreedyMesher(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GreedyMesher):
        """
        Dynamic initializer for GreedyMesher.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GreedyMesher__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GreedyMesher__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def meshVoxels(self, arg0: 'ModelBuilder', arg1: 'MeshPartBuilder', arg2: 'UseCondition'):
        """public void dev.ultreon.quantum.client.render.meshing.GreedyMesher.meshVoxels(com.badlogic.gdx.graphics.g3d.utils.ModelBuilder,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,dev.ultreon.quantum.client.render.meshing.Mesher$UseCondition)"""
        super(_GreedyMesher, self).meshVoxels(arg0, arg1, arg2)

    @overload
    def meshFaces(self, arg0: 'List', arg1: 'MeshPartBuilder'):
        """public void dev.ultreon.quantum.client.render.meshing.GreedyMesher.meshFaces(java.util.List<dev.ultreon.quantum.client.render.meshing.GreedyMesher$Face>,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder)"""
        super(_GreedyMesher, self).meshFaces(arg0, arg1)

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
    def getFaces(self, arg0: 'ModelBuilder', arg1: 'UseCondition', arg2: 'OccludeCondition', arg3: 'MergeCondition') -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.render.meshing.GreedyMesher$Face> dev.ultreon.quantum.client.render.meshing.GreedyMesher.getFaces(com.badlogic.gdx.graphics.g3d.utils.ModelBuilder,dev.ultreon.quantum.client.render.meshing.Mesher$UseCondition,dev.ultreon.quantum.client.render.meshing.GreedyMesher$OccludeCondition,dev.ultreon.quantum.client.render.meshing.GreedyMesher$MergeCondition)"""
        return 'List'._wrap(super(_GreedyMesher, self).getFaces(arg0, arg1, arg2, arg3))

    @overload
    def __init__(self, arg0: 'ClientChunk', arg1: bool):
        """public dev.ultreon.quantum.client.render.meshing.GreedyMesher(dev.ultreon.quantum.client.world.ClientChunk,boolean)"""
        val = _GreedyMesher(arg0, _boolean.valueOf(arg1))
        self.__wrapper = val

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
    def getFaces(self, arg0: 'ModelBuilder', arg1: 'UseCondition') -> 'List':
        """public java.util.List<dev.ultreon.quantum.client.render.meshing.GreedyMesher$Face> dev.ultreon.quantum.client.render.meshing.GreedyMesher.getFaces(com.badlogic.gdx.graphics.g3d.utils.ModelBuilder,dev.ultreon.quantum.client.render.meshing.Mesher$UseCondition)"""
        return 'List'._wrap(super(_GreedyMesher, self).getFaces(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.render.meshing.PerCornerLightData
import dev.ultreon.quantum.client.render.meshing.PerCornerLightData as _PerCornerLightData
_PerCornerLightData = _PerCornerLightData
from builtins import str
from pyquantum_helper import override
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
 
class PerCornerLightData():
    """dev.ultreon.quantum.client.render.meshing.PerCornerLightData"""
 
    @staticmethod
    def _wrap(java_value: _PerCornerLightData) -> 'PerCornerLightData':
        return PerCornerLightData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PerCornerLightData):
        """
        Dynamic initializer for PerCornerLightData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PerCornerLightData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PerCornerLightData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.render.meshing.PerCornerLightData()"""
        val = _PerCornerLightData()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.client.render.meshing.PerCornerLightData.equals(java.lang.Object)"""
        return bool._wrap(super(_PerCornerLightData, self).equals(arg0))

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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.render.meshing.PerCornerLightData()"""
        val = _PerCornerLightData()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())