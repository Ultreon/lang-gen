from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue as _RangedNumericValue
_RangedNumericValue = _RangedNumericValue
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
import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as _ParticleControllerComponent
_ParticleControllerComponent = _ParticleControllerComponent
from builtins import float
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter as _RegularEmitter
_RegularEmitter = _RegularEmitter
try:
    from pygdx.graphics.g3d.particles import values
except ImportError:
    values = _import_once("pygdx.graphics.g3d.particles.values")

import com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter as _RegularEmitter_EmissionMode
_EmissionMode = _RegularEmitter_EmissionMode.EmissionMode
import com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter as _Emitter
_Emitter = _Emitter
import com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue as _ScaledNumericValue
_ScaledNumericValue = _ScaledNumericValue
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RegularEmitter():
    """com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter"""
 
    @staticmethod
    def _wrap(java_value: _RegularEmitter) -> 'RegularEmitter':
        return RegularEmitter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RegularEmitter):
        """
        Dynamic initializer for RegularEmitter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RegularEmitter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RegularEmitter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getDelay(self) -> 'values.RangedNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getDelay()"""
        return 'values.RangedNumericValue'._wrap(super(RegularEmitter, self).getDelay())

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def copy(self) -> 'particles.ParticleControllerComponent':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.copy()"""
        return 'particles.ParticleControllerComponent'._wrap(super(RegularEmitter, self).copy())

    @overload
    def getLifeOffset(self) -> 'values.ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getLifeOffset()"""
        return 'values.ScaledNumericValue'._wrap(super(RegularEmitter, self).getLifeOffset())

    @overload
    def getDuration(self) -> 'values.RangedNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getDuration()"""
        return 'values.RangedNumericValue'._wrap(super(RegularEmitter, self).getDuration())

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
    def getEmission(self) -> 'values.ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getEmission()"""
        return 'values.ScaledNumericValue'._wrap(super(RegularEmitter, self).getEmission())

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.update()"""
        super(RegularEmitter, self).update()

    @overload
    def set(self, arg0: 'RegularEmitter'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.set(com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter)"""
        super(_RegularEmitter, self).set(arg0)

    @overload
    def getPercentComplete(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getPercentComplete()"""
        return float._wrap(super(RegularEmitter, self).getPercentComplete())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setEmissionMode(self, arg0: 'EmissionMode'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.setEmissionMode(com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter$EmissionMode)"""
        super(_RegularEmitter, self).setEmissionMode(arg0)

    @override
    @overload
    def setMinParticleCount(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.setMinParticleCount(int)"""
        super(_Emitter, self).setMinParticleCount(_int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter()"""
        val = _RegularEmitter()
        self.__wrapper = val

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.start()"""
        super(RegularEmitter, self).start()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(particles.ParticleControllerComponent, self).dispose()

    @override
    @overload
    def setParticleCount(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.setParticleCount(int,int)"""
        super(_Emitter, self).setParticleCount(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getMaxParticleCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.getMaxParticleCount()"""
        return int._wrap(super(Emitter, self).getMaxParticleCount())

    @overload
    def isContinuous(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.isContinuous()"""
        return bool._wrap(super(RegularEmitter, self).isContinuous())

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.end()"""
        super(Emitter, self).end()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.isComplete()"""
        return bool._wrap(super(RegularEmitter, self).isComplete())

    @override
    @overload
    def set(self, arg0: 'Emitter'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.set(com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter)"""
        super(_Emitter, self).set(arg0)

    @override
    @overload
    def setMaxParticleCount(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.setMaxParticleCount(int)"""
        super(_Emitter, self).setMaxParticleCount(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(_particles.ParticleControllerComponent, self).killParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getLife(self) -> 'values.ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getLife()"""
        return 'values.ScaledNumericValue'._wrap(super(RegularEmitter, self).getLife())

    @override
    @overload
    def getMinParticleCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.getMinParticleCount()"""
        return int._wrap(super(Emitter, self).getMinParticleCount())

    @overload
    def setContinuous(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.setContinuous(boolean)"""
        super(_RegularEmitter, self).setContinuous(_boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'RegularEmitter'):
        """public com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter(com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter)"""
        val = _RegularEmitter(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_RegularEmitter, self).read(arg0, arg1)

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.write(com.badlogic.gdx.utils.Json)"""
        super(_RegularEmitter, self).write(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter()"""
        val = _RegularEmitter()
        self.__wrapper = val

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.allocateChannels()"""
        super(RegularEmitter, self).allocateChannels()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def set(self, arg0: 'ParticleController'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(_particles.ParticleControllerComponent, self).set(arg0)

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.activateParticles(int,int)"""
        super(_RegularEmitter, self).activateParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_particles.ParticleControllerComponent, self).save(arg0, arg1)

    @overload
    def getEmissionMode(self) -> 'EmissionMode':
        """public com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter$EmissionMode com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getEmissionMode()"""
        return 'EmissionMode'._wrap(super(RegularEmitter, self).getEmissionMode())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue as _RangedNumericValue
_RangedNumericValue = _RangedNumericValue
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
import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as _ParticleControllerComponent
_ParticleControllerComponent = _ParticleControllerComponent
from builtins import float
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter as _RegularEmitter
_RegularEmitter = _RegularEmitter
try:
    from pygdx.graphics.g3d.particles import values
except ImportError:
    values = _import_once("pygdx.graphics.g3d.particles.values")

import com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter as _RegularEmitter_EmissionMode
_EmissionMode = _RegularEmitter_EmissionMode.EmissionMode
import com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter as _Emitter
_Emitter = _Emitter
import com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue as _ScaledNumericValue
_ScaledNumericValue = _ScaledNumericValue
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RegularEmitter():
    """com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter"""
 
    @staticmethod
    def _wrap(java_value: _RegularEmitter) -> 'RegularEmitter':
        return RegularEmitter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RegularEmitter):
        """
        Dynamic initializer for RegularEmitter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RegularEmitter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RegularEmitter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getDelay(self) -> 'values.RangedNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getDelay()"""
        return 'values.RangedNumericValue'._wrap(super(RegularEmitter, self).getDelay())

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def copy(self) -> 'particles.ParticleControllerComponent':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.copy()"""
        return 'particles.ParticleControllerComponent'._wrap(super(RegularEmitter, self).copy())

    @overload
    def getLifeOffset(self) -> 'values.ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getLifeOffset()"""
        return 'values.ScaledNumericValue'._wrap(super(RegularEmitter, self).getLifeOffset())

    @overload
    def getDuration(self) -> 'values.RangedNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.RangedNumericValue com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getDuration()"""
        return 'values.RangedNumericValue'._wrap(super(RegularEmitter, self).getDuration())

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
    def getEmission(self) -> 'values.ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getEmission()"""
        return 'values.ScaledNumericValue'._wrap(super(RegularEmitter, self).getEmission())

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.update()"""
        super(RegularEmitter, self).update()

    @overload
    def set(self, arg0: 'RegularEmitter'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.set(com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter)"""
        super(_RegularEmitter, self).set(arg0)

    @overload
    def getPercentComplete(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getPercentComplete()"""
        return float._wrap(super(RegularEmitter, self).getPercentComplete())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setEmissionMode(self, arg0: 'EmissionMode'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.setEmissionMode(com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter$EmissionMode)"""
        super(_RegularEmitter, self).setEmissionMode(arg0)

    @override
    @overload
    def setMinParticleCount(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.setMinParticleCount(int)"""
        super(_Emitter, self).setMinParticleCount(_int.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter()"""
        val = _RegularEmitter()
        self.__wrapper = val

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.start()"""
        super(RegularEmitter, self).start()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(particles.ParticleControllerComponent, self).dispose()

    @override
    @overload
    def setParticleCount(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.setParticleCount(int,int)"""
        super(_Emitter, self).setParticleCount(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getMaxParticleCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.getMaxParticleCount()"""
        return int._wrap(super(Emitter, self).getMaxParticleCount())

    @overload
    def isContinuous(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.isContinuous()"""
        return bool._wrap(super(RegularEmitter, self).isContinuous())

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.end()"""
        super(Emitter, self).end()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.isComplete()"""
        return bool._wrap(super(RegularEmitter, self).isComplete())

    @override
    @overload
    def set(self, arg0: 'Emitter'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.set(com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter)"""
        super(_Emitter, self).set(arg0)

    @override
    @overload
    def setMaxParticleCount(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.setMaxParticleCount(int)"""
        super(_Emitter, self).setMaxParticleCount(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(_particles.ParticleControllerComponent, self).killParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getLife(self) -> 'values.ScaledNumericValue':
        """public com.badlogic.gdx.graphics.g3d.particles.values.ScaledNumericValue com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getLife()"""
        return 'values.ScaledNumericValue'._wrap(super(RegularEmitter, self).getLife())

    @override
    @overload
    def getMinParticleCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.getMinParticleCount()"""
        return int._wrap(super(Emitter, self).getMinParticleCount())

    @overload
    def setContinuous(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.setContinuous(boolean)"""
        super(_RegularEmitter, self).setContinuous(_boolean.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'RegularEmitter'):
        """public com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter(com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter)"""
        val = _RegularEmitter(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_RegularEmitter, self).read(arg0, arg1)

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.write(com.badlogic.gdx.utils.Json)"""
        super(_RegularEmitter, self).write(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter()"""
        val = _RegularEmitter()
        self.__wrapper = val

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.allocateChannels()"""
        super(RegularEmitter, self).allocateChannels()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def set(self, arg0: 'ParticleController'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(_particles.ParticleControllerComponent, self).set(arg0)

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.activateParticles(int,int)"""
        super(_RegularEmitter, self).activateParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_particles.ParticleControllerComponent, self).save(arg0, arg1)

    @overload
    def getEmissionMode(self) -> 'EmissionMode':
        """public com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter$EmissionMode com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.getEmissionMode()"""
        return 'EmissionMode'._wrap(super(RegularEmitter, self).getEmissionMode())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter$EmissionMode
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter as _RegularEmitter_EmissionMode
_EmissionMode = _RegularEmitter_EmissionMode.EmissionMode
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
 
class EmissionMode():
    """com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter.EmissionMode"""
 
    @staticmethod
    def _wrap(java_value: _EmissionMode) -> 'EmissionMode':
        return EmissionMode(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EmissionMode):
        """
        Dynamic initializer for EmissionMode.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EmissionMode__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EmissionMode__wrapper":
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
    def values() -> List['EmissionMode']:
        """public static com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter$EmissionMode[] com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter$EmissionMode.values()"""
        return List[EmissionMode]._wrap(_EmissionMode.values())

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

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'EmissionMode':
        """public static com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter$EmissionMode com.badlogic.gdx.graphics.g3d.particles.emitters.RegularEmitter$EmissionMode.valueOf(java.lang.String)"""
        return EmissionMode._wrap(_EmissionMode.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter
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
import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as _ParticleControllerComponent
_ParticleControllerComponent = _ParticleControllerComponent
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter as _Emitter
_Emitter = _Emitter
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Emitter():
    """com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter"""
 
    @staticmethod
    def _wrap(java_value: _Emitter) -> 'Emitter':
        return Emitter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Emitter):
        """
        Dynamic initializer for Emitter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Emitter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Emitter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setMaxParticleCount(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.setMaxParticleCount(int)"""
        super(_Emitter, self).setMaxParticleCount(_int.valueOf(arg0))

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.allocateChannels()"""
        super(particles.ParticleControllerComponent, self).allocateChannels()

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter()"""
        val = _Emitter()
        self.__wrapper = val

    @overload
    def setMinParticleCount(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.setMinParticleCount(int)"""
        super(_Emitter, self).setMinParticleCount(_int.valueOf(arg0))

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.update()"""
        super(particles.ParticleControllerComponent, self).update()

    @overload
    def __init__(self, arg0: 'Emitter'):
        """public com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter(com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter)"""
        val = _Emitter(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.activateParticles(int,int)"""
        super(_particles.ParticleControllerComponent, self).activateParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(particles.ParticleControllerComponent, self).dispose()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.write(com.badlogic.gdx.utils.Json)"""
        super(_Emitter, self).write(arg0)

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_Emitter, self).read(arg0, arg1)

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
    def getMinParticleCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.getMinParticleCount()"""
        return int._wrap(super(Emitter, self).getMinParticleCount())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter()"""
        val = _Emitter()
        self.__wrapper = val

    @overload
    def setParticleCount(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.setParticleCount(int,int)"""
        super(_Emitter, self).setParticleCount(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.init()"""
        super(Emitter, self).init()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(_particles.ParticleControllerComponent, self).killParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getMaxParticleCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.getMaxParticleCount()"""
        return int._wrap(super(Emitter, self).getMaxParticleCount())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def isComplete(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.isComplete()"""
        return bool._wrap(super(Emitter, self).isComplete())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def set(self, arg0: 'ParticleController'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(_particles.ParticleControllerComponent, self).set(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self, arg0: 'Emitter'):
        """public void com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter.set(com.badlogic.gdx.graphics.g3d.particles.emitters.Emitter)"""
        super(_Emitter, self).set(arg0)

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_particles.ParticleControllerComponent, self).save(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())