from __future__ import annotations
from overload import overload


 
import dev.ultreon.quantum.client.particle.ParticleEmitters as _ParticleEmitters
_ParticleEmitters = _ParticleEmitters
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
 
class ParticleEmitters():
    """dev.ultreon.quantum.client.particle.ParticleEmitters"""
 
    @staticmethod
    def _wrap(java_value: _ParticleEmitters) -> 'ParticleEmitters':
        return ParticleEmitters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleEmitters):
        """
        Dynamic initializer for ParticleEmitters.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleEmitters__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleEmitters__wrapper":
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
        """public dev.ultreon.quantum.client.particle.ParticleEmitters()"""
        val = _ParticleEmitters()
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
        """public dev.ultreon.quantum.client.particle.ParticleEmitters()"""
        val = _ParticleEmitters()
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

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.client.particle.ParticleEmitters.init()"""
            _ParticleEmitters.init()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.particle.ParticleEmitters
import dev.ultreon.quantum.client.particle.ParticleEmitters as _ParticleEmitters
_ParticleEmitters = _ParticleEmitters
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
 
class ParticleEmitters():
    """dev.ultreon.quantum.client.particle.ParticleEmitters"""
 
    @staticmethod
    def _wrap(java_value: _ParticleEmitters) -> 'ParticleEmitters':
        return ParticleEmitters(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleEmitters):
        """
        Dynamic initializer for ParticleEmitters.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleEmitters__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleEmitters__wrapper":
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
        """public dev.ultreon.quantum.client.particle.ParticleEmitters()"""
        val = _ParticleEmitters()
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
        """public dev.ultreon.quantum.client.particle.ParticleEmitters()"""
        val = _ParticleEmitters()
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

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.client.particle.ParticleEmitters.init()"""
            _ParticleEmitters.init()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.particle.ParticleEmitters 
 
 
# CLASS: dev.ultreon.quantum.client.particle.ParticleControllers
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
import dev.ultreon.quantum.client.particle.ParticleControllers as _ParticleControllers
_ParticleControllers = _ParticleControllers
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParticleControllers():
    """dev.ultreon.quantum.client.particle.ParticleControllers"""
 
    @staticmethod
    def _wrap(java_value: _ParticleControllers) -> 'ParticleControllers':
        return ParticleControllers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleControllers):
        """
        Dynamic initializer for ParticleControllers.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleControllers__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleControllers__wrapper":
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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.particle.ParticleControllers()"""
        val = _ParticleControllers()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.client.particle.ParticleControllers.init()"""
            _ParticleControllers.init()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.client.particle.ParticleControllers()"""
        val = _ParticleControllers()
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
 
 
# CLASS: dev.ultreon.quantum.client.particle.PFXPool
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.particle.PFXPool as _PFXPool
_PFXPool = _PFXPool
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
import com.badlogic.gdx.utils.Pool as _Pool
_Pool = _Pool
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PFXPool():
    """dev.ultreon.quantum.client.particle.PFXPool"""
 
    @staticmethod
    def _wrap(java_value: _PFXPool) -> 'PFXPool':
        return PFXPool(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PFXPool):
        """
        Dynamic initializer for PFXPool.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PFXPool__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PFXPool__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'ParticleEffect'):
        """public dev.ultreon.quantum.client.particle.PFXPool(com.badlogic.gdx.graphics.g3d.particles.ParticleEffect)"""
        val = _PFXPool(arg0)
        self.__wrapper = val

    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.utils.Pool.clear()"""
        super(utils.Pool, self).clear()

    @override
    @overload
    def getFree(self) -> int:
        """public int com.badlogic.gdx.utils.Pool.getFree()"""
        return int._wrap(super(utils.Pool, self).getFree())

    @overload
    def free(self, arg0: 'ParticleEffect'):
        """public void dev.ultreon.quantum.client.particle.PFXPool.free(com.badlogic.gdx.graphics.g3d.particles.ParticleEffect)"""
        super(_PFXPool, self).free(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def fill(self, arg0: int):
        """public void com.badlogic.gdx.utils.Pool.fill(int)"""
        super(_utils.Pool, self).fill(_int.valueOf(arg0))

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

    @override
    @overload
    def obtain(self) -> object:
        """public T com.badlogic.gdx.utils.Pool.obtain()"""
        return object._wrap(super(utils.Pool, self).obtain())

    @override
    @overload
    def freeAll(self, arg0: 'Array'):
        """public void com.badlogic.gdx.utils.Pool.freeAll(com.badlogic.gdx.utils.Array<T>)"""
        super(_utils.Pool, self).freeAll(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.client.particle.ClientParticle
from pyquantum_helper import import_once as _import_once
import dev.ultreon.quantum.client.particle.PFXPool as _PFXPool
_PFXPool = _PFXPool
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
import dev.ultreon.quantum.world.particles.ParticleType as _ParticleType
_ParticleType = _ParticleType
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.particles.ParticleController as _ParticleController
_ParticleController = _ParticleController
import dev.ultreon.quantum.client.particle.ClientParticle as _ClientParticle
_ClientParticle = _ClientParticle
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.ParticleEffect as _ParticleEffect
_ParticleEffect = _ParticleEffect
try:
    from pyquantum.world import particles
except ImportError:
    particles = _import_once("pyquantum.world.particles")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ClientParticle():
    """dev.ultreon.quantum.client.particle.ClientParticle"""
 
    @staticmethod
    def _wrap(java_value: _ClientParticle) -> 'ClientParticle':
        return ClientParticle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClientParticle):
        """
        Dynamic initializer for ClientParticle.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClientParticle__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClientParticle__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def load(self, arg0: 'Array'):
        """public void dev.ultreon.quantum.client.particle.ClientParticle.load(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>>)"""
        super(_ClientParticle, self).load(arg0)

    @overload
    def getParticleEffect(self) -> 'particles.ParticleEffect':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleEffect dev.ultreon.quantum.client.particle.ClientParticle.getParticleEffect()"""
        return 'particles.ParticleEffect'._wrap(super(ClientParticle, self).getParticleEffect())

    @overload
    def __init__(self, arg0: 'ParticleType'):
        """public dev.ultreon.quantum.client.particle.ClientParticle(dev.ultreon.quantum.world.particles.ParticleType)"""
        val = _ClientParticle(arg0)
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
    def getPool(self) -> 'PFXPool':
        """public dev.ultreon.quantum.client.particle.PFXPool dev.ultreon.quantum.client.particle.ClientParticle.getPool()"""
        return 'PFXPool'._wrap(super(ClientParticle, self).getPool())

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
    def getType(self) -> 'particles.ParticleType':
        """public dev.ultreon.quantum.world.particles.ParticleType dev.ultreon.quantum.client.particle.ClientParticle.getType()"""
        return 'particles.ParticleType'._wrap(super(ClientParticle, self).getType())

    @overload
    def getParticleController(self) -> 'particles.ParticleController':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleController dev.ultreon.quantum.client.particle.ClientParticle.getParticleController()"""
        return 'particles.ParticleController'._wrap(super(ClientParticle, self).getParticleController())

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
 
 
# CLASS: dev.ultreon.quantum.client.particle.ClientParticleRegistry
from pyquantum_helper import import_once as _import_once
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
import dev.ultreon.quantum.client.particle.ClientParticleRegistry as _ClientParticleRegistry
_ClientParticleRegistry = _ClientParticleRegistry
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.particles.ParticleController as _ParticleController
_ParticleController = _ParticleController
import dev.ultreon.quantum.client.particle.ClientParticle as _ClientParticle
_ClientParticle = _ClientParticle
import java.lang.Integer as _int
try:
    from pyquantum.world import particles
except ImportError:
    particles = _import_once("pyquantum.world.particles")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ClientParticleRegistry():
    """dev.ultreon.quantum.client.particle.ClientParticleRegistry"""
 
    @staticmethod
    def _wrap(java_value: _ClientParticleRegistry) -> 'ClientParticleRegistry':
        return ClientParticleRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClientParticleRegistry):
        """
        Dynamic initializer for ClientParticleRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClientParticleRegistry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClientParticleRegistry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public dev.ultreon.quantum.client.particle.ClientParticleRegistry()"""
        val = _ClientParticleRegistry()
        self.__wrapper = val

    @staticmethod
    @overload
    def getController(arg0: 'ParticleType') -> 'particles.ParticleController':
        """public static com.badlogic.gdx.graphics.g3d.particles.ParticleController dev.ultreon.quantum.client.particle.ClientParticleRegistry.getController(dev.ultreon.quantum.world.particles.ParticleType)"""
        return particles.ParticleController._wrap(_ClientParticleRegistry.getController(arg0))

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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.particle.ClientParticleRegistry()"""
        val = _ClientParticleRegistry()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getParticle(arg0: 'ParticleType') -> 'ClientParticle':
        """public static dev.ultreon.quantum.client.particle.ClientParticle dev.ultreon.quantum.client.particle.ClientParticleRegistry.getParticle(dev.ultreon.quantum.world.particles.ParticleType)"""
        return ClientParticle._wrap(_ClientParticleRegistry.getParticle(arg0))

        @staticmethod
        @overload
        def registerAll():
            """public static void dev.ultreon.quantum.client.particle.ClientParticleRegistry.registerAll()"""
            _ClientParticleRegistry.registerAll()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def registerController(arg0: 'ParticleType', arg1: 'ParticleController'):
        """public static void dev.ultreon.quantum.client.particle.ClientParticleRegistry.registerController(dev.ultreon.quantum.world.particles.ParticleType,com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        _ClientParticleRegistry.registerController(arg0, arg1)

    @staticmethod
    @overload
    def loadAll(arg0: 'Array'):
        """public static void dev.ultreon.quantum.client.particle.ClientParticleRegistry.loadAll(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>>)"""
        _ClientParticleRegistry.loadAll(arg0)

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
 
 
# CLASS: dev.ultreon.quantum.client.particle.ParticleControllerRenderers
from builtins import str
import dev.ultreon.quantum.client.particle.ParticleControllerRenderers as _ParticleControllerRenderers
_ParticleControllerRenderers = _ParticleControllerRenderers
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
 
class ParticleControllerRenderers():
    """dev.ultreon.quantum.client.particle.ParticleControllerRenderers"""
 
    @staticmethod
    def _wrap(java_value: _ParticleControllerRenderers) -> 'ParticleControllerRenderers':
        return ParticleControllerRenderers(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleControllerRenderers):
        """
        Dynamic initializer for ParticleControllerRenderers.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleControllerRenderers__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleControllerRenderers__wrapper":
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
    def __init__(self, ):
        """public dev.ultreon.quantum.client.particle.ParticleControllerRenderers()"""
        val = _ParticleControllerRenderers()
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
    def __init__(self):
        """public dev.ultreon.quantum.client.particle.ParticleControllerRenderers()"""
        val = _ParticleControllerRenderers()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.client.particle.ParticleControllerRenderers.init()"""
            _ParticleControllerRenderers.init()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())