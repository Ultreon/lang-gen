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
import com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter as __RegularEmitter_EmissionMode
__EmissionMode = __RegularEmitter_EmissionMode.EmissionMode
from builtins import float
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter as __RegularEmitter
__RegularEmitter = __RegularEmitter
import com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue as __RangedNumericValue
__RangedNumericValue = __RangedNumericValue
try:
    from pygdx.graphics.g3d.particles import values
except ImportError:
    values = __import_once__("pygdx.graphics.g3d.particles.values")

import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as __ParticleControllerComponent
__ParticleControllerComponent = __ParticleControllerComponent
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter as __Emitter
__Emitter = __Emitter
import java.lang.Integer as __int
import com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue as __ScaledNumericValue
__ScaledNumericValue = __ScaledNumericValue
from builtins import bool
from builtins import int
 
class RegularEmitter(__Emitter, Emitter, pygdx.__Json_Serializable, utils.Json$Serializable):
    """com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter"""
 
    @staticmethod
    def __wrap(java_value: __RegularEmitter) -> 'RegularEmitter':
        return RegularEmitter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RegularEmitter):
        """
        Dynamic initializer for RegularEmitter.
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
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__particles.ParticleControllerComponent, self).save(arg0, arg1)

    @overload
    def setContinuous(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.setContinuous(boolean)"""
        super(__RegularEmitter, self).setContinuous(__boolean.valueOf(arg0))

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__RegularEmitter, self).read(arg0, arg1)

    @override
    @overload
    def set(self, arg0: 'Emitter'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.set(com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter)"""
        super(__Emitter, self).set(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.init()"""
        super(RegularEmitter, self).init()

    @overload
    def getDuration(self) -> 'values.RangedNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getDuration()"""
        return 'values.RangedNumericValue'.__wrap(super(RegularEmitter, self).getDuration())

    @overload
    def getEmissionMode(self) -> 'EmissionMode':
        """public com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter$EmissionMode com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getEmissionMode()"""
        return 'EmissionMode'.__wrap(super(RegularEmitter, self).getEmissionMode())

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.update()"""
        super(RegularEmitter, self).update()

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(__particles.ParticleControllerComponent, self).killParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getDelay(self) -> 'values.RangedNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getDelay()"""
        return 'values.RangedNumericValue'.__wrap(super(RegularEmitter, self).getDelay())

    @override
    @overload
    def copy(self) -> 'particles.ParticleControllerComponent':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.copy()"""
        return 'particles.ParticleControllerComponent'.__wrap(super(RegularEmitter, self).copy())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.start()"""
        super(RegularEmitter, self).start()

    @override
    @overload
    def setMaxParticleCount(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.setMaxParticleCount(int)"""
        super(__Emitter, self).setMaxParticleCount(__int.valueOf(arg0))

    @override
    @overload
    def set(self, arg0: 'ParticleController'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(__particles.ParticleControllerComponent, self).set(arg0)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(particles.ParticleControllerComponent, self).dispose()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getLifeOffset(self) -> 'values.ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getLifeOffset()"""
        return 'values.ScaledNumericValue'.__wrap(super(RegularEmitter, self).getLifeOffset())

    @overload
    def getPercentComplete(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getPercentComplete()"""
        return float.__wrap(super(RegularEmitter, self).getPercentComplete())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter()"""
        val = __RegularEmitter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setMinParticleCount(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.setMinParticleCount(int)"""
        super(__Emitter, self).setMinParticleCount(__int.valueOf(arg0))

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.end()"""
        super(Emitter, self).end()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.write(com.badlogic.gdx.utils.Json)"""
        super(__RegularEmitter, self).write(arg0)

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.isComplete()"""
        return bool.__wrap(super(RegularEmitter, self).isComplete())

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.activateParticles(int,int)"""
        super(__RegularEmitter, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getMaxParticleCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.getMaxParticleCount()"""
        return int.__wrap(super(Emitter, self).getMaxParticleCount())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def set(self, arg0: 'RegularEmitter'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.set(com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter)"""
        super(__RegularEmitter, self).set(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter()"""
        val = __RegularEmitter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setEmissionMode(self, arg0: 'EmissionMode'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.setEmissionMode(com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter$EmissionMode)"""
        super(__RegularEmitter, self).setEmissionMode(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def isContinuous(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.isContinuous()"""
        return bool.__wrap(super(RegularEmitter, self).isContinuous())

    @override
    @overload
    def getMinParticleCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.getMinParticleCount()"""
        return int.__wrap(super(Emitter, self).getMinParticleCount())

    @overload
    def getLife(self) -> 'values.ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getLife()"""
        return 'values.ScaledNumericValue'.__wrap(super(RegularEmitter, self).getLife())

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.allocateChannels()"""
        super(RegularEmitter, self).allocateChannels()

    @override
    @overload
    def setParticleCount(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.setParticleCount(int,int)"""
        super(__Emitter, self).setParticleCount(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getEmission(self) -> 'values.ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getEmission()"""
        return 'values.ScaledNumericValue'.__wrap(super(RegularEmitter, self).getEmission())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'RegularEmitter'):
        """public com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter(com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter)"""
        val = __RegularEmitter(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter
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
import com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter as __RegularEmitter_EmissionMode
__EmissionMode = __RegularEmitter_EmissionMode.EmissionMode
from builtins import float
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter as __RegularEmitter
__RegularEmitter = __RegularEmitter
import com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue as __RangedNumericValue
__RangedNumericValue = __RangedNumericValue
try:
    from pygdx.graphics.g3d.particles import values
except ImportError:
    values = __import_once__("pygdx.graphics.g3d.particles.values")

import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as __ParticleControllerComponent
__ParticleControllerComponent = __ParticleControllerComponent
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter as __Emitter
__Emitter = __Emitter
import java.lang.Integer as __int
import com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue as __ScaledNumericValue
__ScaledNumericValue = __ScaledNumericValue
from builtins import bool
from builtins import int
 
class RegularEmitter(__Emitter, Emitter, pygdx.__Json_Serializable, utils.Json$Serializable):
    """com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter"""
 
    @staticmethod
    def __wrap(java_value: __RegularEmitter) -> 'RegularEmitter':
        return RegularEmitter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RegularEmitter):
        """
        Dynamic initializer for RegularEmitter.
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
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__particles.ParticleControllerComponent, self).save(arg0, arg1)

    @overload
    def setContinuous(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.setContinuous(boolean)"""
        super(__RegularEmitter, self).setContinuous(__boolean.valueOf(arg0))

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__RegularEmitter, self).read(arg0, arg1)

    @override
    @overload
    def set(self, arg0: 'Emitter'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.set(com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter)"""
        super(__Emitter, self).set(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.init()"""
        super(RegularEmitter, self).init()

    @overload
    def getDuration(self) -> 'values.RangedNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getDuration()"""
        return 'values.RangedNumericValue'.__wrap(super(RegularEmitter, self).getDuration())

    @overload
    def getEmissionMode(self) -> 'EmissionMode':
        """public com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter$EmissionMode com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getEmissionMode()"""
        return 'EmissionMode'.__wrap(super(RegularEmitter, self).getEmissionMode())

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.update()"""
        super(RegularEmitter, self).update()

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(__particles.ParticleControllerComponent, self).killParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getDelay(self) -> 'values.RangedNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getDelay()"""
        return 'values.RangedNumericValue'.__wrap(super(RegularEmitter, self).getDelay())

    @override
    @overload
    def copy(self) -> 'particles.ParticleControllerComponent':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.copy()"""
        return 'particles.ParticleControllerComponent'.__wrap(super(RegularEmitter, self).copy())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.start()"""
        super(RegularEmitter, self).start()

    @override
    @overload
    def setMaxParticleCount(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.setMaxParticleCount(int)"""
        super(__Emitter, self).setMaxParticleCount(__int.valueOf(arg0))

    @override
    @overload
    def set(self, arg0: 'ParticleController'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(__particles.ParticleControllerComponent, self).set(arg0)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(particles.ParticleControllerComponent, self).dispose()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getLifeOffset(self) -> 'values.ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getLifeOffset()"""
        return 'values.ScaledNumericValue'.__wrap(super(RegularEmitter, self).getLifeOffset())

    @overload
    def getPercentComplete(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getPercentComplete()"""
        return float.__wrap(super(RegularEmitter, self).getPercentComplete())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter()"""
        val = __RegularEmitter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def setMinParticleCount(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.setMinParticleCount(int)"""
        super(__Emitter, self).setMinParticleCount(__int.valueOf(arg0))

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.end()"""
        super(Emitter, self).end()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.write(com.badlogic.gdx.utils.Json)"""
        super(__RegularEmitter, self).write(arg0)

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.isComplete()"""
        return bool.__wrap(super(RegularEmitter, self).isComplete())

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.activateParticles(int,int)"""
        super(__RegularEmitter, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getMaxParticleCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.getMaxParticleCount()"""
        return int.__wrap(super(Emitter, self).getMaxParticleCount())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def set(self, arg0: 'RegularEmitter'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.set(com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter)"""
        super(__RegularEmitter, self).set(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter()"""
        val = __RegularEmitter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setEmissionMode(self, arg0: 'EmissionMode'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.setEmissionMode(com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter$EmissionMode)"""
        super(__RegularEmitter, self).setEmissionMode(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def isContinuous(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.isContinuous()"""
        return bool.__wrap(super(RegularEmitter, self).isContinuous())

    @override
    @overload
    def getMinParticleCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.getMinParticleCount()"""
        return int.__wrap(super(Emitter, self).getMinParticleCount())

    @overload
    def getLife(self) -> 'values.ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getLife()"""
        return 'values.ScaledNumericValue'.__wrap(super(RegularEmitter, self).getLife())

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.allocateChannels()"""
        super(RegularEmitter, self).allocateChannels()

    @override
    @overload
    def setParticleCount(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.setParticleCount(int,int)"""
        super(__Emitter, self).setParticleCount(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getEmission(self) -> 'values.ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getEmission()"""
        return 'values.ScaledNumericValue'.__wrap(super(RegularEmitter, self).getEmission())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'RegularEmitter'):
        """public com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter(com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter)"""
        val = __RegularEmitter(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter
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
import com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter as __Emitter
__Emitter = __Emitter
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Emitter(ABC, g3d.__ParticleControllerComponent, particles.ParticleControllerComponent, pygdx.__Json_Serializable, utils.Json$Serializable):
    """com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter"""
 
    @staticmethod
    def __wrap(java_value: __Emitter) -> 'Emitter':
        return Emitter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Emitter):
        """
        Dynamic initializer for Emitter.
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
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__particles.ParticleControllerComponent, self).save(arg0, arg1)

    @overload
    def setParticleCount(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.setParticleCount(int,int)"""
        super(__Emitter, self).setParticleCount(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.allocateChannels()"""
        super(particles.ParticleControllerComponent, self).allocateChannels()

    @overload
    def getMaxParticleCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.getMaxParticleCount()"""
        return int.__wrap(super(Emitter, self).getMaxParticleCount())

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.start()"""
        super(particles.ParticleControllerComponent, self).start()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.activateParticles(int,int)"""
        super(__particles.ParticleControllerComponent, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.isComplete()"""
        return bool.__wrap(super(Emitter, self).isComplete())

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.update()"""
        super(particles.ParticleControllerComponent, self).update()

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(__particles.ParticleControllerComponent, self).killParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.write(com.badlogic.gdx.utils.Json)"""
        super(__Emitter, self).write(arg0)

    @override
    @overload
    def set(self, arg0: 'ParticleController'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(__particles.ParticleControllerComponent, self).set(arg0)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(particles.ParticleControllerComponent, self).dispose()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def set(self, arg0: 'Emitter'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.set(com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter)"""
        super(__Emitter, self).set(arg0)

    @overload
    def setMinParticleCount(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.setMinParticleCount(int)"""
        super(__Emitter, self).setMinParticleCount(__int.valueOf(arg0))

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.copy()"""
        pass

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.end()"""
        super(Emitter, self).end()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter()"""
        val = __Emitter()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getMinParticleCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.getMinParticleCount()"""
        return int.__wrap(super(Emitter, self).getMinParticleCount())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.init()"""
        super(Emitter, self).init()

    @overload
    def setMaxParticleCount(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.setMaxParticleCount(int)"""
        super(__Emitter, self).setMaxParticleCount(__int.valueOf(arg0))

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__Emitter, self).read(arg0, arg1)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter()"""
        val = __Emitter()
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
    def __init__(self, arg0: 'Emitter'):
        """public com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter(com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter)"""
        val = __Emitter(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter$EmissionMode
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter as __RegularEmitter_EmissionMode
__EmissionMode = __RegularEmitter_EmissionMode.EmissionMode
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
 
class EmissionMode(__Enum, Enum):
    """com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.EmissionMode"""
 
    @staticmethod
    def __wrap(java_value: __EmissionMode) -> 'EmissionMode':
        return EmissionMode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EmissionMode):
        """
        Dynamic initializer for EmissionMode.
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
    def valueOf(arg0: str) -> 'EmissionMode':
        """public static com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter$EmissionMode com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter$EmissionMode.valueOf(java.lang.String)"""
        return EmissionMode.__wrap(__EmissionMode.valueOf(arg0))

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
    def values() -> List['EmissionMode']:
        """public static com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter$EmissionMode[] com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter$EmissionMode.values()"""
        return List[EmissionMode].__wrap(__EmissionMode.values())

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