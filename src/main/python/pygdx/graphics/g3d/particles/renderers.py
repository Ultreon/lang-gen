from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteControllerRenderData as _PointSpriteControllerRenderData
_PointSpriteControllerRenderData = _PointSpriteControllerRenderData
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PointSpriteControllerRenderData():
    """com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteControllerRenderData"""
 
    @staticmethod
    def _wrap(java_value: _PointSpriteControllerRenderData) -> 'PointSpriteControllerRenderData':
        return PointSpriteControllerRenderData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PointSpriteControllerRenderData):
        """
        Dynamic initializer for PointSpriteControllerRenderData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PointSpriteControllerRenderData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PointSpriteControllerRenderData__wrapper":
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
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteControllerRenderData()"""
        val = _PointSpriteControllerRenderData()
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteControllerRenderData()"""
        val = _PointSpriteControllerRenderData()
        self.__wrapper = val

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteControllerRenderData
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteControllerRenderData as _PointSpriteControllerRenderData
_PointSpriteControllerRenderData = _PointSpriteControllerRenderData
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PointSpriteControllerRenderData():
    """com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteControllerRenderData"""
 
    @staticmethod
    def _wrap(java_value: _PointSpriteControllerRenderData) -> 'PointSpriteControllerRenderData':
        return PointSpriteControllerRenderData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PointSpriteControllerRenderData):
        """
        Dynamic initializer for PointSpriteControllerRenderData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PointSpriteControllerRenderData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PointSpriteControllerRenderData__wrapper":
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
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteControllerRenderData()"""
        val = _PointSpriteControllerRenderData()
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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteControllerRenderData()"""
        val = _PointSpriteControllerRenderData()
        self.__wrapper = val

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteControllerRenderData 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardControllerRenderData
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardControllerRenderData as _BillboardControllerRenderData
_BillboardControllerRenderData = _BillboardControllerRenderData
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BillboardControllerRenderData():
    """com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardControllerRenderData"""
 
    @staticmethod
    def _wrap(java_value: _BillboardControllerRenderData) -> 'BillboardControllerRenderData':
        return BillboardControllerRenderData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BillboardControllerRenderData):
        """
        Dynamic initializer for BillboardControllerRenderData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BillboardControllerRenderData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BillboardControllerRenderData__wrapper":
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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardControllerRenderData()"""
        val = _BillboardControllerRenderData()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardControllerRenderData()"""
        val = _BillboardControllerRenderData()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer
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
import com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer as _ModelInstanceRenderer
_ModelInstanceRenderer = _ModelInstanceRenderer
try:
    from pygdx.graphics.g3d.particles import batches
except ImportError:
    batches = _import_once("pygdx.graphics.g3d.particles.batches")

import java.lang.Integer as _int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer as _ParticleControllerRenderer
_ParticleControllerRenderer = _ParticleControllerRenderer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ModelInstanceRenderer():
    """com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer"""
 
    @staticmethod
    def _wrap(java_value: _ModelInstanceRenderer) -> 'ModelInstanceRenderer':
        return ModelInstanceRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModelInstanceRenderer):
        """
        Dynamic initializer for ModelInstanceRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModelInstanceRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModelInstanceRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer.allocateChannels()"""
        super(ModelInstanceRenderer, self).allocateChannels()

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer.init()"""
        super(ModelInstanceRenderer, self).init()

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_particles.ParticleControllerComponent, self).load(arg0, arg1)

    @overload
    def isCompatible(self, arg0: 'ParticleBatch') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer.isCompatible(com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>)"""
        return bool._wrap(super(_ModelInstanceRenderer, self).isCompatible(arg0))

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @overload
    def setBatch(self, arg0: 'ParticleBatch') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.setBatch(com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>)"""
        return bool._wrap(super(_ParticleControllerRenderer, self).setBatch(arg0))

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
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer()"""
        val = _ModelInstanceRenderer()
        self.__wrapper = val

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer.update()"""
        super(ModelInstanceRenderer, self).update()

    @override
    @overload
    def copy(self) -> 'particles.ParticleControllerComponent':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer.copy()"""
        return 'particles.ParticleControllerComponent'._wrap(super(ModelInstanceRenderer, self).copy())

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
    def set(self, arg0: 'ParticleController'):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(_ParticleControllerRenderer, self).set(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer()"""
        val = _ModelInstanceRenderer()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'ModelInstanceParticleBatch'):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceRenderer(com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch)"""
        val = _ModelInstanceRenderer(arg0)
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteRenderer
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
    from pygdx.graphics.g3d.particles import batches
except ImportError:
    batches = _import_once("pygdx.graphics.g3d.particles.batches")

import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteRenderer as _PointSpriteRenderer
_PointSpriteRenderer = _PointSpriteRenderer
from builtins import bool
import com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer as _ParticleControllerRenderer
_ParticleControllerRenderer = _ParticleControllerRenderer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PointSpriteRenderer():
    """com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteRenderer"""
 
    @staticmethod
    def _wrap(java_value: _PointSpriteRenderer) -> 'PointSpriteRenderer':
        return PointSpriteRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PointSpriteRenderer):
        """
        Dynamic initializer for PointSpriteRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PointSpriteRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PointSpriteRenderer__wrapper":
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
    def copy(self) -> 'particles.ParticleControllerComponent':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteRenderer.copy()"""
        return 'particles.ParticleControllerComponent'._wrap(super(PointSpriteRenderer, self).copy())

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.end()"""
        super(particles.ParticleControllerComponent, self).end()

    @overload
    def setBatch(self, arg0: 'ParticleBatch') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.setBatch(com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>)"""
        return bool._wrap(super(_ParticleControllerRenderer, self).setBatch(arg0))

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
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteRenderer()"""
        val = _PointSpriteRenderer()
        self.__wrapper = val

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(_particles.ParticleControllerComponent, self).write(arg0)

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.update()"""
        super(ParticleControllerRenderer, self).update()

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
    def isCompatible(self, arg0: 'ParticleBatch') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteRenderer.isCompatible(com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>)"""
        return bool._wrap(super(_PointSpriteRenderer, self).isCompatible(arg0))

    @override
    @overload
    def set(self, arg0: 'ParticleController'):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(_ParticleControllerRenderer, self).set(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.PointSpriteRenderer()"""
        val = _PointSpriteRenderer()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_particles.ParticleControllerComponent, self).read(arg0, arg1)

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
        val = _PointSpriteRenderer(arg0)
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerControllerRenderer
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

import com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerControllerRenderer as _ParticleControllerControllerRenderer
_ParticleControllerControllerRenderer = _ParticleControllerControllerRenderer
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
    from pygdx.graphics.g3d.particles import batches
except ImportError:
    batches = _import_once("pygdx.graphics.g3d.particles.batches")

import java.lang.Integer as _int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer as _ParticleControllerRenderer
_ParticleControllerRenderer = _ParticleControllerRenderer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParticleControllerControllerRenderer():
    """com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerControllerRenderer"""
 
    @staticmethod
    def _wrap(java_value: _ParticleControllerControllerRenderer) -> 'ParticleControllerControllerRenderer':
        return ParticleControllerControllerRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleControllerControllerRenderer):
        """
        Dynamic initializer for ParticleControllerControllerRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleControllerControllerRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleControllerControllerRenderer__wrapper":
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
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerControllerRenderer.update()"""
        super(ParticleControllerControllerRenderer, self).update()

    @overload
    def setBatch(self, arg0: 'ParticleBatch') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.setBatch(com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>)"""
        return bool._wrap(super(_ParticleControllerRenderer, self).setBatch(arg0))

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
    def copy(self) -> 'particles.ParticleControllerComponent':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerControllerRenderer.copy()"""
        return 'particles.ParticleControllerComponent'._wrap(super(ParticleControllerControllerRenderer, self).copy())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerControllerRenderer()"""
        val = _ParticleControllerControllerRenderer()
        self.__wrapper = val

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
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerControllerRenderer()"""
        val = _ParticleControllerControllerRenderer()
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
    def set(self, arg0: 'ParticleController'):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(_ParticleControllerRenderer, self).set(arg0)

    @overload
    def isCompatible(self, arg0: 'ParticleBatch') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerControllerRenderer.isCompatible(com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch)"""
        return bool._wrap(super(_ParticleControllerControllerRenderer, self).isCompatible(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def read(self, arg0: 'Json', arg1: 'JsonValue'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.read(com.badlogic.gdx.utils.Json,com.badlogic.gdx.utils.JsonValue)"""
        super(_particles.ParticleControllerComponent, self).read(arg0, arg1)

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderData
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderData as _ParticleControllerRenderData
_ParticleControllerRenderData = _ParticleControllerRenderData
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParticleControllerRenderData():
    """com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderData"""
 
    @staticmethod
    def _wrap(java_value: _ParticleControllerRenderData) -> 'ParticleControllerRenderData':
        return ParticleControllerRenderData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleControllerRenderData):
        """
        Dynamic initializer for ParticleControllerRenderData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleControllerRenderData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleControllerRenderData__wrapper":
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
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderData()"""
        val = _ParticleControllerRenderData()
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderData()"""
        val = _ParticleControllerRenderData()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardRenderer
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
    from pygdx.graphics.g3d.particles import batches
except ImportError:
    batches = _import_once("pygdx.graphics.g3d.particles.batches")

import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardRenderer as _BillboardRenderer
_BillboardRenderer = _BillboardRenderer
from builtins import bool
import com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer as _ParticleControllerRenderer
_ParticleControllerRenderer = _ParticleControllerRenderer
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BillboardRenderer():
    """com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardRenderer"""
 
    @staticmethod
    def _wrap(java_value: _BillboardRenderer) -> 'BillboardRenderer':
        return BillboardRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BillboardRenderer):
        """
        Dynamic initializer for BillboardRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BillboardRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BillboardRenderer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def allocateChannels(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardRenderer.allocateChannels()"""
        super(BillboardRenderer, self).allocateChannels()

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
    def setBatch(self, arg0: 'ParticleBatch') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.setBatch(com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>)"""
        return bool._wrap(super(_ParticleControllerRenderer, self).setBatch(arg0))

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
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardRenderer()"""
        val = _BillboardRenderer()
        self.__wrapper = val

    @override
    @overload
    def init(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.init()"""
        super(particles.ParticleControllerComponent, self).init()

    @override
    @overload
    def write(self, arg0: 'Json'):
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(_particles.ParticleControllerComponent, self).write(arg0)

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.update()"""
        super(ParticleControllerRenderer, self).update()

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
    def copy(self) -> 'particles.ParticleControllerComponent':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardRenderer.copy()"""
        return 'particles.ParticleControllerComponent'._wrap(super(BillboardRenderer, self).copy())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: 'BillboardParticleBatch'):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardRenderer(com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch)"""
        val = _BillboardRenderer(arg0)
        self.__wrapper = val

    @overload
    def isCompatible(self, arg0: 'ParticleBatch') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardRenderer.isCompatible(com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>)"""
        return bool._wrap(super(_BillboardRenderer, self).isCompatible(arg0))

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
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.BillboardRenderer()"""
        val = _BillboardRenderer()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def set(self, arg0: 'ParticleController'):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(_ParticleControllerRenderer, self).set(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceControllerRenderData
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceControllerRenderData as _ModelInstanceControllerRenderData
_ModelInstanceControllerRenderData = _ModelInstanceControllerRenderData
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ModelInstanceControllerRenderData():
    """com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceControllerRenderData"""
 
    @staticmethod
    def _wrap(java_value: _ModelInstanceControllerRenderData) -> 'ModelInstanceControllerRenderData':
        return ModelInstanceControllerRenderData(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModelInstanceControllerRenderData):
        """
        Dynamic initializer for ModelInstanceControllerRenderData.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModelInstanceControllerRenderData__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModelInstanceControllerRenderData__wrapper":
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
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceControllerRenderData()"""
        val = _ModelInstanceControllerRenderData()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceControllerRenderData()"""
        val = _ModelInstanceControllerRenderData()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer
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
try:
    from pygdx.graphics.g3d.particles import batches
except ImportError:
    batches = _import_once("pygdx.graphics.g3d.particles.batches")

import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer as _ParticleControllerRenderer
_ParticleControllerRenderer = _ParticleControllerRenderer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ParticleControllerRenderer():
    """com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer"""
 
    @staticmethod
    def _wrap(java_value: _ParticleControllerRenderer) -> 'ParticleControllerRenderer':
        return ParticleControllerRenderer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleControllerRenderer):
        """
        Dynamic initializer for ParticleControllerRenderer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleControllerRenderer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleControllerRenderer__wrapper":
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

    @overload
    def setBatch(self, arg0: 'ParticleBatch') -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.setBatch(com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>)"""
        return bool._wrap(super(_ParticleControllerRenderer, self).setBatch(arg0))

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
        """public void com.badlogic.gdx.graphics.g3d.particles.ParticleControllerComponent.write(com.badlogic.gdx.utils.Json)"""
        super(_particles.ParticleControllerComponent, self).write(arg0)

    @override
    @overload
    def update(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.update()"""
        super(ParticleControllerRenderer, self).update()

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

    @abstractmethod
    def isCompatible(self, arg0: 'ParticleBatch'):
        """public abstract boolean com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.isCompatible(com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch<?>)"""
        pass

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
    def set(self, arg0: 'ParticleController'):
        """public void com.badlogic.gdx.graphics.g3d.particles.renderers.ParticleControllerRenderer.set(com.badlogic.gdx.graphics.g3d.particles.ParticleController)"""
        super(_ParticleControllerRenderer, self).set(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

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