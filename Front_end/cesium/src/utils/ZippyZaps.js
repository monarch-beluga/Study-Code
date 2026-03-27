import * as Cesium from "cesium";

function createMaterialAppearance() {
    const customMaterial = new Cesium.Material({
        translucent: false,
        fabric: {
            type: "CustomBoxShader",
            uniforms: {
                iTime: 0.0,
                iResolution: new Cesium.Cartesian2(1024, 1024),
            },
            // https://www.shadertoy.com/view/XXyGzh
            source: `
            
            const float PI = 3.1415926535897932;
            
            // play with these parameters to custimize the effect
            // ==================================================
            
            //speed
            const float speed = 0.2;
            const float speed_x = 0.3;
            const float speed_y = 0.3;
            
            // refraction
            const float emboss = 0.50;
            const float intensity = 2.4;
            const int steps = 8;
            const float frequency = 6.0;
            const int angle = 7; // better when a prime
            
            // reflection
            const float delta = 60.;
            const float gain = 700.;
            const float reflectionCutOff = 0.012;
            const float reflectionIntensity = 200000.;
            
            // ===================================================
            
            
              float col(vec2 coord,float time)
              {
                float delta_theta = 2.0 * PI / float(angle);
                float col = 0.0;
                float theta = 0.0;
                for (int i = 0; i < steps; i++)
                {
                  vec2 adjc = coord;
                  theta = delta_theta*float(i);
                  adjc.x += cos(theta)*time*speed + time * speed_x;
                  adjc.y -= sin(theta)*time*speed - time * speed_y;
                  col = col + cos( (adjc.x*cos(theta) - adjc.y*sin(theta))*frequency)*intensity;
                }
            
                return cos(col);
              }
            
            //---------- main
            
            void mainImage( out vec4 fragColor, in vec2 fragCoord )
            {
                float time = iTime*1.3;
            
            vec2 p = (fragCoord.xy) / iResolution.xy, c1 = p, c2 = p;
            float cc1 = col(c1,time);
            
            c2.x += iResolution.x/delta;
            float dx = emboss*(cc1-col(c2,time))/delta;
            
            c2.x = p.x;
            c2.y += iResolution.y/delta;
            float dy = emboss*(cc1-col(c2,time))/delta;
            
            c1.x += dx*2.;
            c1.y = -(c1.y+dy*2.);
            
            float alpha = 1.+dot(dx,dy)*gain;
            
            float ddx = dx - reflectionCutOff;
            float ddy = dy - reflectionCutOff;
            if (ddx > 0. && ddy > 0.)
            alpha = pow(alpha, ddx*ddy*reflectionIntensity);
            vec3 hsl = vec3( 0.0, 0.5, 0.8 );
            vec4 col = hsl*(alpha);
            fragColor = col;
            }
            
            czm_material czm_getMaterial(czm_materialInput materialInput) {
                czm_material material = czm_getDefaultMaterial(materialInput);
                vec4 color = vec4(0.0, 0.0, 0.0, 1.0);
                mainImage(color, materialInput.st * iResolution);
                material.diffuse = color.rgb;
                material.alpha = 0.5;//color.a;
                return material;
            }
            `,
        },
    });

    return new Cesium.MaterialAppearance({
        material: customMaterial,
        flat: false,
        faceForward: true,
        translucent: true,
        closed: true,
        materialCacheKey: "shadertoy-material-appearance",
    });
}

const boxSize = 25;
function createBoxPrimitive(destination, appearance) {
    const boxGeometry = Cesium.BoxGeometry.fromDimensions({
        dimensions: new Cesium.Cartesian3(boxSize, boxSize, boxSize),
    });

    const modelMatrix = Cesium.Transforms.eastNorthUpToFixedFrame(destination);

    const boxInstance = new Cesium.GeometryInstance({
        geometry: boxGeometry,
    });

    const primitive = new Cesium.Primitive({
        geometryInstances: boxInstance,
        appearance: appearance,
        asynchronous: false,
        modelMatrix: modelMatrix,
    });

    return primitive;
}

export { createMaterialAppearance, createBoxPrimitive};
