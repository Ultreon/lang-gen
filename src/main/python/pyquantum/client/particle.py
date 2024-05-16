from __future__ import annotations
from overload import overload


 
import dev.ultreon.quantum.client.particle.ParticleEmitters as __ParticleEmitters
__ParticleEmitters = __ParticleEmitters
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
 
class ParticleEmitters():
    """dev.ultreon.quantum.client.particle.ParticleEmitters"""
 
    @staticmethod
    def __wrap(java_value: __ParticleEmitters) -> 'ParticleEmitters':
        return ParticleEmitters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleEmitters):
        """
        Dynamic initializer for ParticleEmitters.
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
        """public dev.ultreon.quantum.client.particle.ParticleEmitters()"""
        val = __ParticleEmitters()
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.particle.ParticleEmitters()"""
        val = __ParticleEmitters()
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

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.client.particle.ParticleEmitters.init()"""
            __ParticleEmitters.init()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.particle.ParticleEmitters
import dev.ultreon.quantum.client.particle.ParticleEmitters as __ParticleEmitters
__ParticleEmitters = __ParticleEmitters
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
 
class ParticleEmitters():
    """dev.ultreon.quantum.client.particle.ParticleEmitters"""
 
    @staticmethod
    def __wrap(java_value: __ParticleEmitters) -> 'ParticleEmitters':
        return ParticleEmitters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleEmitters):
        """
        Dynamic initializer for ParticleEmitters.
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
        """public dev.ultreon.quantum.client.particle.ParticleEmitters()"""
        val = __ParticleEmitters()
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.particle.ParticleEmitters()"""
        val = __ParticleEmitters()
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

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.client.particle.ParticleEmitters.init()"""
            __ParticleEmitters.init()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.client.particle.ParticleEmitters 
 
 
# CLASS: dev.ultreon.quantum.client.particle.ParticleControllers
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
import dev.ultreon.quantum.client.particle.ParticleControllers as __ParticleControllers
__ParticleControllers = __ParticleControllers
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ParticleControllers():
    """dev.ultreon.quantum.client.particle.ParticleControllers"""
 
    @staticmethod
    def __wrap(java_value: __ParticleControllers) -> 'ParticleControllers':
        return ParticleControllers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleControllers):
        """
        Dynamic initializer for ParticleControllers.
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
        """public dev.ultreon.quantum.client.particle.ParticleControllers()"""
        val = __ParticleControllers()
        self.__dict__ = val.__dict__
        self.__wrapper = val

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.client.particle.ParticleControllers.init()"""
            __ParticleControllers.init()

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
        """public dev.ultreon.quantum.client.particle.ParticleControllers()"""
        val = __ParticleControllers()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: dev.ultreon.quantum.client.particle.PFXPool
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
import java.lang.Object as __object
from builtins import type
from builtins import object
import java.lang.Long as __long
import dev.ultreon.quantum.client.particle.PFXPool as __PFXPool
__PFXPool = __PFXPool
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
 
class PFXPool(pygdx.__Pool, utils.Pool):
    """dev.ultreon.quantum.client.particle.PFXPool"""
 
    @staticmethod
    def __wrap(java_value: __PFXPool) -> 'PFXPool':
        return PFXPool(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PFXPool):
        """
        Dynamic initializer for PFXPool.
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
    def free(self, arg0: 'ParticleEffect'):
        """public void dev.ultreon.quantum.client.particle.PFXPool.free(com.badlogic.gdx.graphics.g3d.particles.ParticleEffect)"""
        super(__PFXPool, self).free(arg0)

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

    @overload
    def __init__(self, arg0: 'ParticleEffect'):
        """public dev.ultreon.quantum.client.particle.PFXPool(com.badlogic.gdx.graphics.g3d.particles.ParticleEffect)"""
        val = __PFXPool(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.client.particle.ClientParticle
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
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.particle.ClientParticle as __ClientParticle
__ClientParticle = __ClientParticle
import dev.ultreon.quantum.world.particles.ParticleType as __ParticleType
__ParticleType = __ParticleType
import java.lang.Long as __long
import dev.ultreon.quantum.client.particle.PFXPool as __PFXPool
__PFXPool = __PFXPool
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g3d.particles.ParticleController as __ParticleController
__ParticleController = __ParticleController
try:
    from pyquantum.world import particles
except ImportError:
    particles = __import_once__("pyquantum.world.particles")

import java.lang.Integer as __int
import com.badlogic.gdx.graphics.g3d.particles.ParticleEffect as __ParticleEffect
__ParticleEffect = __ParticleEffect
from builtins import bool
from builtins import int
 
class ClientParticle():
    """dev.ultreon.quantum.client.particle.ClientParticle"""
 
    @staticmethod
    def __wrap(java_value: __ClientParticle) -> 'ClientParticle':
        return ClientParticle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientParticle):
        """
        Dynamic initializer for ClientParticle.
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
    def getParticleController(self) -> 'particles.ParticleController':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleController dev.ultreon.quantum.client.particle.ClientParticle.getParticleController()"""
        return 'particles.ParticleController'.__wrap(super(ClientParticle, self).getParticleController())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'ParticleType'):
        """public dev.ultreon.quantum.client.particle.ClientParticle(dev.ultreon.quantum.world.particles.ParticleType)"""
        val = __ClientParticle(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getParticleEffect(self) -> 'particles.ParticleEffect':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleEffect dev.ultreon.quantum.client.particle.ClientParticle.getParticleEffect()"""
        return 'particles.ParticleEffect'.__wrap(super(ClientParticle, self).getParticleEffect())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getType(self) -> 'particles.ParticleType':
        """public dev.ultreon.quantum.world.particles.ParticleType dev.ultreon.quantum.client.particle.ClientParticle.getType()"""
        return 'particles.ParticleType'.__wrap(super(ClientParticle, self).getType())

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
    def getPool(self) -> 'PFXPool':
        """public dev.ultreon.quantum.client.particle.PFXPool dev.ultreon.quantum.client.particle.ClientParticle.getPool()"""
        return 'PFXPool'.__wrap(super(ClientParticle, self).getPool())

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
    def load(self, arg0: 'Array'):
        """public void dev.ultreon.quantum.client.particle.ClientParticle.load(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>>)"""
        super(__ClientParticle, self).load(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.particle.ClientParticleRegistry
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
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.client.particle.ClientParticle as __ClientParticle
__ClientParticle = __ClientParticle
import dev.ultreon.quantum.client.particle.ClientParticleRegistry as __ClientParticleRegistry
__ClientParticleRegistry = __ClientParticleRegistry
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g3d.particles.ParticleController as __ParticleController
__ParticleController = __ParticleController
try:
    from pyquantum.world import particles
except ImportError:
    particles = __import_once__("pyquantum.world.particles")

import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ClientParticleRegistry():
    """dev.ultreon.quantum.client.particle.ClientParticleRegistry"""
 
    @staticmethod
    def __wrap(java_value: __ClientParticleRegistry) -> 'ClientParticleRegistry':
        return ClientParticleRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClientParticleRegistry):
        """
        Dynamic initializer for ClientParticleRegistry.
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
    def getController(arg0: 'ParticleType') -> 'particles.ParticleController':
        """public static com.badlogic.gdx.graphics.g3d.particles.ParticleController dev.ultreon.quantum.client.particle.ClientParticleRegistry.getController(dev.ultreon.quantum.world.particles.ParticleType)"""
        return particles.ParticleController.__wrap(__ClientParticleRegistry.getController(arg0))

    @staticmethod
    @overload
    def registerController(arg0: 'ParticleType', arg1: 'ParticleController'):
        """public static void dev.ultreon.quantum.client.particle.ClientParticleRegistry.registerController(dev.ultreon.quantum.world.particles.ParticleType,com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        __ClientParticleRegistry.registerController(arg0, arg1)

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.particle.ClientParticleRegistry()"""
        val = __ClientParticleRegistry()
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

    @staticmethod
    @overload
    def getParticle(arg0: 'ParticleType') -> 'ClientParticle':
        """public static dev.ultreon.quantum.client.particle.ClientParticle dev.ultreon.quantum.client.particle.ClientParticleRegistry.getParticle(dev.ultreon.quantum.world.particles.ParticleType)"""
        return ClientParticle.__wrap(__ClientParticleRegistry.getParticle(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

        @staticmethod
        @overload
        def registerAll():
            """public static void dev.ultreon.quantum.client.particle.ClientParticleRegistry.registerAll()"""
            __ClientParticleRegistry.registerAll()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.particle.ClientParticleRegistry()"""
        val = __ClientParticleRegistry()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def loadAll(arg0: 'Array'):
        """public static void dev.ultreon.quantum.client.particle.ClientParticleRegistry.loadAll(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>>)"""
        __ClientParticleRegistry.loadAll(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.client.particle.ParticleControllerRenderers
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
import dev.ultreon.quantum.client.particle.ParticleControllerRenderers as __ParticleControllerRenderers
__ParticleControllerRenderers = __ParticleControllerRenderers
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ParticleControllerRenderers():
    """dev.ultreon.quantum.client.particle.ParticleControllerRenderers"""
 
    @staticmethod
    def __wrap(java_value: __ParticleControllerRenderers) -> 'ParticleControllerRenderers':
        return ParticleControllerRenderers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleControllerRenderers):
        """
        Dynamic initializer for ParticleControllerRenderers.
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
    def __init__(self):
        """public dev.ultreon.quantum.client.particle.ParticleControllerRenderers()"""
        val = __ParticleControllerRenderers()
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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.particle.ParticleControllerRenderers()"""
        val = __ParticleControllerRenderers()
        self.__dict__ = val.__dict__
        self.__wrapper = val

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.client.particle.ParticleControllerRenderers.init()"""
            __ParticleControllerRenderers.init()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))