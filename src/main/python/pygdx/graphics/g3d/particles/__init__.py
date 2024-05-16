from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

try:
    from pygdx.graphics.g3d.particles import renderers
except ImportError:
    renderers = __import_once__("pygdx.graphics.g3d.particles.renderers")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

try:
    from pygdx.graphics.g3d.particles import influencers
except ImportError:
    influencers = __import_once__("pygdx.graphics.g3d.particles.influencers")

try:
    from pygdx.math import collision
except ImportError:
    collision = __import_once__("pygdx.math.collision")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer as __Influencer
__Influencer = __Influencer
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.math.collision.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
import com.badlogic.gdx.graphics.g3d.particles.ParticleController as __ParticleController
__ParticleController = __ParticleController
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.graphics.g3d.particles import emitters
except ImportError:
    emitters = __import_once__("pygdx.graphics.g3d.particles.emitters")

from builtins import int
 
class ParticleController():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleController"""
 
    @staticmethod
    def __wrap(java_value: __ParticleController) -> 'ParticleController':
        return ParticleController(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleController):
        """
        Dynamic initializer for ParticleController.
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
    def reset(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.reset()"""
        super(ParticleController, self).reset()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.ParticleController.isComplete()"""
        return bool.__wrap(super(ParticleController, self).isComplete())

    @overload
    def setTransform(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.setTransform(com.badlogic.gdx.math.Matrix4)"""
        super(__ParticleController, self).setTransform(arg0)

    @overload
    def __init__(self, arg0: str, arg1: 'Emitter', arg2: 'ParticleControllerRenderer', *arg3: 'influencers.Influencer'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleController(java.lang.String,com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter,com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer<?, ?>,com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer...)"""
        val = __ParticleController(arg0, arg1, arg2, arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getBoundingBox(self) -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g3d.particles.ParticleController.getBoundingBox()"""
        return 'collision.BoundingBox'.__wrap(super(ParticleController, self).getBoundingBox())

    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.killParticles(int,int)"""
        super(__ParticleController, self).killParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def scale(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.scale(float,float,float)"""
        super(__ParticleController, self).scale(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def draw(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.draw()"""
        super(ParticleController, self).draw()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleController()"""
        val = __ParticleController()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.activateParticles(int,int)"""
        super(__ParticleController, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def scale(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.scale(com.badlogic.gdx.math.Vector3)"""
        super(__ParticleController, self).scale(arg0)

    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.init()"""
        super(ParticleController, self).init()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def removeInfluencer(self, arg0: 'Class'):
        """public <K extends com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer> void com.badlogic.gdx.graphics.g3d.particles.ParticleController.removeInfluencer(java.lang.Class<K>)"""
        super(__ParticleController, self).removeInfluencer(arg0)

    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.update()"""
        super(ParticleController, self).update()

    @overload
    def rotate(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.rotate(com.badlogic.gdx.math.Vector3,float)"""
        super(__ParticleController, self).rotate(arg0, __float.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__ParticleController, self).read(arg0, arg1)

    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.dispose()"""
        super(ParticleController, self).dispose()

    @overload
    def setTransform(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.setTransform(float,float,float,float,float,float,float,float)"""
        super(__ParticleController, self).setTransform(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7))

    @overload
    def update(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.update(float)"""
        super(__ParticleController, self).update(__float.valueOf(arg0))

    @overload
    def rotate(self, arg0: 'Quaternion'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.rotate(com.badlogic.gdx.math.Quaternion)"""
        super(__ParticleController, self).rotate(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.start()"""
        super(ParticleController, self).start()

    @overload
    def findInfluencer(self, arg0: 'Class') -> 'influencers.Influencer':
        """public <K extends com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer> K com.badlogic.gdx.graphics.g3d.particles.ParticleController.findInfluencer(java.lang.Class<K>)"""
        return 'influencers.Influencer'.__wrap(super(__ParticleController, self).findInfluencer(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.end()"""
        super(ParticleController, self).end()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.write(com.badlogic.gdx.utils.Json)"""
        super(__ParticleController, self).write(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleController()"""
        val = __ParticleController()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def copy(self) -> 'ParticleController':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleController com.badlogic.gdx.graphics.g3d.particles.ParticleController.copy()"""
        return 'ParticleController'.__wrap(super(ParticleController, self).copy())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setTranslation(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.setTranslation(com.badlogic.gdx.math.Vector3)"""
        super(__ParticleController, self).setTranslation(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__ParticleController, self).load(arg0, arg1)

    @overload
    def getTransform(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.getTransform(com.badlogic.gdx.math.Matrix4)"""
        super(__ParticleController, self).getTransform(arg0)

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__ParticleController, self).save(arg0, arg1)

    @overload
    def mul(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.mul(com.badlogic.gdx.math.Matrix4)"""
        super(__ParticleController, self).mul(arg0)

    @overload
    def translate(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.translate(com.badlogic.gdx.math.Vector3)"""
        super(__ParticleController, self).translate(arg0)

    @overload
    def replaceInfluencer(self, arg0: 'Class', arg1: 'Influencer') -> bool:
        """public <K extends com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer> boolean com.badlogic.gdx.graphics.g3d.particles.ParticleController.replaceInfluencer(java.lang.Class<K>,K)"""
        return bool.__wrap(super(__ParticleController, self).replaceInfluencer(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleController
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

try:
    from pygdx.graphics.g3d.particles import renderers
except ImportError:
    renderers = __import_once__("pygdx.graphics.g3d.particles.renderers")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

try:
    from pygdx.graphics.g3d.particles import influencers
except ImportError:
    influencers = __import_once__("pygdx.graphics.g3d.particles.influencers")

try:
    from pygdx.math import collision
except ImportError:
    collision = __import_once__("pygdx.math.collision")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer as __Influencer
__Influencer = __Influencer
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.math.collision.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
import com.badlogic.gdx.graphics.g3d.particles.ParticleController as __ParticleController
__ParticleController = __ParticleController
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.graphics.g3d.particles import emitters
except ImportError:
    emitters = __import_once__("pygdx.graphics.g3d.particles.emitters")

from builtins import int
 
class ParticleController():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleController"""
 
    @staticmethod
    def __wrap(java_value: __ParticleController) -> 'ParticleController':
        return ParticleController(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleController):
        """
        Dynamic initializer for ParticleController.
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
    def reset(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.reset()"""
        super(ParticleController, self).reset()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.ParticleController.isComplete()"""
        return bool.__wrap(super(ParticleController, self).isComplete())

    @overload
    def setTransform(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.setTransform(com.badlogic.gdx.math.Matrix4)"""
        super(__ParticleController, self).setTransform(arg0)

    @overload
    def __init__(self, arg0: str, arg1: 'Emitter', arg2: 'ParticleControllerRenderer', *arg3: 'influencers.Influencer'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleController(java.lang.String,com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter,com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer<?, ?>,com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer...)"""
        val = __ParticleController(arg0, arg1, arg2, arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getBoundingBox(self) -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g3d.particles.ParticleController.getBoundingBox()"""
        return 'collision.BoundingBox'.__wrap(super(ParticleController, self).getBoundingBox())

    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.killParticles(int,int)"""
        super(__ParticleController, self).killParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def scale(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.scale(float,float,float)"""
        super(__ParticleController, self).scale(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def draw(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.draw()"""
        super(ParticleController, self).draw()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleController()"""
        val = __ParticleController()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.activateParticles(int,int)"""
        super(__ParticleController, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def scale(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.scale(com.badlogic.gdx.math.Vector3)"""
        super(__ParticleController, self).scale(arg0)

    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.init()"""
        super(ParticleController, self).init()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def removeInfluencer(self, arg0: 'Class'):
        """public <K extends com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer> void com.badlogic.gdx.graphics.g3d.particles.ParticleController.removeInfluencer(java.lang.Class<K>)"""
        super(__ParticleController, self).removeInfluencer(arg0)

    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.update()"""
        super(ParticleController, self).update()

    @overload
    def rotate(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.rotate(com.badlogic.gdx.math.Vector3,float)"""
        super(__ParticleController, self).rotate(arg0, __float.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__ParticleController, self).read(arg0, arg1)

    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.dispose()"""
        super(ParticleController, self).dispose()

    @overload
    def setTransform(self, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.setTransform(float,float,float,float,float,float,float,float)"""
        super(__ParticleController, self).setTransform(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4), __float.valueOf(arg5), __float.valueOf(arg6), __float.valueOf(arg7))

    @overload
    def update(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.update(float)"""
        super(__ParticleController, self).update(__float.valueOf(arg0))

    @overload
    def rotate(self, arg0: 'Quaternion'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.rotate(com.badlogic.gdx.math.Quaternion)"""
        super(__ParticleController, self).rotate(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.start()"""
        super(ParticleController, self).start()

    @overload
    def findInfluencer(self, arg0: 'Class') -> 'influencers.Influencer':
        """public <K extends com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer> K com.badlogic.gdx.graphics.g3d.particles.ParticleController.findInfluencer(java.lang.Class<K>)"""
        return 'influencers.Influencer'.__wrap(super(__ParticleController, self).findInfluencer(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.end()"""
        super(ParticleController, self).end()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.write(com.badlogic.gdx.utils.Json)"""
        super(__ParticleController, self).write(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleController()"""
        val = __ParticleController()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def copy(self) -> 'ParticleController':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleController com.badlogic.gdx.graphics.g3d.particles.ParticleController.copy()"""
        return 'ParticleController'.__wrap(super(ParticleController, self).copy())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setTranslation(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.setTranslation(com.badlogic.gdx.math.Vector3)"""
        super(__ParticleController, self).setTranslation(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__ParticleController, self).load(arg0, arg1)

    @overload
    def getTransform(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.getTransform(com.badlogic.gdx.math.Matrix4)"""
        super(__ParticleController, self).getTransform(arg0)

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__ParticleController, self).save(arg0, arg1)

    @overload
    def mul(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.mul(com.badlogic.gdx.math.Matrix4)"""
        super(__ParticleController, self).mul(arg0)

    @overload
    def translate(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleController.translate(com.badlogic.gdx.math.Vector3)"""
        super(__ParticleController, self).translate(arg0)

    @overload
    def replaceInfluencer(self, arg0: 'Class', arg1: 'Influencer') -> bool:
        """public <K extends com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer> boolean com.badlogic.gdx.graphics.g3d.particles.ParticleController.replaceInfluencer(java.lang.Class<K>,K)"""
        return bool.__wrap(super(__ParticleController, self).replaceInfluencer(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleController 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Inputs
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
import java.lang.Integer as __int
import com.badlogic.gdx.graphics.g3d.particles.ParticleShader as __ParticleShader_Inputs
__Inputs = __ParticleShader_Inputs.Inputs
from builtins import bool
from builtins import int
 
class Inputs():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleShader.Inputs"""
 
    @staticmethod
    def __wrap(java_value: __Inputs) -> 'Inputs':
        return Inputs(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Inputs):
        """
        Dynamic initializer for Inputs.
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
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Inputs()"""
        val = __Inputs()
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Inputs()"""
        val = __Inputs()
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$Rotation2dInitializer
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.ParticleChannels as __ParticleChannels_Rotation2dInitializer
__Rotation2dInitializer = __ParticleChannels_Rotation2dInitializer.Rotation2dInitializer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Rotation2dInitializer():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleChannels.Rotation2dInitializer"""
 
    @staticmethod
    def __wrap(java_value: __Rotation2dInitializer) -> 'Rotation2dInitializer':
        return Rotation2dInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Rotation2dInitializer):
        """
        Dynamic initializer for Rotation2dInitializer.
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
    def init(self, arg0: 'FloatChannel'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$Rotation2dInitializer.init(com.badlogic.gdx.graphics.g3d.particles.ParallelArray$FloatChannel)"""
        super(__Rotation2dInitializer, self).init(arg0)

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$Rotation2dInitializer()"""
        val = __Rotation2dInitializer()
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$Rotation2dInitializer()"""
        val = __Rotation2dInitializer()
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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def get() -> 'Rotation2dInitializer':
        """public static com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$Rotation2dInitializer com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$Rotation2dInitializer.get()"""
        return Rotation2dInitializer.__wrap(__Rotation2dInitializer.get())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.assets.AssetDescriptor as __AssetDescriptor
__AssetDescriptor = __AssetDescriptor
from builtins import object
import com.badlogic.gdx.graphics.g3d.particles.ResourceData as __ResourceData_SaveData
__SaveData = __ResourceData_SaveData.SaveData
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
 
class SaveData():
    """com.badlogic.gdx.graphics.g3d.particles.ResourceData.SaveData"""
 
    @staticmethod
    def __wrap(java_value: __SaveData) -> 'SaveData':
        return SaveData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SaveData):
        """
        Dynamic initializer for SaveData.
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
    def __init__(self, arg0: 'ResourceData'):
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData(com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        val = __SaveData(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def load(self, arg0: str) -> object:
        """public <K> K com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData.load(java.lang.String)"""
        return object.__wrap(super(__SaveData, self).load(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def save(self, arg0: str, arg1: object):
        """public void com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData.save(java.lang.String,java.lang.Object)"""
        super(__SaveData, self).save(arg0, arg1)

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData.write(com.badlogic.gdx.utils.Json)"""
        super(__SaveData, self).write(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData()"""
        val = __SaveData()
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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def saveAsset(self, arg0: str, arg1: 'Class'):
        """public <K> void com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData.saveAsset(java.lang.String,java.lang.Class<K>)"""
        super(__SaveData, self).saveAsset(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData()"""
        val = __SaveData()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__SaveData, self).read(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def loadAsset(self) -> 'assets.AssetDescriptor':
        """public com.badlogic.gdx.assets.AssetDescriptor com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData.loadAsset()"""
        return 'assets.AssetDescriptor'.__wrap(super(SaveData, self).loadAsset()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ResourceData$Configurable
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.g3d.particles.ResourceData as __ResourceData_Configurable
__Configurable = __ResourceData_Configurable.Configurable
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

from abc import abstractmethod, ABC
 
class Configurable(ABC):
    """com.badlogic.gdx.graphics.g3d.particles.ResourceData.Configurable"""
 
    @staticmethod
    def __wrap(java_value: __Configurable) -> 'Configurable':
        return Configurable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Configurable):
        """
        Dynamic initializer for Configurable.
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
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.ResourceData$Configurable.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData<T>)"""
        pass

    @abstractmethod
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.ResourceData$Configurable.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData<T>)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleSorter
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from abc import abstractmethod, ABC
import com.badlogic.gdx.graphics.g3d.particles.ParticleSorter as __ParticleSorter
__ParticleSorter = __ParticleSorter
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class ParticleSorter(ABC):
    """com.badlogic.gdx.graphics.g3d.particles.ParticleSorter"""
 
    @staticmethod
    def __wrap(java_value: __ParticleSorter) -> 'ParticleSorter':
        return ParticleSorter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleSorter):
        """
        Dynamic initializer for ParticleSorter.
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
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSorter.ensureCapacity(int)"""
        super(__ParticleSorter, self).ensureCapacity(__int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleSorter()"""
        val = __ParticleSorter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleSorter()"""
        val = __ParticleSorter()
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
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSorter.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(__ParticleSorter, self).setCamera(arg0)

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

    @abstractmethod
    def sort(self, arg0: 'Array'):
        """public abstract <T extends com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderData> int[] com.badlogic.gdx.graphics.g3d.particles.ParticleSorter.sort(com.badlogic.gdx.utils.Array<T>)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleSorter$None
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.ParticleSorter as __ParticleSorter
__ParticleSorter = __ParticleSorter
import com.badlogic.gdx.graphics.g3d.particles.ParticleSorter as __ParticleSorter_None
__None = __ParticleSorter_None.None
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class None():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleSorter.None"""
 
    @staticmethod
    def __wrap(java_value: __None) -> 'None':
        return None(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __None):
        """
        Dynamic initializer for None.
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleSorter$None()"""
        val = __None()
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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleSorter$None()"""
        val = __None()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def sort(self, arg0: 'Array') -> List[int]:
        """public <T extends com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderData> int[] com.badlogic.gdx.graphics.g3d.particles.ParticleSorter$None.sort(com.badlogic.gdx.utils.Array<T>)"""
        return List[int].__wrap(super(__None, self).sort(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSorter$None.ensureCapacity(int)"""
        super(__None, self).ensureCapacity(__int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSorter.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(__ParticleSorter, self).setCamera(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader$ParticleEffectSaveParameter
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
import com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader as __ParticleEffectLoader_ParticleEffectSaveParameter
__ParticleEffectSaveParameter = __ParticleEffectLoader_ParticleEffectSaveParameter.ParticleEffectSaveParameter
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import files
except ImportError:
    files = __import_once__("pygdx.files")

from builtins import bool
from builtins import int
 
class ParticleEffectSaveParameter():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader.ParticleEffectSaveParameter"""
 
    @staticmethod
    def __wrap(java_value: __ParticleEffectSaveParameter) -> 'ParticleEffectSaveParameter':
        return ParticleEffectSaveParameter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleEffectSaveParameter):
        """
        Dynamic initializer for ParticleEffectSaveParameter.
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

    @overload
    def __init__(self, arg0: 'FileHandle', arg1: 'AssetManager', arg2: 'Array'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader$ParticleEffectSaveParameter(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>>)"""
        val = __ParticleEffectSaveParameter(arg0, arg1, arg2)
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
    def __init__(self, arg0: 'FileHandle', arg1: 'AssetManager', arg2: 'Array', arg3: 'OutputType', arg4: bool):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader$ParticleEffectSaveParameter(com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>>,com.badlogic.gdx.utils.JsonWriter$OutputType,boolean)"""
        val = __ParticleEffectSaveParameter(arg0, arg1, arg2, arg3, __boolean.valueOf(arg4))
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleShader$ParticleType
import com.badlogic.gdx.graphics.g3d.particles.ParticleShader as __ParticleShader_ParticleType
__ParticleType = __ParticleShader_ParticleType.ParticleType
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
from builtins import int
 
class ParticleType():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleShader.ParticleType"""
 
    @staticmethod
    def __wrap(java_value: __ParticleType) -> 'ParticleType':
        return ParticleType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleType):
        """
        Dynamic initializer for ParticleType.
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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'ParticleType':
        """public static com.badlogic.gdx.graphics.g3d.particles.ParticleShader$ParticleType com.badlogic.gdx.graphics.g3d.particles.ParticleShader$ParticleType.valueOf(java.lang.String)"""
        return ParticleType.__wrap(__ParticleType.valueOf(arg0))

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
    def values() -> List['ParticleType']:
        """public static com.badlogic.gdx.graphics.g3d.particles.ParticleShader$ParticleType[] com.badlogic.gdx.graphics.g3d.particles.ParticleShader$ParticleType.values()"""
        return List[ParticleType].__wrap(__ParticleType.values()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleSystem
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.ParticleSystem as __ParticleSystem
__ParticleSystem = __ParticleSystem
try:
    from pygdx.graphics.g3d.particles import batches
except ImportError:
    batches = __import_once__("pygdx.graphics.g3d.particles.batches")

import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.Array as __Array
__Array = __Array
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ParticleSystem():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleSystem"""
 
    @staticmethod
    def __wrap(java_value: __ParticleSystem) -> 'ParticleSystem':
        return ParticleSystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleSystem):
        """
        Dynamic initializer for ParticleSystem.
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleSystem()"""
        val = __ParticleSystem()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def update(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.update(float)"""
        super(__ParticleSystem, self).update(__float.valueOf(arg0))

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.end()"""
        super(ParticleSystem, self).end()

    @overload
    def add(self, arg0: 'ParticleBatch'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.add(com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>)"""
        super(__ParticleSystem, self).add(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def remove(self, arg0: 'ParticleEffect'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.remove(com.badlogic.gdx.graphics.g3d.particles.ParticleEffect)"""
        super(__ParticleSystem, self).remove(arg0)

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
    def draw(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.draw()"""
        super(ParticleSystem, self).draw()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleSystem()"""
        val = __ParticleSystem()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def updateAndDraw(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.updateAndDraw(float)"""
        super(__ParticleSystem, self).updateAndDraw(__float.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def getRenderables(self, arg0: 'Array', arg1: 'Pool'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.getRenderables(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>,com.badlogic.gdx.utils.Pool<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        super(__ParticleSystem, self).getRenderables(arg0, arg1)

    @overload
    def getBatches(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>> com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.getBatches()"""
        return 'utils.Array'.__wrap(super(ParticleSystem, self).getBatches())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def get() -> 'ParticleSystem':
        """public static com.badlogic.gdx.graphics.g3d.particles.ParticleSystem com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.get()"""
        return ParticleSystem.__wrap(__ParticleSystem.get())

    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.update()"""
        super(ParticleSystem, self).update()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def add(self, arg0: 'ParticleEffect'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.add(com.badlogic.gdx.graphics.g3d.particles.ParticleEffect)"""
        super(__ParticleSystem, self).add(arg0)

    @overload
    def updateAndDraw(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSystem.updateAndDraw()"""
        super(ParticleSystem, self).updateAndDraw() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import com.badlogic.gdx.graphics.g3d.particles.ParticleShader as __ParticleShader_AlignMode
__AlignMode = __ParticleShader_AlignMode.AlignMode
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
 
class AlignMode():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleShader.AlignMode"""
 
    @staticmethod
    def __wrap(java_value: __AlignMode) -> 'AlignMode':
        return AlignMode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AlignMode):
        """
        Dynamic initializer for AlignMode.
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
    def valueOf(arg0: str) -> 'AlignMode':
        """public static com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode.valueOf(java.lang.String)"""
        return AlignMode.__wrap(__AlignMode.valueOf(arg0))

    @staticmethod
    @overload
    def values() -> List['AlignMode']:
        """public static com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode[] com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode.values()"""
        return List[AlignMode].__wrap(__AlignMode.values())

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$Rotation3dInitializer
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import com.badlogic.gdx.graphics.g3d.particles.ParticleChannels as __ParticleChannels_Rotation3dInitializer
__Rotation3dInitializer = __ParticleChannels_Rotation3dInitializer.Rotation3dInitializer
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Rotation3dInitializer():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleChannels.Rotation3dInitializer"""
 
    @staticmethod
    def __wrap(java_value: __Rotation3dInitializer) -> 'Rotation3dInitializer':
        return Rotation3dInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Rotation3dInitializer):
        """
        Dynamic initializer for Rotation3dInitializer.
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
    def get() -> 'Rotation3dInitializer':
        """public static com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$Rotation3dInitializer com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$Rotation3dInitializer.get()"""
        return Rotation3dInitializer.__wrap(__Rotation3dInitializer.get())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def init(self, arg0: 'FloatChannel'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$Rotation3dInitializer.init(com.badlogic.gdx.graphics.g3d.particles.ParallelArray$FloatChannel)"""
        super(__Rotation3dInitializer, self).init(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$Rotation3dInitializer()"""
        val = __Rotation3dInitializer()
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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$Rotation3dInitializer()"""
        val = __Rotation3dInitializer()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParallelArray$Channel
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
from abc import abstractmethod, ABC
import com.badlogic.gdx.graphics.g3d.particles.ParallelArray as __ParallelArray_Channel
__Channel = __ParallelArray_Channel.Channel
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
 
class Channel(ABC):
    """com.badlogic.gdx.graphics.g3d.particles.ParallelArray.Channel"""
 
    @staticmethod
    def __wrap(java_value: __Channel) -> 'Channel':
        return Channel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Channel):
        """
        Dynamic initializer for Channel.
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

    @abstractmethod
    def add(self, arg0: int, *arg1: object):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.ParallelArray$Channel.add(int,java.lang.Object...)"""
        pass

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'ParallelArray', arg1: int, arg2: object, arg3: int):
        """public com.badlogic.gdx.graphics.g3d.particles.ParallelArray$Channel(com.badlogic.gdx.graphics.g3d.particles.ParallelArray,int,java.lang.Object,int)"""
        val = __Channel(arg0, __int.valueOf(arg1), arg2, __int.valueOf(arg3))
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

    @abstractmethod
    def swap(self, arg0: int, arg1: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.ParallelArray$Channel.swap(int,int)"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParallelArray$IntChannel
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import com.badlogic.gdx.graphics.g3d.particles.ParallelArray as __ParallelArray_IntChannel
__IntChannel = __ParallelArray_IntChannel.IntChannel
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
 
class IntChannel():
    """com.badlogic.gdx.graphics.g3d.particles.ParallelArray.IntChannel"""
 
    @staticmethod
    def __wrap(java_value: __IntChannel) -> 'IntChannel':
        return IntChannel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntChannel):
        """
        Dynamic initializer for IntChannel.
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
    def setCapacity(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParallelArray$IntChannel.setCapacity(int)"""
        super(__IntChannel, self).setCapacity(__int.valueOf(arg0))

    @override
    @overload
    def swap(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParallelArray$IntChannel.swap(int,int)"""
        super(__IntChannel, self).swap(__int.valueOf(arg0), __int.valueOf(arg1))

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
    def add(self, arg0: int, *arg1: object):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParallelArray$IntChannel.add(int,java.lang.Object...)"""
        super(__IntChannel, self).add(__int.valueOf(arg0), arg1)

    @overload
    def __init__(self, arg0: 'ParallelArray', arg1: int, arg2: int, arg3: int):
        """public com.badlogic.gdx.graphics.g3d.particles.ParallelArray$IntChannel(com.badlogic.gdx.graphics.g3d.particles.ParallelArray,int,int,int)"""
        val = __IntChannel(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleShader
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

from builtins import type
import java.lang.Long as __long
try:
    from pygdx.graphics.g3d import shaders
except ImportError:
    shaders = __import_once__("pygdx.graphics.g3d.shaders")

import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import com.badlogic.gdx.graphics.g3d.shaders.BaseShader as __BaseShader
__BaseShader = __BaseShader
import com.badlogic.gdx.graphics.g3d.particles.ParticleShader as __ParticleShader
__ParticleShader = __ParticleShader
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

from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = __import_once__("pygdx.graphics.g3d.utils")

from builtins import int
 
class ParticleShader():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleShader"""
 
    @staticmethod
    def __wrap(java_value: __ParticleShader) -> 'ParticleShader':
        return ParticleShader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleShader):
        """
        Dynamic initializer for ParticleShader.
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
    def set(self, arg0: int, arg1: float, arg2: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float)"""
        return bool.__wrap(super(__shaders.BaseShader, self).set(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2)))

    @overload
    def register(self, arg0: str, arg1: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int.__wrap(super(__shaders.BaseShader, self).register(arg0, arg1))

    @overload
    def getUniformAlias(self, arg0: int) -> str:
        """public java.lang.String com.badlogic.gdx.graphics.g3d.shaders.BaseShader.getUniformAlias(int)"""
        return str.__wrap(super(__shaders.BaseShader, self).getUniformAlias(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleShader.end()"""
        super(ParticleShader, self).end()

    @override
    @overload
    def render(self, arg0: 'Renderable'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleShader.render(com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(__ParticleShader, self).render(arg0)

    @overload
    def set(self, arg0: int, arg1: int, arg2: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int)"""
        return bool.__wrap(super(__shaders.BaseShader, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int,int)"""
        return bool.__wrap(super(__shaders.BaseShader, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3)))

    @overload
    def register(self, arg0: str, arg1: 'Validator') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator)"""
        return int.__wrap(super(__shaders.BaseShader, self).register(arg0, arg1))

    @overload
    def getDefaultCullFace(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.ParticleShader.getDefaultCullFace()"""
        return int.__wrap(super(ParticleShader, self).getDefaultCullFace())

    @overload
    def set(self, arg0: int, arg1: 'Vector2') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Vector2)"""
        return bool.__wrap(super(__shaders.BaseShader, self).set(__int.valueOf(arg0), arg1))

    @overload
    def set(self, arg0: int, arg1: 'Color') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.Color)"""
        return bool.__wrap(super(__shaders.BaseShader, self).set(__int.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def canRender(self, arg0: 'Renderable') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.ParticleShader.canRender(com.badlogic.gdx.graphics.g3d.Renderable)"""
        return bool.__wrap(super(__ParticleShader, self).canRender(arg0))

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: str, arg3: str, arg4: str):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config,java.lang.String,java.lang.String,java.lang.String)"""
        val = __ParticleShader(arg0, arg1, arg2, arg3, arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def compareTo(self, arg0: 'Shader') -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.ParticleShader.compareTo(com.badlogic.gdx.graphics.g3d.Shader)"""
        return int.__wrap(super(__ParticleShader, self).compareTo(arg0))

    @overload
    def set(self, arg0: int, arg1: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float)"""
        return bool.__wrap(super(__shaders.BaseShader, self).set(__int.valueOf(arg0), __float.valueOf(arg1)))

    @overload
    def register(self, arg0: 'Uniform', arg1: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int.__wrap(super(__shaders.BaseShader, self).register(arg0, arg1))

    @overload
    def __init__(self, arg0: 'Renderable'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader(com.badlogic.gdx.graphics.g3d.Renderable)"""
        val = __ParticleShader(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config)"""
        val = __ParticleShader(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def set(self, arg0: int, arg1: float, arg2: float, arg3: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float,float)"""
        return bool.__wrap(super(__shaders.BaseShader, self).set(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3)))

    @staticmethod
    @overload
    def getDefaultVertexShader() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.g3d.particles.ParticleShader.getDefaultVertexShader()"""
        return str.__wrap(__ParticleShader.getDefaultVertexShader())

    @overload
    def setDefaultCullFace(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleShader.setDefaultCullFace(int)"""
        super(__ParticleShader, self).setDefaultCullFace(__int.valueOf(arg0))

    @overload
    def set(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int,int,int,int)"""
        return bool.__wrap(super(__shaders.BaseShader, self).set(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), __int.valueOf(arg4)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: int, arg1: 'GLTexture') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.GLTexture)"""
        return bool.__wrap(super(__shaders.BaseShader, self).set(__int.valueOf(arg0), arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def init(self, arg0: 'ShaderProgram', arg1: 'Renderable'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.init(com.badlogic.gdx.graphics.glutils.ShaderProgram,com.badlogic.gdx.graphics.g3d.Renderable)"""
        super(__shaders.BaseShader, self).init(arg0, arg1)

    @overload
    def equals(self, arg0: 'ParticleShader') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.ParticleShader.equals(com.badlogic.gdx.graphics.g3d.particles.ParticleShader)"""
        return bool.__wrap(super(__ParticleShader, self).equals(arg0))

    @override
    @overload
    def begin(self, arg0: 'Camera', arg1: 'RenderContext'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleShader.begin(com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.graphics.g3d.utils.RenderContext)"""
        super(__ParticleShader, self).begin(arg0, arg1)

    @overload
    def getUniformID(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.getUniformID(java.lang.String)"""
        return int.__wrap(super(__shaders.BaseShader, self).getUniformID(arg0))

    @overload
    def register(self, arg0: str) -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String)"""
        return int.__wrap(super(__shaders.BaseShader, self).register(arg0))

    @overload
    def set(self, arg0: int, arg1: 'Matrix4') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Matrix4)"""
        return bool.__wrap(super(__shaders.BaseShader, self).set(__int.valueOf(arg0), arg1))

    @overload
    def register(self, arg0: 'Uniform') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Uniform)"""
        return int.__wrap(super(__shaders.BaseShader, self).register(arg0))

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: 'ShaderProgram'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config,com.badlogic.gdx.graphics.glutils.ShaderProgram)"""
        val = __ParticleShader(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Renderable', arg1: 'Config', arg2: str):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config,java.lang.String)"""
        val = __ParticleShader(arg0, arg1, arg2)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def render(self, arg0: 'Renderable', arg1: 'Attributes'):
        """public void com.badlogic.gdx.graphics.g3d.shaders.BaseShader.render(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.Attributes)"""
        super(__shaders.BaseShader, self).render(arg0, arg1)

    @overload
    def set(self, arg0: int, arg1: 'TextureDescriptor') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.graphics.g3d.utils.TextureDescriptor)"""
        return bool.__wrap(super(__shaders.BaseShader, self).set(__int.valueOf(arg0), arg1))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleShader.dispose()"""
        super(ParticleShader, self).dispose()

    @staticmethod
    @overload
    def getDefaultFragmentShader() -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.g3d.particles.ParticleShader.getDefaultFragmentShader()"""
        return str.__wrap(__ParticleShader.getDefaultFragmentShader())

    @overload
    def getDefaultDepthFunc(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.ParticleShader.getDefaultDepthFunc()"""
        return int.__wrap(super(ParticleShader, self).getDefaultDepthFunc())

    @overload
    def set(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,float,float,float,float)"""
        return bool.__wrap(super(__shaders.BaseShader, self).set(__int.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3), __float.valueOf(arg4)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.ParticleShader.equals(java.lang.Object)"""
        return bool.__wrap(super(__ParticleShader, self).equals(arg0))

    @overload
    def set(self, arg0: int, arg1: 'Vector3') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Vector3)"""
        return bool.__wrap(super(__shaders.BaseShader, self).set(__int.valueOf(arg0), arg1))

    @overload
    def register(self, arg0: str, arg1: 'Validator', arg2: 'Setter') -> int:
        """public int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.register(java.lang.String,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Validator,com.badlogic.gdx.graphics.g3d.shaders.BaseShader$Setter)"""
        return int.__wrap(super(__shaders.BaseShader, self).register(arg0, arg1, arg2))

    @overload
    def set(self, arg0: int, arg1: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,int)"""
        return bool.__wrap(super(__shaders.BaseShader, self).set(__int.valueOf(arg0), __int.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def loc(self, arg0: int) -> int:
        """public final int com.badlogic.gdx.graphics.g3d.shaders.BaseShader.loc(int)"""
        return int.__wrap(super(__shaders.BaseShader, self).loc(__int.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def createPrefix(arg0: 'Renderable', arg1: 'Config') -> str:
        """public static java.lang.String com.badlogic.gdx.graphics.g3d.particles.ParticleShader.createPrefix(com.badlogic.gdx.graphics.g3d.Renderable,com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config)"""
        return str.__wrap(__ParticleShader.createPrefix(arg0, arg1))

    @overload
    def setDefaultDepthFunc(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleShader.setDefaultDepthFunc(int)"""
        super(__ParticleShader, self).setDefaultDepthFunc(__int.valueOf(arg0))

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleShader.init()"""
        super(ParticleShader, self).init()

    @overload
    def has(self, arg0: int) -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.has(int)"""
        return bool.__wrap(super(__shaders.BaseShader, self).has(__int.valueOf(arg0)))

    @overload
    def set(self, arg0: int, arg1: 'Matrix3') -> bool:
        """public final boolean com.badlogic.gdx.graphics.g3d.shaders.BaseShader.set(int,com.badlogic.gdx.math.Matrix3)"""
        return bool.__wrap(super(__shaders.BaseShader, self).set(__int.valueOf(arg0), arg1)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$ColorInitializer
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.graphics.g3d.particles.ParticleChannels as __ParticleChannels_ColorInitializer
__ColorInitializer = __ParticleChannels_ColorInitializer.ColorInitializer
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ColorInitializer():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleChannels.ColorInitializer"""
 
    @staticmethod
    def __wrap(java_value: __ColorInitializer) -> 'ColorInitializer':
        return ColorInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ColorInitializer):
        """
        Dynamic initializer for ColorInitializer.
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
    def init(self, arg0: 'FloatChannel'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$ColorInitializer.init(com.badlogic.gdx.graphics.g3d.particles.ParallelArray$FloatChannel)"""
        super(__ColorInitializer, self).init(arg0)

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
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$ColorInitializer()"""
        val = __ColorInitializer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def get() -> 'ColorInitializer':
        """public static com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$ColorInitializer com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$ColorInitializer.get()"""
        return ColorInitializer.__wrap(__ColorInitializer.get())

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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$ColorInitializer()"""
        val = __ColorInitializer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ChannelInitializer
import com.badlogic.gdx.graphics.g3d.particles.ParallelArray as __ParallelArray_ChannelInitializer
__ChannelInitializer = __ParallelArray_ChannelInitializer.ChannelInitializer
from abc import abstractmethod, ABC
 
class ChannelInitializer(ABC):
    """com.badlogic.gdx.graphics.g3d.particles.ParallelArray.ChannelInitializer"""
 
    @staticmethod
    def __wrap(java_value: __ChannelInitializer) -> 'ChannelInitializer':
        return ChannelInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ChannelInitializer):
        """
        Dynamic initializer for ChannelInitializer.
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
    def init(self, arg0: 'Channel'):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ChannelInitializer.init(T)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Setters
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
import com.badlogic.gdx.graphics.g3d.particles.ParticleShader as __ParticleShader_Setters
__Setters = __ParticleShader_Setters.Setters
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Setters():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleShader.Setters"""
 
    @staticmethod
    def __wrap(java_value: __Setters) -> 'Setters':
        return Setters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Setters):
        """
        Dynamic initializer for Setters.
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
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Setters()"""
        val = __Setters()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Setters()"""
        val = __Setters()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

from abc import abstractmethod, ABC
import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as __ParticleControllerComponent
__ParticleControllerComponent = __ParticleControllerComponent
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
 
class ParticleControllerComponent(ABC):
    """com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent"""
 
    @staticmethod
    def __wrap(java_value: __ParticleControllerComponent) -> 'ParticleControllerComponent':
        return ParticleControllerComponent(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleControllerComponent):
        """
        Dynamic initializer for ParticleControllerComponent.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.start()"""
        super(ParticleControllerComponent, self).start()

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__ParticleControllerComponent, self).save(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__ParticleControllerComponent, self).read(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.update()"""
        super(ParticleControllerComponent, self).update()

    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(ParticleControllerComponent, self).init()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent()"""
        val = __ParticleControllerComponent()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.copy()"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(__ParticleControllerComponent, self).killParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(ParticleControllerComponent, self).dispose()

    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.allocateChannels()"""
        super(ParticleControllerComponent, self).allocateChannels()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def set(self, arg0: 'ParticleController'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(__ParticleControllerComponent, self).set(arg0)

    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.activateParticles(int,int)"""
        super(__ParticleControllerComponent, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent()"""
        val = __ParticleControllerComponent()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(ParticleControllerComponent, self).end()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(__ParticleControllerComponent, self).write(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__ParticleControllerComponent, self).load(arg0, arg1) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ObjectChannel
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import com.badlogic.gdx.graphics.g3d.particles.ParallelArray as __ParallelArray_ObjectChannel
__ObjectChannel = __ParallelArray_ObjectChannel.ObjectChannel
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
 
class ObjectChannel():
    """com.badlogic.gdx.graphics.g3d.particles.ParallelArray.ObjectChannel"""
 
    @staticmethod
    def __wrap(java_value: __ObjectChannel) -> 'ObjectChannel':
        return ObjectChannel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ObjectChannel):
        """
        Dynamic initializer for ObjectChannel.
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
    def setCapacity(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ObjectChannel.setCapacity(int)"""
        super(__ObjectChannel, self).setCapacity(__int.valueOf(arg0))

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
    def swap(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ObjectChannel.swap(int,int)"""
        super(__ObjectChannel, self).swap(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def add(self, arg0: int, *arg1: object):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ObjectChannel.add(int,java.lang.Object...)"""
        super(__ObjectChannel, self).add(__int.valueOf(arg0), arg1)

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
    def __init__(self, arg0: 'ParallelArray', arg1: int, arg2: int, arg3: int, arg4: 'Class'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ObjectChannel(int,int,int,java.lang.Class<T>)"""
        val = __ObjectChannel(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3), arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$ScaleInitializer
import com.badlogic.gdx.graphics.g3d.particles.ParticleChannels as __ParticleChannels_ScaleInitializer
__ScaleInitializer = __ParticleChannels_ScaleInitializer.ScaleInitializer
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
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ScaleInitializer():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleChannels.ScaleInitializer"""
 
    @staticmethod
    def __wrap(java_value: __ScaleInitializer) -> 'ScaleInitializer':
        return ScaleInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ScaleInitializer):
        """
        Dynamic initializer for ScaleInitializer.
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$ScaleInitializer()"""
        val = __ScaleInitializer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$ScaleInitializer()"""
        val = __ScaleInitializer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def get() -> 'ScaleInitializer':
        """public static com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$ScaleInitializer com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$ScaleInitializer.get()"""
        return ScaleInitializer.__wrap(__ScaleInitializer.get())

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
    def init(self, arg0: 'FloatChannel'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$ScaleInitializer.init(com.badlogic.gdx.graphics.g3d.particles.ParallelArray$FloatChannel)"""
        super(__ScaleInitializer, self).init(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleEffect
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

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
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.math.collision.BoundingBox as __BoundingBox
__BoundingBox = __BoundingBox
import com.badlogic.gdx.graphics.g3d.particles.ParticleController as __ParticleController
__ParticleController = __ParticleController
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
import com.badlogic.gdx.graphics.g3d.particles.ParticleEffect as __ParticleEffect
__ParticleEffect = __ParticleEffect
from builtins import bool
from builtins import int
 
class ParticleEffect():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleEffect"""
 
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

    @overload
    def copy(self) -> 'ParticleEffect':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleEffect com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.copy()"""
        return 'ParticleEffect'.__wrap(super(ParticleEffect, self).copy())

    @overload
    def __init__(self, *arg0: 'ParticleController'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleEffect(com.badlogic.gdx.graphics.g3d.particles.ParticleController...)"""
        val = __ParticleEffect(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.isComplete()"""
        return bool.__wrap(super(ParticleEffect, self).isComplete())

    @overload
    def getControllers(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.particles.ParticleController> com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.getControllers()"""
        return 'utils.Array'.__wrap(super(ParticleEffect, self).getControllers())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleEffect()"""
        val = __ParticleEffect()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def scale(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.scale(float,float,float)"""
        super(__ParticleEffect, self).scale(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def scale(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.scale(com.badlogic.gdx.math.Vector3)"""
        super(__ParticleEffect, self).scale(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__ParticleEffect, self).load(arg0, arg1)

    @overload
    def reset(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.reset()"""
        super(ParticleEffect, self).reset()

    @overload
    def update(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.update(float)"""
        super(__ParticleEffect, self).update(__float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def setBatch(self, arg0: 'Array'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.setBatch(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>>)"""
        super(__ParticleEffect, self).setBatch(arg0)

    @overload
    def setTransform(self, arg0: 'Matrix4'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.setTransform(com.badlogic.gdx.math.Matrix4)"""
        super(__ParticleEffect, self).setTransform(arg0)

    @overload
    def findController(self, arg0: str) -> 'ParticleController':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleController com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.findController(java.lang.String)"""
        return 'ParticleController'.__wrap(super(__ParticleEffect, self).findController(arg0))

    @overload
    def __init__(self, arg0: 'ParticleEffect'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleEffect(com.badlogic.gdx.graphics.g3d.particles.ParticleEffect)"""
        val = __ParticleEffect(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def translate(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.translate(com.badlogic.gdx.math.Vector3)"""
        super(__ParticleEffect, self).translate(arg0)

    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.start()"""
        super(ParticleEffect, self).start()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__ParticleEffect, self).save(arg0, arg1)

    @overload
    def rotate(self, arg0: 'Quaternion'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.rotate(com.badlogic.gdx.math.Quaternion)"""
        super(__ParticleEffect, self).rotate(arg0)

    @overload
    def rotate(self, arg0: 'Vector3', arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.rotate(com.badlogic.gdx.math.Vector3,float)"""
        super(__ParticleEffect, self).rotate(arg0, __float.valueOf(arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.end()"""
        super(ParticleEffect, self).end()

    @overload
    def draw(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.draw()"""
        super(ParticleEffect, self).draw()

    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.update()"""
        super(ParticleEffect, self).update()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleEffect()"""
        val = __ParticleEffect()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getBoundingBox(self) -> 'collision.BoundingBox':
        """public com.badlogic.gdx.math.collision.BoundingBox com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.getBoundingBox()"""
        return 'collision.BoundingBox'.__wrap(super(ParticleEffect, self).getBoundingBox())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.dispose()"""
        super(ParticleEffect, self).dispose()

    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffect.init()"""
        super(ParticleEffect, self).init()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleSorter$Distance
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.ParticleSorter as __ParticleSorter_Distance
__Distance = __ParticleSorter_Distance.Distance
import com.badlogic.gdx.graphics.g3d.particles.ParticleSorter as __ParticleSorter
__ParticleSorter = __ParticleSorter
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class Distance():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleSorter.Distance"""
 
    @staticmethod
    def __wrap(java_value: __Distance) -> 'Distance':
        return Distance(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Distance):
        """
        Dynamic initializer for Distance.
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
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSorter$Distance.ensureCapacity(int)"""
        super(__Distance, self).ensureCapacity(__int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def qsort(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSorter$Distance.qsort(int,int)"""
        super(__Distance, self).qsort(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def sort(self, arg0: 'Array') -> List[int]:
        """public <T extends com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderData> int[] com.badlogic.gdx.graphics.g3d.particles.ParticleSorter$Distance.sort(com.badlogic.gdx.utils.Array<T>)"""
        return List[int].__wrap(super(__Distance, self).sort(arg0))

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
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleSorter$Distance()"""
        val = __Distance()
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

    @override
    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleSorter.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(__ParticleSorter, self).setCamera(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleSorter$Distance()"""
        val = __Distance()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ResourceData
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.ResourceData as __ResourceData
__ResourceData = __ResourceData
import com.badlogic.gdx.graphics.g3d.particles.ResourceData as __ResourceData_SaveData
__SaveData = __ResourceData_SaveData.SaveData
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
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ResourceData():
    """com.badlogic.gdx.graphics.g3d.particles.ResourceData"""
 
    @staticmethod
    def __wrap(java_value: __ResourceData) -> 'ResourceData':
        return ResourceData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ResourceData):
        """
        Dynamic initializer for ResourceData.
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
    def getSaveData(self, arg0: str) -> 'SaveData':
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData com.badlogic.gdx.graphics.g3d.particles.ResourceData.getSaveData(java.lang.String)"""
        return 'SaveData'.__wrap(super(__ResourceData, self).getSaveData(arg0))

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ResourceData.write(com.badlogic.gdx.utils.Json)"""
        super(__ResourceData, self).write(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: object):
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData(T)"""
        val = __ResourceData(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData()"""
        val = __ResourceData()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def createSaveData(self, arg0: str) -> 'SaveData':
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData com.badlogic.gdx.graphics.g3d.particles.ResourceData.createSaveData(java.lang.String)"""
        return 'SaveData'.__wrap(super(__ResourceData, self).createSaveData(arg0))

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
    def getAssets(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.particles.ResourceData$AssetData> com.badlogic.gdx.graphics.g3d.particles.ResourceData.getAssets()"""
        return 'utils.Array'.__wrap(super(ResourceData, self).getAssets())

    @overload
    def createSaveData(self) -> 'SaveData':
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData com.badlogic.gdx.graphics.g3d.particles.ResourceData.createSaveData()"""
        return 'SaveData'.__wrap(super(ResourceData, self).createSaveData())

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
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData()"""
        val = __ResourceData()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getSaveData(self) -> 'SaveData':
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData$SaveData com.badlogic.gdx.graphics.g3d.particles.ResourceData.getSaveData()"""
        return 'SaveData'.__wrap(super(ResourceData, self).getSaveData())

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ResourceData.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__ResourceData, self).read(arg0, arg1)

    @overload
    def getAssetDescriptors(self) -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.graphics.g3d.particles.ResourceData.getAssetDescriptors()"""
        return 'utils.Array'.__wrap(super(ResourceData, self).getAssetDescriptors())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParallelArray$FloatChannel
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g3d.particles.ParallelArray as __ParallelArray_FloatChannel
__FloatChannel = __ParallelArray_FloatChannel.FloatChannel
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class FloatChannel():
    """com.badlogic.gdx.graphics.g3d.particles.ParallelArray.FloatChannel"""
 
    @staticmethod
    def __wrap(java_value: __FloatChannel) -> 'FloatChannel':
        return FloatChannel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FloatChannel):
        """
        Dynamic initializer for FloatChannel.
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
    def __init__(self, arg0: 'ParallelArray', arg1: int, arg2: int, arg3: int):
        """public com.badlogic.gdx.graphics.g3d.particles.ParallelArray$FloatChannel(com.badlogic.gdx.graphics.g3d.particles.ParallelArray,int,int,int)"""
        val = __FloatChannel(arg0, __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def swap(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParallelArray$FloatChannel.swap(int,int)"""
        super(__FloatChannel, self).swap(__int.valueOf(arg0), __int.valueOf(arg1))

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
    def setCapacity(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParallelArray$FloatChannel.setCapacity(int)"""
        super(__FloatChannel, self).setCapacity(__int.valueOf(arg0))

    @override
    @overload
    def add(self, arg0: int, *arg1: object):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParallelArray$FloatChannel.add(int,java.lang.Object...)"""
        super(__FloatChannel, self).add(__int.valueOf(arg0), arg1)

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleChannels
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
import com.badlogic.gdx.graphics.g3d.particles.ParticleChannels as __ParticleChannels
__ParticleChannels = __ParticleChannels
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ParticleChannels():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleChannels"""
 
    @staticmethod
    def __wrap(java_value: __ParticleChannels) -> 'ParticleChannels':
        return ParticleChannels(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleChannels):
        """
        Dynamic initializer for ParticleChannels.
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
    def newGlobalId() -> int:
        """public static int com.badlogic.gdx.graphics.g3d.particles.ParticleChannels.newGlobalId()"""
        return int.__wrap(__ParticleChannels.newGlobalId())

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
    def newId(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.ParticleChannels.newId()"""
        return int.__wrap(super(ParticleChannels, self).newId())

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleChannels()"""
        val = __ParticleChannels()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleChannels()"""
        val = __ParticleChannels()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ResourceData$AssetData
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
import com.badlogic.gdx.graphics.g3d.particles.ResourceData as __ResourceData_AssetData
__AssetData = __ResourceData_AssetData.AssetData
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AssetData():
    """com.badlogic.gdx.graphics.g3d.particles.ResourceData.AssetData"""
 
    @staticmethod
    def __wrap(java_value: __AssetData) -> 'AssetData':
        return AssetData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AssetData):
        """
        Dynamic initializer for AssetData.
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData$AssetData()"""
        val = __AssetData()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData$AssetData()"""
        val = __AssetData()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ResourceData$AssetData.write(com.badlogic.gdx.utils.Json)"""
        super(__AssetData, self).write(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: str, arg1: 'Class'):
        """public com.badlogic.gdx.graphics.g3d.particles.ResourceData$AssetData(java.lang.String,java.lang.Class<T>)"""
        val = __AssetData(arg0, arg1)
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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ResourceData$AssetData.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__AssetData, self).read(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.ParticleShader as __ParticleShader_Config
__Config = __ParticleShader_Config.Config
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Config():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleShader.Config"""
 
    @staticmethod
    def __wrap(java_value: __Config) -> 'Config':
        return Config(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Config):
        """
        Dynamic initializer for Config.
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
    def __init__(self, arg0: 'AlignMode'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config(com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode)"""
        val = __Config(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config()"""
        val = __Config()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: str):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config(java.lang.String,java.lang.String)"""
        val = __Config(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, arg0: 'AlignMode', arg1: 'ParticleType'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config(com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode,com.badlogic.gdx.graphics.g3d.particles.ParticleShader$ParticleType)"""
        val = __Config(arg0, arg1)
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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config()"""
        val = __Config()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'ParticleType'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config(com.badlogic.gdx.graphics.g3d.particles.ParticleShader$ParticleType)"""
        val = __Config(arg0)
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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$TextureRegionInitializer
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
import java.lang.Integer as __int
import com.badlogic.gdx.graphics.g3d.particles.ParticleChannels as __ParticleChannels_TextureRegionInitializer
__TextureRegionInitializer = __ParticleChannels_TextureRegionInitializer.TextureRegionInitializer
from builtins import bool
from builtins import int
 
class TextureRegionInitializer():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleChannels.TextureRegionInitializer"""
 
    @staticmethod
    def __wrap(java_value: __TextureRegionInitializer) -> 'TextureRegionInitializer':
        return TextureRegionInitializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TextureRegionInitializer):
        """
        Dynamic initializer for TextureRegionInitializer.
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$TextureRegionInitializer()"""
        val = __TextureRegionInitializer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$TextureRegionInitializer()"""
        val = __TextureRegionInitializer()
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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def get() -> 'TextureRegionInitializer':
        """public static com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$TextureRegionInitializer com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$TextureRegionInitializer.get()"""
        return TextureRegionInitializer.__wrap(__TextureRegionInitializer.get())

    @overload
    def init(self, arg0: 'FloatChannel'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleChannels$TextureRegionInitializer.init(com.badlogic.gdx.graphics.g3d.particles.ParallelArray$FloatChannel)"""
        super(__TextureRegionInitializer, self).init(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader
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
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader as __AsynchronousAssetLoader
__AsynchronousAssetLoader = __AsynchronousAssetLoader
try:
    from pygdx.assets import loaders
except ImportError:
    loaders = __import_once__("pygdx.assets.loaders")

import com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader as __ParticleEffectLoader
__ParticleEffectLoader = __ParticleEffectLoader
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
import com.badlogic.gdx.graphics.g3d.particles.ParticleEffect as __ParticleEffect
__ParticleEffect = __ParticleEffect
from builtins import bool
from builtins import int
 
class ParticleEffectLoader():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader"""
 
    @staticmethod
    def __wrap(java_value: __ParticleEffectLoader) -> 'ParticleEffectLoader':
        return ParticleEffectLoader(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleEffectLoader):
        """
        Dynamic initializer for ParticleEffectLoader.
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
    def save(self, arg0: 'ParticleEffect', arg1: 'ParticleEffectSaveParameter'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader.save(com.badlogic.gdx.graphics.g3d.particles.ParticleEffect,com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader$ParticleEffectSaveParameter) throws java.io.IOException"""
        super(__ParticleEffectLoader, self).save(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'FileHandleResolver'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader(com.badlogic.gdx.assets.loaders.FileHandleResolver)"""
        val = __ParticleEffectLoader(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getDependencies(self, arg0: str, arg1: 'FileHandle', arg2: 'ParticleEffectLoadParameter') -> 'utils.Array':
        """public com.badlogic.gdx.utils.Array<com.badlogic.gdx.assets.AssetDescriptor> com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader.getDependencies(java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader$ParticleEffectLoadParameter)"""
        return 'utils.Array'.__wrap(super(__ParticleEffectLoader, self).getDependencies(arg0, arg1, arg2))

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
    def loadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'ParticleEffectLoadParameter'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader.loadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader$ParticleEffectLoadParameter)"""
        super(__ParticleEffectLoader, self).loadAsync(arg0, arg1, arg2, arg3)

    @overload
    def loadSync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'ParticleEffectLoadParameter') -> 'ParticleEffect':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleEffect com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader.loadSync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader$ParticleEffectLoadParameter)"""
        return 'ParticleEffect'.__wrap(super(__ParticleEffectLoader, self).loadSync(arg0, arg1, arg2, arg3))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def unloadAsync(self, arg0: 'AssetManager', arg1: str, arg2: 'FileHandle', arg3: 'AssetLoaderParameters'):
        """public void com.badlogic.gdx.assets.loaders.AsynchronousAssetLoader.unloadAsync(com.badlogic.gdx.assets.AssetManager,java.lang.String,com.badlogic.gdx.files.FileHandle,P)"""
        super(__loaders.AsynchronousAssetLoader, self).unloadAsync(arg0, arg1, arg2, arg3)

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader$ParticleEffectLoadParameter
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
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader as __ParticleEffectLoader_ParticleEffectLoadParameter
__ParticleEffectLoadParameter = __ParticleEffectLoader_ParticleEffectLoadParameter.ParticleEffectLoadParameter
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ParticleEffectLoadParameter():
    """com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader.ParticleEffectLoadParameter"""
 
    @staticmethod
    def __wrap(java_value: __ParticleEffectLoadParameter) -> 'ParticleEffectLoadParameter':
        return ParticleEffectLoadParameter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleEffectLoadParameter):
        """
        Dynamic initializer for ParticleEffectLoadParameter.
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
    def __init__(self, arg0: 'Array'):
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleEffectLoader$ParticleEffectLoadParameter(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>>)"""
        val = __ParticleEffectLoadParameter(arg0)
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ChannelDescriptor
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.ParallelArray as __ParallelArray_ChannelDescriptor
__ChannelDescriptor = __ParallelArray_ChannelDescriptor.ChannelDescriptor
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ChannelDescriptor():
    """com.badlogic.gdx.graphics.g3d.particles.ParallelArray.ChannelDescriptor"""
 
    @staticmethod
    def __wrap(java_value: __ChannelDescriptor) -> 'ChannelDescriptor':
        return ChannelDescriptor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ChannelDescriptor):
        """
        Dynamic initializer for ChannelDescriptor.
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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: int, arg1: 'Class', arg2: int):
        """public com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ChannelDescriptor(int,java.lang.Class<?>,int)"""
        val = __ChannelDescriptor(__int.valueOf(arg0), arg1, __int.valueOf(arg2))
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.ParallelArray
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.ParallelArray as __ParallelArray
__ParallelArray = __ParallelArray
from builtins import object
import com.badlogic.gdx.graphics.g3d.particles.ParallelArray as __ParallelArray_Channel
__Channel = __ParallelArray_Channel.Channel
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
 
class ParallelArray():
    """com.badlogic.gdx.graphics.g3d.particles.ParallelArray"""
 
    @staticmethod
    def __wrap(java_value: __ParallelArray) -> 'ParallelArray':
        return ParallelArray(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParallelArray):
        """
        Dynamic initializer for ParallelArray.
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
    def addChannel(self, arg0: 'ChannelDescriptor') -> 'Channel':
        """public <T extends com.badlogic.gdx.graphics.g3d.particles.ParallelArray$Channel> T com.badlogic.gdx.graphics.g3d.particles.ParallelArray.addChannel(com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ChannelDescriptor)"""
        return 'Channel'.__wrap(super(__ParallelArray, self).addChannel(arg0))

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
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.particles.ParallelArray(int)"""
        val = __ParallelArray(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getChannel(self, arg0: 'ChannelDescriptor') -> 'Channel':
        """public <T extends com.badlogic.gdx.graphics.g3d.particles.ParallelArray$Channel> T com.badlogic.gdx.graphics.g3d.particles.ParallelArray.getChannel(com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ChannelDescriptor)"""
        return 'Channel'.__wrap(super(__ParallelArray, self).getChannel(arg0))

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
    def addElement(self, *arg0: object):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParallelArray.addElement(java.lang.Object...)"""
        super(__ParallelArray, self).addElement(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def addChannel(self, arg0: 'ChannelDescriptor', arg1: 'ChannelInitializer') -> 'Channel':
        """public <T extends com.badlogic.gdx.graphics.g3d.particles.ParallelArray$Channel> T com.badlogic.gdx.graphics.g3d.particles.ParallelArray.addChannel(com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ChannelDescriptor,com.badlogic.gdx.graphics.g3d.particles.ParallelArray$ChannelInitializer<T>)"""
        return 'Channel'.__wrap(super(__ParallelArray, self).addChannel(arg0, arg1))

    @overload
    def removeElement(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParallelArray.removeElement(int)"""
        super(__ParallelArray, self).removeElement(__int.valueOf(arg0))

    @overload
    def setCapacity(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParallelArray.setCapacity(int)"""
        super(__ParallelArray, self).setCapacity(__int.valueOf(arg0))

    @overload
    def removeArray(self, arg0: int):
        """public <T> void com.badlogic.gdx.graphics.g3d.particles.ParallelArray.removeArray(int)"""
        super(__ParallelArray, self).removeArray(__int.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))