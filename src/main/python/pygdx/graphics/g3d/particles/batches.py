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

try:
    from pygdx.graphics.g3d.particles import renderers
except ImportError:
    renderers = _import_once("pygdx.graphics.g3d.particles.renderers")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.Texture as _Texture
_Texture = _Texture
import java.lang.Object as _object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute as _BlendingAttribute
_BlendingAttribute = _BlendingAttribute
import com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch as _BufferedParticleBatch
_BufferedParticleBatch = _BufferedParticleBatch
import java.lang.String as _String
_String = _String
try:
    from pygdx.graphics.g3d import attributes
except ImportError:
    attributes = _import_once("pygdx.graphics.g3d.attributes")

import com.badlogic.gdx.graphics.g3d.particles.ParticleSorter as _ParticleSorter
_ParticleSorter = _ParticleSorter
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch as _BillboardParticleBatch
_BillboardParticleBatch = _BillboardParticleBatch
import com.badlogic.gdx.graphics.g3d.particles.ParticleShader as _ParticleShader_AlignMode
_AlignMode = _ParticleShader_AlignMode.AlignMode
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BillboardParticleBatch():
    """com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch"""
 
    @staticmethod
    def _wrap(java_value: _BillboardParticleBatch) -> 'BillboardParticleBatch':
        return BillboardParticleBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BillboardParticleBatch):
        """
        Dynamic initializer for BillboardParticleBatch.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BillboardParticleBatch__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BillboardParticleBatch__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def getAlignMode(self) -> 'particles.ParticleShader$AlignMode':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.getAlignMode()"""
        return 'particles.ParticleShader$AlignMode'._wrap(super(BillboardParticleBatch, self).getAlignMode())

    @override
    @overload
    def setSorter(self, arg0: 'ParticleSorter'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.setSorter(com.badlogic.gdx.graphics.g3d.particles.ParticleSorter)"""
        super(_BufferedParticleBatch, self).setSorter(arg0)

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
    def getBufferedCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.getBufferedCount()"""
        return int._wrap(super(BufferedParticleBatch, self).getBufferedCount())

    @overload
    def __init__(self, arg0: 'AlignMode', arg1: bool, arg2: int, arg3: 'BlendingAttribute', arg4: 'DepthTestAttribute'):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch(com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode,boolean,int,com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute,com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute)"""
        val = _BillboardParticleBatch(arg0, _boolean.valueOf(arg1), _int.valueOf(arg2), arg3, arg4)
        self.__wrapper = val

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
    def draw(self, arg0: 'ParticleControllerRenderData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.draw(T)"""
        super(_BufferedParticleBatch, self).draw(arg0)

    @override
    @overload
    def getRenderables(self, arg0: 'Array', arg1: 'Pool'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.getRenderables(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>,com.badlogic.gdx.utils.Pool<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        super(_BillboardParticleBatch, self).getRenderables(arg0, arg1)

    @override
    @overload
    def getSorter(self) -> 'particles.ParticleSorter':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleSorter com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.getSorter()"""
        return 'particles.ParticleSorter'._wrap(super(BufferedParticleBatch, self).getSorter())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch()"""
        val = _BillboardParticleBatch()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch(int)"""
        val = _BillboardParticleBatch(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.end()"""
        super(BufferedParticleBatch, self).end()

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_BillboardParticleBatch, self).load(arg0, arg1)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch()"""
        val = _BillboardParticleBatch()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.getTexture()"""
        return 'graphics.Texture'._wrap(super(BillboardParticleBatch, self).getTexture())

    @override
    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.ensureCapacity(int)"""
        super(_BufferedParticleBatch, self).ensureCapacity(_int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setUseGpu(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.setUseGpu(boolean)"""
        super(_BillboardParticleBatch, self).setUseGpu(_boolean.valueOf(arg0))

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_BillboardParticleBatch, self).save(arg0, arg1)

    @overload
    def setTexture(self, arg0: 'Texture'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.setTexture(com.badlogic.gdx.graphics.Texture)"""
        super(_BillboardParticleBatch, self).setTexture(arg0)

    @overload
    def setAlignMode(self, arg0: 'AlignMode'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.setAlignMode(com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode)"""
        super(_BillboardParticleBatch, self).setAlignMode(arg0)

    @overload
    def allocParticlesData(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.allocParticlesData(int)"""
        super(_BillboardParticleBatch, self).allocParticlesData(_int.valueOf(arg0))

    @override
    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(_BufferedParticleBatch, self).setCamera(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'AlignMode', arg1: bool, arg2: int):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch(com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode,boolean,int)"""
        val = _BillboardParticleBatch(arg0, _boolean.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isUseGPU(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.isUseGPU()"""
        return bool._wrap(super(BillboardParticleBatch, self).isUseGPU())

    @overload
    def getBlendingAttribute(self) -> 'attributes.BlendingAttribute':
        """public com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.getBlendingAttribute()"""
        return 'attributes.BlendingAttribute'._wrap(super(BillboardParticleBatch, self).getBlendingAttribute())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch
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

try:
    from pygdx.graphics.g3d.particles import renderers
except ImportError:
    renderers = _import_once("pygdx.graphics.g3d.particles.renderers")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.Texture as _Texture
_Texture = _Texture
import java.lang.Object as _object
from builtins import type
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute as _BlendingAttribute
_BlendingAttribute = _BlendingAttribute
import com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch as _BufferedParticleBatch
_BufferedParticleBatch = _BufferedParticleBatch
import java.lang.String as _String
_String = _String
try:
    from pygdx.graphics.g3d import attributes
except ImportError:
    attributes = _import_once("pygdx.graphics.g3d.attributes")

import com.badlogic.gdx.graphics.g3d.particles.ParticleSorter as _ParticleSorter
_ParticleSorter = _ParticleSorter
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch as _BillboardParticleBatch
_BillboardParticleBatch = _BillboardParticleBatch
import com.badlogic.gdx.graphics.g3d.particles.ParticleShader as _ParticleShader_AlignMode
_AlignMode = _ParticleShader_AlignMode.AlignMode
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BillboardParticleBatch():
    """com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch"""
 
    @staticmethod
    def _wrap(java_value: _BillboardParticleBatch) -> 'BillboardParticleBatch':
        return BillboardParticleBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BillboardParticleBatch):
        """
        Dynamic initializer for BillboardParticleBatch.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BillboardParticleBatch__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BillboardParticleBatch__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def getAlignMode(self) -> 'particles.ParticleShader$AlignMode':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.getAlignMode()"""
        return 'particles.ParticleShader$AlignMode'._wrap(super(BillboardParticleBatch, self).getAlignMode())

    @override
    @overload
    def setSorter(self, arg0: 'ParticleSorter'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.setSorter(com.badlogic.gdx.graphics.g3d.particles.ParticleSorter)"""
        super(_BufferedParticleBatch, self).setSorter(arg0)

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
    def getBufferedCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.getBufferedCount()"""
        return int._wrap(super(BufferedParticleBatch, self).getBufferedCount())

    @overload
    def __init__(self, arg0: 'AlignMode', arg1: bool, arg2: int, arg3: 'BlendingAttribute', arg4: 'DepthTestAttribute'):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch(com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode,boolean,int,com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute,com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute)"""
        val = _BillboardParticleBatch(arg0, _boolean.valueOf(arg1), _int.valueOf(arg2), arg3, arg4)
        self.__wrapper = val

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
    def draw(self, arg0: 'ParticleControllerRenderData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.draw(T)"""
        super(_BufferedParticleBatch, self).draw(arg0)

    @override
    @overload
    def getRenderables(self, arg0: 'Array', arg1: 'Pool'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.getRenderables(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>,com.badlogic.gdx.utils.Pool<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        super(_BillboardParticleBatch, self).getRenderables(arg0, arg1)

    @override
    @overload
    def getSorter(self) -> 'particles.ParticleSorter':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleSorter com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.getSorter()"""
        return 'particles.ParticleSorter'._wrap(super(BufferedParticleBatch, self).getSorter())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch()"""
        val = _BillboardParticleBatch()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch(int)"""
        val = _BillboardParticleBatch(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.end()"""
        super(BufferedParticleBatch, self).end()

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_BillboardParticleBatch, self).load(arg0, arg1)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch()"""
        val = _BillboardParticleBatch()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.getTexture()"""
        return 'graphics.Texture'._wrap(super(BillboardParticleBatch, self).getTexture())

    @override
    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.ensureCapacity(int)"""
        super(_BufferedParticleBatch, self).ensureCapacity(_int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setUseGpu(self, arg0: bool):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.setUseGpu(boolean)"""
        super(_BillboardParticleBatch, self).setUseGpu(_boolean.valueOf(arg0))

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_BillboardParticleBatch, self).save(arg0, arg1)

    @overload
    def setTexture(self, arg0: 'Texture'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.setTexture(com.badlogic.gdx.graphics.Texture)"""
        super(_BillboardParticleBatch, self).setTexture(arg0)

    @overload
    def setAlignMode(self, arg0: 'AlignMode'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.setAlignMode(com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode)"""
        super(_BillboardParticleBatch, self).setAlignMode(arg0)

    @overload
    def allocParticlesData(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.allocParticlesData(int)"""
        super(_BillboardParticleBatch, self).allocParticlesData(_int.valueOf(arg0))

    @override
    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(_BufferedParticleBatch, self).setCamera(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'AlignMode', arg1: bool, arg2: int):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch(com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode,boolean,int)"""
        val = _BillboardParticleBatch(arg0, _boolean.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isUseGPU(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.isUseGPU()"""
        return bool._wrap(super(BillboardParticleBatch, self).isUseGPU())

    @overload
    def getBlendingAttribute(self) -> 'attributes.BlendingAttribute':
        """public com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.getBlendingAttribute()"""
        return 'attributes.BlendingAttribute'._wrap(super(BillboardParticleBatch, self).getBlendingAttribute())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch
from pyquantum_helper import import_once as _import_once
try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = _import_once("pygdx.graphics.g3d.particles")

try:
    from pygdx.graphics.g3d.particles import renderers
except ImportError:
    renderers = _import_once("pygdx.graphics.g3d.particles.renderers")

try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch as _ParticleBatch
_ParticleBatch = _ParticleBatch
from abc import abstractmethod, ABC
import com.badlogic.gdx.graphics.g3d.RenderableProvider as _RenderableProvider
_RenderableProvider = _RenderableProvider
 
class ParticleBatch():
    """com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch"""
 
    @staticmethod
    def _wrap(java_value: _ParticleBatch) -> 'ParticleBatch':
        return ParticleBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParticleBatch):
        """
        Dynamic initializer for ParticleBatch.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParticleBatch__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParticleBatch__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = _import_once("pygdx.graphics.g3d.particles")

try:
    from pygdx.graphics.g3d.particles import renderers
except ImportError:
    renderers = _import_once("pygdx.graphics.g3d.particles.renderers")

try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch as _ModelInstanceParticleBatch
_ModelInstanceParticleBatch = _ModelInstanceParticleBatch
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ModelInstanceParticleBatch():
    """com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch"""
 
    @staticmethod
    def _wrap(java_value: _ModelInstanceParticleBatch) -> 'ModelInstanceParticleBatch':
        return ModelInstanceParticleBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ModelInstanceParticleBatch):
        """
        Dynamic initializer for ModelInstanceParticleBatch.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ModelInstanceParticleBatch__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ModelInstanceParticleBatch__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def draw(self, arg0: 'ModelInstanceControllerRenderData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch.draw(com.badlogic.gdx.graphics.g3d.particles.renderers.ModelInstanceControllerRenderData)"""
        super(_ModelInstanceParticleBatch, self).draw(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_ModelInstanceParticleBatch, self).load(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch()"""
        val = _ModelInstanceParticleBatch()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch()"""
        val = _ModelInstanceParticleBatch()
        self.__wrapper = val

    @override
    @overload
    def begin(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch.begin()"""
        super(ModelInstanceParticleBatch, self).begin()

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
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch.end()"""
        super(ModelInstanceParticleBatch, self).end()

    @overload
    def getBufferedCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch.getBufferedCount()"""
        return int._wrap(super(ModelInstanceParticleBatch, self).getBufferedCount())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_ModelInstanceParticleBatch, self).save(arg0, arg1)

    @override
    @overload
    def getRenderables(self, arg0: 'Array', arg1: 'Pool'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.ModelInstanceParticleBatch.getRenderables(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>,com.badlogic.gdx.utils.Pool<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        super(_ModelInstanceParticleBatch, self).getRenderables(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch$Config
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx.graphics.g3d import particles
except ImportError:
    particles = _import_once("pygdx.graphics.g3d.particles")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch as _BillboardParticleBatch_Config
_Config = _BillboardParticleBatch_Config.Config
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Config():
    """com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch.Config"""
 
    @staticmethod
    def _wrap(java_value: _Config) -> 'Config':
        return Config(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Config):
        """
        Dynamic initializer for Config.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Config__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Config__wrapper":
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
    def __init__(self, arg0: bool, arg1: 'AlignMode'):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch$Config(boolean,com.badlogic.gdx.graphics.g3d.particles.ParticleShader$AlignMode)"""
        val = _Config(_boolean.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch$Config()"""
        val = _Config()
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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.BillboardParticleBatch$Config()"""
        val = _Config()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx.graphics.g3d.particles import renderers
except ImportError:
    renderers = _import_once("pygdx.graphics.g3d.particles.renderers")

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
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch as _ParticleBatch
_ParticleBatch = _ParticleBatch
import com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch as _BufferedParticleBatch
_BufferedParticleBatch = _BufferedParticleBatch
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import com.badlogic.gdx.graphics.g3d.RenderableProvider as _RenderableProvider
_RenderableProvider = _RenderableProvider
import com.badlogic.gdx.graphics.g3d.particles.ParticleSorter as _ParticleSorter
_ParticleSorter = _ParticleSorter
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BufferedParticleBatch():
    """com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch"""
 
    @staticmethod
    def _wrap(java_value: _BufferedParticleBatch) -> 'BufferedParticleBatch':
        return BufferedParticleBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BufferedParticleBatch):
        """
        Dynamic initializer for BufferedParticleBatch.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BufferedParticleBatch__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BufferedParticleBatch__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.end()"""
        super(BufferedParticleBatch, self).end()

    @overload
    def resetCapacity(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.resetCapacity()"""
        super(BufferedParticleBatch, self).resetCapacity()

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
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(_BufferedParticleBatch, self).setCamera(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getBufferedCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.getBufferedCount()"""
        return int._wrap(super(BufferedParticleBatch, self).getBufferedCount())

    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.ensureCapacity(int)"""
        super(_BufferedParticleBatch, self).ensureCapacity(_int.valueOf(arg0))

    @abstractmethod
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public abstract void com.badlogic.gdx.graphics.g3d.particles.batches.ParticleBatch.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        pass

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

    @abstractmethod
    def getRenderables(self, arg0: 'Array', arg1: 'Pool'):
        """public abstract void com.badlogic.gdx.graphics.g3d.RenderableProvider.getRenderables(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>,com.badlogic.gdx.utils.Pool<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def setSorter(self, arg0: 'ParticleSorter'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.setSorter(com.badlogic.gdx.graphics.g3d.particles.ParticleSorter)"""
        super(_BufferedParticleBatch, self).setSorter(arg0)

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
    def draw(self, arg0: 'ParticleControllerRenderData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.draw(T)"""
        super(_BufferedParticleBatch, self).draw(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getSorter(self) -> 'particles.ParticleSorter':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleSorter com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.getSorter()"""
        return 'particles.ParticleSorter'._wrap(super(BufferedParticleBatch, self).getSorter())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch
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

try:
    from pygdx.graphics.g3d.particles import renderers
except ImportError:
    renderers = _import_once("pygdx.graphics.g3d.particles.renderers")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.Texture as _Texture
_Texture = _Texture
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch as _PointSpriteParticleBatch
_PointSpriteParticleBatch = _PointSpriteParticleBatch
try:
    from pygdx import assets
except ImportError:
    assets = _import_once("pygdx.assets")

import com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute as _BlendingAttribute
_BlendingAttribute = _BlendingAttribute
import com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch as _BufferedParticleBatch
_BufferedParticleBatch = _BufferedParticleBatch
import java.lang.String as _String
_String = _String
try:
    from pygdx.graphics.g3d import attributes
except ImportError:
    attributes = _import_once("pygdx.graphics.g3d.attributes")

import com.badlogic.gdx.graphics.g3d.particles.ParticleSorter as _ParticleSorter
_ParticleSorter = _ParticleSorter
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PointSpriteParticleBatch():
    """com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch"""
 
    @staticmethod
    def _wrap(java_value: _PointSpriteParticleBatch) -> 'PointSpriteParticleBatch':
        return PointSpriteParticleBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PointSpriteParticleBatch):
        """
        Dynamic initializer for PointSpriteParticleBatch.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PointSpriteParticleBatch__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PointSpriteParticleBatch__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def resetCapacity(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.resetCapacity()"""
        super(BufferedParticleBatch, self).resetCapacity()

    @override
    @overload
    def setSorter(self, arg0: 'ParticleSorter'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.setSorter(com.badlogic.gdx.graphics.g3d.particles.ParticleSorter)"""
        super(_BufferedParticleBatch, self).setSorter(arg0)

    @overload
    def __init__(self, arg0: int, arg1: 'Config', arg2: 'BlendingAttribute', arg3: 'DepthTestAttribute'):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch(int,com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config,com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute,com.badlogic.gdx.graphics.g3d.attributes.DepthTestAttribute)"""
        val = _PointSpriteParticleBatch(_int.valueOf(arg0), arg1, arg2, arg3)
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getBlendingAttribute(self) -> 'attributes.BlendingAttribute':
        """public com.badlogic.gdx.graphics.g3d.attributes.BlendingAttribute com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch.getBlendingAttribute()"""
        return 'attributes.BlendingAttribute'._wrap(super(PointSpriteParticleBatch, self).getBlendingAttribute())

    @override
    @overload
    def getBufferedCount(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.getBufferedCount()"""
        return int._wrap(super(BufferedParticleBatch, self).getBufferedCount())

    @overload
    def getTexture(self) -> 'graphics.Texture':
        """public com.badlogic.gdx.graphics.Texture com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch.getTexture()"""
        return 'graphics.Texture'._wrap(super(PointSpriteParticleBatch, self).getTexture())

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
    def getRenderables(self, arg0: 'Array', arg1: 'Pool'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch.getRenderables(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.Renderable>,com.badlogic.gdx.utils.Pool<com.badlogic.gdx.graphics.g3d.Renderable>)"""
        super(_PointSpriteParticleBatch, self).getRenderables(arg0, arg1)

    @override
    @overload
    def draw(self, arg0: 'ParticleControllerRenderData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.draw(T)"""
        super(_BufferedParticleBatch, self).draw(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch()"""
        val = _PointSpriteParticleBatch()
        self.__wrapper = val

    @override
    @overload
    def getSorter(self) -> 'particles.ParticleSorter':
        """public com.badlogic.gdx.graphics.g3d.particles.ParticleSorter com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.getSorter()"""
        return 'particles.ParticleSorter'._wrap(super(BufferedParticleBatch, self).getSorter())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def end(self):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.end()"""
        super(BufferedParticleBatch, self).end()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def ensureCapacity(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.ensureCapacity(int)"""
        super(_BufferedParticleBatch, self).ensureCapacity(_int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch(int)"""
        val = _PointSpriteParticleBatch(_int.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def load(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch.load(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_PointSpriteParticleBatch, self).load(arg0, arg1)

    @override
    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.BufferedParticleBatch.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(_BufferedParticleBatch, self).setCamera(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: int, arg1: 'Config'):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch(int,com.badlogic.gdx.graphics.g3d.particles.ParticleShader$Config)"""
        val = _PointSpriteParticleBatch(_int.valueOf(arg0), arg1)
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

    @overload
    def setTexture(self, arg0: 'Texture'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch.setTexture(com.badlogic.gdx.graphics.Texture)"""
        super(_PointSpriteParticleBatch, self).setTexture(arg0)

    @override
    @overload
    def save(self, arg0: 'AssetManager', arg1: 'ResourceData'):
        """public void com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch.save(com.badlogic.gdx.assets.AssetManager,com.badlogic.gdx.graphics.g3d.particles.ResourceData)"""
        super(_PointSpriteParticleBatch, self).save(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.particles.batches.PointSpriteParticleBatch()"""
        val = _PointSpriteParticleBatch()
        self.__wrapper = val