# Smart Data Story

A project for analyzing and visualizing GitHub event data.

## Resources

### GitHub Event Data
- [GitHub REST API Event Types Documentation](https://docs.github.com/en/rest/using-the-rest-api/github-event-types?apiVersion=2022-11-28)

- [GH Archive - GitHub Activity Data](https://www.gharchive.org)

# Smart DataStory  

**Objetivo del Proyecto**: Analizar cómo la adopción de GitHub Actions (lanzada el 13/11/2019) impactó la eficiencia del flujo de trabajo en repositorios de código abierto, comparando la correlación entre *issues cerrados* (`IssueEvent` con `action: closed`) y *lanzamientos de software* (`ReleaseEvent`) en dos momentos clave: **un día antes de su lanzamiento (12/11/2019)** y **un año después (13/11/2020)**. Utilizando datos públicos de GitHub, se calculará el coeficiente de correlación de Pearson y la proporción de lanzamientos por issue resuelto para evaluar si la automatización aceleró la relación entre resolución de problemas y despliegues. El análisis, con visualizaciones claras (gráficos de dispersión, métricas comparativas), se completará en **2 semanas**, brindando insights accionables para optimizar procesos en proyectos colaborativos.  

**Ejemplo de Métricas Clave**:  
| Período         | Issues Cerrados | Lanzamientos | Correlación (r) | Lanzamientos/Issue |  
|-----------------|------------------|--------------|------------------|---------------------|  
| Pre-Actions     | 500              | 100          | 0.45             | 0.20                |  
| Post-Actions    | 800              | 400          | 0.75             | 0.50                |  

**Resultado Esperado**: Entender cuantitativamente cómo herramientas de automatización como GitHub Actions contribuyen a flujos de trabajo más ágiles y predecibles en el ecosistema open source.  
