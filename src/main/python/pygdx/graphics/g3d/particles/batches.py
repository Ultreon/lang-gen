from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = __import_once__("pygdx.graphics.g3d.particles")

try:
    from pygdx.graphics.g3d.particles import renderers
except ImportError:
    renderers = __import_once__("pygdx.graphics.g3d.particles.renderers")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import com.badlogic.gdx.graphics.g3d.RenderableProvider as __RenderableProvider
__RenderableProvider = __RenderableProvider
import com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch as __ParticleBatch
__ParticleBatch = __ParticleBatch
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

from abc import abstractmethod, ABC
 
class ParticleBatch(ABC):
    """com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch"""
 
    @staticmethod
    def __wrap(java_value: __ParticleBatch) -> 'ParticleBatch':
        return ParticleBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleBatch):
        """
        Dynamic initializer for ParticleBatch.
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
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        pass

    @abstractmethod
    def end(self, ):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch.end()"""
        pass

    @abstractmethod
    def getRenderables(self, arg0: 'Array', arg1: 'Pool'):
        """public abstract void com.badlogic.gdx.graphics.g3d.RenderableProvider.getRenderables(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>,com.badlogic.gdx.utils.Pool<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        pass

    @abstractmethod
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'ParticleControllerRenderData'):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch.draw(T)"""
        pass

    @abstractmethod
    def begin(self, ):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch.begin()"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = __import_once__("pygdx.graphics.g3d.particles")

try:
    from pygdx.graphics.g3d.particles import renderers
except ImportError:
    renderers = __import_once__("pygdx.graphics.g3d.particles.renderers")

try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import com.badlogic.gdx.graphics.g3d.RenderableProvider as __RenderableProvider
__RenderableProvider = __RenderableProvider
import com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch as __ParticleBatch
__ParticleBatch = __ParticleBatch
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

from abc import abstractmethod, ABC
 
class ParticleBatch(ABC):
    """com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch"""
 
    @staticmethod
    def __wrap(java_value: __ParticleBatch) -> 'ParticleBatch':
        return ParticleBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParticleBatch):
        """
        Dynamic initializer for ParticleBatch.
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
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        pass

    @abstractmethod
    def end(self, ):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch.end()"""
        pass

    @abstractmethod
    def getRenderables(self, arg0: 'Array', arg1: 'Pool'):
        """public abstract void com.badlogic.gdx.graphics.g3d.RenderableProvider.getRenderables(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>,com.badlogic.gdx.utils.Pool<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        pass

    @abstractmethod
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        pass

    @abstractmethod
    def draw(self, arg0: 'ParticleControllerRenderData'):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch.draw(T)"""
        pass

    @abstractmethod
    def begin(self, ):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch.begin()"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch$Config
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = __import_once__("pygdx.graphics.g3d.particles")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch as __BillboardParticleBatch_Config
__Config = __BillboardParticleBatch_Config.Config
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Config():
    """com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.Config"""
 
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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch$Config()"""
        val = __Config()
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
    def __init__(self, arg0: bool, arg1: 'AlignMode'):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch$Config(boolean,com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode)"""
        val = __Config(__boolean.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch$Config()"""
        val = __Config()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.graphics.g3d.particles import renderers
except ImportError:
    renderers = __import_once__("pygdx.graphics.g3d.particles.renderers")

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
import com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch as __ParticleBatch
__ParticleBatch = __ParticleBatch
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

from abc import abstractmethod, ABC
import com.badlogic.gdx.graphics.g3d.particles.ParticleSorter as __ParticleSorter
__ParticleSorter = __ParticleSorter
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.graphics.g3d.RenderableProvider as __RenderableProvider
__RenderableProvider = __RenderableProvider
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch as __BufferedParticleBatch
__BufferedParticleBatch = __BufferedParticleBatch
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class BufferedParticleBatch(ABC):
    """com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch"""
 
    @staticmethod
    def __wrap(java_value: __BufferedParticleBatch) -> 'BufferedParticleBatch':
        return BufferedParticleBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BufferedParticleBatch):
        """
        Dynamic initializer for BufferedParticleBatch.
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
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.end()"""
        super(BufferedParticleBatch, self).end()

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
    def resetCapacity(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.resetCapacity()"""
        super(BufferedParticleBatch, self).resetCapacity()

    @overload
    def getSorter(self) -> 'particles.ParticleSorter':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleSorter com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.getSorter()"""
        return 'particles.ParticleSorter'.__wrap(super(BufferedParticleBatch, self).getSorter())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(__BufferedParticleBatch, self).setCamera(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def setSorter(self, arg0: 'ParticleSorter'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.setSorter(com.badlogic.gdx.graphics.g3d.particles.ParticleSorter)"""
        super(__BufferedParticleBatch, self).setSorter(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @abstractmethod
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        pass

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def getRenderables(self, arg0: 'Array', arg1: 'Pool'):
        """public abstract void com.badlogic.gdx.graphics.g3d.RenderableProvider.getRenderables(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>,com.badlogic.gdx.utils.Pool<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        pass

    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.ensureCapacity(int)"""
        super(__BufferedParticleBatch, self).ensureCapacity(__int.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @abstractmethod
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        pass

    @override
    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.begin()"""
        super(BufferedParticleBatch, self).begin()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def draw(self, arg0: 'ParticleControllerRenderData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.draw(T)"""
        super(__BufferedParticleBatch, self).draw(arg0)

    @overload
    def getBufferedCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.getBufferedCount()"""
        return int.__wrap(super(BufferedParticleBatch, self).getBufferedCount())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch
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

try:
    from pygdx.graphics.g3d.particles import renderers
except ImportError:
    renderers = __import_once__("pygdx.graphics.g3d.particles.renderers")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute as __BlendingAttribute
__BlendingAttribute = __BlendingAttribute
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.ParticleSorter as __ParticleSorter
__ParticleSorter = __ParticleSorter
try:
    from pygdx.graphics.g3d import attributes
except ImportError:
    attributes = __import_once__("pygdx.graphics.g3d.attributes")

import com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch as __PointSpriteParticleBatch
__PointSpriteParticleBatch = __PointSpriteParticleBatch
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Texture as __Texture
__Texture = __Texture
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

import com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch as __BufferedParticleBatch
__BufferedParticleBatch = __BufferedParticleBatch
from builtins import bool
from builtins import int
 
class PointSpriteParticleBatch():
    """com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch"""
 
    @staticmethod
    def __wrap(java_value: __PointSpriteParticleBatch) -> 'PointSpriteParticleBatch':
        return PointSpriteParticleBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PointSpriteParticleBatch):
        """
        Dynamic initializer for PointSpriteParticleBatch.
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
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch.getTexture()"""
        return 'graphics.Texture'.__wrap(super(PointSpriteParticleBatch, self).getTexture())

    @override
    @overload
    def resetCapacity(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.resetCapacity()"""
        super(BufferedParticleBatch, self).resetCapacity()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch()"""
        val = __PointSpriteParticleBatch()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setSorter(self, arg0: 'ParticleSorter'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.setSorter(com.badlogic.gdx.graphics.g3d.particles.ParticleSorter)"""
        super(__BufferedParticleBatch, self).setSorter(arg0)

    @overload
    def __init__(self, arg0: int, arg1: 'Config'):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch(int,com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config)"""
        val = __PointSpriteParticleBatch(__int.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: 'Config', arg2: 'BlendingAttribute', arg3: 'DepthTestAttribute'):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch(int,com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config,com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute,com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute)"""
        val = __PointSpriteParticleBatch(__int.valueOf(arg0), arg1, arg2, arg3)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__PointSpriteParticleBatch, self).save(arg0, arg1)

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__PointSpriteParticleBatch, self).load(arg0, arg1)

    @override
    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.ensureCapacity(int)"""
        super(__BufferedParticleBatch, self).ensureCapacity(__int.valueOf(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getBufferedCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.getBufferedCount()"""
        return int.__wrap(super(BufferedParticleBatch, self).getBufferedCount())

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.end()"""
        super(BufferedParticleBatch, self).end()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch()"""
        val = __PointSpriteParticleBatch()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(__BufferedParticleBatch, self).setCamera(arg0)

    @overload
    def setTexture(self, arg0: 'Texture'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch.setTexture(com.badlogic.gdx.graphics.Texture)"""
        super(__PointSpriteParticleBatch, self).setTexture(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getBlendingAttribute(self) -> 'attributes.BlendingAttribute':
        """public com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch.getBlendingAttribute()"""
        return 'attributes.BlendingAttribute'.__wrap(super(PointSpriteParticleBatch, self).getBlendingAttribute())

    @override
    @overload
    def getRenderables(self, arg0: 'Array', arg1: 'Pool'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch.getRenderables(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>,com.badlogic.gdx.utils.Pool<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        super(__PointSpriteParticleBatch, self).getRenderables(arg0, arg1)

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch(int)"""
        val = __PointSpriteParticleBatch(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.begin()"""
        super(BufferedParticleBatch, self).begin()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def draw(self, arg0: 'ParticleControllerRenderData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.draw(T)"""
        super(__BufferedParticleBatch, self).draw(arg0)

    @override
    @overload
    def getSorter(self) -> 'particles.ParticleSorter':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleSorter com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.getSorter()"""
        return 'particles.ParticleSorter'.__wrap(super(BufferedParticleBatch, self).getSorter()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = __import_once__("pygdx.graphics.g3d.particles")

try:
    from pygdx.graphics.g3d.particles import renderers
except ImportError:
    renderers = __import_once__("pygdx.graphics.g3d.particles.renderers")

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

import com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch as __ModelInstanceParticleBatch
__ModelInstanceParticleBatch = __ModelInstanceParticleBatch
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
 
class ModelInstanceParticleBatch():
    """com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch"""
 
    @staticmethod
    def __wrap(java_value: __ModelInstanceParticleBatch) -> 'ModelInstanceParticleBatch':
        return ModelInstanceParticleBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ModelInstanceParticleBatch):
        """
        Dynamic initializer for ModelInstanceParticleBatch.
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
    def draw(self, arg0: 'ModelInstanceControllerRenderData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch.draw(com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceControllerRenderData)"""
        super(__ModelInstanceParticleBatch, self).draw(arg0)

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
        """public com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch()"""
        val = __ModelInstanceParticleBatch()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch.begin()"""
        super(ModelInstanceParticleBatch, self).begin()

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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch()"""
        val = __ModelInstanceParticleBatch()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch.end()"""
        super(ModelInstanceParticleBatch, self).end()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def getRenderables(self, arg0: 'Array', arg1: 'Pool'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch.getRenderables(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>,com.badlogic.gdx.utils.Pool<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        super(__ModelInstanceParticleBatch, self).getRenderables(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__ModelInstanceParticleBatch, self).load(arg0, arg1)

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__ModelInstanceParticleBatch, self).save(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getBufferedCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch.getBufferedCount()"""
        return int.__wrap(super(ModelInstanceParticleBatch, self).getBufferedCount()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch
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

try:
    from pygdx.graphics.g3d.particles import renderers
except ImportError:
    renderers = __import_once__("pygdx.graphics.g3d.particles.renderers")

from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute as __BlendingAttribute
__BlendingAttribute = __BlendingAttribute
try:
    from pygdx import assets
except ImportError:
    assets = __import_once__("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.ParticleSorter as __ParticleSorter
__ParticleSorter = __ParticleSorter
try:
    from pygdx.graphics.g3d import attributes
except ImportError:
    attributes = __import_once__("pygdx.graphics.g3d.attributes")

import com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch as __BillboardParticleBatch
__BillboardParticleBatch = __BillboardParticleBatch
import java.lang.Long as __long
import com.badlogic.gdx.graphics.g3d.particles.ParticleShader as __ParticleShader_AlignMode
__AlignMode = __ParticleShader_AlignMode.AlignMode
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.Texture as __Texture
__Texture = __Texture
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
import com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch as __BufferedParticleBatch
__BufferedParticleBatch = __BufferedParticleBatch
from builtins import int
 
class BillboardParticleBatch():
    """com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch"""
 
    @staticmethod
    def __wrap(java_value: __BillboardParticleBatch) -> 'BillboardParticleBatch':
        return BillboardParticleBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BillboardParticleBatch):
        """
        Dynamic initializer for BillboardParticleBatch.
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
    def setTexture(self, arg0: 'Texture'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.setTexture(com.badlogic.gdx.graphics.Texture)"""
        super(__BillboardParticleBatch, self).setTexture(arg0)

    @override
    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.begin()"""
        super(BillboardParticleBatch, self).begin()

    @override
    @overload
    def resetCapacity(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.resetCapacity()"""
        super(BufferedParticleBatch, self).resetCapacity()

    @overload
    def setVertexData(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.setVertexData()"""
        super(BillboardParticleBatch, self).setVertexData()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def setSorter(self, arg0: 'ParticleSorter'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.setSorter(com.badlogic.gdx.graphics.g3d.particles.ParticleSorter)"""
        super(__BufferedParticleBatch, self).setSorter(arg0)

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__BillboardParticleBatch, self).load(arg0, arg1)

    @override
    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.ensureCapacity(int)"""
        super(__BufferedParticleBatch, self).ensureCapacity(__int.valueOf(arg0))

    @overload
    def getAlignMode(self) -> 'particles.ParticleShader$AlignMode':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.getAlignMode()"""
        return 'particles.ParticleShader$AlignMode'.__wrap(super(BillboardParticleBatch, self).getAlignMode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: 'AlignMode', arg1: bool, arg2: int):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch(com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode,boolean,int)"""
        val = __BillboardParticleBatch(arg0, __boolean.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def getBufferedCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.getBufferedCount()"""
        return int.__wrap(super(BufferedParticleBatch, self).getBufferedCount())

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.end()"""
        super(BufferedParticleBatch, self).end()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getBlendingAttribute(self) -> 'attributes.BlendingAttribute':
        """public com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.getBlendingAttribute()"""
        return 'attributes.BlendingAttribute'.__wrap(super(BillboardParticleBatch, self).getBlendingAttribute())

    @overload
    def __init__(self, arg0: 'AlignMode', arg1: bool, arg2: int, arg3: 'BlendingAttribute', arg4: 'DepthTestAttribute'):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch(com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode,boolean,int,com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute,com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute)"""
        val = __BillboardParticleBatch(arg0, __boolean.valueOf(arg1), __int.valueOf(arg2), arg3, arg4)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setAlignMode(self, arg0: 'AlignMode'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.setAlignMode(com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode)"""
        super(__BillboardParticleBatch, self).setAlignMode(arg0)

    @overload
    def allocParticlesData(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.allocParticlesData(int)"""
        super(__BillboardParticleBatch, self).allocParticlesData(__int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(__BufferedParticleBatch, self).setCamera(arg0)

    @overload
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.getTexture()"""
        return 'graphics.Texture'.__wrap(super(BillboardParticleBatch, self).getTexture())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch()"""
        val = __BillboardParticleBatch()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getRenderables(self, arg0: 'Array', arg1: 'Pool'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.getRenderables(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>,com.badlogic.gdx.utils.Pool<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        super(__BillboardParticleBatch, self).getRenderables(arg0, arg1)

    @overload
    def isUseGPU(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.isUseGPU()"""
        return bool.__wrap(super(BillboardParticleBatch, self).isUseGPU())

    @overload
    def setUseGpu(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.setUseGpu(boolean)"""
        super(__BillboardParticleBatch, self).setUseGpu(__boolean.valueOf(arg0))

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(__BillboardParticleBatch, self).save(arg0, arg1)

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch(int)"""
        val = __BillboardParticleBatch(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch()"""
        val = __BillboardParticleBatch()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def draw(self, arg0: 'ParticleControllerRenderData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.draw(T)"""
        super(__BufferedParticleBatch, self).draw(arg0)

    @override
    @overload
    def getSorter(self) -> 'particles.ParticleSorter':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleSorter com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.getSorter()"""
        return 'particles.ParticleSorter'.__wrap(super(BufferedParticleBatch, self).getSorter())