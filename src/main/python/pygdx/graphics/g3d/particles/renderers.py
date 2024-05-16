from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer as __ModelInstanceRenderer
__ModelInstanceRenderer = __ModelInstanceRenderer
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
try:
    from pygdx.graphics.g3d.particles import batches
except ImportError:
    batches = __import_once__("pygdx.graphics.g3d.particles.batches")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer as __ParticleControllerRenderer
__ParticleControllerRenderer = __ParticleControllerRenderer
from builtins import int
 
class ModelInstanceRenderer():
    """com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer"""
 
    @staticmethod
    def __wrap(java_value: __ModelInstanceRenderer) -> 'ModelInstanceRenderer':
        return ModelInstanceRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModelInstanceRenderer):
        """
        Dynamic initializer for ModelInstanceRenderer.
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
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer.allocateChannels()"""
        super(ModelInstanceRenderer, self).allocateChannels()

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__particles.ParticleControllerComponent, self).save(arg0, arg1)

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer.init()"""
        super(ModelInstanceRenderer, self).init()

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @overload
    def isCompatible(self, arg0: 'ParticleBatch') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer.isCompatible(com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>)"""
        return bool.__wrap(super(__ModelInstanceRenderer, self).isCompatible(arg0))

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
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer.update()"""
        super(ModelInstanceRenderer, self).update()

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

    @override
    @overload
    def set(self, arg0: 'ParticleController'):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(__ParticleControllerRenderer, self).set(arg0)

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer()"""
        val = __ModelInstanceRenderer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__particles.ParticleControllerComponent, self).read(arg0, arg1)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer()"""
        val = __ModelInstanceRenderer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def setBatch(self, arg0: 'ParticleBatch') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.setBatch(com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>)"""
        return bool.__wrap(super(__ParticleControllerRenderer, self).setBatch(arg0))

    @overload
    def __init__(self, arg0: 'ModelInstanceParticleBatch'):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer(com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch)"""
        val = __ModelInstanceRenderer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def copy(self) -> 'particles.ParticleControllerComponent':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer.copy()"""
        return 'particles.ParticleControllerComponent'.__wrap(super(ModelInstanceRenderer, self).copy())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer as __ModelInstanceRenderer
__ModelInstanceRenderer = __ModelInstanceRenderer
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
try:
    from pygdx.graphics.g3d.particles import batches
except ImportError:
    batches = __import_once__("pygdx.graphics.g3d.particles.batches")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer as __ParticleControllerRenderer
__ParticleControllerRenderer = __ParticleControllerRenderer
from builtins import int
 
class ModelInstanceRenderer():
    """com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer"""
 
    @staticmethod
    def __wrap(java_value: __ModelInstanceRenderer) -> 'ModelInstanceRenderer':
        return ModelInstanceRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModelInstanceRenderer):
        """
        Dynamic initializer for ModelInstanceRenderer.
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
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer.allocateChannels()"""
        super(ModelInstanceRenderer, self).allocateChannels()

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__particles.ParticleControllerComponent, self).save(arg0, arg1)

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer.init()"""
        super(ModelInstanceRenderer, self).init()

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @overload
    def isCompatible(self, arg0: 'ParticleBatch') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer.isCompatible(com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>)"""
        return bool.__wrap(super(__ModelInstanceRenderer, self).isCompatible(arg0))

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
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer.update()"""
        super(ModelInstanceRenderer, self).update()

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

    @override
    @overload
    def set(self, arg0: 'ParticleController'):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(__ParticleControllerRenderer, self).set(arg0)

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer()"""
        val = __ModelInstanceRenderer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(__particles.ParticleControllerComponent, self).read(arg0, arg1)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer()"""
        val = __ModelInstanceRenderer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def setBatch(self, arg0: 'ParticleBatch') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.setBatch(com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>)"""
        return bool.__wrap(super(__ParticleControllerRenderer, self).setBatch(arg0))

    @overload
    def __init__(self, arg0: 'ModelInstanceParticleBatch'):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer(com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch)"""
        val = __ModelInstanceRenderer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def copy(self) -> 'particles.ParticleControllerComponent':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer.copy()"""
        return 'particles.ParticleControllerComponent'.__wrap(super(ModelInstanceRenderer, self).copy())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardRenderer
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
try:
    from pygdx.graphics.g3d.particles import batches
except ImportError:
    batches = __import_once__("pygdx.graphics.g3d.particles.batches")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardRenderer as __BillboardRenderer
__BillboardRenderer = __BillboardRenderer
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer as __ParticleControllerRenderer
__ParticleControllerRenderer = __ParticleControllerRenderer
from builtins import int
 
class BillboardRenderer():
    """com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardRenderer"""
 
    @staticmethod
    def __wrap(java_value: __BillboardRenderer) -> 'BillboardRenderer':
        return BillboardRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BillboardRenderer):
        """
        Dynamic initializer for BillboardRenderer.
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
    def isCompatible(self, arg0: 'ParticleBatch') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardRenderer.isCompatible(com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>)"""
        return bool.__wrap(super(__BillboardRenderer, self).isCompatible(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardRenderer.allocateChannels()"""
        super(BillboardRenderer, self).allocateChannels()

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
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(__ParticleControllerRenderer, self).set(arg0)

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.update()"""
        super(ParticleControllerRenderer, self).update()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardRenderer()"""
        val = __BillboardRenderer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardRenderer()"""
        val = __BillboardRenderer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'BillboardParticleBatch'):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardRenderer(com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch)"""
        val = __BillboardRenderer(arg0)
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
    def copy(self) -> 'particles.ParticleControllerComponent':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardRenderer.copy()"""
        return 'particles.ParticleControllerComponent'.__wrap(super(BillboardRenderer, self).copy())

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
    def setBatch(self, arg0: 'ParticleBatch') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.setBatch(com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>)"""
        return bool.__wrap(super(__ParticleControllerRenderer, self).setBatch(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteControllerRenderData
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
import com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteControllerRenderData as __PointSpriteControllerRenderData
__PointSpriteControllerRenderData = __PointSpriteControllerRenderData
from builtins import bool
from builtins import int
 
class PointSpriteControllerRenderData():
    """com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteControllerRenderData"""
 
    @staticmethod
    def __wrap(java_value: __PointSpriteControllerRenderData) -> 'PointSpriteControllerRenderData':
        return PointSpriteControllerRenderData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PointSpriteControllerRenderData):
        """
        Dynamic initializer for PointSpriteControllerRenderData.
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
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteControllerRenderData()"""
        val = __PointSpriteControllerRenderData()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteControllerRenderData()"""
        val = __PointSpriteControllerRenderData()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardControllerRenderData
import com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardControllerRenderData as __BillboardControllerRenderData
__BillboardControllerRenderData = __BillboardControllerRenderData
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
 
class BillboardControllerRenderData():
    """com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardControllerRenderData"""
 
    @staticmethod
    def __wrap(java_value: __BillboardControllerRenderData) -> 'BillboardControllerRenderData':
        return BillboardControllerRenderData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BillboardControllerRenderData):
        """
        Dynamic initializer for BillboardControllerRenderData.
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
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardControllerRenderData()"""
        val = __BillboardControllerRenderData()
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardControllerRenderData()"""
        val = __BillboardControllerRenderData()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer
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
try:
    from pygdx.graphics.g3d.particles import batches
except ImportError:
    batches = __import_once__("pygdx.graphics.g3d.particles.batches")

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
import com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer as __ParticleControllerRenderer
__ParticleControllerRenderer = __ParticleControllerRenderer
from builtins import bool
from builtins import int
 
class ParticleControllerRenderer(ABC):
    """com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer"""
 
    @staticmethod
    def __wrap(java_value: __ParticleControllerRenderer) -> 'ParticleControllerRenderer':
        return ParticleControllerRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleControllerRenderer):
        """
        Dynamic initializer for ParticleControllerRenderer.
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
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(__ParticleControllerRenderer, self).set(arg0)

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.update()"""
        super(ParticleControllerRenderer, self).update()

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

    @abstractmethod
    def isCompatible(self, arg0: 'ParticleBatch'):
        """public abstract boolean com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.isCompatible(com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>)"""
        pass

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
    def setBatch(self, arg0: 'ParticleBatch') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.setBatch(com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>)"""
        return bool.__wrap(super(__ParticleControllerRenderer, self).setBatch(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerControllerRenderer
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
import com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerControllerRenderer as __ParticleControllerControllerRenderer
__ParticleControllerControllerRenderer = __ParticleControllerControllerRenderer
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as __ParticleControllerComponent
__ParticleControllerComponent = __ParticleControllerComponent
try:
    from pygdx.graphics.g3d.particles import batches
except ImportError:
    batches = __import_once__("pygdx.graphics.g3d.particles.batches")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer as __ParticleControllerRenderer
__ParticleControllerRenderer = __ParticleControllerRenderer
from builtins import int
 
class ParticleControllerControllerRenderer():
    """com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerControllerRenderer"""
 
    @staticmethod
    def __wrap(java_value: __ParticleControllerControllerRenderer) -> 'ParticleControllerControllerRenderer':
        return ParticleControllerControllerRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleControllerControllerRenderer):
        """
        Dynamic initializer for ParticleControllerControllerRenderer.
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
    def copy(self) -> 'particles.ParticleControllerComponent':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerControllerRenderer.copy()"""
        return 'particles.ParticleControllerComponent'.__wrap(super(ParticleControllerControllerRenderer, self).copy())

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
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerControllerRenderer.update()"""
        super(ParticleControllerControllerRenderer, self).update()

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerControllerRenderer()"""
        val = __ParticleControllerControllerRenderer()
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
    def set(self, arg0: 'ParticleController'):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(__ParticleControllerRenderer, self).set(arg0)

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
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(__particles.ParticleControllerComponent, self).write(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerControllerRenderer()"""
        val = __ParticleControllerControllerRenderer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def isCompatible(self, arg0: 'ParticleBatch') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerControllerRenderer.isCompatible(com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch)"""
        return bool.__wrap(super(__ParticleControllerControllerRenderer, self).isCompatible(arg0))

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
    def setBatch(self, arg0: 'ParticleBatch') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.setBatch(com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>)"""
        return bool.__wrap(super(__ParticleControllerRenderer, self).setBatch(arg0))

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerControllerRenderer.init()"""
        super(ParticleControllerControllerRenderer, self).init()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceControllerRenderData
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceControllerRenderData as __ModelInstanceControllerRenderData
__ModelInstanceControllerRenderData = __ModelInstanceControllerRenderData
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ModelInstanceControllerRenderData():
    """com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceControllerRenderData"""
 
    @staticmethod
    def __wrap(java_value: __ModelInstanceControllerRenderData) -> 'ModelInstanceControllerRenderData':
        return ModelInstanceControllerRenderData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModelInstanceControllerRenderData):
        """
        Dynamic initializer for ModelInstanceControllerRenderData.
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceControllerRenderData()"""
        val = __ModelInstanceControllerRenderData()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceControllerRenderData()"""
        val = __ModelInstanceControllerRenderData()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderData
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
import com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderData as __ParticleControllerRenderData
__ParticleControllerRenderData = __ParticleControllerRenderData
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ParticleControllerRenderData(ABC):
    """com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderData"""
 
    @staticmethod
    def __wrap(java_value: __ParticleControllerRenderData) -> 'ParticleControllerRenderData':
        return ParticleControllerRenderData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleControllerRenderData):
        """
        Dynamic initializer for ParticleControllerRenderData.
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderData()"""
        val = __ParticleControllerRenderData()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderData()"""
        val = __ParticleControllerRenderData()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteRenderer
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

import com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteRenderer as __PointSpriteRenderer
__PointSpriteRenderer = __PointSpriteRenderer
import com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent as __ParticleControllerComponent
__ParticleControllerComponent = __ParticleControllerComponent
try:
    from pygdx.graphics.g3d.particles import batches
except ImportError:
    batches = __import_once__("pygdx.graphics.g3d.particles.batches")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer as __ParticleControllerRenderer
__ParticleControllerRenderer = __ParticleControllerRenderer
from builtins import int
 
class PointSpriteRenderer():
    """com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteRenderer"""
 
    @staticmethod
    def __wrap(java_value: __PointSpriteRenderer) -> 'PointSpriteRenderer':
        return PointSpriteRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PointSpriteRenderer):
        """
        Dynamic initializer for PointSpriteRenderer.
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
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(__ParticleControllerRenderer, self).set(arg0)

    @override
    @overload
    def copy(self) -> 'particles.ParticleControllerComponent':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteRenderer.copy()"""
        return 'particles.ParticleControllerComponent'.__wrap(super(PointSpriteRenderer, self).copy())

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.update()"""
        super(ParticleControllerRenderer, self).update()

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
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteRenderer()"""
        val = __PointSpriteRenderer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(__particles.ParticleControllerComponent, self).write(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def isCompatible(self, arg0: 'ParticleBatch') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteRenderer.isCompatible(com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>)"""
        return bool.__wrap(super(__PointSpriteRenderer, self).isCompatible(arg0))

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
    def setBatch(self, arg0: 'ParticleBatch') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.setBatch(com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>)"""
        return bool.__wrap(super(__ParticleControllerRenderer, self).setBatch(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteRenderer()"""
        val = __PointSpriteRenderer()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteRenderer.allocateChannels()"""
        super(PointSpriteRenderer, self).allocateChannels()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'PointSpriteParticleBatch'):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteRenderer(com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch)"""
        val = __PointSpriteRenderer(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val