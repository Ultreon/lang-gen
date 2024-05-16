from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

try:
    from pygdx.graphics.g3d.particles import renderers
except ImportError:
    renderers = _import_once("pygdx.graphics.g3d.particles.renderers")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer as _Influencer
_Influencer = _Influencer
import java.lang.String as _String
_String = _String
try:
    from pygdx.graphics.g3d.particles import influencers
except ImportError:
    influencers = _import_once("pygdx.graphics.g3d.particles.influencers")

import java.lang.Float as _float
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import java.lang.String as _string
import com.badlogic.gdx.graphics.g3d.particles.ParticleController as _ParticleController
_ParticleController = _ParticleController
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.math.collision.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
from builtins import bool
try:
    from pygdx.graphics.g3d.particles import emitters
except ImportError:
    emitters = _import_once("pygdx.graphics.g3d.particles.emitters")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParticleController():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleController"""
 
    @staticmethod
    def _wrap(java_value: _ParticleController) -> 'ParticleController':
        return ParticleController(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleController):
        """
        Dynamic initializer for ParticleController.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleController__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleController__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.reset()"""
        super(ParticleController, self).reset()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.write(com.badlogic.gdx.utils.Json)"""
        super(_ParticleController, self).write(arg0)

    @overload
    def scale(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.scale(com.badlogic.gdx.math.Vector3)"""
        super(_ParticleController, self).scale(arg0)

    @overload
    def __init__(self, arg0: str, arg1: 'Emitter', arg2: 'ParticleControllerRenderer', *arg3: 'influencers.Influencer'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleController(java.lang.String,com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter,com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer<?, ?>,com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer...)"""
        val = _ParticleController(arg0, arg1, arg2, arg3)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_ParticleController, self).load(arg0, arg1)

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_ParticleController, self).save(arg0, arg1)

    @overload
    def getBoundingBox(self) -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g3d.particles.ParticleController.getBoundingBox()"""
        return 'collision.BoundingBox'._wrap(super(ParticleController, self).getBoundingBox())

    @overload
    def draw(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.draw()"""
        super(ParticleController, self).draw()

    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.init()"""
        super(ParticleController, self).init()

    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.ParticleController.isComplete()"""
        return bool._wrap(super(ParticleController, self).isComplete())

    @overload
    def removeInfluencer(self, arg0: 'Class'):
        """public <K extends com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer> void com.badlogic.gdx.graphics.g3d.particles.ParticleController.removeInfluencer(java.lang.Class<K>)"""
        super(_ParticleController, self).removeInfluencer(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setTransform(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.setTransform(float,float,float,float,float,float,float,float)"""
        super(_ParticleController, self).setTransform(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleController()"""
        val = _ParticleController()
        self.__wrapper = val

    @overload
    def findInfluencer(self, arg0: 'Class') -> 'influencers.Influencer':
        """public <K extends com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer> K com.badlogic.gdx.graphics.g3d.particles.ParticleController.findInfluencer(java.lang.Class<K>)"""
        return 'influencers.Influencer'._wrap(super(_ParticleController, self).findInfluencer(arg0))

    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.update()"""
        super(ParticleController, self).update()

    @overload
    def setTransform(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.setTransform(com.badlogic.gdx.math.Matrix4)"""
        super(_ParticleController, self).setTransform(arg0)

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_ParticleController, self).read(arg0, arg1)

    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.dispose()"""
        super(ParticleController, self).dispose()

    @overload
    def rotate(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.rotate(com.badlogic.gdx.math.Vector3,float)"""
        super(_ParticleController, self).rotate(arg0, _float.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.start()"""
        super(ParticleController, self).start()

    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.activateParticles(int,int)"""
        super(_ParticleController, self).activateParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setTranslation(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.setTranslation(com.badlogic.gdx.math.Vector3)"""
        super(_ParticleController, self).setTranslation(arg0)

    @overload
    def mul(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.mul(com.badlogic.gdx.math.Matrix4)"""
        super(_ParticleController, self).mul(arg0)

    @overload
    def translate(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.translate(com.badlogic.gdx.math.Vector3)"""
        super(_ParticleController, self).translate(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.end()"""
        super(ParticleController, self).end()

    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.killParticles(int,int)"""
        super(_ParticleController, self).killParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def scale(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.scale(float,float,float)"""
        super(_ParticleController, self).scale(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def copy(self) -> 'ParticleController':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleController com.badlogic.gdx.graphics.g3d.particles.ParticleController.copy()"""
        return 'ParticleController'._wrap(super(ParticleController, self).copy())

    @overload
    def replaceInfluencer(self, arg0: 'Class', arg1: 'Influencer') -> bool:
        """public <K extends com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer> boolean com.badlogic.gdx.graphics.g3d.particles.ParticleController.replaceInfluencer(java.lang.Class<K>,K)"""
        return bool._wrap(super(_ParticleController, self).replaceInfluencer(arg0, arg1))

    @overload
    def update(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.update(float)"""
        super(_ParticleController, self).update(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def rotate(self, arg0: 'Quaternion'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.rotate(com.badlogic.gdx.math.Quaternion)"""
        super(_ParticleController, self).rotate(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getTransform(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.getTransform(com.badlogic.gdx.math.Matrix4)"""
        super(_ParticleController, self).getTransform(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleController()"""
        val = _ParticleController()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleController
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

try:
    from pygdx.graphics.g3d.particles import renderers
except ImportError:
    renderers = _import_once("pygdx.graphics.g3d.particles.renderers")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer as _Influencer
_Influencer = _Influencer
import java.lang.String as _String
_String = _String
try:
    from pygdx.graphics.g3d.particles import influencers
except ImportError:
    influencers = _import_once("pygdx.graphics.g3d.particles.influencers")

import java.lang.Float as _float
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import java.lang.String as _string
import com.badlogic.gdx.graphics.g3d.particles.ParticleController as _ParticleController
_ParticleController = _ParticleController
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.math.collision.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
from builtins import bool
try:
    from pygdx.graphics.g3d.particles import emitters
except ImportError:
    emitters = _import_once("pygdx.graphics.g3d.particles.emitters")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParticleController():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleController"""
 
    @staticmethod
    def _wrap(java_value: _ParticleController) -> 'ParticleController':
        return ParticleController(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleController):
        """
        Dynamic initializer for ParticleController.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleController__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleController__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.reset()"""
        super(ParticleController, self).reset()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.write(com.badlogic.gdx.utils.Json)"""
        super(_ParticleController, self).write(arg0)

    @overload
    def scale(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.scale(com.badlogic.gdx.math.Vector3)"""
        super(_ParticleController, self).scale(arg0)

    @overload
    def __init__(self, arg0: str, arg1: 'Emitter', arg2: 'ParticleControllerRenderer', *arg3: 'influencers.Influencer'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleController(java.lang.String,com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter,com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer<?, ?>,com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer...)"""
        val = _ParticleController(arg0, arg1, arg2, arg3)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_ParticleController, self).load(arg0, arg1)

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_ParticleController, self).save(arg0, arg1)

    @overload
    def getBoundingBox(self) -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g3d.particles.ParticleController.getBoundingBox()"""
        return 'collision.BoundingBox'._wrap(super(ParticleController, self).getBoundingBox())

    @overload
    def draw(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.draw()"""
        super(ParticleController, self).draw()

    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.init()"""
        super(ParticleController, self).init()

    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.ParticleController.isComplete()"""
        return bool._wrap(super(ParticleController, self).isComplete())

    @overload
    def removeInfluencer(self, arg0: 'Class'):
        """public <K extends com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer> void com.badlogic.gdx.graphics.g3d.particles.ParticleController.removeInfluencer(java.lang.Class<K>)"""
        super(_ParticleController, self).removeInfluencer(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setTransform(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.setTransform(float,float,float,float,float,float,float,float)"""
        super(_ParticleController, self).setTransform(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleController()"""
        val = _ParticleController()
        self.__wrapper = val

    @overload
    def findInfluencer(self, arg0: 'Class') -> 'influencers.Influencer':
        """public <K extends com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer> K com.badlogic.gdx.graphics.g3d.particles.ParticleController.findInfluencer(java.lang.Class<K>)"""
        return 'influencers.Influencer'._wrap(super(_ParticleController, self).findInfluencer(arg0))

    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.update()"""
        super(ParticleController, self).update()

    @overload
    def setTransform(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.setTransform(com.badlogic.gdx.math.Matrix4)"""
        super(_ParticleController, self).setTransform(arg0)

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_ParticleController, self).read(arg0, arg1)

    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.dispose()"""
        super(ParticleController, self).dispose()

    @overload
    def rotate(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.rotate(com.badlogic.gdx.math.Vector3,float)"""
        super(_ParticleController, self).rotate(arg0, _float.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.start()"""
        super(ParticleController, self).start()

    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.activateParticles(int,int)"""
        super(_ParticleController, self).activateParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setTranslation(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.setTranslation(com.badlogic.gdx.math.Vector3)"""
        super(_ParticleController, self).setTranslation(arg0)

    @overload
    def mul(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.mul(com.badlogic.gdx.math.Matrix4)"""
        super(_ParticleController, self).mul(arg0)

    @overload
    def translate(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.translate(com.badlogic.gdx.math.Vector3)"""
        super(_ParticleController, self).translate(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.end()"""
        super(ParticleController, self).end()

    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.killParticles(int,int)"""
        super(_ParticleController, self).killParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def scale(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.scale(float,float,float)"""
        super(_ParticleController, self).scale(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def copy(self) -> 'ParticleController':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleController com.badlogic.gdx.graphics.g3d.particles.ParticleController.copy()"""
        return 'ParticleController'._wrap(super(ParticleController, self).copy())

    @overload
    def replaceInfluencer(self, arg0: 'Class', arg1: 'Influencer') -> bool:
        """public <K extends com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer> boolean com.badlogic.gdx.graphics.g3d.particles.ParticleController.replaceInfluencer(java.lang.Class<K>,K)"""
        return bool._wrap(super(_ParticleController, self).replaceInfluencer(arg0, arg1))

    @overload
    def update(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.update(float)"""
        super(_ParticleController, self).update(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def rotate(self, arg0: 'Quaternion'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.rotate(com.badlogic.gdx.math.Quaternion)"""
        super(_ParticleController, self).rotate(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getTransform(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.getTransform(com.badlogic.gdx.math.Matrix4)"""
        super(_ParticleController, self).getTransform(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleController()"""
        val = _ParticleController()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleController 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ResourceData$Configurable
from pyquantum_helper import import_once as _import_once
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

from abc import abstractmethod, ABC
import com.badlogic.gdx.graphics.g3d.particles.ResourceData as _ResourceData_Configurable
_Configurable = _ResourceData_Configurable.Configurable
 
class Configurable():
    """com.badlogic.gdx.graphics.g3d.particles.ResourceData.Configurable"""
 
    @staticmethod
    def _wrap(java_value: _Configurable) -> 'Configurable':
        return Configurable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Configurable):
        """
        Dynamic initializer for Configurable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Configurable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Configurable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.ResourceData$Configurable.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData<T>)"""
        pass

    @abstractmethod
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.ResourceData$Configurable.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData<T>)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader$ParticleEffectSaveParameter
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
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader as _ParticleEffectLoader_ParticleEffectSaveParameter
_ParticleEffectSaveParameter = _ParticleEffectLoader_ParticleEffectSaveParameter.ParticleEffectSaveParameter
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParticleEffectSaveParameter():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader.ParticleEffectSaveParameter"""
 
    @staticmethod
    def _wrap(java_value: _ParticleEffectSaveParameter) -> 'ParticleEffectSaveParameter':
        return ParticleEffectSaveParameter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleEffectSaveParameter):
        """
        Dynamic initializer for ParticleEffectSaveParameter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleEffectSaveParameter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleEffectSaveParameter__wrapper":
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

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'AssetManager', arg2: 'Array'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader$ParticleEffectSaveParameter(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>>)"""
        val = _ParticleEffectSaveParameter(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'AssetManager', arg2: 'Array', arg3: 'OutputType', arg4: bool):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader$ParticleEffectSaveParameter(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>>,com.badlogic.gdx.utils.JsonWriter$OutputType,boolean)"""
        val = _ParticleEffectSaveParameter(arg0, arg1, arg2, arg3, _boolean.valueOf(arg4))
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleSystem
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
import com.badlogic.gdx.graphics.g3d.particles.ParticleSystem as _ParticleSystem
_ParticleSystem = _ParticleSystem
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import java.lang.Float as _float
try:
    from pygdx.graphics.g3d.particles import batches
except ImportError:
    batches = _import_once("pygdx.graphics.g3d.particles.batches")

import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParticleSystem():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleSystem"""
 
    @staticmethod
    def _wrap(java_value: _ParticleSystem) -> 'ParticleSystem':
        return ParticleSystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleSystem):
        """
        Dynamic initializer for ParticleSystem.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleSystem__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleSystem__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getRenderables(self, arg0: 'Array', arg1: 'Pool'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.getRenderables(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>,com.badlogic.gdx.utils.Pool<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        super(_ParticleSystem, self).getRenderables(arg0, arg1)

    @overload
    def update(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.update(float)"""
        super(_ParticleSystem, self).update(_float.valueOf(arg0))

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.end()"""
        super(ParticleSystem, self).end()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def add(self, arg0: 'ParticleEffect'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.add(com.badlogic.gdx.graphics.g3d.particles.ParticleEffect)"""
        super(_ParticleSystem, self).add(arg0)

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
    def remove(self, arg0: 'ParticleEffect'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.remove(com.badlogic.gdx.graphics.g3d.particles.ParticleEffect)"""
        super(_ParticleSystem, self).remove(arg0)

    @overload
    def updateAndDraw(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.updateAndDraw(float)"""
        super(_ParticleSystem, self).updateAndDraw(_float.valueOf(arg0))

    @overload
    def draw(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.draw()"""
        super(ParticleSystem, self).draw()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleSystem()"""
        val = _ParticleSystem()
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

    @overload
    def getBatches(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>> com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.getBatches()"""
        return 'utils.Array'._wrap(super(ParticleSystem, self).getBatches())

    @overload
    def add(self, arg0: 'ParticleBatch'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.add(com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>)"""
        super(_ParticleSystem, self).add(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.update()"""
        super(ParticleSystem, self).update()

    @overload
    def removeAll(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.removeAll()"""
        super(ParticleSystem, self).removeAll()

    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.begin()"""
        super(ParticleSystem, self).begin()

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
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleSystem()"""
        val = _ParticleSystem()
        self.__wrapper = val

    @staticmethod
    @overload
    def get() -> 'ParticleSystem':
        """public static com.badlogic.gdx.graphics.g3d.particles.ParticleSystem com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.get()"""
        return ParticleSystem._wrap(_ParticleSystem.get())

    @overload
    def updateAndDraw(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.updateAndDraw()"""
        super(ParticleSystem, self).updateAndDraw()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData
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
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.ResourceData as _ResourceData_SaveData
_SaveData = _ResourceData_SaveData.SaveData
import com.badlogic.gdx.assets.AssetDescriptor as _AssetDescriptor
_AssetDescriptor = _AssetDescriptor
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SaveData():
    """com.badlogic.gdx.graphics.g3d.particles.ResourceData.SaveData"""
 
    @staticmethod
    def _wrap(java_value: _SaveData) -> 'SaveData':
        return SaveData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SaveData):
        """
        Dynamic initializer for SaveData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SaveData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SaveData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def saveAsset(self, arg0: str, arg1: 'Class'):
        """public <K> void com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData.saveAsset(java.lang.String,java.lang.Class<K>)"""
        super(_SaveData, self).saveAsset(arg0, arg1)

    @overload
    def __init__(self, arg0: 'ResourceData'):
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData(com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        val = _SaveData(arg0)
        self.__wrapper = val

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData.write(com.badlogic.gdx.utils.Json)"""
        super(_SaveData, self).write(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def save(self, arg0: str, arg1: object):
        """public void com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData.save(java.lang.String,java.lang.Object)"""
        super(_SaveData, self).save(arg0, arg1)

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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData()"""
        val = _SaveData()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData()"""
        val = _SaveData()
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

    @overload
    def load(self, arg0: str) -> object:
        """public <K> K com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData.load(java.lang.String)"""
        return object._wrap(super(_SaveData, self).load(arg0))

    @overload
    def loadAsset(self) -> 'assets.AssetDescriptor':
        """public com.badlogic.gdx.assets.AssetDescriptor com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData.loadAsset()"""
        return 'assets.AssetDescriptor'._wrap(super(SaveData, self).loadAsset())

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
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_SaveData, self).read(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ResourceData
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
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.graphics.g3d.particles.ResourceData as _ResourceData
_ResourceData = _ResourceData
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.ResourceData as _ResourceData_SaveData
_SaveData = _ResourceData_SaveData.SaveData
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ResourceData():
    """com.badlogic.gdx.graphics.g3d.particles.ResourceData"""
 
    @staticmethod
    def _wrap(java_value: _ResourceData) -> 'ResourceData':
        return ResourceData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ResourceData):
        """
        Dynamic initializer for ResourceData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ResourceData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ResourceData__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getSaveData(self) -> 'SaveData':
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData com.badlogic.gdx.graphics.g3d.particles.ResourceData.getSaveData()"""
        return 'SaveData'._wrap(super(ResourceData, self).getSaveData())

    @overload
    def __init__(self, arg0: object):
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData(T)"""
        val = _ResourceData(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ResourceData.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_ResourceData, self).read(arg0, arg1)

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
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ResourceData.write(com.badlogic.gdx.utils.Json)"""
        super(_ResourceData, self).write(arg0)

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
    def getAssetDescriptors(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.graphics.g3d.particles.ResourceData.getAssetDescriptors()"""
        return 'utils.Array'._wrap(super(ResourceData, self).getAssetDescriptors())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData()"""
        val = _ResourceData()
        self.__wrapper = val

    @overload
    def createSaveData(self) -> 'SaveData':
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData com.badlogic.gdx.graphics.g3d.particles.ResourceData.createSaveData()"""
        return 'SaveData'._wrap(super(ResourceData, self).createSaveData())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getAssets(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.particles.ResourceData$AssetData> com.badlogic.gdx.graphics.g3d.particles.ResourceData.getAssets()"""
        return 'utils.Array'._wrap(super(ResourceData, self).getAssets())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData()"""
        val = _ResourceData()
        self.__wrapper = val

    @overload
    def createSaveData(self, arg0: str) -> 'SaveData':
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData com.badlogic.gdx.graphics.g3d.particles.ResourceData.createSaveData(java.lang.String)"""
        return 'SaveData'._wrap(super(_ResourceData, self).createSaveData(arg0))

    @overload
    def getSaveData(self, arg0: str) -> 'SaveData':
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData com.badlogic.gdx.graphics.g3d.particles.ResourceData.getSaveData(java.lang.String)"""
        return 'SaveData'._wrap(super(_ResourceData, self).getSaveData(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Setters
from builtins import str
import com.badlogic.gdx.graphics.g3d.particles.ParticleShader as _ParticleShader_Setters
_Setters = _ParticleShader_Setters.Setters
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
 
class Setters():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleShader.Setters"""
 
    @staticmethod
    def _wrap(java_value: _Setters) -> 'Setters':
        return Setters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Setters):
        """
        Dynamic initializer for Setters.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Setters__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Setters__wrapper":
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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Setters()"""
        val = _Setters()
        self.__wrapper = val

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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Setters()"""
        val = _Setters()
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode
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
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
import com.badlogic.gdx.graphics.g3d.particles.ParticleShader as _ParticleShader_AlignMode
_AlignMode = _ParticleShader_AlignMode.AlignMode
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AlignMode():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleShader.AlignMode"""
 
    @staticmethod
    def _wrap(java_value: _AlignMode) -> 'AlignMode':
        return AlignMode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AlignMode):
        """
        Dynamic initializer for AlignMode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AlignMode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AlignMode__wrapper":
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
    def values() -> List['AlignMode']:
        """public static com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode[] com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode.values()"""
        return List[AlignMode]._wrap(_AlignMode.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'AlignMode':
        """public static com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode.valueOf(java.lang.String)"""
        return AlignMode._wrap(_AlignMode.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleSorter$Distance
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
import com.badlogic.gdx.graphics.g3d.particles.ParticleSorter as _ParticleSorter_Distance
_Distance = _ParticleSorter_Distance.Distance
from typing import List
import com.badlogic.gdx.graphics.g3d.particles.ParticleSorter as _ParticleSorter
_ParticleSorter = _ParticleSorter
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Distance():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleSorter.Distance"""
 
    @staticmethod
    def _wrap(java_value: _Distance) -> 'Distance':
        return Distance(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Distance):
        """
        Dynamic initializer for Distance.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Distance__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Distance__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleSorter$Distance()"""
        val = _Distance()
        self.__wrapper = val

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
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSorter$Distance.ensureCapacity(int)"""
        super(_Distance, self).ensureCapacity(_int.valueOf(arg0))

    @overload
    def sort(self, arg0: 'Array') -> List[int]:
        """public <T extends com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderData> int[] com.badlogic.gdx.graphics.g3d.particles.ParticleSorter$Distance.sort(com.badlogic.gdx.utils.Array<T>)"""
        return List[int]._wrap(super(_Distance, self).sort(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSorter.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(_ParticleSorter, self).setCamera(arg0)

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleSorter$Distance()"""
        val = _Distance()
        self.__wrapper = val

    @overload
    def qsort(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSorter$Distance.qsort(int,int)"""
        super(_Distance, self).qsort(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ChannelInitializer
import com.badlogic.gdx.graphics.g3d.particles.ParallelArray as _ParallelArray_ChannelInitializer
_ChannelInitializer = _ParallelArray_ChannelInitializer.ChannelInitializer
from abc import abstractmethod, ABC
 
class ChannelInitializer():
    """com.badlogic.gdx.graphics.g3d.particles.ParallelArray.ChannelInitializer"""
 
    @staticmethod
    def _wrap(java_value: _ChannelInitializer) -> 'ChannelInitializer':
        return ChannelInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ChannelInitializer):
        """
        Dynamic initializer for ChannelInitializer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ChannelInitializer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ChannelInitializer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def init(self, arg0: 'Channel'):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ChannelInitializer.init(T)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParallelArray
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.ParallelArray as _ParallelArray
_ParallelArray = _ParallelArray
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.particles.ParallelArray as _ParallelArray_Channel
_Channel = _ParallelArray_Channel.Channel
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParallelArray():
    """com.badlogic.gdx.graphics.g3d.particles.ParallelArray"""
 
    @staticmethod
    def _wrap(java_value: _ParallelArray) -> 'ParallelArray':
        return ParallelArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParallelArray):
        """
        Dynamic initializer for ParallelArray.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParallelArray__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParallelArray__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def removeElement(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParallelArray.removeElement(int)"""
        super(_ParallelArray, self).removeElement(_int.valueOf(arg0))

    @overload
    def addChannel(self, arg0: 'ChannelDescriptor', arg1: 'ChannelInitializer') -> 'Channel':
        """public <T extends com.badlogic.gdx.graphics.g3d.particles.ParallelArray$Channel> T com.badlogic.gdx.graphics.g3d.particles.ParallelArray.addChannel(com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ChannelDescriptor,com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ChannelInitializer<T>)"""
        return 'Channel'._wrap(super(_ParallelArray, self).addChannel(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def clear(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParallelArray.clear()"""
        super(ParallelArray, self).clear()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setCapacity(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParallelArray.setCapacity(int)"""
        super(_ParallelArray, self).setCapacity(_int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def removeArray(self, arg0: int):
        """public <T> void com.badlogic.gdx.graphics.g3d.particles.ParallelArray.removeArray(int)"""
        super(_ParallelArray, self).removeArray(_int.valueOf(arg0))

    @overload
    def addElement(self, *arg0: object):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParallelArray.addElement(java.lang.Object...)"""
        super(_ParallelArray, self).addElement(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def addChannel(self, arg0: 'ChannelDescriptor') -> 'Channel':
        """public <T extends com.badlogic.gdx.graphics.g3d.particles.ParallelArray$Channel> T com.badlogic.gdx.graphics.g3d.particles.ParallelArray.addChannel(com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ChannelDescriptor)"""
        return 'Channel'._wrap(super(_ParallelArray, self).addChannel(arg0))

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
    def getChannel(self, arg0: 'ChannelDescriptor') -> 'Channel':
        """public <T extends com.badlogic.gdx.graphics.g3d.particles.ParallelArray$Channel> T com.badlogic.gdx.graphics.g3d.particles.ParallelArray.getChannel(com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ChannelDescriptor)"""
        return 'Channel'._wrap(super(_ParallelArray, self).getChannel(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.particles.ParallelArray(int)"""
        val = _ParallelArray(_int.valueOf(arg0))
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader
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
import com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader as _AsynchronousAssetLoader
_AsynchronousAssetLoader = _AsynchronousAssetLoader
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader as _ParticleEffectLoader
_ParticleEffectLoader = _ParticleEffectLoader
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import com.badlogic.gdx.files.FileHandle as _FileHandle
_FileHandle = _FileHandle
try:
    from pygdx.assets import loaders
except ImportError:
    loaders = _import_once("pygdx.assets.loaders")

import com.badlogic.gdx.assets.loaders.AssetLoader as _AssetLoader
_AssetLoader = _AssetLoader
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.ParticleEffect as _ParticleEffect
_ParticleEffect = _ParticleEffect
try:
    from pygdx import files
except ImportError:
    files = _import_once("pygdx.files")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParticleEffectLoader():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader"""
 
    @staticmethod
    def _wrap(java_value: _ParticleEffectLoader) -> 'ParticleEffectLoader':
        return ParticleEffectLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleEffectLoader):
        """
        Dynamic initializer for ParticleEffectLoader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleEffectLoader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleEffectLoader__wrapper":
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

    @overload
    def save(self, arg0: 'ParticleEffect', arg1: 'ParticleEffectSaveParameter'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader.save(com.badlogic.gdx.graphics.g3d.particles.ParticleEffect,com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader$ParticleEffectSaveParameter) throws java.io.IOException"""
        super(_ParticleEffectLoader, self).save(arg0, arg1)

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
    def loadSync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'ParticleEffectLoadParameter') -> 'ParticleEffect':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleEffect com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader.loadSync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader$ParticleEffectLoadParameter)"""
        return 'ParticleEffect'._wrap(super(_ParticleEffectLoader, self).loadSync(arg0, arg1, arg2, arg3))

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
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = _ParticleEffectLoader(arg0)
        self.__wrapper = val

    @overload
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'ParticleEffectLoadParameter') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader$ParticleEffectLoadParameter)"""
        return 'utils.Array'._wrap(super(_ParticleEffectLoader, self).getDependencies(arg0, arg1, arg2))

    @overload
    def resolve(self, arg0: str) -> 'files.FileHandle':
        """public com.badlogic.gdx.files.FileHandle com.badlogic.gdx.assets.loaders.AssetLoader.resolve(java.lang.String)"""
        return 'files.FileHandle'._wrap(super(_loaders.AssetLoader, self).resolve(arg0))

    @override
    @overload
    def unloadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.unloadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(_loaders.AsynchronousAssetLoader, self).unloadAsync(arg0, arg1, arg2, arg3)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def loadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'ParticleEffectLoadParameter'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader.loadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader$ParticleEffectLoadParameter)"""
        super(_ParticleEffectLoader, self).loadAsync(arg0, arg1, arg2, arg3)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader$ParticleEffectLoadParameter
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
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader as _ParticleEffectLoader_ParticleEffectLoadParameter
_ParticleEffectLoadParameter = _ParticleEffectLoader_ParticleEffectLoadParameter.ParticleEffectLoadParameter
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParticleEffectLoadParameter():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader.ParticleEffectLoadParameter"""
 
    @staticmethod
    def _wrap(java_value: _ParticleEffectLoadParameter) -> 'ParticleEffectLoadParameter':
        return ParticleEffectLoadParameter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleEffectLoadParameter):
        """
        Dynamic initializer for ParticleEffectLoadParameter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleEffectLoadParameter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleEffectLoadParameter__wrapper":
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
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader$ParticleEffectLoadParameter(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>>)"""
        val = _ParticleEffectLoadParameter(arg0)
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Inputs
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.ParticleShader as _ParticleShader_Inputs
_Inputs = _ParticleShader_Inputs.Inputs
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Inputs():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleShader.Inputs"""
 
    @staticmethod
    def _wrap(java_value: _Inputs) -> 'Inputs':
        return Inputs(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Inputs):
        """
        Dynamic initializer for Inputs.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Inputs__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Inputs__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Inputs()"""
        val = _Inputs()
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Inputs()"""
        val = _Inputs()
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParallelArray$Channel
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.particles.ParallelArray as _ParallelArray_Channel
_Channel = _ParallelArray_Channel.Channel
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Channel():
    """com.badlogic.gdx.graphics.g3d.particles.ParallelArray.Channel"""
 
    @staticmethod
    def _wrap(java_value: _Channel) -> 'Channel':
        return Channel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Channel):
        """
        Dynamic initializer for Channel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Channel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Channel__wrapper":
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

    @overload
    def __init__(self, arg0: 'ParallelArray', arg1: int, arg2: object, arg3: int):
        """public com.badlogic.gdx.graphics.g3d.particles.ParallelArray$Channel(com.badlogic.gdx.graphics.g3d.particles.ParallelArray,int,java.lang.Object,int)"""
        val = _Channel(arg0, _int.valueOf(arg1), arg2, _int.valueOf(arg3))
        self.__wrapper = val

    @abstractmethod
    def add(self, arg0: int, *arg1: object):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.ParallelArray$Channel.add(int,java.lang.Object...)"""
        pass

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

    @abstractmethod
    def swap(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.ParallelArray$Channel.swap(int,int)"""
        pass

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$TextureRegionInitializer
from builtins import str
import com.badlogic.gdx.graphics.g3d.particles.ParticleChannels as _ParticleChannels_TextureRegionInitializer
_TextureRegionInitializer = _ParticleChannels_TextureRegionInitializer.TextureRegionInitializer
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
 
class TextureRegionInitializer():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleChannels.TextureRegionInitializer"""
 
    @staticmethod
    def _wrap(java_value: _TextureRegionInitializer) -> 'TextureRegionInitializer':
        return TextureRegionInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TextureRegionInitializer):
        """
        Dynamic initializer for TextureRegionInitializer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TextureRegionInitializer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TextureRegionInitializer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def init(self, arg0: 'FloatChannel'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$TextureRegionInitializer.init(com.badlogic.gdx.graphics.g3d.particles.ParallelArray$FloatChannel)"""
        super(_TextureRegionInitializer, self).init(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$TextureRegionInitializer()"""
        val = _TextureRegionInitializer()
        self.__wrapper = val

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$TextureRegionInitializer()"""
        val = _TextureRegionInitializer()
        self.__wrapper = val

    @staticmethod
    @overload
    def get() -> 'TextureRegionInitializer':
        """public static com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$TextureRegionInitializer com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$TextureRegionInitializer.get()"""
        return TextureRegionInitializer._wrap(_TextureRegionInitializer.get())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$ColorInitializer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.ParticleChannels as _ParticleChannels_ColorInitializer
_ColorInitializer = _ParticleChannels_ColorInitializer.ColorInitializer
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ColorInitializer():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleChannels.ColorInitializer"""
 
    @staticmethod
    def _wrap(java_value: _ColorInitializer) -> 'ColorInitializer':
        return ColorInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ColorInitializer):
        """
        Dynamic initializer for ColorInitializer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ColorInitializer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ColorInitializer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def get() -> 'ColorInitializer':
        """public static com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$ColorInitializer com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$ColorInitializer.get()"""
        return ColorInitializer._wrap(_ColorInitializer.get())

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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$ColorInitializer()"""
        val = _ColorInitializer()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$ColorInitializer()"""
        val = _ColorInitializer()
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
    def init(self, arg0: 'FloatChannel'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$ColorInitializer.init(com.badlogic.gdx.graphics.g3d.particles.ParallelArray$FloatChannel)"""
        super(_ColorInitializer, self).init(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleShader
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import com.badlogic.gdx.graphics.g3d.particles.ParticleShader as _ParticleShader
_ParticleShader = _ParticleShader
try:
    from pygdx.graphics.g3d import shaders
except ImportError:
    shaders = _import_once("pygdx.graphics.g3d.shaders")

import java.lang.Integer as _int
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as _BaseShader
_BaseShader = _BaseShader
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParticleShader():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleShader"""
 
    @staticmethod
    def _wrap(java_value: _ParticleShader) -> 'ParticleShader':
        return ParticleShader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleShader):
        """
        Dynamic initializer for ParticleShader.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleShader__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleShader__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int,int)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3)))

    @overload
    def loc(self, arg0: int) -> int:
        """public final int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.loc(int)"""
        return int._wrap(super(_shaders.BaseShader, self).loc(_int.valueOf(arg0)))

    @overload
    def register(self, arg0: 'Uniform', arg1: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int._wrap(super(_shaders.BaseShader, self).register(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.ParticleShader.equals(java.lang.Object)"""
        return bool._wrap(super(_ParticleShader, self).equals(arg0))

    @override
    @overload
    def begin(self, arg0: 'Camera', arg1: 'RenderContext'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleShader.begin(com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.graphics.g3d.utils.RenderContext)"""
        super(_ParticleShader, self).begin(arg0, arg1)

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleShader.end()"""
        super(ParticleShader, self).end()

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
    def set(self, arg0: int, arg1: 'TextureDescriptor') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def register(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String)"""
        return int._wrap(super(_shaders.BaseShader, self).register(arg0))

    @overload
    def set(self, arg0: int, arg1: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def register(self, arg0: str, arg1: 'Validator', arg2: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int._wrap(super(_shaders.BaseShader, self).register(arg0, arg1, arg2))

    @overload
    def compareTo(self, arg0: 'Shader') -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.ParticleShader.compareTo(com.badlogic.gdx.graphics.g3d.Shader)"""
        return int._wrap(super(_ParticleShader, self).compareTo(arg0))

    @overload
    def register(self, arg0: str, arg1: 'Validator') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator)"""
        return int._wrap(super(_shaders.BaseShader, self).register(arg0, arg1))

    @staticmethod
    @overload
    def getDefaultVertexShader() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.g3d.particles.ParticleShader.getDefaultVertexShader()"""
        return str._wrap(_ParticleShader.getDefaultVertexShader())

    @overload
    def setDefaultDepthFunc(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleShader.setDefaultDepthFunc(int)"""
        super(_ParticleShader, self).setDefaultDepthFunc(_int.valueOf(arg0))

    @overload
    def equals(self, arg0: 'ParticleShader') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.ParticleShader.equals(com.badlogic.gdx.graphics.g3d.particles.ParticleShader)"""
        return bool._wrap(super(_ParticleShader, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getDefaultDepthFunc(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.ParticleShader.getDefaultDepthFunc()"""
        return int._wrap(super(ParticleShader, self).getDefaultDepthFunc())

    @overload
    def has(self, arg0: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.has(int)"""
        return bool._wrap(super(_shaders.BaseShader, self).has(_int.valueOf(arg0)))

    @overload
    def getDefaultCullFace(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.ParticleShader.getDefaultCullFace()"""
        return int._wrap(super(ParticleShader, self).getDefaultCullFace())

    @overload
    def set(self, arg0: int, arg1: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), _float.valueOf(arg1)))

    @overload
    def setDefaultCullFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleShader.setDefaultCullFace(int)"""
        super(_ParticleShader, self).setDefaultCullFace(_int.valueOf(arg0))

    @overload
    def register(self, arg0: str, arg1: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int._wrap(super(_shaders.BaseShader, self).register(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: int, arg1: float, arg2: float, arg3: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float,float)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def set(self, arg0: int, arg1: 'Matrix3') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Matrix3)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: 'ShaderProgram'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config,com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        val = _ParticleShader(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def set(self, arg0: int, arg1: 'GLTexture') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.GLTexture)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int,int,int)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), _int.valueOf(arg4)))

    @override
    @overload
    def render(self, arg0: 'Renderable'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleShader.render(com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(_ParticleShader, self).render(arg0)

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: str, arg3: str, arg4: str):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config,java.lang.String,java.lang.String,java.lang.String)"""
        val = _ParticleShader(arg0, arg1, arg2, arg3, arg4)
        self.__wrapper = val

    @staticmethod
    @overload
    def getDefaultFragmentShader() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.g3d.particles.ParticleShader.getDefaultFragmentShader()"""
        return str._wrap(_ParticleShader.getDefaultFragmentShader())

    @override
    @overload
    def init(self, arg0: 'ShaderProgram', arg1: 'Renderable'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.init(com.badlogic.gdx.graphics.glutils.ShaderProgram,com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(_shaders.BaseShader, self).init(arg0, arg1)

    @staticmethod
    @overload
    def createPrefix(arg0: 'Renderable', arg1: 'Config') -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.g3d.particles.ParticleShader.createPrefix(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config)"""
        return str._wrap(_ParticleShader.createPrefix(arg0, arg1))

    @overload
    def canRender(self, arg0: 'Renderable') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.ParticleShader.canRender(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return bool._wrap(super(_ParticleShader, self).canRender(arg0))

    @overload
    def set(self, arg0: int, arg1: 'Matrix4') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Matrix4)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: str):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config,java.lang.String)"""
        val = _ParticleShader(arg0, arg1, arg2)
        self.__wrapper = val

    @overload
    def set(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleShader.dispose()"""
        super(ParticleShader, self).dispose()

    @overload
    def set(self, arg0: int, arg1: 'Color') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.Color)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: int, arg1: 'Vector3') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Vector3)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def __init__(self, arg0: 'Renderable'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        val = _ParticleShader(arg0)
        self.__wrapper = val

    @overload
    def set(self, arg0: int, arg1: float, arg2: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def set(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float,float,float)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4)))

    @overload
    def getUniformID(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.getUniformID(java.lang.String)"""
        return int._wrap(super(_shaders.BaseShader, self).getUniformID(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getUniformAlias(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.shaders.BaseShader.getUniformAlias(int)"""
        return str._wrap(super(_shaders.BaseShader, self).getUniformAlias(_int.valueOf(arg0)))

    @override
    @overload
    def render(self, arg0: 'Renderable', arg1: 'Attributes'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.render(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Attributes)"""
        super(_shaders.BaseShader, self).render(arg0, arg1)

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleShader.init()"""
        super(ParticleShader, self).init()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def register(self, arg0: 'Uniform') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform)"""
        return int._wrap(super(_shaders.BaseShader, self).register(arg0))

    @overload
    def set(self, arg0: int, arg1: 'Vector2') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Vector2)"""
        return bool._wrap(super(_shaders.BaseShader, self).set(_int.valueOf(arg0), arg1))

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config)"""
        val = _ParticleShader(arg0, arg1)
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleEffect
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
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.Array as _Array
_Array = _Array
import java.lang.Float as _float
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import java.lang.String as _string
import com.badlogic.gdx.graphics.g3d.particles.ParticleController as _ParticleController
_ParticleController = _ParticleController
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.ParticleEffect as _ParticleEffect
_ParticleEffect = _ParticleEffect
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import com.badlogic.gdx.math.collision.BoundingBox as _BoundingBox
_BoundingBox = _BoundingBox
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParticleEffect():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleEffect"""
 
    @staticmethod
    def _wrap(java_value: _ParticleEffect) -> 'ParticleEffect':
        return ParticleEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleEffect):
        """
        Dynamic initializer for ParticleEffect.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleEffect__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleEffect__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def rotate(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.rotate(com.badlogic.gdx.math.Vector3,float)"""
        super(_ParticleEffect, self).rotate(arg0, _float.valueOf(arg1))

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_ParticleEffect, self).save(arg0, arg1)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleEffect()"""
        val = _ParticleEffect()
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
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setTransform(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.setTransform(com.badlogic.gdx.math.Matrix4)"""
        super(_ParticleEffect, self).setTransform(arg0)

    @overload
    def translate(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.translate(com.badlogic.gdx.math.Vector3)"""
        super(_ParticleEffect, self).translate(arg0)

    @overload
    def rotate(self, arg0: 'Quaternion'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.rotate(com.badlogic.gdx.math.Quaternion)"""
        super(_ParticleEffect, self).rotate(arg0)

    @overload
    def findController(self, arg0: str) -> 'ParticleController':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleController com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.findController(java.lang.String)"""
        return 'ParticleController'._wrap(super(_ParticleEffect, self).findController(arg0))

    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.reset()"""
        super(ParticleEffect, self).reset()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'ParticleEffect'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleEffect(com.badlogic.gdx.graphics.g3d.particles.ParticleEffect)"""
        val = _ParticleEffect(arg0)
        self.__wrapper = val

    @overload
    def update(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.update(float)"""
        super(_ParticleEffect, self).update(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def copy(self) -> 'ParticleEffect':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleEffect com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.copy()"""
        return 'ParticleEffect'._wrap(super(ParticleEffect, self).copy())

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_ParticleEffect, self).load(arg0, arg1)

    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.isComplete()"""
        return bool._wrap(super(ParticleEffect, self).isComplete())

    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.start()"""
        super(ParticleEffect, self).start()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.end()"""
        super(ParticleEffect, self).end()

    @overload
    def draw(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.draw()"""
        super(ParticleEffect, self).draw()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleEffect()"""
        val = _ParticleEffect()
        self.__wrapper = val

    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.update()"""
        super(ParticleEffect, self).update()

    @overload
    def __init__(self, *arg0: 'ParticleController'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleEffect(com.badlogic.gdx.graphics.g3d.particles.ParticleController...)"""
        val = _ParticleEffect(arg0)
        self.__wrapper = val

    @overload
    def getBoundingBox(self) -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.getBoundingBox()"""
        return 'collision.BoundingBox'._wrap(super(ParticleEffect, self).getBoundingBox())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setBatch(self, arg0: 'Array'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.setBatch(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>>)"""
        super(_ParticleEffect, self).setBatch(arg0)

    @overload
    def scale(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.scale(float,float,float)"""
        super(_ParticleEffect, self).scale(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.dispose()"""
        super(ParticleEffect, self).dispose()

    @overload
    def getControllers(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.particles.ParticleController> com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.getControllers()"""
        return 'utils.Array'._wrap(super(ParticleEffect, self).getControllers())

    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.init()"""
        super(ParticleEffect, self).init()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def scale(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.scale(com.badlogic.gdx.math.Vector3)"""
        super(_ParticleEffect, self).scale(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ResourceData$AssetData
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g3d.particles.ResourceData as _ResourceData_AssetData
_AssetData = _ResourceData_AssetData.AssetData
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
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AssetData():
    """com.badlogic.gdx.graphics.g3d.particles.ResourceData.AssetData"""
 
    @staticmethod
    def _wrap(java_value: _AssetData) -> 'AssetData':
        return AssetData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AssetData):
        """
        Dynamic initializer for AssetData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AssetData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AssetData__wrapper":
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

    @overload
    def __init__(self, arg0: str, arg1: 'Class'):
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData$AssetData(java.lang.String,java.lang.Class<T>)"""
        val = _AssetData(arg0, arg1)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData$AssetData()"""
        val = _AssetData()
        self.__wrapper = val

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ResourceData$AssetData.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_AssetData, self).read(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ResourceData$AssetData.write(com.badlogic.gdx.utils.Json)"""
        super(_AssetData, self).write(arg0)

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData$AssetData()"""
        val = _AssetData()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleSorter$None
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
from typing import List
import com.badlogic.gdx.graphics.g3d.particles.ParticleSorter as _ParticleSorter
_ParticleSorter = _ParticleSorter
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.graphics.g3d.particles.ParticleSorter as _ParticleSorter_None
_None = _ParticleSorter_None.None
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class None():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleSorter.None"""
 
    @staticmethod
    def _wrap(java_value: _None) -> 'None':
        return None(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _None):
        """
        Dynamic initializer for None.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_None__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_None__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def sort(self, arg0: 'Array') -> List[int]:
        """public <T extends com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderData> int[] com.badlogic.gdx.graphics.g3d.particles.ParticleSorter$None.sort(com.badlogic.gdx.utils.Array<T>)"""
        return List[int]._wrap(super(_None, self).sort(arg0))

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
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSorter$None.ensureCapacity(int)"""
        super(_None, self).ensureCapacity(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleSorter$None()"""
        val = _None()
        self.__wrapper = val

    @override
    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSorter.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(_ParticleSorter, self).setCamera(arg0)

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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleSorter$None()"""
        val = _None()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$Rotation3dInitializer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.ParticleChannels as _ParticleChannels_Rotation3dInitializer
_Rotation3dInitializer = _ParticleChannels_Rotation3dInitializer.Rotation3dInitializer
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Rotation3dInitializer():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleChannels.Rotation3dInitializer"""
 
    @staticmethod
    def _wrap(java_value: _Rotation3dInitializer) -> 'Rotation3dInitializer':
        return Rotation3dInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Rotation3dInitializer):
        """
        Dynamic initializer for Rotation3dInitializer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Rotation3dInitializer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Rotation3dInitializer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def get() -> 'Rotation3dInitializer':
        """public static com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$Rotation3dInitializer com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$Rotation3dInitializer.get()"""
        return Rotation3dInitializer._wrap(_Rotation3dInitializer.get())

    @overload
    def init(self, arg0: 'FloatChannel'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$Rotation3dInitializer.init(com.badlogic.gdx.graphics.g3d.particles.ParallelArray$FloatChannel)"""
        super(_Rotation3dInitializer, self).init(arg0)

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$Rotation3dInitializer()"""
        val = _Rotation3dInitializer()
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$Rotation3dInitializer()"""
        val = _Rotation3dInitializer()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.ParticleShader as _ParticleShader_Config
_Config = _ParticleShader_Config.Config
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Config():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleShader.Config"""
 
    @staticmethod
    def _wrap(java_value: _Config) -> 'Config':
        return Config(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Config):
        """
        Dynamic initializer for Config.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Config__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Config__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: str, arg1: str):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config(java.lang.String,java.lang.String)"""
        val = _Config(arg0, arg1)
        self.__wrapper = val

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

    @overload
    def __init__(self, arg0: 'AlignMode', arg1: 'ParticleType'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config(com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode,com.badlogic.gdx.graphics.g3d.particles.ParticleShader$ParticleType)"""
        val = _Config(arg0, arg1)
        self.__wrapper = val

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
    def __init__(self, arg0: 'AlignMode'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config(com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode)"""
        val = _Config(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config()"""
        val = _Config()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config()"""
        val = _Config()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'ParticleType'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config(com.badlogic.gdx.graphics.g3d.particles.ParticleShader$ParticleType)"""
        val = _Config(arg0)
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParallelArray$IntChannel
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.particles.ParallelArray as _ParallelArray_IntChannel
_IntChannel = _ParallelArray_IntChannel.IntChannel
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IntChannel():
    """com.badlogic.gdx.graphics.g3d.particles.ParallelArray.IntChannel"""
 
    @staticmethod
    def _wrap(java_value: _IntChannel) -> 'IntChannel':
        return IntChannel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IntChannel):
        """
        Dynamic initializer for IntChannel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IntChannel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IntChannel__wrapper":
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

    @overload
    def __init__(self, arg0: 'ParallelArray', arg1: int, arg2: int, arg3: int):
        """public com.badlogic.gdx.graphics.g3d.particles.ParallelArray$IntChannel(com.badlogic.gdx.graphics.g3d.particles.ParallelArray,int,int,int)"""
        val = _IntChannel(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def swap(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParallelArray$IntChannel.swap(int,int)"""
        super(_IntChannel, self).swap(_int.valueOf(arg0), _int.valueOf(arg1))

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

    @overload
    def setCapacity(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParallelArray$IntChannel.setCapacity(int)"""
        super(_IntChannel, self).setCapacity(_int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def add(self, arg0: int, *arg1: object):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParallelArray$IntChannel.add(int,java.lang.Object...)"""
        super(_IntChannel, self).add(_int.valueOf(arg0), arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$ScaleInitializer
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.graphics.g3d.particles.ParticleChannels as _ParticleChannels_ScaleInitializer
_ScaleInitializer = _ParticleChannels_ScaleInitializer.ScaleInitializer
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
 
class ScaleInitializer():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleChannels.ScaleInitializer"""
 
    @staticmethod
    def _wrap(java_value: _ScaleInitializer) -> 'ScaleInitializer':
        return ScaleInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ScaleInitializer):
        """
        Dynamic initializer for ScaleInitializer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ScaleInitializer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ScaleInitializer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def get() -> 'ScaleInitializer':
        """public static com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$ScaleInitializer com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$ScaleInitializer.get()"""
        return ScaleInitializer._wrap(_ScaleInitializer.get())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$ScaleInitializer()"""
        val = _ScaleInitializer()
        self.__wrapper = val

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
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$ScaleInitializer()"""
        val = _ScaleInitializer()
        self.__wrapper = val

    @overload
    def init(self, arg0: 'FloatChannel'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$ScaleInitializer.init(com.badlogic.gdx.graphics.g3d.particles.ParallelArray$FloatChannel)"""
        super(_ScaleInitializer, self).init(arg0)

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent
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
import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as _ParticleControllerComponent
_ParticleControllerComponent = _ParticleControllerComponent
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParticleControllerComponent():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent"""
 
    @staticmethod
    def _wrap(java_value: _ParticleControllerComponent) -> 'ParticleControllerComponent':
        return ParticleControllerComponent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleControllerComponent):
        """
        Dynamic initializer for ParticleControllerComponent.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleControllerComponent__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleControllerComponent__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def set(self, arg0: 'ParticleController'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(_ParticleControllerComponent, self).set(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.start()"""
        super(ParticleControllerComponent, self).start()

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
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_ParticleControllerComponent, self).save(arg0, arg1)

    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.update()"""
        super(ParticleControllerComponent, self).update()

    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(ParticleControllerComponent, self).init()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent()"""
        val = _ParticleControllerComponent()
        self.__wrapper = val

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.copy()"""
        pass

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent()"""
        val = _ParticleControllerComponent()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_ParticleControllerComponent, self).read(arg0, arg1)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(ParticleControllerComponent, self).dispose()

    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.allocateChannels()"""
        super(ParticleControllerComponent, self).allocateChannels()

    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.activateParticles(int,int)"""
        super(_ParticleControllerComponent, self).activateParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(_ParticleControllerComponent, self).write(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(ParticleControllerComponent, self).end()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(_ParticleControllerComponent, self).killParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleSorter
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
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.particles.ParticleSorter as _ParticleSorter
_ParticleSorter = _ParticleSorter
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParticleSorter():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleSorter"""
 
    @staticmethod
    def _wrap(java_value: _ParticleSorter) -> 'ParticleSorter':
        return ParticleSorter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleSorter):
        """
        Dynamic initializer for ParticleSorter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleSorter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleSorter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleSorter()"""
        val = _ParticleSorter()
        self.__wrapper = val

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
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleSorter()"""
        val = _ParticleSorter()
        self.__wrapper = val

    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSorter.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(_ParticleSorter, self).setCamera(arg0)

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
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSorter.ensureCapacity(int)"""
        super(_ParticleSorter, self).ensureCapacity(_int.valueOf(arg0))

    @abstractmethod
    def sort(self, arg0: 'Array'):
        """public abstract <T extends com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderData> int[] com.badlogic.gdx.graphics.g3d.particles.ParticleSorter.sort(com.badlogic.gdx.utils.Array<T>)"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleShader$ParticleType
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.ParticleShader as _ParticleShader_ParticleType
_ParticleType = _ParticleShader_ParticleType.ParticleType
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
 
class ParticleType():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleShader.ParticleType"""
 
    @staticmethod
    def _wrap(java_value: _ParticleType) -> 'ParticleType':
        return ParticleType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleType):
        """
        Dynamic initializer for ParticleType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleType__wrapper":
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
    def values() -> List['ParticleType']:
        """public static com.badlogic.gdx.graphics.g3d.particles.ParticleShader$ParticleType[] com.badlogic.gdx.graphics.g3d.particles.ParticleShader$ParticleType.values()"""
        return List[ParticleType]._wrap(_ParticleType.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ParticleType':
        """public static com.badlogic.gdx.graphics.g3d.particles.ParticleShader$ParticleType com.badlogic.gdx.graphics.g3d.particles.ParticleShader$ParticleType.valueOf(java.lang.String)"""
        return ParticleType._wrap(_ParticleType.valueOf(arg0))

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ObjectChannel
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.ParallelArray as _ParallelArray_ObjectChannel
_ObjectChannel = _ParallelArray_ObjectChannel.ObjectChannel
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ObjectChannel():
    """com.badlogic.gdx.graphics.g3d.particles.ParallelArray.ObjectChannel"""
 
    @staticmethod
    def _wrap(java_value: _ObjectChannel) -> 'ObjectChannel':
        return ObjectChannel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ObjectChannel):
        """
        Dynamic initializer for ObjectChannel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ObjectChannel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ObjectChannel__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def add(self, arg0: int, *arg1: object):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ObjectChannel.add(int,java.lang.Object...)"""
        super(_ObjectChannel, self).add(_int.valueOf(arg0), arg1)

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
    def __init__(self, arg0: 'ParallelArray', arg1: int, arg2: int, arg3: int, arg4: 'Class'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ObjectChannel(int,int,int,java.lang.Class<T>)"""
        val = _ObjectChannel(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3), arg4)
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
    def setCapacity(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ObjectChannel.setCapacity(int)"""
        super(_ObjectChannel, self).setCapacity(_int.valueOf(arg0))

    @override
    @overload
    def swap(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ObjectChannel.swap(int,int)"""
        super(_ObjectChannel, self).swap(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleChannels
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
import com.badlogic.gdx.graphics.g3d.particles.ParticleChannels as _ParticleChannels
_ParticleChannels = _ParticleChannels
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParticleChannels():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleChannels"""
 
    @staticmethod
    def _wrap(java_value: _ParticleChannels) -> 'ParticleChannels':
        return ParticleChannels(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleChannels):
        """
        Dynamic initializer for ParticleChannels.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleChannels__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleChannels__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def newGlobalId() -> int:
        """public static int com.badlogic.gdx.graphics.g3d.particles.ParticleChannels.newGlobalId()"""
        return int._wrap(_ParticleChannels.newGlobalId())

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleChannels()"""
        val = _ParticleChannels()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleChannels()"""
        val = _ParticleChannels()
        self.__wrapper = val

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
    def newId(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.ParticleChannels.newId()"""
        return int._wrap(super(ParticleChannels, self).newId())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$Rotation2dInitializer
import com.badlogic.gdx.graphics.g3d.particles.ParticleChannels as _ParticleChannels_Rotation2dInitializer
_Rotation2dInitializer = _ParticleChannels_Rotation2dInitializer.Rotation2dInitializer
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
 
class Rotation2dInitializer():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleChannels.Rotation2dInitializer"""
 
    @staticmethod
    def _wrap(java_value: _Rotation2dInitializer) -> 'Rotation2dInitializer':
        return Rotation2dInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Rotation2dInitializer):
        """
        Dynamic initializer for Rotation2dInitializer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Rotation2dInitializer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Rotation2dInitializer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def get() -> 'Rotation2dInitializer':
        """public static com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$Rotation2dInitializer com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$Rotation2dInitializer.get()"""
        return Rotation2dInitializer._wrap(_Rotation2dInitializer.get())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$Rotation2dInitializer()"""
        val = _Rotation2dInitializer()
        self.__wrapper = val

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
    def init(self, arg0: 'FloatChannel'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$Rotation2dInitializer.init(com.badlogic.gdx.graphics.g3d.particles.ParallelArray$FloatChannel)"""
        super(_Rotation2dInitializer, self).init(arg0)

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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$Rotation2dInitializer()"""
        val = _Rotation2dInitializer()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ChannelDescriptor
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.particles.ParallelArray as _ParallelArray_ChannelDescriptor
_ChannelDescriptor = _ParallelArray_ChannelDescriptor.ChannelDescriptor
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ChannelDescriptor():
    """com.badlogic.gdx.graphics.g3d.particles.ParallelArray.ChannelDescriptor"""
 
    @staticmethod
    def _wrap(java_value: _ChannelDescriptor) -> 'ChannelDescriptor':
        return ChannelDescriptor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ChannelDescriptor):
        """
        Dynamic initializer for ChannelDescriptor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ChannelDescriptor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ChannelDescriptor__wrapper":
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

    @overload
    def __init__(self, arg0: int, arg1: 'Class', arg2: int):
        """public com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ChannelDescriptor(int,java.lang.Class<?>,int)"""
        val = _ChannelDescriptor(_int.valueOf(arg0), arg1, _int.valueOf(arg2))
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParallelArray$FloatChannel
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.g3d.particles.ParallelArray as _ParallelArray_FloatChannel
_FloatChannel = _ParallelArray_FloatChannel.FloatChannel
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FloatChannel():
    """com.badlogic.gdx.graphics.g3d.particles.ParallelArray.FloatChannel"""
 
    @staticmethod
    def _wrap(java_value: _FloatChannel) -> 'FloatChannel':
        return FloatChannel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FloatChannel):
        """
        Dynamic initializer for FloatChannel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FloatChannel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FloatChannel__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setCapacity(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParallelArray$FloatChannel.setCapacity(int)"""
        super(_FloatChannel, self).setCapacity(_int.valueOf(arg0))

    @override
    @overload
    def swap(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParallelArray$FloatChannel.swap(int,int)"""
        super(_FloatChannel, self).swap(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def add(self, arg0: int, *arg1: object):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParallelArray$FloatChannel.add(int,java.lang.Object...)"""
        super(_FloatChannel, self).add(_int.valueOf(arg0), arg1)

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
    def __init__(self, arg0: 'ParallelArray', arg1: int, arg2: int, arg3: int):
        """public com.badlogic.gdx.graphics.g3d.particles.ParallelArray$FloatChannel(com.badlogic.gdx.graphics.g3d.particles.ParallelArray,int,int,int)"""
        val = _FloatChannel(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))
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