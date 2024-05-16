from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
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
import com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer as _ParticleControllerInfluencer_Single
_Single = _ParticleControllerInfluencer_Single.Single
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as _ParticleControllerComponent
_ParticleControllerComponent = _ParticleControllerComponent
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer as _ParticleControllerInfluencer
_ParticleControllerInfluencer = _ParticleControllerInfluencer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Single():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.Single"""
 
    @staticmethod
    def _wrap(java_value: _Single) -> 'Single':
        return Single(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Single):
        """
        Dynamic initializer for Single.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Single__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Single__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.update()"""
        super(particles.ParticleControllerComponent, self).update()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(_particles.ParticleControllerComponent, self).write(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single.activateParticles(int,int)"""
        super(_Single, self).activateParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single.killParticles(int,int)"""
        super(_Single, self).killParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single.init()"""
        super(Single, self).init()

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_ParticleControllerInfluencer, self).load(arg0, arg1)

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single()"""
        val = _Single()
        self.__wrapper = val

    @override
    @overload
    def copy(self) -> 'Single':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single.copy()"""
        return 'Single'._wrap(super(Single, self).copy())

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.end()"""
        super(ParticleControllerInfluencer, self).end()

    @overload
    def __init__(self, arg0: 'Single'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single(com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single)"""
        val = _Single(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single()"""
        val = _Single()
        self.__wrapper = val

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
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_particles.ParticleControllerComponent, self).read(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, *arg0: 'particles.ParticleController'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single(com.badlogic.gdx.graphics.g3d.particles.ParticleController...)"""
        val = _Single(arg0)
        self.__wrapper = val

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_ParticleControllerInfluencer, self).save(arg0, arg1)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.dispose()"""
        super(ParticleControllerInfluencer, self).dispose()

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.allocateChannels()"""
        super(ParticleControllerInfluencer, self).allocateChannels()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single
from pyquantum_helper import import_once as _import_once
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
import com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer as _ParticleControllerInfluencer_Single
_Single = _ParticleControllerInfluencer_Single.Single
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as _ParticleControllerComponent
_ParticleControllerComponent = _ParticleControllerComponent
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer as _ParticleControllerInfluencer
_ParticleControllerInfluencer = _ParticleControllerInfluencer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Single():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.Single"""
 
    @staticmethod
    def _wrap(java_value: _Single) -> 'Single':
        return Single(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Single):
        """
        Dynamic initializer for Single.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Single__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Single__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.update()"""
        super(particles.ParticleControllerComponent, self).update()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(_particles.ParticleControllerComponent, self).write(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single.activateParticles(int,int)"""
        super(_Single, self).activateParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single.killParticles(int,int)"""
        super(_Single, self).killParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single.init()"""
        super(Single, self).init()

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_ParticleControllerInfluencer, self).load(arg0, arg1)

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single()"""
        val = _Single()
        self.__wrapper = val

    @override
    @overload
    def copy(self) -> 'Single':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single.copy()"""
        return 'Single'._wrap(super(Single, self).copy())

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.end()"""
        super(ParticleControllerInfluencer, self).end()

    @overload
    def __init__(self, arg0: 'Single'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single(com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single)"""
        val = _Single(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single()"""
        val = _Single()
        self.__wrapper = val

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
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_particles.ParticleControllerComponent, self).read(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, *arg0: 'particles.ParticleController'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single(com.badlogic.gdx.graphics.g3d.particles.ParticleController...)"""
        val = _Single(arg0)
        self.__wrapper = val

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_ParticleControllerInfluencer, self).save(arg0, arg1)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.dispose()"""
        super(ParticleControllerInfluencer, self).dispose()

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.allocateChannels()"""
        super(ParticleControllerInfluencer, self).allocateChannels()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer
from pyquantum_helper import import_once as _import_once
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
import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as _ParticleControllerComponent
_ParticleControllerComponent = _ParticleControllerComponent
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
try:
    from pygdx.graphics.g3d.particles import values
except ImportError:
    values = _import_once("pygdx.graphics.g3d.particles.values")

import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer as _SpawnInfluencer
_SpawnInfluencer = _SpawnInfluencer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SpawnInfluencer():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer"""
 
    @staticmethod
    def _wrap(java_value: _SpawnInfluencer) -> 'SpawnInfluencer':
        return SpawnInfluencer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SpawnInfluencer):
        """
        Dynamic initializer for SpawnInfluencer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SpawnInfluencer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SpawnInfluencer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer.start()"""
        super(SpawnInfluencer, self).start()

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_SpawnInfluencer, self).read(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.update()"""
        super(particles.ParticleControllerComponent, self).update()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer.init()"""
        super(SpawnInfluencer, self).init()

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_SpawnInfluencer, self).save(arg0, arg1)

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

    @overload
    def __init__(self, arg0: 'SpawnInfluencer'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer(com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer)"""
        val = _SpawnInfluencer(arg0)
        self.__wrapper = val

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_SpawnInfluencer, self).load(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def copy(self) -> 'SpawnInfluencer':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer.copy()"""
        return 'SpawnInfluencer'._wrap(super(SpawnInfluencer, self).copy())

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer.allocateChannels()"""
        super(SpawnInfluencer, self).allocateChannels()

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

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer.write(com.badlogic.gdx.utils.Json)"""
        super(_SpawnInfluencer, self).write(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer.activateParticles(int,int)"""
        super(_SpawnInfluencer, self).activateParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer()"""
        val = _SpawnInfluencer()
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer()"""
        val = _SpawnInfluencer()
        self.__wrapper = val

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
    def __init__(self, arg0: 'SpawnShapeValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer(com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue)"""
        val = _SpawnInfluencer(arg0)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Single
from pyquantum_helper import import_once as _import_once
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
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer as _RegionInfluencer_Single
_Single = _RegionInfluencer_Single.Single
import com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer as _RegionInfluencer
_RegionInfluencer = _RegionInfluencer
import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as _ParticleControllerComponent
_ParticleControllerComponent = _ParticleControllerComponent
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Single():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.Single"""
 
    @staticmethod
    def _wrap(java_value: _Single) -> 'Single':
        return Single(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Single):
        """
        Dynamic initializer for Single.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Single__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Single__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.clear()"""
        super(RegionInfluencer, self).clear()

    @overload
    def __init__(self, arg0: 'TextureRegion'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Single(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = _Single(arg0)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Single()"""
        val = _Single()
        self.__wrapper = val

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_RegionInfluencer, self).load(arg0, arg1)

    @overload
    def __init__(self, arg0: 'Texture'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Single(com.badlogic.gdx.graphics.Texture)"""
        val = _Single(arg0)
        self.__wrapper = val

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_RegionInfluencer, self).read(arg0, arg1)

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.allocateChannels()"""
        super(RegionInfluencer, self).allocateChannels()

    @override
    @overload
    def setAtlasName(self, arg0: str):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.setAtlasName(java.lang.String)"""
        super(_RegionInfluencer, self).setAtlasName(arg0)

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
    def __init__(self, arg0: 'Single'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Single(com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Single)"""
        val = _Single(arg0)
        self.__wrapper = val

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.update()"""
        super(particles.ParticleControllerComponent, self).update()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.write(com.badlogic.gdx.utils.Json)"""
        super(_RegionInfluencer, self).write(arg0)

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
    def add(self, *arg0: 'g2d.TextureRegion'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.add(com.badlogic.gdx.graphics.g2d.TextureRegion...)"""
        super(_RegionInfluencer, self).add(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def copy(self) -> 'Single':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Single com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Single.copy()"""
        return 'Single'._wrap(super(Single, self).copy())

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Single()"""
        val = _Single()
        self.__wrapper = val

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_RegionInfluencer, self).save(arg0, arg1)

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
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Single.init()"""
        super(Single, self).init()

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Single
from pyquantum_helper import import_once as _import_once
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
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as _ParticleControllerComponent
_ParticleControllerComponent = _ParticleControllerComponent
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer as _ModelInfluencer
_ModelInfluencer = _ModelInfluencer
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer as _ModelInfluencer_Single
_Single = _ModelInfluencer_Single.Single
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Single():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer.Single"""
 
    @staticmethod
    def _wrap(java_value: _Single) -> 'Single':
        return Single(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Single):
        """
        Dynamic initializer for Single.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Single__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Single__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_ModelInfluencer, self).save(arg0, arg1)

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
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.update()"""
        super(particles.ParticleControllerComponent, self).update()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(_particles.ParticleControllerComponent, self).write(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Single()"""
        val = _Single()
        self.__wrapper = val

    @override
    @overload
    def copy(self) -> 'Single':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Single com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Single.copy()"""
        return 'Single'._wrap(super(Single, self).copy())

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

    @overload
    def __init__(self, arg0: 'Single'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Single(com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Single)"""
        val = _Single(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, *arg0: 'g3d.Model'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Single(com.badlogic.gdx.graphics.g3d.Model...)"""
        val = _Single(arg0)
        self.__wrapper = val

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer.allocateChannels()"""
        super(ModelInfluencer, self).allocateChannels()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Single()"""
        val = _Single()
        self.__wrapper = val

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Single.init()"""
        super(Single, self).init()

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_ModelInfluencer, self).load(arg0, arg1)

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
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_particles.ParticleControllerComponent, self).read(arg0, arg1)

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer
from pyquantum_helper import import_once as _import_once
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
import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as _ParticleControllerComponent
_ParticleControllerComponent = _ParticleControllerComponent
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer as _Influencer
_Influencer = _Influencer
from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Influencer():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer"""
 
    @staticmethod
    def _wrap(java_value: _Influencer) -> 'Influencer':
        return Influencer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Influencer):
        """
        Dynamic initializer for Influencer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Influencer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Influencer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

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

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.update()"""
        super(particles.ParticleControllerComponent, self).update()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(_particles.ParticleControllerComponent, self).write(arg0)

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

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.copy()"""
        pass

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
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(_particles.ParticleControllerComponent, self).killParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer()"""
        val = _Influencer()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer()"""
        val = _Influencer()
        self.__wrapper = val

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
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_particles.ParticleControllerComponent, self).read(arg0, arg1)

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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength
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
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as _DynamicsModifier_Strength
_Strength = _DynamicsModifier_Strength.Strength
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Strength():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.Strength"""
 
    @staticmethod
    def _wrap(java_value: _Strength) -> 'Strength':
        return Strength(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Strength):
        """
        Dynamic initializer for Strength.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Strength__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Strength__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength()"""
        val = _Strength()
        self.__wrapper = val

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.write(com.badlogic.gdx.utils.Json)"""
        super(_Strength, self).write(arg0)

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
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength()"""
        val = _Strength()
        self.__wrapper = val

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.update()"""
        super(particles.ParticleControllerComponent, self).update()

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
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(particles.ParticleControllerComponent, self).dispose()

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.copy()"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.allocateChannels()"""
        super(Strength, self).allocateChannels()

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.activateParticles(int,int)"""
        super(_Strength, self).activateParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Strength'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength(com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength)"""
        val = _Strength(arg0)
        self.__wrapper = val

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_Strength, self).read(arg0, arg1)

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational2D
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as _DynamicsModifier_Rotational2D
_Rotational2D = _DynamicsModifier_Rotational2D.Rotational2D
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

import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as _DynamicsModifier_Strength
_Strength = _DynamicsModifier_Strength.Strength
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Rotational2D():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.Rotational2D"""
 
    @staticmethod
    def _wrap(java_value: _Rotational2D) -> 'Rotational2D':
        return Rotational2D(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Rotational2D):
        """
        Dynamic initializer for Rotational2D.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Rotational2D__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Rotational2D__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.write(com.badlogic.gdx.utils.Json)"""
        super(_Strength, self).write(arg0)

    @override
    @overload
    def copy(self) -> 'Rotational2D':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational2D com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational2D.copy()"""
        return 'Rotational2D'._wrap(super(Rotational2D, self).copy())

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
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

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
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(particles.ParticleControllerComponent, self).dispose()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational2D()"""
        val = _Rotational2D()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Rotational2D'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational2D(com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational2D)"""
        val = _Rotational2D(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational2D()"""
        val = _Rotational2D()
        self.__wrapper = val

    @override
    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(_particles.ParticleControllerComponent, self).killParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational2D.update()"""
        super(Rotational2D, self).update()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.activateParticles(int,int)"""
        super(_Strength, self).activateParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational2D.allocateChannels()"""
        super(Rotational2D, self).allocateChannels()

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_Strength, self).read(arg0, arg1)

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer
from pyquantum_helper import import_once as _import_once
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
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer as _RegionInfluencer
_RegionInfluencer = _RegionInfluencer
import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as _ParticleControllerComponent
_ParticleControllerComponent = _ParticleControllerComponent
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

from abc import abstractmethod, ABC
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RegionInfluencer():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer"""
 
    @staticmethod
    def _wrap(java_value: _RegionInfluencer) -> 'RegionInfluencer':
        return RegionInfluencer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RegionInfluencer):
        """
        Dynamic initializer for RegionInfluencer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RegionInfluencer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RegionInfluencer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def clear(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.clear()"""
        super(RegionInfluencer, self).clear()

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_RegionInfluencer, self).load(arg0, arg1)

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_RegionInfluencer, self).read(arg0, arg1)

    @overload
    def __init__(self, arg0: 'RegionInfluencer'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer(com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer)"""
        val = _RegionInfluencer(arg0)
        self.__wrapper = val

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.allocateChannels()"""
        super(RegionInfluencer, self).allocateChannels()

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
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.update()"""
        super(particles.ParticleControllerComponent, self).update()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.write(com.badlogic.gdx.utils.Json)"""
        super(_RegionInfluencer, self).write(arg0)

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer()"""
        val = _RegionInfluencer()
        self.__wrapper = val

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.copy()"""
        pass

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer()"""
        val = _RegionInfluencer()
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
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(_particles.ParticleControllerComponent, self).killParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Texture'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer(com.badlogic.gdx.graphics.Texture)"""
        val = _RegionInfluencer(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer(int)"""
        val = _RegionInfluencer(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def add(self, *arg0: 'g2d.TextureRegion'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.add(com.badlogic.gdx.graphics.g2d.TextureRegion...)"""
        super(_RegionInfluencer, self).add(arg0)

    @overload
    def __init__(self, *arg0: 'g2d.TextureRegion'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer(com.badlogic.gdx.graphics.g2d.TextureRegion...)"""
        val = _RegionInfluencer(arg0)
        self.__wrapper = val

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_RegionInfluencer, self).save(arg0, arg1)

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

    @overload
    def setAtlasName(self, arg0: str):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.setAtlasName(java.lang.String)"""
        super(_RegionInfluencer, self).setAtlasName(arg0)

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Random
from pyquantum_helper import import_once as _import_once
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
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer as _RegionInfluencer
_RegionInfluencer = _RegionInfluencer
import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as _ParticleControllerComponent
_ParticleControllerComponent = _ParticleControllerComponent
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer as _RegionInfluencer_Random
_Random = _RegionInfluencer_Random.Random
import java.lang.Integer as _int
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Random():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.Random"""
 
    @staticmethod
    def _wrap(java_value: _Random) -> 'Random':
        return Random(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Random):
        """
        Dynamic initializer for Random.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Random__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Random__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.clear()"""
        super(RegionInfluencer, self).clear()

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_RegionInfluencer, self).load(arg0, arg1)

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @overload
    def __init__(self, arg0: 'Random'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Random(com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Random)"""
        val = _Random(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Random()"""
        val = _Random()
        self.__wrapper = val

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_RegionInfluencer, self).read(arg0, arg1)

    @overload
    def __init__(self, arg0: 'TextureRegion'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Random(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = _Random(arg0)
        self.__wrapper = val

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.allocateChannels()"""
        super(RegionInfluencer, self).allocateChannels()

    @override
    @overload
    def setAtlasName(self, arg0: str):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.setAtlasName(java.lang.String)"""
        super(_RegionInfluencer, self).setAtlasName(arg0)

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
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Random.activateParticles(int,int)"""
        super(_Random, self).activateParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.update()"""
        super(particles.ParticleControllerComponent, self).update()

    @overload
    def __init__(self, arg0: 'Texture'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Random(com.badlogic.gdx.graphics.Texture)"""
        val = _Random(arg0)
        self.__wrapper = val

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.write(com.badlogic.gdx.utils.Json)"""
        super(_RegionInfluencer, self).write(arg0)

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
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(particles.ParticleControllerComponent, self).dispose()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Random()"""
        val = _Random()
        self.__wrapper = val

    @override
    @overload
    def add(self, *arg0: 'g2d.TextureRegion'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.add(com.badlogic.gdx.graphics.g2d.TextureRegion...)"""
        super(_RegionInfluencer, self).add(arg0)

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
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(_particles.ParticleControllerComponent, self).killParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def copy(self) -> 'Random':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Random com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Random.copy()"""
        return 'Random'._wrap(super(Random, self).copy())

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_RegionInfluencer, self).save(arg0, arg1)

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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$TangentialAcceleration
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as _DynamicsModifier_TangentialAcceleration
_TangentialAcceleration = _DynamicsModifier_TangentialAcceleration.TangentialAcceleration
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

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as _DynamicsModifier_Angular
_Angular = _DynamicsModifier_Angular.Angular
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TangentialAcceleration():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.TangentialAcceleration"""
 
    @staticmethod
    def _wrap(java_value: _TangentialAcceleration) -> 'TangentialAcceleration':
        return TangentialAcceleration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TangentialAcceleration):
        """
        Dynamic initializer for TangentialAcceleration.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TangentialAcceleration__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TangentialAcceleration__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.activateParticles(int,int)"""
        super(_Angular, self).activateParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$TangentialAcceleration()"""
        val = _TangentialAcceleration()
        self.__wrapper = val

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$TangentialAcceleration.update()"""
        super(TangentialAcceleration, self).update()

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
    def __init__(self, arg0: 'TangentialAcceleration'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$TangentialAcceleration(com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$TangentialAcceleration)"""
        val = _TangentialAcceleration(arg0)
        self.__wrapper = val

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.write(com.badlogic.gdx.utils.Json)"""
        super(_Angular, self).write(arg0)

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
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(particles.ParticleControllerComponent, self).dispose()

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$TangentialAcceleration.allocateChannels()"""
        super(TangentialAcceleration, self).allocateChannels()

    @override
    @overload
    def copy(self) -> 'TangentialAcceleration':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$TangentialAcceleration com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$TangentialAcceleration.copy()"""
        return 'TangentialAcceleration'._wrap(super(TangentialAcceleration, self).copy())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$TangentialAcceleration()"""
        val = _TangentialAcceleration()
        self.__wrapper = val

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_Angular, self).read(arg0, arg1)

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$BrownianAcceleration
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

import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as _DynamicsModifier_Strength
_Strength = _DynamicsModifier_Strength.Strength
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as _DynamicsModifier_BrownianAcceleration
_BrownianAcceleration = _DynamicsModifier_BrownianAcceleration.BrownianAcceleration
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BrownianAcceleration():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.BrownianAcceleration"""
 
    @staticmethod
    def _wrap(java_value: _BrownianAcceleration) -> 'BrownianAcceleration':
        return BrownianAcceleration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BrownianAcceleration):
        """
        Dynamic initializer for BrownianAcceleration.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BrownianAcceleration__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BrownianAcceleration__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def copy(self) -> 'BrownianAcceleration':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$BrownianAcceleration com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$BrownianAcceleration.copy()"""
        return 'BrownianAcceleration'._wrap(super(BrownianAcceleration, self).copy())

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.write(com.badlogic.gdx.utils.Json)"""
        super(_Strength, self).write(arg0)

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
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$BrownianAcceleration.update()"""
        super(BrownianAcceleration, self).update()

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

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
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(particles.ParticleControllerComponent, self).dispose()

    @overload
    def __init__(self, arg0: 'BrownianAcceleration'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$BrownianAcceleration(com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$BrownianAcceleration)"""
        val = _BrownianAcceleration(arg0)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$BrownianAcceleration()"""
        val = _BrownianAcceleration()
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
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(_particles.ParticleControllerComponent, self).killParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.activateParticles(int,int)"""
        super(_Strength, self).activateParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$BrownianAcceleration()"""
        val = _BrownianAcceleration()
        self.__wrapper = val

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$BrownianAcceleration.allocateChannels()"""
        super(BrownianAcceleration, self).allocateChannels()

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_Strength, self).read(arg0, arg1)

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$FaceDirection
from pyquantum_helper import import_once as _import_once
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
import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as _ParticleControllerComponent
_ParticleControllerComponent = _ParticleControllerComponent
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as _DynamicsModifier_FaceDirection
_FaceDirection = _DynamicsModifier_FaceDirection.FaceDirection
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as _DynamicsModifier
_DynamicsModifier = _DynamicsModifier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FaceDirection():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.FaceDirection"""
 
    @staticmethod
    def _wrap(java_value: _FaceDirection) -> 'FaceDirection':
        return FaceDirection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FaceDirection):
        """
        Dynamic initializer for FaceDirection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FaceDirection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FaceDirection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

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
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$FaceDirection()"""
        val = _FaceDirection()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'FaceDirection'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$FaceDirection(com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$FaceDirection)"""
        val = _FaceDirection(arg0)
        self.__wrapper = val

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

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
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_DynamicsModifier, self).read(arg0, arg1)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(particles.ParticleControllerComponent, self).dispose()

    @override
    @overload
    def copy(self) -> 'particles.ParticleControllerComponent':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$FaceDirection.copy()"""
        return 'particles.ParticleControllerComponent'._wrap(super(FaceDirection, self).copy())

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
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(_particles.ParticleControllerComponent, self).killParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$FaceDirection()"""
        val = _FaceDirection()
        self.__wrapper = val

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.write(com.badlogic.gdx.utils.Json)"""
        super(_DynamicsModifier, self).write(arg0)

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$FaceDirection.allocateChannels()"""
        super(FaceDirection, self).allocateChannels()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$FaceDirection.update()"""
        super(FaceDirection, self).update()

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single
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

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer as _ColorInfluencer_Single
_Single = _ColorInfluencer_Single.Single
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Single():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer.Single"""
 
    @staticmethod
    def _wrap(java_value: _Single) -> 'Single':
        return Single(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Single):
        """
        Dynamic initializer for Single.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Single__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Single__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

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
    def __init__(self, arg0: 'Single'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single(com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single)"""
        val = _Single(arg0)
        self.__wrapper = val

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single.allocateChannels()"""
        super(Single, self).allocateChannels()

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

    @override
    @overload
    def copy(self) -> 'Single':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single.copy()"""
        return 'Single'._wrap(super(Single, self).copy())

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
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(particles.ParticleControllerComponent, self).dispose()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single.write(com.badlogic.gdx.utils.Json)"""
        super(_Single, self).write(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single()"""
        val = _Single()
        self.__wrapper = val

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single.update()"""
        super(Single, self).update()

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_Single, self).read(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def set(self, arg0: 'Single'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single.set(com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single)"""
        super(_Single, self).set(arg0)

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single.activateParticles(int,int)"""
        super(_Single, self).activateParticles(_int.valueOf(arg0), _int.valueOf(arg1))

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single()"""
        val = _Single()
        self.__wrapper = val

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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Random
from pyquantum_helper import import_once as _import_once
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
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as _ParticleControllerComponent
_ParticleControllerComponent = _ParticleControllerComponent
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer as _ModelInfluencer
_ModelInfluencer = _ModelInfluencer
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer as _ModelInfluencer_Random
_Random = _ModelInfluencer_Random.Random
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Random():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer.Random"""
 
    @staticmethod
    def _wrap(java_value: _Random) -> 'Random':
        return Random(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Random):
        """
        Dynamic initializer for Random.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Random__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Random__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_ModelInfluencer, self).save(arg0, arg1)

    @override
    @overload
    def copy(self) -> 'Random':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Random com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Random.copy()"""
        return 'Random'._wrap(super(Random, self).copy())

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Random.init()"""
        super(Random, self).init()

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
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.update()"""
        super(particles.ParticleControllerComponent, self).update()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(_particles.ParticleControllerComponent, self).write(arg0)

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
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(particles.ParticleControllerComponent, self).dispose()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Random()"""
        val = _Random()
        self.__wrapper = val

    @overload
    def __init__(self, *arg0: 'g3d.Model'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Random(com.badlogic.gdx.graphics.g3d.Model...)"""
        val = _Random(arg0)
        self.__wrapper = val

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer.allocateChannels()"""
        super(ModelInfluencer, self).allocateChannels()

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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_ModelInfluencer, self).load(arg0, arg1)

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
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_particles.ParticleControllerComponent, self).read(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Random.activateParticles(int,int)"""
        super(_Random, self).activateParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Random.killParticles(int,int)"""
        super(_Random, self).killParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Random()"""
        val = _Random()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Random'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Random(com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Random)"""
        val = _Random(arg0)
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerFinalizerInfluencer
from pyquantum_helper import import_once as _import_once
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
import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as _ParticleControllerComponent
_ParticleControllerComponent = _ParticleControllerComponent
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerFinalizerInfluencer as _ParticleControllerFinalizerInfluencer
_ParticleControllerFinalizerInfluencer = _ParticleControllerFinalizerInfluencer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParticleControllerFinalizerInfluencer():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerFinalizerInfluencer"""
 
    @staticmethod
    def _wrap(java_value: _ParticleControllerFinalizerInfluencer) -> 'ParticleControllerFinalizerInfluencer':
        return ParticleControllerFinalizerInfluencer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleControllerFinalizerInfluencer):
        """
        Dynamic initializer for ParticleControllerFinalizerInfluencer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleControllerFinalizerInfluencer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleControllerFinalizerInfluencer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

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
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerFinalizerInfluencer.init()"""
        super(ParticleControllerFinalizerInfluencer, self).init()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(_particles.ParticleControllerComponent, self).write(arg0)

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerFinalizerInfluencer()"""
        val = _ParticleControllerFinalizerInfluencer()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerFinalizerInfluencer()"""
        val = _ParticleControllerFinalizerInfluencer()
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
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(_particles.ParticleControllerComponent, self).killParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerFinalizerInfluencer.allocateChannels()"""
        super(ParticleControllerFinalizerInfluencer, self).allocateChannels()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def copy(self) -> 'ParticleControllerFinalizerInfluencer':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerFinalizerInfluencer com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerFinalizerInfluencer.copy()"""
        return 'ParticleControllerFinalizerInfluencer'._wrap(super(ParticleControllerFinalizerInfluencer, self).copy())

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerFinalizerInfluencer.update()"""
        super(ParticleControllerFinalizerInfluencer, self).update()

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
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_particles.ParticleControllerComponent, self).read(arg0, arg1)

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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$AspectTextureRegion
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer as _RegionInfluencer_AspectTextureRegion
_AspectTextureRegion = _RegionInfluencer_AspectTextureRegion.AspectTextureRegion
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AspectTextureRegion():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.AspectTextureRegion"""
 
    @staticmethod
    def _wrap(java_value: _AspectTextureRegion) -> 'AspectTextureRegion':
        return AspectTextureRegion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AspectTextureRegion):
        """
        Dynamic initializer for AspectTextureRegion.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AspectTextureRegion__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AspectTextureRegion__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$AspectTextureRegion()"""
        val = _AspectTextureRegion()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$AspectTextureRegion()"""
        val = _AspectTextureRegion()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'TextureRegion'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$AspectTextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = _AspectTextureRegion(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def set(self, arg0: 'AspectTextureRegion'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$AspectTextureRegion.set(com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$AspectTextureRegion)"""
        super(_AspectTextureRegion, self).set(arg0)

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
    def updateUV(self, arg0: 'TextureAtlas'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$AspectTextureRegion.updateUV(com.badlogic.gdx.graphics.g2d.TextureAtlas)"""
        super(_AspectTextureRegion, self).updateUV(arg0)

    @overload
    def set(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$AspectTextureRegion.set(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(_AspectTextureRegion, self).set(arg0)

    @overload
    def __init__(self, arg0: 'AspectTextureRegion'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$AspectTextureRegion(com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$AspectTextureRegion)"""
        val = _AspectTextureRegion(arg0)
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular
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
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as _DynamicsModifier_Angular
_Angular = _DynamicsModifier_Angular.Angular
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Angular():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.Angular"""
 
    @staticmethod
    def _wrap(java_value: _Angular) -> 'Angular':
        return Angular(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Angular):
        """
        Dynamic initializer for Angular.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Angular__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Angular__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.activateParticles(int,int)"""
        super(_Angular, self).activateParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.allocateChannels()"""
        super(Angular, self).allocateChannels()

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
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.update()"""
        super(particles.ParticleControllerComponent, self).update()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.write(com.badlogic.gdx.utils.Json)"""
        super(_Angular, self).write(arg0)

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
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(particles.ParticleControllerComponent, self).dispose()

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.copy()"""
        pass

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
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(_particles.ParticleControllerComponent, self).killParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular()"""
        val = _Angular()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Angular'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular(com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular)"""
        val = _Angular(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_Angular, self).read(arg0, arg1)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular()"""
        val = _Angular()
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$CentripetalAcceleration
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

import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as _DynamicsModifier_Strength
_Strength = _DynamicsModifier_Strength.Strength
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as _DynamicsModifier_CentripetalAcceleration
_CentripetalAcceleration = _DynamicsModifier_CentripetalAcceleration.CentripetalAcceleration
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CentripetalAcceleration():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.CentripetalAcceleration"""
 
    @staticmethod
    def _wrap(java_value: _CentripetalAcceleration) -> 'CentripetalAcceleration':
        return CentripetalAcceleration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CentripetalAcceleration):
        """
        Dynamic initializer for CentripetalAcceleration.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CentripetalAcceleration__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CentripetalAcceleration__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$CentripetalAcceleration()"""
        val = _CentripetalAcceleration()
        self.__wrapper = val

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$CentripetalAcceleration.update()"""
        super(CentripetalAcceleration, self).update()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.write(com.badlogic.gdx.utils.Json)"""
        super(_Strength, self).write(arg0)

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
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

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
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(particles.ParticleControllerComponent, self).dispose()

    @overload
    def __init__(self, arg0: 'CentripetalAcceleration'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$CentripetalAcceleration(com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$CentripetalAcceleration)"""
        val = _CentripetalAcceleration(arg0)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$CentripetalAcceleration.allocateChannels()"""
        super(CentripetalAcceleration, self).allocateChannels()

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

    @override
    @overload
    def copy(self) -> 'CentripetalAcceleration':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$CentripetalAcceleration com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$CentripetalAcceleration.copy()"""
        return 'CentripetalAcceleration'._wrap(super(CentripetalAcceleration, self).copy())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.activateParticles(int,int)"""
        super(_Strength, self).activateParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_Strength, self).read(arg0, arg1)

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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$CentripetalAcceleration()"""
        val = _CentripetalAcceleration()
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer
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
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer as _SimpleInfluencer
_SimpleInfluencer = _SimpleInfluencer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SimpleInfluencer():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer"""
 
    @staticmethod
    def _wrap(java_value: _SimpleInfluencer) -> 'SimpleInfluencer':
        return SimpleInfluencer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SimpleInfluencer):
        """
        Dynamic initializer for SimpleInfluencer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SimpleInfluencer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SimpleInfluencer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

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
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

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
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(particles.ParticleControllerComponent, self).dispose()

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.copy()"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_SimpleInfluencer, self).read(arg0, arg1)

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

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer.write(com.badlogic.gdx.utils.Json)"""
        super(_SimpleInfluencer, self).write(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer.activateParticles(int,int)"""
        super(_SimpleInfluencer, self).activateParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer.allocateChannels()"""
        super(SimpleInfluencer, self).allocateChannels()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer()"""
        val = _SimpleInfluencer()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer()"""
        val = _SimpleInfluencer()
        self.__wrapper = val

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
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer.update()"""
        super(SimpleInfluencer, self).update()

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
    def __init__(self, arg0: 'SimpleInfluencer'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer(com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer)"""
        val = _SimpleInfluencer(arg0)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Random
from pyquantum_helper import import_once as _import_once
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
import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as _ParticleControllerComponent
_ParticleControllerComponent = _ParticleControllerComponent
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer as _ParticleControllerInfluencer_Random
_Random = _ParticleControllerInfluencer_Random.Random
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer as _ParticleControllerInfluencer
_ParticleControllerInfluencer = _ParticleControllerInfluencer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Random():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.Random"""
 
    @staticmethod
    def _wrap(java_value: _Random) -> 'Random':
        return Random(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Random):
        """
        Dynamic initializer for Random.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Random__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Random__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Random.dispose()"""
        super(Random, self).dispose()

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
    def __init__(self, *arg0: 'particles.ParticleController'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Random(com.badlogic.gdx.graphics.g3d.particles.ParticleController...)"""
        val = _Random(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Random'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Random(com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Random)"""
        val = _Random(arg0)
        self.__wrapper = val

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.update()"""
        super(particles.ParticleControllerComponent, self).update()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(_particles.ParticleControllerComponent, self).write(arg0)

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
    def copy(self) -> 'Random':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Random com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Random.copy()"""
        return 'Random'._wrap(super(Random, self).copy())

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_ParticleControllerInfluencer, self).load(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Random.killParticles(int,int)"""
        super(_Random, self).killParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Random()"""
        val = _Random()
        self.__wrapper = val

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.end()"""
        super(ParticleControllerInfluencer, self).end()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Random.activateParticles(int,int)"""
        super(_Random, self).activateParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def set(self, arg0: 'ParticleController'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(_particles.ParticleControllerComponent, self).set(arg0)

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_particles.ParticleControllerComponent, self).read(arg0, arg1)

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Random.init()"""
        super(Random, self).init()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_ParticleControllerInfluencer, self).save(arg0, arg1)

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.allocateChannels()"""
        super(ParticleControllerInfluencer, self).allocateChannels()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Random()"""
        val = _Random()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer as _ColorInfluencer
_ColorInfluencer = _ColorInfluencer
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
 
class ColorInfluencer():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer"""
 
    @staticmethod
    def _wrap(java_value: _ColorInfluencer) -> 'ColorInfluencer':
        return ColorInfluencer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ColorInfluencer):
        """
        Dynamic initializer for ColorInfluencer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ColorInfluencer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ColorInfluencer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer()"""
        val = _ColorInfluencer()
        self.__wrapper = val

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

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
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.update()"""
        super(particles.ParticleControllerComponent, self).update()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(_particles.ParticleControllerComponent, self).write(arg0)

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

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.copy()"""
        pass

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer.allocateChannels()"""
        super(ColorInfluencer, self).allocateChannels()

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
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(_particles.ParticleControllerComponent, self).killParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer()"""
        val = _ColorInfluencer()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_particles.ParticleControllerComponent, self).read(arg0, arg1)

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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer
from pyquantum_helper import import_once as _import_once
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
import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as _ParticleControllerComponent
_ParticleControllerComponent = _ParticleControllerComponent
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer as _DynamicsInfluencer
_DynamicsInfluencer = _DynamicsInfluencer
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DynamicsInfluencer():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer"""
 
    @staticmethod
    def _wrap(java_value: _DynamicsInfluencer) -> 'DynamicsInfluencer':
        return DynamicsInfluencer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DynamicsInfluencer):
        """
        Dynamic initializer for DynamicsInfluencer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DynamicsInfluencer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DynamicsInfluencer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer.write(com.badlogic.gdx.utils.Json)"""
        super(_DynamicsInfluencer, self).write(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'DynamicsInfluencer'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer(com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer)"""
        val = _DynamicsInfluencer(arg0)
        self.__wrapper = val

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(particles.ParticleControllerComponent, self).dispose()

    @override
    @overload
    def copy(self) -> 'DynamicsInfluencer':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer.copy()"""
        return 'DynamicsInfluencer'._wrap(super(DynamicsInfluencer, self).copy())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer()"""
        val = _DynamicsInfluencer()
        self.__wrapper = val

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer.activateParticles(int,int)"""
        super(_DynamicsInfluencer, self).activateParticles(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(_particles.ParticleControllerComponent, self).killParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def set(self, arg0: 'ParticleController'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(_DynamicsInfluencer, self).set(arg0)

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_DynamicsInfluencer, self).read(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer.init()"""
        super(DynamicsInfluencer, self).init()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer()"""
        val = _DynamicsInfluencer()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer.allocateChannels()"""
        super(DynamicsInfluencer, self).allocateChannels()

    @overload
    def __init__(self, *arg0: 'DynamicsModifier'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer(com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier...)"""
        val = _DynamicsInfluencer(arg0)
        self.__wrapper = val

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer.update()"""
        super(DynamicsInfluencer, self).update()

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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier
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
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as _DynamicsModifier
_DynamicsModifier = _DynamicsModifier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DynamicsModifier():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier"""
 
    @staticmethod
    def _wrap(java_value: _DynamicsModifier) -> 'DynamicsModifier':
        return DynamicsModifier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DynamicsModifier):
        """
        Dynamic initializer for DynamicsModifier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DynamicsModifier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DynamicsModifier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'DynamicsModifier'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier(com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier)"""
        val = _DynamicsModifier(arg0)
        self.__wrapper = val

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

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
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.allocateChannels()"""
        super(DynamicsModifier, self).allocateChannels()

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.update()"""
        super(particles.ParticleControllerComponent, self).update()

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
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_DynamicsModifier, self).read(arg0, arg1)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(particles.ParticleControllerComponent, self).dispose()

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.copy()"""
        pass

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier()"""
        val = _DynamicsModifier()
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier()"""
        val = _DynamicsModifier()
        self.__wrapper = val

    @override
    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(_particles.ParticleControllerComponent, self).killParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.write(com.badlogic.gdx.utils.Json)"""
        super(_DynamicsModifier, self).write(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$PolarAcceleration
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as _DynamicsModifier_PolarAcceleration
_PolarAcceleration = _DynamicsModifier_PolarAcceleration.PolarAcceleration
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

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as _DynamicsModifier_Angular
_Angular = _DynamicsModifier_Angular.Angular
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PolarAcceleration():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.PolarAcceleration"""
 
    @staticmethod
    def _wrap(java_value: _PolarAcceleration) -> 'PolarAcceleration':
        return PolarAcceleration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PolarAcceleration):
        """
        Dynamic initializer for PolarAcceleration.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PolarAcceleration__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PolarAcceleration__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def copy(self) -> 'PolarAcceleration':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$PolarAcceleration com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$PolarAcceleration.copy()"""
        return 'PolarAcceleration'._wrap(super(PolarAcceleration, self).copy())

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.activateParticles(int,int)"""
        super(_Angular, self).activateParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$PolarAcceleration.update()"""
        super(PolarAcceleration, self).update()

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
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.write(com.badlogic.gdx.utils.Json)"""
        super(_Angular, self).write(arg0)

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
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(particles.ParticleControllerComponent, self).dispose()

    @overload
    def __init__(self, arg0: 'PolarAcceleration'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$PolarAcceleration(com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$PolarAcceleration)"""
        val = _PolarAcceleration(arg0)
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
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(_particles.ParticleControllerComponent, self).killParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$PolarAcceleration()"""
        val = _PolarAcceleration()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$PolarAcceleration.allocateChannels()"""
        super(PolarAcceleration, self).allocateChannels()

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_Angular, self).read(arg0, arg1)

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$PolarAcceleration()"""
        val = _PolarAcceleration()
        self.__wrapper = val

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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Animated
from pyquantum_helper import import_once as _import_once
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
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer as _RegionInfluencer
_RegionInfluencer = _RegionInfluencer
import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as _ParticleControllerComponent
_ParticleControllerComponent = _ParticleControllerComponent
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import java.lang.String as _string
import com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer as _RegionInfluencer_Animated
_Animated = _RegionInfluencer_Animated.Animated
import java.lang.Integer as _int
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Animated():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.Animated"""
 
    @staticmethod
    def _wrap(java_value: _Animated) -> 'Animated':
        return Animated(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Animated):
        """
        Dynamic initializer for Animated.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Animated__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Animated__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def clear(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.clear()"""
        super(RegionInfluencer, self).clear()

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_RegionInfluencer, self).load(arg0, arg1)

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Animated.allocateChannels()"""
        super(Animated, self).allocateChannels()

    @override
    @overload
    def copy(self) -> 'Animated':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Animated com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Animated.copy()"""
        return 'Animated'._wrap(super(Animated, self).copy())

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_RegionInfluencer, self).read(arg0, arg1)

    @override
    @overload
    def setAtlasName(self, arg0: str):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.setAtlasName(java.lang.String)"""
        super(_RegionInfluencer, self).setAtlasName(arg0)

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
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.write(com.badlogic.gdx.utils.Json)"""
        super(_RegionInfluencer, self).write(arg0)

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

    @overload
    def __init__(self, arg0: 'Animated'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Animated(com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Animated)"""
        val = _Animated(arg0)
        self.__wrapper = val

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Animated.update()"""
        super(Animated, self).update()

    @override
    @overload
    def add(self, *arg0: 'g2d.TextureRegion'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.add(com.badlogic.gdx.graphics.g2d.TextureRegion...)"""
        super(_RegionInfluencer, self).add(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'TextureRegion'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Animated(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = _Animated(arg0)
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Animated()"""
        val = _Animated()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Animated()"""
        val = _Animated()
        self.__wrapper = val

    @override
    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(_particles.ParticleControllerComponent, self).killParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_RegionInfluencer, self).save(arg0, arg1)

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
    def __init__(self, arg0: 'Texture'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Animated(com.badlogic.gdx.graphics.Texture)"""
        val = _Animated(arg0)
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational3D
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

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as _DynamicsModifier_Rotational3D
_Rotational3D = _DynamicsModifier_Rotational3D.Rotational3D
from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as _DynamicsModifier_Angular
_Angular = _DynamicsModifier_Angular.Angular
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Rotational3D():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.Rotational3D"""
 
    @staticmethod
    def _wrap(java_value: _Rotational3D) -> 'Rotational3D':
        return Rotational3D(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Rotational3D):
        """
        Dynamic initializer for Rotational3D.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Rotational3D__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Rotational3D__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.activateParticles(int,int)"""
        super(_Angular, self).activateParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

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
    def copy(self) -> 'Rotational3D':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational3D com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational3D.copy()"""
        return 'Rotational3D'._wrap(super(Rotational3D, self).copy())

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.write(com.badlogic.gdx.utils.Json)"""
        super(_Angular, self).write(arg0)

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
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(particles.ParticleControllerComponent, self).dispose()

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational3D.allocateChannels()"""
        super(Rotational3D, self).allocateChannels()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational3D()"""
        val = _Rotational3D()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational3D()"""
        val = _Rotational3D()
        self.__wrapper = val

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational3D.update()"""
        super(Rotational3D, self).update()

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_Angular, self).read(arg0, arg1)

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
    def __init__(self, arg0: 'Rotational3D'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational3D(com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational3D)"""
        val = _Rotational3D(arg0)
        self.__wrapper = val

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer
from pyquantum_helper import import_once as _import_once
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
import com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer as _ParticleControllerInfluencer
_ParticleControllerInfluencer = _ParticleControllerInfluencer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParticleControllerInfluencer():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer"""
 
    @staticmethod
    def _wrap(java_value: _ParticleControllerInfluencer) -> 'ParticleControllerInfluencer':
        return ParticleControllerInfluencer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleControllerInfluencer):
        """
        Dynamic initializer for ParticleControllerInfluencer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleControllerInfluencer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleControllerInfluencer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'ParticleControllerInfluencer'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer(com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer)"""
        val = _ParticleControllerInfluencer(arg0)
        self.__wrapper = val

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer()"""
        val = _ParticleControllerInfluencer()
        self.__wrapper = val

    @overload
    def __init__(self, *arg0: 'particles.ParticleController'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer(com.badlogic.gdx.graphics.g3d.particles.ParticleController...)"""
        val = _ParticleControllerInfluencer(arg0)
        self.__wrapper = val

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.update()"""
        super(particles.ParticleControllerComponent, self).update()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(_particles.ParticleControllerComponent, self).write(arg0)

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

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.copy()"""
        pass

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_ParticleControllerInfluencer, self).load(arg0, arg1)

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
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(_particles.ParticleControllerComponent, self).killParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.end()"""
        super(ParticleControllerInfluencer, self).end()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer()"""
        val = _ParticleControllerInfluencer()
        self.__wrapper = val

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
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_particles.ParticleControllerComponent, self).read(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_ParticleControllerInfluencer, self).save(arg0, arg1)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.dispose()"""
        super(ParticleControllerInfluencer, self).dispose()

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.allocateChannels()"""
        super(ParticleControllerInfluencer, self).allocateChannels()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.ScaleInfluencer
from pyquantum_helper import import_once as _import_once
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
import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as _ParticleControllerComponent
_ParticleControllerComponent = _ParticleControllerComponent
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.influencers.ScaleInfluencer as _ScaleInfluencer
_ScaleInfluencer = _ScaleInfluencer
import com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer as _SimpleInfluencer
_SimpleInfluencer = _SimpleInfluencer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ScaleInfluencer():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.ScaleInfluencer"""
 
    @staticmethod
    def _wrap(java_value: _ScaleInfluencer) -> 'ScaleInfluencer':
        return ScaleInfluencer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ScaleInfluencer):
        """
        Dynamic initializer for ScaleInfluencer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ScaleInfluencer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ScaleInfluencer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ScaleInfluencer()"""
        val = _ScaleInfluencer()
        self.__wrapper = val

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
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

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
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(particles.ParticleControllerComponent, self).dispose()

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ScaleInfluencer.activateParticles(int,int)"""
        super(_ScaleInfluencer, self).activateParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ScaleInfluencer()"""
        val = _ScaleInfluencer()
        self.__wrapper = val

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_SimpleInfluencer, self).read(arg0, arg1)

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

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer.write(com.badlogic.gdx.utils.Json)"""
        super(_SimpleInfluencer, self).write(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer.allocateChannels()"""
        super(SimpleInfluencer, self).allocateChannels()

    @overload
    def __init__(self, arg0: 'ScaleInfluencer'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ScaleInfluencer(com.badlogic.gdx.graphics.g3d.particles.influencers.ScaleInfluencer)"""
        val = _ScaleInfluencer(arg0)
        self.__wrapper = val

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
    def copy(self) -> 'particles.ParticleControllerComponent':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.influencers.ScaleInfluencer.copy()"""
        return 'particles.ParticleControllerComponent'._wrap(super(ScaleInfluencer, self).copy())

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer.update()"""
        super(SimpleInfluencer, self).update()

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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Random
from pyquantum_helper import import_once as _import_once
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
import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as _ParticleControllerComponent
_ParticleControllerComponent = _ParticleControllerComponent
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer as _ColorInfluencer_Random
_Random = _ColorInfluencer_Random.Random
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Random():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer.Random"""
 
    @staticmethod
    def _wrap(java_value: _Random) -> 'Random':
        return Random(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Random):
        """
        Dynamic initializer for Random.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Random__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Random__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @override
    @overload
    def copy(self) -> 'Random':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Random com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Random.copy()"""
        return 'Random'._wrap(super(Random, self).copy())

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
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.update()"""
        super(particles.ParticleControllerComponent, self).update()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(_particles.ParticleControllerComponent, self).write(arg0)

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Random.activateParticles(int,int)"""
        super(_Random, self).activateParticles(_int.valueOf(arg0), _int.valueOf(arg1))

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
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(particles.ParticleControllerComponent, self).dispose()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Random()"""
        val = _Random()
        self.__wrapper = val

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Random.allocateChannels()"""
        super(Random, self).allocateChannels()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Random()"""
        val = _Random()
        self.__wrapper = val

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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

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
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_particles.ParticleControllerComponent, self).read(arg0, arg1)

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

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer
from pyquantum_helper import import_once as _import_once
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
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as _ParticleControllerComponent
_ParticleControllerComponent = _ParticleControllerComponent
import com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer as _ModelInfluencer
_ModelInfluencer = _ModelInfluencer
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
 
class ModelInfluencer():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer"""
 
    @staticmethod
    def _wrap(java_value: _ModelInfluencer) -> 'ModelInfluencer':
        return ModelInfluencer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModelInfluencer):
        """
        Dynamic initializer for ModelInfluencer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModelInfluencer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModelInfluencer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_ModelInfluencer, self).save(arg0, arg1)

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
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.update()"""
        super(particles.ParticleControllerComponent, self).update()

    @overload
    def __init__(self, *arg0: 'g3d.Model'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer(com.badlogic.gdx.graphics.g3d.Model...)"""
        val = _ModelInfluencer(arg0)
        self.__wrapper = val

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(_particles.ParticleControllerComponent, self).write(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer()"""
        val = _ModelInfluencer()
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

    @overload
    def __init__(self, arg0: 'ModelInfluencer'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer(com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer)"""
        val = _ModelInfluencer(arg0)
        self.__wrapper = val

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.copy()"""
        pass

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer.allocateChannels()"""
        super(ModelInfluencer, self).allocateChannels()

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
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(_particles.ParticleControllerComponent, self).killParticles(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_ModelInfluencer, self).load(arg0, arg1)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer()"""
        val = _ModelInfluencer()
        self.__wrapper = val

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
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_particles.ParticleControllerComponent, self).read(arg0, arg1)

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