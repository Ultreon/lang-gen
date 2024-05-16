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
import java.lang.Object as __object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

from abc import abstractmethod, ABC
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as __DynamicsModifier_Angular
__Angular = __DynamicsModifier_Angular.Angular
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
 
class Angular(ABC):
    """com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.Angular"""
 
    @staticmethod
    def __wrap(java_value: __Angular) -> 'Angular':
        return Angular(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Angular):
        """
        Dynamic initializer for Angular.
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
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular()"""
        val = __Angular()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__particles.ParticleControllerComponent, self).save(arg0, arg1)

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
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__Angular, self).read(arg0, arg1)

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

    @overload
    def __init__(self, arg0: 'Angular'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular(com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular)"""
        val = __Angular(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.copy()"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

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
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular()"""
        val = __Angular()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.activateParticles(int,int)"""
        super(__Angular, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.write(com.badlogic.gdx.utils.Json)"""
        super(__Angular, self).write(arg0)

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular
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
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as __DynamicsModifier_Angular
__Angular = __DynamicsModifier_Angular.Angular
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
 
class Angular(ABC):
    """com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.Angular"""
 
    @staticmethod
    def __wrap(java_value: __Angular) -> 'Angular':
        return Angular(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Angular):
        """
        Dynamic initializer for Angular.
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
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular()"""
        val = __Angular()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__particles.ParticleControllerComponent, self).save(arg0, arg1)

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
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__Angular, self).read(arg0, arg1)

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

    @overload
    def __init__(self, arg0: 'Angular'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular(com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular)"""
        val = __Angular(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.copy()"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

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
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular()"""
        val = __Angular()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.activateParticles(int,int)"""
        super(__Angular, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.write(com.badlogic.gdx.utils.Json)"""
        super(__Angular, self).write(arg0)

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$AspectTextureRegion
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer as __RegionInfluencer_AspectTextureRegion
__AspectTextureRegion = __RegionInfluencer_AspectTextureRegion.AspectTextureRegion
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
 
class AspectTextureRegion():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.AspectTextureRegion"""
 
    @staticmethod
    def __wrap(java_value: __AspectTextureRegion) -> 'AspectTextureRegion':
        return AspectTextureRegion(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AspectTextureRegion):
        """
        Dynamic initializer for AspectTextureRegion.
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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$AspectTextureRegion()"""
        val = __AspectTextureRegion()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'AspectTextureRegion'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$AspectTextureRegion(com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$AspectTextureRegion)"""
        val = __AspectTextureRegion(arg0)
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
    def set(self, arg0: 'AspectTextureRegion'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$AspectTextureRegion.set(com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$AspectTextureRegion)"""
        super(__AspectTextureRegion, self).set(arg0)

    @overload
    def set(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$AspectTextureRegion.set(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(__AspectTextureRegion, self).set(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'TextureRegion'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$AspectTextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = __AspectTextureRegion(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def updateUV(self, arg0: 'TextureAtlas'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$AspectTextureRegion.updateUV(com.badlogic.gdx.graphics.g2d.TextureAtlas)"""
        super(__AspectTextureRegion, self).updateUV(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$AspectTextureRegion()"""
        val = __AspectTextureRegion()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier
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
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as __DynamicsModifier
__DynamicsModifier = __DynamicsModifier
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
 
class DynamicsModifier(ABC):
    """com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier"""
 
    @staticmethod
    def __wrap(java_value: __DynamicsModifier) -> 'DynamicsModifier':
        return DynamicsModifier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DynamicsModifier):
        """
        Dynamic initializer for DynamicsModifier.
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

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @overload
    def __init__(self, arg0: 'DynamicsModifier'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier(com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier)"""
        val = __DynamicsModifier(arg0)
        self.__dict__ = val.__dict__
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
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.allocateChannels()"""
        super(DynamicsModifier, self).allocateChannels()

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.activateParticles(int,int)"""
        super(__particles.ParticleControllerComponent, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

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

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.copy()"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

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
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__DynamicsModifier, self).read(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier()"""
        val = __DynamicsModifier()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.write(com.badlogic.gdx.utils.Json)"""
        super(__DynamicsModifier, self).write(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier()"""
        val = __DynamicsModifier()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer
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
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer as __SimpleInfluencer
__SimpleInfluencer = __SimpleInfluencer
from builtins import int
 
class SimpleInfluencer(ABC):
    """com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer"""
 
    @staticmethod
    def __wrap(java_value: __SimpleInfluencer) -> 'SimpleInfluencer':
        return SimpleInfluencer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SimpleInfluencer):
        """
        Dynamic initializer for SimpleInfluencer.
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
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__SimpleInfluencer, self).read(arg0, arg1)

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__particles.ParticleControllerComponent, self).save(arg0, arg1)

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer.activateParticles(int,int)"""
        super(__SimpleInfluencer, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

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
    def __init__(self, arg0: 'SimpleInfluencer'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer(com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer)"""
        val = __SimpleInfluencer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

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

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.copy()"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer.write(com.badlogic.gdx.utils.Json)"""
        super(__SimpleInfluencer, self).write(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer.allocateChannels()"""
        super(SimpleInfluencer, self).allocateChannels()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer()"""
        val = __SimpleInfluencer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer()"""
        val = __SimpleInfluencer()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer
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
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer as __RegionInfluencer
__RegionInfluencer = __RegionInfluencer
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
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class RegionInfluencer(ABC):
    """com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer"""
 
    @staticmethod
    def __wrap(java_value: __RegionInfluencer) -> 'RegionInfluencer':
        return RegionInfluencer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RegionInfluencer):
        """
        Dynamic initializer for RegionInfluencer.
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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer()"""
        val = __RegionInfluencer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def clear(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.clear()"""
        super(RegionInfluencer, self).clear()

    @overload
    def add(self, *arg0: 'g2d.TextureRegion'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.add(com.badlogic.gdx.graphics.g2d.TextureRegion...)"""
        super(__RegionInfluencer, self).add(arg0)

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @overload
    def __init__(self, *arg0: 'g2d.TextureRegion'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer(com.badlogic.gdx.graphics.g2d.TextureRegion...)"""
        val = __RegionInfluencer(arg0)
        self.__dict__ = val.__dict__
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
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.activateParticles(int,int)"""
        super(__particles.ParticleControllerComponent, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

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
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(__particles.ParticleControllerComponent, self).killParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__RegionInfluencer, self).read(arg0, arg1)

    @overload
    def __init__(self, arg0: 'RegionInfluencer'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer(com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer)"""
        val = __RegionInfluencer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setAtlasName(self, arg0: str):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.setAtlasName(java.lang.String)"""
        super(__RegionInfluencer, self).setAtlasName(arg0)

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

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.write(com.badlogic.gdx.utils.Json)"""
        super(__RegionInfluencer, self).write(arg0)

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.copy()"""
        pass

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Texture'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer(com.badlogic.gdx.graphics.Texture)"""
        val = __RegionInfluencer(arg0)
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer(int)"""
        val = __RegionInfluencer(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer()"""
        val = __RegionInfluencer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__RegionInfluencer, self).load(arg0, arg1)

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__RegionInfluencer, self).save(arg0, arg1) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single
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

import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as __ParticleControllerComponent
__ParticleControllerComponent = __ParticleControllerComponent
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer as __ColorInfluencer_Single
__Single = __ColorInfluencer_Single.Single
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Single():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer.Single"""
 
    @staticmethod
    def __wrap(java_value: __Single) -> 'Single':
        return Single(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Single):
        """
        Dynamic initializer for Single.
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
    def __init__(self, arg0: 'Single'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single(com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single)"""
        val = __Single(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__particles.ParticleControllerComponent, self).save(arg0, arg1)

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single.activateParticles(int,int)"""
        super(__Single, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single()"""
        val = __Single()
        self.__dict__ = val.__dict__
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
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__Single, self).read(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single.update()"""
        super(Single, self).update()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single()"""
        val = __Single()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def set(self, arg0: 'Single'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single.set(com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single)"""
        super(__Single, self).set(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def copy(self) -> 'Single':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single.copy()"""
        return 'Single'.__wrap(super(Single, self).copy())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Single.write(com.badlogic.gdx.utils.Json)"""
        super(__Single, self).write(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$PolarAcceleration
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

import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as __DynamicsModifier_PolarAcceleration
__PolarAcceleration = __DynamicsModifier_PolarAcceleration.PolarAcceleration
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as __DynamicsModifier_Angular
__Angular = __DynamicsModifier_Angular.Angular
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
 
class PolarAcceleration():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.PolarAcceleration"""
 
    @staticmethod
    def __wrap(java_value: __PolarAcceleration) -> 'PolarAcceleration':
        return PolarAcceleration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PolarAcceleration):
        """
        Dynamic initializer for PolarAcceleration.
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
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__Angular, self).read(arg0, arg1)

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

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
    def __init__(self, arg0: 'PolarAcceleration'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$PolarAcceleration(com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$PolarAcceleration)"""
        val = __PolarAcceleration(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$PolarAcceleration.allocateChannels()"""
        super(PolarAcceleration, self).allocateChannels()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$PolarAcceleration()"""
        val = __PolarAcceleration()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.activateParticles(int,int)"""
        super(__Angular, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$PolarAcceleration()"""
        val = __PolarAcceleration()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def copy(self) -> 'PolarAcceleration':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$PolarAcceleration com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$PolarAcceleration.copy()"""
        return 'PolarAcceleration'.__wrap(super(PolarAcceleration, self).copy())

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.write(com.badlogic.gdx.utils.Json)"""
        super(__Angular, self).write(arg0) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Single
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
import com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer as __ModelInfluencer_Single
__Single = __ModelInfluencer_Single.Single
from builtins import type
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer as __ModelInfluencer
__ModelInfluencer = __ModelInfluencer
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
 
class Single():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer.Single"""
 
    @staticmethod
    def __wrap(java_value: __Single) -> 'Single':
        return Single(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Single):
        """
        Dynamic initializer for Single.
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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Single()"""
        val = __Single()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.activateParticles(int,int)"""
        super(__particles.ParticleControllerComponent, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.update()"""
        super(particles.ParticleControllerComponent, self).update()

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

    @overload
    def __init__(self, *arg0: 'g3d.Model'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Single(com.badlogic.gdx.graphics.g3d.Model...)"""
        val = __Single(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__particles.ParticleControllerComponent, self).read(arg0, arg1)

    @override
    @overload
    def copy(self) -> 'Single':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Single com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Single.copy()"""
        return 'Single'.__wrap(super(Single, self).copy())

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer.allocateChannels()"""
        super(ModelInfluencer, self).allocateChannels()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(__particles.ParticleControllerComponent, self).write(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Single()"""
        val = __Single()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Single.init()"""
        super(Single, self).init()

    @overload
    def __init__(self, arg0: 'Single'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Single(com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Single)"""
        val = __Single(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__ModelInfluencer, self).save(arg0, arg1)

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__ModelInfluencer, self).load(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer
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
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer as __ModelInfluencer
__ModelInfluencer = __ModelInfluencer
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
 
class ModelInfluencer(ABC):
    """com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer"""
 
    @staticmethod
    def __wrap(java_value: __ModelInfluencer) -> 'ModelInfluencer':
        return ModelInfluencer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModelInfluencer):
        """
        Dynamic initializer for ModelInfluencer.
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
    def __init__(self, arg0: 'ModelInfluencer'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer(com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer)"""
        val = __ModelInfluencer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.activateParticles(int,int)"""
        super(__particles.ParticleControllerComponent, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

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
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(__particles.ParticleControllerComponent, self).killParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer()"""
        val = __ModelInfluencer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def __init__(self, *arg0: 'g3d.Model'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer(com.badlogic.gdx.graphics.g3d.Model...)"""
        val = __ModelInfluencer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.copy()"""
        pass

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__particles.ParticleControllerComponent, self).read(arg0, arg1)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer()"""
        val = __ModelInfluencer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer.allocateChannels()"""
        super(ModelInfluencer, self).allocateChannels()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(__particles.ParticleControllerComponent, self).write(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__ModelInfluencer, self).save(arg0, arg1)

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__ModelInfluencer, self).load(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer
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
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

from abc import abstractmethod, ABC
import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as __ParticleControllerComponent
__ParticleControllerComponent = __ParticleControllerComponent
import com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer as __ColorInfluencer
__ColorInfluencer = __ColorInfluencer
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
 
class ColorInfluencer(ABC):
    """com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer"""
 
    @staticmethod
    def __wrap(java_value: __ColorInfluencer) -> 'ColorInfluencer':
        return ColorInfluencer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ColorInfluencer):
        """
        Dynamic initializer for ColorInfluencer.
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
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.activateParticles(int,int)"""
        super(__particles.ParticleControllerComponent, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

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

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.copy()"""
        pass

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__particles.ParticleControllerComponent, self).read(arg0, arg1)

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer.allocateChannels()"""
        super(ColorInfluencer, self).allocateChannels()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(__particles.ParticleControllerComponent, self).write(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

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
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer()"""
        val = __ColorInfluencer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer()"""
        val = __ColorInfluencer()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Random
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer as __RegionInfluencer_Random
__Random = __RegionInfluencer_Random.Random
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
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer as __RegionInfluencer
__RegionInfluencer = __RegionInfluencer
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as __ParticleControllerComponent
__ParticleControllerComponent = __ParticleControllerComponent
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
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class Random():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.Random"""
 
    @staticmethod
    def __wrap(java_value: __Random) -> 'Random':
        return Random(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Random):
        """
        Dynamic initializer for Random.
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
    def clear(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.clear()"""
        super(RegionInfluencer, self).clear()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @overload
    def __init__(self, arg0: 'Texture'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Random(com.badlogic.gdx.graphics.Texture)"""
        val = __Random(arg0)
        self.__dict__ = val.__dict__
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
    def setAtlasName(self, arg0: str):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.setAtlasName(java.lang.String)"""
        super(__RegionInfluencer, self).setAtlasName(arg0)

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
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(__particles.ParticleControllerComponent, self).killParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__RegionInfluencer, self).read(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'TextureRegion'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Random(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = __Random(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def copy(self) -> 'Random':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Random com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Random.copy()"""
        return 'Random'.__wrap(super(Random, self).copy())

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Random.activateParticles(int,int)"""
        super(__Random, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.write(com.badlogic.gdx.utils.Json)"""
        super(__RegionInfluencer, self).write(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Random()"""
        val = __Random()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def add(self, *arg0: 'g2d.TextureRegion'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.add(com.badlogic.gdx.graphics.g2d.TextureRegion...)"""
        super(__RegionInfluencer, self).add(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Random'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Random(com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Random)"""
        val = __Random(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__RegionInfluencer, self).load(arg0, arg1)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Random()"""
        val = __Random()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__RegionInfluencer, self).save(arg0, arg1) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength
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
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as __DynamicsModifier_Strength
__Strength = __DynamicsModifier_Strength.Strength
from builtins import int
 
class Strength(ABC):
    """com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.Strength"""
 
    @staticmethod
    def __wrap(java_value: __Strength) -> 'Strength':
        return Strength(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Strength):
        """
        Dynamic initializer for Strength.
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

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.activateParticles(int,int)"""
        super(__Strength, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

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

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.copy()"""
        pass

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__Strength, self).read(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'Strength'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength(com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength)"""
        val = __Strength(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.allocateChannels()"""
        super(Strength, self).allocateChannels()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength()"""
        val = __Strength()
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.write(com.badlogic.gdx.utils.Json)"""
        super(__Strength, self).write(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength()"""
        val = __Strength()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$CentripetalAcceleration
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
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as __DynamicsModifier_CentripetalAcceleration
__CentripetalAcceleration = __DynamicsModifier_CentripetalAcceleration.CentripetalAcceleration
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

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
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as __DynamicsModifier_Strength
__Strength = __DynamicsModifier_Strength.Strength
from builtins import int
 
class CentripetalAcceleration():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.CentripetalAcceleration"""
 
    @staticmethod
    def __wrap(java_value: __CentripetalAcceleration) -> 'CentripetalAcceleration':
        return CentripetalAcceleration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CentripetalAcceleration):
        """
        Dynamic initializer for CentripetalAcceleration.
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

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @overload
    def __init__(self, arg0: 'CentripetalAcceleration'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$CentripetalAcceleration(com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$CentripetalAcceleration)"""
        val = __CentripetalAcceleration(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$CentripetalAcceleration.update()"""
        super(CentripetalAcceleration, self).update()

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.activateParticles(int,int)"""
        super(__Strength, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

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
    def copy(self) -> 'CentripetalAcceleration':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$CentripetalAcceleration com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$CentripetalAcceleration.copy()"""
        return 'CentripetalAcceleration'.__wrap(super(CentripetalAcceleration, self).copy())

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$CentripetalAcceleration()"""
        val = __CentripetalAcceleration()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__Strength, self).read(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$CentripetalAcceleration.allocateChannels()"""
        super(CentripetalAcceleration, self).allocateChannels()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$CentripetalAcceleration()"""
        val = __CentripetalAcceleration()
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.write(com.badlogic.gdx.utils.Json)"""
        super(__Strength, self).write(arg0) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Random
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
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as __ParticleControllerComponent
__ParticleControllerComponent = __ParticleControllerComponent
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer as __ParticleControllerInfluencer
__ParticleControllerInfluencer = __ParticleControllerInfluencer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer as __ParticleControllerInfluencer_Random
__Random = __ParticleControllerInfluencer_Random.Random
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Random():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.Random"""
 
    @staticmethod
    def __wrap(java_value: __Random) -> 'Random':
        return Random(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Random):
        """
        Dynamic initializer for Random.
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

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Random.activateParticles(int,int)"""
        super(__Random, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.update()"""
        super(particles.ParticleControllerComponent, self).update()

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__ParticleControllerInfluencer, self).load(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def set(self, arg0: 'ParticleController'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(__particles.ParticleControllerComponent, self).set(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Random()"""
        val = __Random()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__particles.ParticleControllerComponent, self).read(arg0, arg1)

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(__particles.ParticleControllerComponent, self).write(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Random.killParticles(int,int)"""
        super(__Random, self).killParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Random()"""
        val = __Random()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.end()"""
        super(ParticleControllerInfluencer, self).end()

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__ParticleControllerInfluencer, self).save(arg0, arg1)

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
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Random.init()"""
        super(Random, self).init()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Random'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Random(com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Random)"""
        val = __Random(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.allocateChannels()"""
        super(ParticleControllerInfluencer, self).allocateChannels()

    @override
    @overload
    def copy(self) -> 'Random':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Random com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Random.copy()"""
        return 'Random'.__wrap(super(Random, self).copy())

    @overload
    def __init__(self, *arg0: 'particles.ParticleController'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Random(com.badlogic.gdx.graphics.g3d.particles.ParticleController...)"""
        val = __Random(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer
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
import com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer as __ParticleControllerInfluencer
__ParticleControllerInfluencer = __ParticleControllerInfluencer
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ParticleControllerInfluencer(ABC):
    """com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer"""
 
    @staticmethod
    def __wrap(java_value: __ParticleControllerInfluencer) -> 'ParticleControllerInfluencer':
        return ParticleControllerInfluencer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleControllerInfluencer):
        """
        Dynamic initializer for ParticleControllerInfluencer.
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
    def __init__(self, arg0: 'ParticleControllerInfluencer'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer(com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer)"""
        val = __ParticleControllerInfluencer(arg0)
        self.__dict__ = val.__dict__
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
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.activateParticles(int,int)"""
        super(__particles.ParticleControllerComponent, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

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
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(__particles.ParticleControllerComponent, self).killParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__ParticleControllerInfluencer, self).load(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def set(self, arg0: 'ParticleController'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(__particles.ParticleControllerComponent, self).set(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer()"""
        val = __ParticleControllerInfluencer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.copy()"""
        pass

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__particles.ParticleControllerComponent, self).read(arg0, arg1)

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(__particles.ParticleControllerComponent, self).write(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.end()"""
        super(ParticleControllerInfluencer, self).end()

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__ParticleControllerInfluencer, self).save(arg0, arg1)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer()"""
        val = __ParticleControllerInfluencer()
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
    def __init__(self, *arg0: 'particles.ParticleController'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer(com.badlogic.gdx.graphics.g3d.particles.ParticleController...)"""
        val = __ParticleControllerInfluencer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational2D
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

import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as __ParticleControllerComponent
__ParticleControllerComponent = __ParticleControllerComponent
import java.lang.Long as __long
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as __DynamicsModifier_Rotational2D
__Rotational2D = __DynamicsModifier_Rotational2D.Rotational2D
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as __DynamicsModifier_Strength
__Strength = __DynamicsModifier_Strength.Strength
from builtins import int
 
class Rotational2D():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.Rotational2D"""
 
    @staticmethod
    def __wrap(java_value: __Rotational2D) -> 'Rotational2D':
        return Rotational2D(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Rotational2D):
        """
        Dynamic initializer for Rotational2D.
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

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.activateParticles(int,int)"""
        super(__Strength, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

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
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(__particles.ParticleControllerComponent, self).killParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational2D()"""
        val = __Rotational2D()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

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
    def copy(self) -> 'Rotational2D':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational2D com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational2D.copy()"""
        return 'Rotational2D'.__wrap(super(Rotational2D, self).copy())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__Strength, self).read(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational2D()"""
        val = __Rotational2D()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational2D.update()"""
        super(Rotational2D, self).update()

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
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational2D.allocateChannels()"""
        super(Rotational2D, self).allocateChannels()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Rotational2D'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational2D(com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational2D)"""
        val = __Rotational2D(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.write(com.badlogic.gdx.utils.Json)"""
        super(__Strength, self).write(arg0) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$BrownianAcceleration
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

import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as __DynamicsModifier_BrownianAcceleration
__BrownianAcceleration = __DynamicsModifier_BrownianAcceleration.BrownianAcceleration
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
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as __DynamicsModifier_Strength
__Strength = __DynamicsModifier_Strength.Strength
from builtins import int
 
class BrownianAcceleration():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.BrownianAcceleration"""
 
    @staticmethod
    def __wrap(java_value: __BrownianAcceleration) -> 'BrownianAcceleration':
        return BrownianAcceleration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BrownianAcceleration):
        """
        Dynamic initializer for BrownianAcceleration.
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

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.activateParticles(int,int)"""
        super(__Strength, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

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
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(__particles.ParticleControllerComponent, self).killParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$BrownianAcceleration()"""
        val = __BrownianAcceleration()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$BrownianAcceleration()"""
        val = __BrownianAcceleration()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__Strength, self).read(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'BrownianAcceleration'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$BrownianAcceleration(com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$BrownianAcceleration)"""
        val = __BrownianAcceleration(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def copy(self) -> 'BrownianAcceleration':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$BrownianAcceleration com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$BrownianAcceleration.copy()"""
        return 'BrownianAcceleration'.__wrap(super(BrownianAcceleration, self).copy())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$BrownianAcceleration.allocateChannels()"""
        super(BrownianAcceleration, self).allocateChannels()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Strength.write(com.badlogic.gdx.utils.Json)"""
        super(__Strength, self).write(arg0) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer
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
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as __ParticleControllerComponent
__ParticleControllerComponent = __ParticleControllerComponent
import java.lang.Long as __long
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer as __DynamicsInfluencer
__DynamicsInfluencer = __DynamicsInfluencer
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DynamicsInfluencer():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer"""
 
    @staticmethod
    def __wrap(java_value: __DynamicsInfluencer) -> 'DynamicsInfluencer':
        return DynamicsInfluencer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DynamicsInfluencer):
        """
        Dynamic initializer for DynamicsInfluencer.
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
    def copy(self) -> 'DynamicsInfluencer':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer.copy()"""
        return 'DynamicsInfluencer'.__wrap(super(DynamicsInfluencer, self).copy())

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

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer.write(com.badlogic.gdx.utils.Json)"""
        super(__DynamicsInfluencer, self).write(arg0)

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
    def set(self, arg0: 'ParticleController'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(__DynamicsInfluencer, self).set(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer.activateParticles(int,int)"""
        super(__DynamicsInfluencer, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer()"""
        val = __DynamicsInfluencer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__DynamicsInfluencer, self).read(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'DynamicsInfluencer'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer(com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer)"""
        val = __DynamicsInfluencer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, *arg0: 'DynamicsModifier'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer(com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier...)"""
        val = __DynamicsInfluencer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer()"""
        val = __DynamicsInfluencer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer.init()"""
        super(DynamicsInfluencer, self).init()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsInfluencer.allocateChannels()"""
        super(DynamicsInfluencer, self).allocateChannels()

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Random
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer as __ColorInfluencer_Random
__Random = __ColorInfluencer_Random.Random
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
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

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
 
class Random():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer.Random"""
 
    @staticmethod
    def __wrap(java_value: __Random) -> 'Random':
        return Random(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Random):
        """
        Dynamic initializer for Random.
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

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Random()"""
        val = __Random()
        self.__dict__ = val.__dict__
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

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Random.allocateChannels()"""
        super(Random, self).allocateChannels()

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__particles.ParticleControllerComponent, self).read(arg0, arg1)

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(__particles.ParticleControllerComponent, self).write(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def copy(self) -> 'Random':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Random com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Random.copy()"""
        return 'Random'.__wrap(super(Random, self).copy())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Random()"""
        val = __Random()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ColorInfluencer$Random.activateParticles(int,int)"""
        super(__Random, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational3D
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
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as __DynamicsModifier_Rotational3D
__Rotational3D = __DynamicsModifier_Rotational3D.Rotational3D
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as __DynamicsModifier_Angular
__Angular = __DynamicsModifier_Angular.Angular
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
 
class Rotational3D():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.Rotational3D"""
 
    @staticmethod
    def __wrap(java_value: __Rotational3D) -> 'Rotational3D':
        return Rotational3D(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Rotational3D):
        """
        Dynamic initializer for Rotational3D.
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
    def __init__(self, arg0: 'Rotational3D'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational3D(com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational3D)"""
        val = __Rotational3D(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__Angular, self).read(arg0, arg1)

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

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
    def set(self, arg0: 'ParticleController'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(__particles.ParticleControllerComponent, self).set(arg0)

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.dispose()"""
        super(particles.ParticleControllerComponent, self).dispose()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational3D()"""
        val = __Rotational3D()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational3D.allocateChannels()"""
        super(Rotational3D, self).allocateChannels()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational3D()"""
        val = __Rotational3D()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def copy(self) -> 'Rotational3D':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational3D com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational3D.copy()"""
        return 'Rotational3D'.__wrap(super(Rotational3D, self).copy())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.activateParticles(int,int)"""
        super(__Angular, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Rotational3D.update()"""
        super(Rotational3D, self).update()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.write(com.badlogic.gdx.utils.Json)"""
        super(__Angular, self).write(arg0) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Single
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
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer as __RegionInfluencer
__RegionInfluencer = __RegionInfluencer
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as __ParticleControllerComponent
__ParticleControllerComponent = __ParticleControllerComponent
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer as __RegionInfluencer_Single
__Single = __RegionInfluencer_Single.Single
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class Single():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.Single"""
 
    @staticmethod
    def __wrap(java_value: __Single) -> 'Single':
        return Single(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Single):
        """
        Dynamic initializer for Single.
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
    def clear(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.clear()"""
        super(RegionInfluencer, self).clear()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @overload
    def __init__(self, arg0: 'TextureRegion'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Single(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = __Single(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Texture'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Single(com.badlogic.gdx.graphics.Texture)"""
        val = __Single(arg0)
        self.__dict__ = val.__dict__
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
    def setAtlasName(self, arg0: str):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.setAtlasName(java.lang.String)"""
        super(__RegionInfluencer, self).setAtlasName(arg0)

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.activateParticles(int,int)"""
        super(__particles.ParticleControllerComponent, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.update()"""
        super(particles.ParticleControllerComponent, self).update()

    @override
    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(__particles.ParticleControllerComponent, self).killParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__RegionInfluencer, self).read(arg0, arg1)

    @override
    @overload
    def copy(self) -> 'Single':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Single com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Single.copy()"""
        return 'Single'.__wrap(super(Single, self).copy())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Single()"""
        val = __Single()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.write(com.badlogic.gdx.utils.Json)"""
        super(__RegionInfluencer, self).write(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def add(self, *arg0: 'g2d.TextureRegion'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.add(com.badlogic.gdx.graphics.g2d.TextureRegion...)"""
        super(__RegionInfluencer, self).add(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Single'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Single(com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Single)"""
        val = __Single(arg0)
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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Single()"""
        val = __Single()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__RegionInfluencer, self).load(arg0, arg1)

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__RegionInfluencer, self).save(arg0, arg1) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$FaceDirection
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
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as __ParticleControllerComponent
__ParticleControllerComponent = __ParticleControllerComponent
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as __DynamicsModifier
__DynamicsModifier = __DynamicsModifier
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as __DynamicsModifier_FaceDirection
__FaceDirection = __DynamicsModifier_FaceDirection.FaceDirection
from builtins import bool
from builtins import int
 
class FaceDirection():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.FaceDirection"""
 
    @staticmethod
    def __wrap(java_value: __FaceDirection) -> 'FaceDirection':
        return FaceDirection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FaceDirection):
        """
        Dynamic initializer for FaceDirection.
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$FaceDirection()"""
        val = __FaceDirection()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.activateParticles(int,int)"""
        super(__particles.ParticleControllerComponent, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$FaceDirection()"""
        val = __FaceDirection()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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

    @override
    @overload
    def copy(self) -> 'particles.ParticleControllerComponent':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$FaceDirection.copy()"""
        return 'particles.ParticleControllerComponent'.__wrap(super(FaceDirection, self).copy())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'FaceDirection'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$FaceDirection(com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$FaceDirection)"""
        val = __FaceDirection(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$FaceDirection.allocateChannels()"""
        super(FaceDirection, self).allocateChannels()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$FaceDirection.update()"""
        super(FaceDirection, self).update()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__DynamicsModifier, self).read(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.write(com.badlogic.gdx.utils.Json)"""
        super(__DynamicsModifier, self).write(arg0) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer
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
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer as __SpawnInfluencer
__SpawnInfluencer = __SpawnInfluencer
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
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SpawnInfluencer():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer"""
 
    @staticmethod
    def __wrap(java_value: __SpawnInfluencer) -> 'SpawnInfluencer':
        return SpawnInfluencer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SpawnInfluencer):
        """
        Dynamic initializer for SpawnInfluencer.
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
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__SpawnInfluencer, self).read(arg0, arg1)

    @override
    @overload
    def start(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer.start()"""
        super(SpawnInfluencer, self).start()

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
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(__particles.ParticleControllerComponent, self).killParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer.init()"""
        super(SpawnInfluencer, self).init()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer()"""
        val = __SpawnInfluencer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

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

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer.write(com.badlogic.gdx.utils.Json)"""
        super(__SpawnInfluencer, self).write(arg0)

    @overload
    def __init__(self, arg0: 'SpawnShapeValue'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer(com.badlogic.gdx.graphics.g3d.particles.values.SpawnShapeValue)"""
        val = __SpawnInfluencer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer()"""
        val = __SpawnInfluencer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def copy(self) -> 'SpawnInfluencer':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer.copy()"""
        return 'SpawnInfluencer'.__wrap(super(SpawnInfluencer, self).copy())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer.activateParticles(int,int)"""
        super(__SpawnInfluencer, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer.allocateChannels()"""
        super(SpawnInfluencer, self).allocateChannels()

    @overload
    def __init__(self, arg0: 'SpawnInfluencer'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer(com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer)"""
        val = __SpawnInfluencer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__SpawnInfluencer, self).save(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SpawnInfluencer.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__SpawnInfluencer, self).load(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer
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
import com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer as __Influencer
__Influencer = __Influencer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Influencer(ABC):
    """com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer"""
 
    @staticmethod
    def __wrap(java_value: __Influencer) -> 'Influencer':
        return Influencer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Influencer):
        """
        Dynamic initializer for Influencer.
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
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.activateParticles(int,int)"""
        super(__particles.ParticleControllerComponent, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

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
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__particles.ParticleControllerComponent, self).load(arg0, arg1)

    @override
    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(__particles.ParticleControllerComponent, self).killParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer()"""
        val = __Influencer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

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

    @abstractmethod
    def copy(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.copy()"""
        pass

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__particles.ParticleControllerComponent, self).read(arg0, arg1)

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(__particles.ParticleControllerComponent, self).write(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.Influencer()"""
        val = __Influencer()
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerFinalizerInfluencer
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
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerFinalizerInfluencer as __ParticleControllerFinalizerInfluencer
__ParticleControllerFinalizerInfluencer = __ParticleControllerFinalizerInfluencer
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
 
class ParticleControllerFinalizerInfluencer():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerFinalizerInfluencer"""
 
    @staticmethod
    def __wrap(java_value: __ParticleControllerFinalizerInfluencer) -> 'ParticleControllerFinalizerInfluencer':
        return ParticleControllerFinalizerInfluencer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleControllerFinalizerInfluencer):
        """
        Dynamic initializer for ParticleControllerFinalizerInfluencer.
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
    def copy(self) -> 'ParticleControllerFinalizerInfluencer':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerFinalizerInfluencer com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerFinalizerInfluencer.copy()"""
        return 'ParticleControllerFinalizerInfluencer'.__wrap(super(ParticleControllerFinalizerInfluencer, self).copy())

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.activateParticles(int,int)"""
        super(__particles.ParticleControllerComponent, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerFinalizerInfluencer()"""
        val = __ParticleControllerFinalizerInfluencer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerFinalizerInfluencer()"""
        val = __ParticleControllerFinalizerInfluencer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__particles.ParticleControllerComponent, self).read(arg0, arg1)

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(__particles.ParticleControllerComponent, self).write(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerFinalizerInfluencer.allocateChannels()"""
        super(ParticleControllerFinalizerInfluencer, self).allocateChannels()

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
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerFinalizerInfluencer.update()"""
        super(ParticleControllerFinalizerInfluencer, self).update()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Animated
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
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer as __RegionInfluencer
__RegionInfluencer = __RegionInfluencer
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as __ParticleControllerComponent
__ParticleControllerComponent = __ParticleControllerComponent
import com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer as __RegionInfluencer_Animated
__Animated = __RegionInfluencer_Animated.Animated
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
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import int
 
class Animated():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.Animated"""
 
    @staticmethod
    def __wrap(java_value: __Animated) -> 'Animated':
        return Animated(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Animated):
        """
        Dynamic initializer for Animated.
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
    def clear(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.clear()"""
        super(RegionInfluencer, self).clear()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

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
    def setAtlasName(self, arg0: str):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.setAtlasName(java.lang.String)"""
        super(__RegionInfluencer, self).setAtlasName(arg0)

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.activateParticles(int,int)"""
        super(__particles.ParticleControllerComponent, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

    @override
    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.killParticles(int,int)"""
        super(__particles.ParticleControllerComponent, self).killParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'TextureRegion'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Animated(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        val = __Animated(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__RegionInfluencer, self).read(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Animated()"""
        val = __Animated()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Animated.update()"""
        super(Animated, self).update()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Animated'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Animated(com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Animated)"""
        val = __Animated(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.write(com.badlogic.gdx.utils.Json)"""
        super(__RegionInfluencer, self).write(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Animated()"""
        val = __Animated()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def copy(self) -> 'Animated':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Animated com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Animated.copy()"""
        return 'Animated'.__wrap(super(Animated, self).copy())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def add(self, *arg0: 'g2d.TextureRegion'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.add(com.badlogic.gdx.graphics.g2d.TextureRegion...)"""
        super(__RegionInfluencer, self).add(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Texture'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer$Animated(com.badlogic.gdx.graphics.Texture)"""
        val = __Animated(arg0)
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__RegionInfluencer, self).load(arg0, arg1)

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.RegionInfluencer.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__RegionInfluencer, self).save(arg0, arg1) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$TangentialAcceleration
from pyquantum_helper import import_once as __import_once__
from builtins import str
import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as __DynamicsModifier_TangentialAcceleration
__TangentialAcceleration = __DynamicsModifier_TangentialAcceleration.TangentialAcceleration
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

import com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier as __DynamicsModifier_Angular
__Angular = __DynamicsModifier_Angular.Angular
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
 
class TangentialAcceleration():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier.TangentialAcceleration"""
 
    @staticmethod
    def __wrap(java_value: __TangentialAcceleration) -> 'TangentialAcceleration':
        return TangentialAcceleration(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TangentialAcceleration):
        """
        Dynamic initializer for TangentialAcceleration.
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

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

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

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__Angular, self).read(arg0, arg1)

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$TangentialAcceleration()"""
        val = __TangentialAcceleration()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

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
    def __init__(self, arg0: 'TangentialAcceleration'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$TangentialAcceleration(com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$TangentialAcceleration)"""
        val = __TangentialAcceleration(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$TangentialAcceleration.allocateChannels()"""
        super(TangentialAcceleration, self).allocateChannels()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def copy(self) -> 'TangentialAcceleration':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$TangentialAcceleration com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$TangentialAcceleration.copy()"""
        return 'TangentialAcceleration'.__wrap(super(TangentialAcceleration, self).copy())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$TangentialAcceleration()"""
        val = __TangentialAcceleration()
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
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.activateParticles(int,int)"""
        super(__Angular, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.DynamicsModifier$Angular.write(com.badlogic.gdx.utils.Json)"""
        super(__Angular, self).write(arg0) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.ScaleInfluencer
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
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as __ParticleControllerComponent
__ParticleControllerComponent = __ParticleControllerComponent
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g3d.particles.influencers.ScaleInfluencer as __ScaleInfluencer
__ScaleInfluencer = __ScaleInfluencer
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer as __SimpleInfluencer
__SimpleInfluencer = __SimpleInfluencer
from builtins import int
 
class ScaleInfluencer():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.ScaleInfluencer"""
 
    @staticmethod
    def __wrap(java_value: __ScaleInfluencer) -> 'ScaleInfluencer':
        return ScaleInfluencer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ScaleInfluencer):
        """
        Dynamic initializer for ScaleInfluencer.
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
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ScaleInfluencer()"""
        val = __ScaleInfluencer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__SimpleInfluencer, self).read(arg0, arg1)

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__particles.ParticleControllerComponent, self).save(arg0, arg1)

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

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ScaleInfluencer.activateParticles(int,int)"""
        super(__ScaleInfluencer, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'ScaleInfluencer'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ScaleInfluencer(com.badlogic.gdx.graphics.g3d.particles.influencers.ScaleInfluencer)"""
        val = __ScaleInfluencer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer.write(com.badlogic.gdx.utils.Json)"""
        super(__SimpleInfluencer, self).write(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ScaleInfluencer()"""
        val = __ScaleInfluencer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.SimpleInfluencer.allocateChannels()"""
        super(SimpleInfluencer, self).allocateChannels()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def copy(self) -> 'particles.ParticleControllerComponent':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.influencers.ScaleInfluencer.copy()"""
        return 'particles.ParticleControllerComponent'.__wrap(super(ScaleInfluencer, self).copy())

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single
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
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as __ParticleControllerComponent
__ParticleControllerComponent = __ParticleControllerComponent
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer as __ParticleControllerInfluencer
__ParticleControllerInfluencer = __ParticleControllerInfluencer
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer as __ParticleControllerInfluencer_Single
__Single = __ParticleControllerInfluencer_Single.Single
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Single():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.Single"""
 
    @staticmethod
    def __wrap(java_value: __Single) -> 'Single':
        return Single(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Single):
        """
        Dynamic initializer for Single.
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
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single.killParticles(int,int)"""
        super(__Single, self).killParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single()"""
        val = __Single()
        self.__dict__ = val.__dict__
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
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.update()"""
        super(particles.ParticleControllerComponent, self).update()

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__ParticleControllerInfluencer, self).load(arg0, arg1)

    @overload
    def __init__(self, *arg0: 'particles.ParticleController'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single(com.badlogic.gdx.graphics.g3d.particles.ParticleController...)"""
        val = __Single(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def set(self, arg0: 'ParticleController'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(__particles.ParticleControllerComponent, self).set(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single.init()"""
        super(Single, self).init()

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__particles.ParticleControllerComponent, self).read(arg0, arg1)

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(__particles.ParticleControllerComponent, self).write(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.end()"""
        super(ParticleControllerInfluencer, self).end()

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__ParticleControllerInfluencer, self).save(arg0, arg1)

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
    def copy(self) -> 'Single':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single.copy()"""
        return 'Single'.__wrap(super(Single, self).copy())

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single.activateParticles(int,int)"""
        super(__Single, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Single'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single(com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single)"""
        val = __Single(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ParticleControllerInfluencer$Single()"""
        val = __Single()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Random
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
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = __import_once__("pygdx.graphics.g3d")

try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer as __ModelInfluencer
__ModelInfluencer = __ModelInfluencer
import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as __ParticleControllerComponent
__ParticleControllerComponent = __ParticleControllerComponent
import com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer as __ModelInfluencer_Random
__Random = __ModelInfluencer_Random.Random
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
 
class Random():
    """com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer.Random"""
 
    @staticmethod
    def __wrap(java_value: __Random) -> 'Random':
        return Random(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Random):
        """
        Dynamic initializer for Random.
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
    def __init__(self, arg0: 'Random'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Random(com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Random)"""
        val = __Random(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Random.init()"""
        super(Random, self).init()

    @override
    @overload
    def activateParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Random.activateParticles(int,int)"""
        super(__Random, self).activateParticles(__int.valueOf(arg0), __int.valueOf(arg1))

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
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Random()"""
        val = __Random()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def copy(self) -> 'Random':
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Random com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Random.copy()"""
        return 'Random'.__wrap(super(Random, self).copy())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__particles.ParticleControllerComponent, self).read(arg0, arg1)

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer.allocateChannels()"""
        super(ModelInfluencer, self).allocateChannels()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(__particles.ParticleControllerComponent, self).write(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def killParticles(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Random.killParticles(int,int)"""
        super(__Random, self).killParticles(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__ModelInfluencer, self).save(arg0, arg1)

    @overload
    def __init__(self, *arg0: 'g3d.Model'):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Random(com.badlogic.gdx.graphics.g3d.Model...)"""
        val = __Random(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__ModelInfluencer, self).load(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.influencers.ModelInfluencer$Random()"""
        val = __Random()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()