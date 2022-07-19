#***************************************************************
#SimLab Version 2022 
#Created at Tue Jul 19 14:44:00 2022
#***************************************************************
#For debugging this python script,Please comment(#) out the line "from hwx import simlab" and uncomment the line "import simlab"
#import simlab
from hwx import simlab

UnitSystem=''' <UnitSystem UUID="3aca8564-4d38-4b0b-887c-6a542d4001c6">
  <SetCurrentDisplaySystem Name="MMKS (mm kg N C s)"/>
 </UnitSystem>''';
simlab.execute(UnitSystem);

ImportProE=''' <ImportProE CheckBox="ON" UUID="ccfb0134-4019-48a1-8387-e95c1b04f1a0" gda="">
  <tag Value="1"/>
  <FileName Value="./../../Desktop/creo/flex_plate.prt.1"/>
  <SolidBodyType Value="1"/>
  <QuiltBodyType Value="0"/>
  <CurveBodyType Value="0"/>
  <ExactGeom Value="1"/>
  <Facets Value="0"/>
  <CoOrdinates Value="0"/>
  <DatumPoints Value="0"/>
  <DesignParameters Value="1"/>
  <SimRep Value="0"/>
  <Regenerate Value="0"/>
  <ImportOption Value="0"/>
  <RegenModelId Value="0"/>
  <ImportAssemblyStructure Value="1"/>
  <InstanceName Value=""/>
  <SaveGeometry Value="0"/>
  <Path Value=""/>
  <ConvertUnitsTomm Value="0"/>
  <Output/>
 </ImportProE>''';
simlab.execute(ImportProE);

SurfaceMesh=''' <SurfaceMesh UUID="08df0ff6-f369-4003-956c-82781326c876">
  <tag Value="-1"/>
  <SurfaceMeshType Value="Tri"/>
  <SupportEntities>
   <Entities>
    <Model>$Geometry</Model>
    <Body></Body>
   </Entities>
  </SupportEntities>
  <Tri>
   <ElementType Value="Tri3"/>
   <AverageElementSize Checked="1" Value="5 mm"/>
   <MaximumElementSize Checked="0" Value="7.07 mm"/>
   <MinimumElementSize Value="0.5 mm"/>
   <GradeFactor Value="1.5"/>
   <MaximumAnglePerElement Value="45 deg"/>
   <CurvatureMinimumElementSize Value="2.5 mm"/>
   <AspectRatio Value="10"/>
   <IdentifyFeaturesAndMesh Checked="1"/>
   <CreateMatchingMesh Checked="0"/>
   <AdvancedOptions>
    <ImprintMeshing Checked="0"/>
    <BetterGeometryApproximation Checked="0"/>
    <CoarseMesh Checked="0"/>
    <CoarseMesh_UseExistingNodes Checked="0"/>
    <CreateNewMeshModel Checked="0"/>
    <UserDefinedModelName Value=""/>
    <Tri6WithStraightEdges Checked="0"/>
    <ImproveSkewAngle Value="0"/>
    <MappedMesh Value="0"/>
    <MeshPattern Value="0"/>
   </AdvancedOptions>
  </Tri>
 </SurfaceMesh>''';
simlab.execute(SurfaceMesh);

SelectAdjacentLayers=''' <SelectAdjacentLayers clearSelection="1" UUID="EEDC5B06-8DC9-4754-AA76-F9E32643765A" gda="">
  <Name Value=""/>
  <tag Value="-1"/>
  <Show Value="0"/>
  <Select Value="1"/>
  <CheckVisibleFaces Value="1"/>
  <SupportEntities ModelIds="" EntityTypes="" Value=""/>
  <PickFaceType Value="GuideFaces"/>
  <GuideFaces>
   <Entities>
    <Model>flex_plate1_SM.gda</Model>
    <Face>96,</Face>
   </Entities>
  </GuideFaces>
  <LimitFaces>
   <Entities>
    <Model>flex_plate1_SM.gda</Model>
    <Face>61,65,</Face>
   </Entities>
  </LimitFaces>
  <AddPlanarFacestoLimitFaces Value="0"/>
  <AddCylindricalFacestoLimitFaces Value="0"/>
  <UptoNonManifoldEdges Value="0"/>
  <BreakAngle Value="0"/>
  <Angle Value="45 deg"/>
  <NoOfLayers Value="72"/>
  <CreateGroup Value="0" Name="Adjacent_Faces_1"/>
 </SelectAdjacentLayers>''';
simlab.execute(SelectAdjacentLayers);

FluidDomain=''' <CreateFluidDomain UUID="ad9c28d6-665f-4ff6-8c0f-5ab1f80caa6d">
  <BodyName Value="Fluid body 1"/>
  <CreationMethod Value="WettedSurface"/>
  <WettedFaces>
   <Entities>
    <Model>flex_plate1_SM.gda</Model>
    <Face>1402,94,1400,160,158,892,890,175,173,1370,1368,190,188,936,934,205,203,1338,1336,220,218,968,966,235,233,1306,1304,250,248,1000,998,265,263,1274,1272,280,278,1032,1030,295,293,1242,1240,310,308,1064,1062,325,323,1210,1208,340,338,1096,1094,355,353,1170,1168,370,368,1128,1126,385,383,96,</Face>
   </Entities>
  </WettedFaces>
  <InletOutletFaces/>
  <LocalReMeshSize Checked="0" Value="0 mm"/>
  <RedoFlag Value=""/>
 </CreateFluidDomain>''';
simlab.execute(FluidDomain);

CFDMesh=''' <CFDMesh UUID="1a7e9145-d7bc-4d30-b0c2-1ca3782f35e6">
  <Body>
   <SolidBodies>
    <Entities>
     <Model>flex_plate1_SM.gda</Model>
     <Body>"flex_plate.prt.1",</Body>
    </Entities>
   </SolidBodies>
   <FluidBodies>
    <Entities>
     <Model>flex_plate1_SM.gda</Model>
     <Body>"Fluid body 1",</Body>
    </Entities>
   </FluidBodies>
   <IgnoreFaces>
    <Entities>
     <Model>flex_plate1_SM.gda</Model>
     <Face>1642,1640,</Face>
    </Entities>
   </IgnoreFaces>
  </Body>
  <BoundaryLayerParameters>
   <FirstLayerThickness Method="Constant" Value="0.1 mm"/>
   <TotalNumberOfLayers Value="5"/>
   <GrowthMethod Value="Constant"/>
   <GrowthRate Value="1.2"/>
   <LayersWithInitialGrowthRate Value="3"/>
   <GrowthRateFactor Value="1.1"/>
   <MaxGrowthRate Value="1.5"/>
   <TerminationPolicy Value="Squeeze"/>
  </BoundaryLayerParameters>
  <TetCore>
   <AverageElementSize Value="5 mm"/>
   <InternalGrading Value="1.2"/>
  </TetCore>
  <AdvancedOptions>
   <FillAllVoids Value="1"/>
   <ImprintBLOnAdjacentFaces Value="1"/>
   <BLElementType Value="Tetra"/>
   <SharpEdgeTreatment Value="Node Collapse"/>
   <SharpEdgeAngle Value="5 deg"/>
   <MaxAdjacentLayerDiff Value="2"/>
   <MaxBLCompressionFactor Value="0.9"/>
   <RestrictMinBLHeight Value="0"/>
   <MinTetCoreToHeightRatio Value="1.3"/>
   <MaxCellSkewness Value="0.95"/>
   <MinimumNormalizedJacobian Value="0.01"/>
   <GenerateBLOnly Value="0"/>
  </AdvancedOptions>
 </CFDMesh>''';
simlab.execute(CFDMesh);

DropTestParameters=''' <DropTestParameters UUID="467f776e-febc-4c63-8fde-b4a01fbb61c9">
  <InputBodies>
   <Entities>
    <Model>flex_plate1_SM.gda</Model>
    <Body>"Fluid body 1",</Body>
   </Entities>
  </InputBodies>
  <MeshType Value=""/>
  <MeshSize Value=""/>
  <MinimumElementSize Value=""/>
  <Material Name="Water"/>
  <QualitySpec Name=""/>
 </DropTestParameters>''';
simlab.execute(DropTestParameters);

DropTestParameters=''' <DropTestParameters UUID="467f776e-febc-4c63-8fde-b4a01fbb61c9">
  <InputBodies>
   <Entities>
    <Model>flex_plate1_SM.gda</Model>
    <Body>"flex_plate.prt.1",</Body>
   </Entities>
  </InputBodies>
  <MeshType Value=""/>
  <MeshSize Value=""/>
  <MinimumElementSize Value=""/>
  <Material Name="Steel"/>
  <QualitySpec Name=""/>
 </DropTestParameters>''';
simlab.execute(DropTestParameters);

CreateSolution=''' <CreateSolution BCType="Solution" UUID="1210abd7-c815-4f67-8615-6ab616274dcc">
  <tag Value="-1"/>
  <Name Value="Flow"/>
  <SolutionType Value="STEADYSTATE"/>
  <Solver Value="ACUSOLVE"/>
  <CreateDefSettings Value="1"/>
  <SupportEntities>
   <Entities>
    <Model>flex_plate1_SM.gda</Model>
    <Body></Body>
   </Entities>
  </SupportEntities>
  <CreateAndSetActiveLC Value="0"/>
  <AutoContact Value=""/>
  <AcuSolveParameters>
   <MultiflowType Value="0"/>
   <CompressibleFlowType Value="0"/>
   <FlowEquation Index="2" Value="Turbulent"/>
   <TurbulenceEquation Index="0" Value="Spalart-Allmaras"/>
   <MultiphaseType Index="0" Value="Immiscible"/>
   <EnhanceFeature Value="0"/>
   <TemperatureEquation Value="1"/>
   <SolveForBoiling Value="0"/>
   <IncludeElectricalEffects Value="0"/>
   <RadiationEquation Index="0" Value="None"/>
   <RadiationQuadrature Index="1" Value="S4"/>
   <MeshType Index="0" Value="None"/>
   <NfxAcuSolveCoupling Value="0"/>
   <GravityCheck Value="0"/>
   <GravityAcceleration Value=""/>
  </AcuSolveParameters>
  <AnalysisType Value="Flow"/>
 </CreateSolution>''';
simlab.execute(CreateSolution);

Inlet=''' <Inlet BCType="Inlet" UUID="67952a80-2996-4ef8-a422-9ef752338fc1">
  <tag Value=""/>
  <Name Value="Inlet_2"/>
  <Entities>
   <Entities>
    <Model>flex_plate1_SM.gda</Model>
    <Face>1642,</Face>
   </Entities>
  </Entities>
  <ReferenceFrameID Value="Global"/>
  <PhasicInflow Value="0"/>
  <InflowType Index="1" Value="Mass Flow Rate"/>
  <InflowVelocityType Value=""/>
  <PhasicInflowData/>
  <XVelocity Value="0.0"/>
  <YVelocity Value="0.0"/>
  <ZVelocity Value="0.0"/>
  <AxialVelocity Value="0.0"/>
  <CylinRadialVelocity Value="0.0"/>
  <TangentVelocity Value="0.0"/>
  <SphereX Value="0.0"/>
  <SphereY Value="0.0"/>
  <SphereZ Value="0.0"/>
  <SphereRadialVelocity Value="0.0"/>
  <NormalVelocity Value="0.0"/>
  <MassFlux Value="0.001 kg/s"/>
  <AverageVelocity Value="0.0"/>
  <FlowRate Value="0.0"/>
  <Pressure Value="0.0"/>
  <PressureLossFactor Value="0.0"/>
  <HydroPressureCheck Value=""/>
  <HydroPressure/>
  <WaveHeight Value="0.0"/>
  <WaveLength Value="0.0"/>
  <WaveDepth Value="0.0"/>
  <HeavyFluidVelocity Value=""/>
  <LightFluidVelocity Value=""/>
  <ABLRoughnessType Value=""/>
  <ABLRoughnessHeight Value="0.0"/>
  <ABLVelocityType Value=""/>
  <ABLVelocity Value="0.0"/>
  <ABLSampleHeight Value="0.0"/>
  <ABLGroundEntity ModelIds="" Value=""/>
  <EddyViscosity Value="17.8 mm2/s"/>
  <Temperature Value="15 C"/>
  <MachNumberType Value=""/>
  <MachNumber Value="0.0"/>
  <MachNumberMultiplier Value=""/>
  <IncomingFluid Index="0" Value="None"/>
  <PhasicVolumeFractionType Value=""/>
  <CarrierVolumeFraction Value="1.0"/>
  <CarrierMultiplier Value=""/>
  <DispersePhaseVolumeFraction Value="0.0,0.0,0.0,0.0,0.0"/>
  <DisperseMultiplier Value=""/>
  <HumidityType Index="0" Value="Relative Humidity"/>
  <Humidity Value="0.0"/>
  <CreateSurfaceOutput Value="1"/>
  <SurfaceOutput>
   <IntegratedFrequency Value="1.0"/>
   <IntegratedTimeInterval Value="0 s"/>
   <StatisticsFrequency Value="1.0"/>
   <StatisticsTimeInterval Value="0 s"/>
   <NodalFrequency Value="0"/>
   <NodalTimeInterval Value="0 s"/>
   <NumSavedStates Value="0"/>
  </SurfaceOutput>
  <CreateRadiationSurface/>
  <AdvancedOptions>
   <MassFluxMultiplierData Value="None"/>
   <TemperatureMultiplierData Value="None"/>
   <TurbulenceInputType Value="Auto"/>
   <TurbulenceIntensityType Value="Auto"/>
   <TurbulenceFlowType Value="Internal"/>
   <PercentTurbulenceIntensity Value="4.0"/>
   <TurbulenceLengthScale Value="0.1 mm"/>
   <TurbulenceViscosityRatio Value="40"/>
   <TurbulenceVelocityScale Value="0 mm/s"/>
  </AdvancedOptions>
 </Inlet>''';
simlab.execute(Inlet);

Outlet=''' <Outlet BCType="Outlet" UUID="de93a74e-2d67-46e6-b80c-f4e7245c2e54">
  <tag Value=""/>
  <Name Value="Outlet_3"/>
  <Entities>
   <Entities>
    <Model>flex_plate1_SM.gda</Model>
    <Face>1640,</Face>
   </Entities>
  </Entities>
  <StaticPressure Value="0 MPa"/>
  <StaticPressureMultiplier Index="0" Value="None"/>
  <PressureLossFactor Value="0.0"/>
  <PressureLossFactorMultiplier Index="0" Value="None"/>
  <PressureConstraint Index="0" Value="Auto Pressure"/>
  <WaveDamping Value="0"/>
  <HydroPressure Value="0"/>
  <OriginX Value="0 mm"/>
  <OriginY Value="0 mm"/>
  <OriginZ Value="0 mm"/>
  <BackFlowCond Value="0"/>
  <BackFlow/>
  <CreateSurfaceOutput Value="1"/>
  <SurfaceOutput>
   <IntegratedFrequency Value="1.0"/>
   <IntegratedTimeInterval Value="0 s"/>
   <StatisticsFrequency Value="1.0"/>
   <StatisticsTimeInterval Value="0 s"/>
   <NodalFrequency Value="0"/>
   <NodalTimeInterval Value="0 s"/>
   <NumSavedStates Value="0"/>
  </SurfaceOutput>
  <CreateRadiationSurface/>
 </Outlet>''';
simlab.execute(Outlet);

Wall=''' <Wall BCType="Wall" UUID="27fb038e-ad1c-44d9-8bb2-979d840f113c">
  <tag Value=""/>
  <Name Value="Wall_4"/>
  <Entities>
   <Entities>
    <Model>flex_plate1_SM.gda</Model>
    <Face>56,</Face>
   </Entities>
  </Entities>
  <ThinSolidSurface Value="0"/>
  <ReferenceFrameID Index="0" Value="None"/>
  <ActiveType Index="0" Value="Always"/>
  <SpecifyContactAngle Value="0"/>
  <WallVelocityType Index="1" Value="Match Mesh Velocity"/>
  <XVelocity Value="0.0"/>
  <YVelocity Value="0.0"/>
  <ZVelocity Value="0.0"/>
  <AxialVelocity Value="0.0"/>
  <CylinRadialVelocity Value="0.0"/>
  <TangentVelocity Value="0.0"/>
  <SphereX Value="0.0"/>
  <SphereY Value="0.0"/>
  <SphereZ Value="0.0"/>
  <SphereRadialVelocity Value="0.0"/>
  <NormalVelocity Value="0.0"/>
  <TemperatureType Index="1" Value="Applied Flux"/>
  <Temperature Value="0.0"/>
  <HeatFlux Value="0.5 mlW/mm2"/>
  <HeatFluxCoeff Value="0"/>
  <HeatFluxRefTemperature Value="0"/>
  <TurbulanceWallType Index="2" Value="Wall Function"/>
  <RoughnessHeight Value="0 mm"/>
  <HeatFluxFactor Value="1.0"/>
  <GranularSpecularity Value="1.0"/>
  <CreateSurfaceOutput Value="1"/>
  <SurfaceOutput>
   <IntegratedFrequency Value="1.0"/>
   <IntegratedTimeInterval Value="0 s"/>
   <StatisticsFrequency Value="1.0"/>
   <StatisticsTimeInterval Value="0 s"/>
   <NodalFrequency Value="0"/>
   <NodalTimeInterval Value="0 s"/>
   <NumSavedStates Value="0"/>
  </SurfaceOutput>
  <AdvancedOptions>
   <HeatFluxMultiplierData Value="None"/>
  </AdvancedOptions>
  <CreateRadiationSurface/>
 </Wall>''';
simlab.execute(Wall);

SolutionParameterOptions=''' <SolutionParamOption pixmap="solution" UUID="0768c58f-4f3f-4e62-9efd-1ab017375c43">
  <tag Value="-1"/>
  <Name Value=""/>
  <SolverName Value="ACUSOLVE"/>
  <FileName Value=""/>
  <WriteMode Value=""/>
  <Renumber Value=""/>
  <RunSolver Value=""/>
  <RemoveOrphanNodes Value=""/>
  <Version Value="15"/>
  <SolverSetingType Value=""/>
  <Solution Value="Flow"/>
  <AnalysisType Index="0" Value="STEADYSTATE">
   <CATEGORY NAME="Offsets">
    <ITEM DISPLAYNAME="" KEY="Absolute pressure offset">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" UNIT="pressure" VALUE="0 MPa"/>
    </ITEM>
    <ITEM DISPLAYNAME="" KEY="Absolute temperature offset">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" UNIT="temperature" VALUE="-273.15 C"/>
    </ITEM>
   </CATEGORY>
   <CATEGORY NAME="Auto Solution Strategy">
    <ITEM DISPLAYNAME="" KEY="Maximun no. of time steps">
     <COLUMN TYPE="EDITBOX" DATATYPE="INT" VALUE="1000"/>
    </ITEM>
    <ITEM DISPLAYNAME="" KEY="Initial time increment">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" UNIT="time" VALUE="1E+10 s"/>
    </ITEM>
    <ITEM DISPLAYNAME="" KEY="Convergence tolerance">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" VALUE="1e-6"/>
    </ITEM>
    <ITEM DISPLAYNAME="" KEY="Number of krylov vectors">
     <COLUMN TYPE="EDITBOX" DATATYPE="INT" VALUE="10"/>
    </ITEM>
    <ITEM DISPLAYNAME="" KEY="Relaxation factor">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" VALUE="0.3"/>
    </ITEM>
    <ITEM DISPLAYNAME="Flow" KEY="Solve flow equation">
     <COLUMN TYPE="CHECKBOX" CHECK="true" DATATYPE="BOOL" VALUE=""/>
    </ITEM>
    <ITEM DISPLAYNAME="Turbulence" KEY="Solve turbulence equation">
     <COLUMN TYPE="CHECKBOX" CHECK="false" DATATYPE="BOOL" VALUE=""/>
    </ITEM>
    <ITEM DISPLAYNAME="Multiphase" KEY="Field">
     <COLUMN TYPE="CHECKBOX" CHECK="true" DATATYPE="BOOL" VALUE=""/>
    </ITEM>
    <ITEM DISPLAYNAME="Temperature" KEY="Solve temperature equation">
     <COLUMN TYPE="CHECKBOX" CHECK="true" DATATYPE="BOOL" VALUE=""/>
    </ITEM>
    <ITEM DISPLAYNAME="Temperature flow" KEY="Solve thermal flow">
     <COLUMN TYPE="CHECKBOX" CHECK="true" DATATYPE="BOOL" VALUE=""/>
    </ITEM>
    <ITEM DISPLAYNAME="Electrical potential" KEY="Electrical potential">
     <COLUMN TYPE="CHECKBOX" CHECK="true" DATATYPE="BOOL" VALUE=""/>
    </ITEM>
    <ITEM DISPLAYNAME="" KEY="Radiation">
     <COLUMN TYPE="CHECKBOX" CHECK="true" DATATYPE="BOOL" VALUE=""/>
    </ITEM>
    <ITEM DISPLAYNAME="Mesh" KEY="Mesh Displacement">
     <COLUMN TYPE="CHECKBOX" CHECK="true" DATATYPE="BOOL" VALUE=""/>
    </ITEM>
   </CATEGORY>
   <CATEGORY NAME="Advanced Solution Strategy">
    <CATEGORY NAME="Flow Stagger">
     <ITEM DISPLAYNAME="" KEY="Modify flow stagger settings">
      <COLUMN TYPE="CHECKBOX" CHECK="false" DATATYPE="BOOL" VALUE=""/>
     </ITEM>
     <ITEM DISPLAYNAME="Minimum stagger iterations" KEY="Flow Minimum stagger iterations">
      <COLUMN TYPE="EDITBOX" DATATYPE="INT" VALUE="1"/>
     </ITEM>
     <ITEM DISPLAYNAME="Maximum stagger iterations" KEY="Flow Maximum stagger iterations">
      <COLUMN TYPE="EDITBOX" DATATYPE="INT" VALUE="1"/>
     </ITEM>
     <ITEM DISPLAYNAME="Minimum linear solve iterations" KEY="Flow Minimum linear solve iterations">
      <COLUMN TYPE="EDITBOX" DATATYPE="INT" VALUE="10"/>
     </ITEM>
     <ITEM DISPLAYNAME="Maximum linear solve iterations" KEY="Flow Maximum linear solve iterations">
      <COLUMN TYPE="EDITBOX" DATATYPE="INT" VALUE="1000"/>
     </ITEM>
    </CATEGORY>
    <CATEGORY NAME="Temperature Stagger">
     <ITEM DISPLAYNAME="" KEY="Modify temperature stagger settings">
      <COLUMN TYPE="CHECKBOX" CHECK="false" DATATYPE="BOOL" VALUE=""/>
     </ITEM>
     <ITEM DISPLAYNAME="Minimum stagger iterations" KEY="Temperature Minimum stagger iterations">
      <COLUMN TYPE="EDITBOX" DATATYPE="INT" VALUE="1"/>
     </ITEM>
     <ITEM DISPLAYNAME="Maximum stagger iterations" KEY="Temperature Maximum stagger iterations">
      <COLUMN TYPE="EDITBOX" DATATYPE="INT" VALUE="1"/>
     </ITEM>
     <ITEM DISPLAYNAME="Minimum linear solve iterations" KEY="Temperature Minimum linear solve iterations">
      <COLUMN TYPE="EDITBOX" DATATYPE="INT" VALUE="10"/>
     </ITEM>
     <ITEM DISPLAYNAME="Maximum linear solve iterations" KEY="Temperature Maximum linear solve iterations">
      <COLUMN TYPE="EDITBOX" DATATYPE="INT" VALUE="1000"/>
     </ITEM>
    </CATEGORY>
   </CATEGORY>
   <CATEGORY NAME="Restart Parameters">
    <ITEM DISPLAYNAME="Restart from" KEY="Restart from">
     <COLUMN LIST="None" INDEX="0" TYPE="COMBOBOX" DATATYPE="INDEX" VALUE="None"/>
    </ITEM>
    <ITEM DISPLAYNAME="Restart from solution" KEY="Flow Solution Name List">
     <COLUMN LIST="None" INDEX="0" TYPE="COMBOBOX" DATATYPE="USER" VALUE="None"/>
    </ITEM>
    <ITEM DISPLAYNAME="From time step" KEY="Restart Time Step">
     <COLUMN TYPE="EDITBOX" DATATYPE="INT" VALUE="0"/>
    </ITEM>
    <ITEM DISPLAYNAME="" KEY="Reset time step">
     <COLUMN TYPE="CHECKBOX" CHECK="false" DATATYPE="BOOL" VALUE=""/>
    </ITEM>
   </CATEGORY>
   <CATEGORY NAME="Default Wall Parameters">
    <ITEM DISPLAYNAME="Wall velocity type" KEY="Wall velocity type">
     <COLUMN LIST="Match Mesh Velocity" INDEX="1" TYPE="COMBOBOX" DATATYPE="INDEX" VALUE="Match Mesh Velocity"/>
    </ITEM>
    <ITEM DISPLAYNAME="Thermal condition" KEY="WallThermaltype">
     <COLUMN LIST="Applied Flux" INDEX="1" TYPE="COMBOBOX" DATATYPE="INDEX" VALUE="Applied Flux"/>
    </ITEM>
    <ITEM DISPLAYNAME="Temperature" KEY="WallTemperature">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" UNIT="temperature" VALUE="0 C"/>
    </ITEM>
    <ITEM DISPLAYNAME="Heat flux" KEY="WallHeatFlux">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" UNIT="heat flux" VALUE="0 mlW/mm2"/>
    </ITEM>
    <ITEM DISPLAYNAME="Heat transfer coefficient" KEY="WallHeatTransferCoefficient">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" UNIT="heat transfer coefficient" VALUE="0 mlW/(mm2*C)"/>
    </ITEM>
    <ITEM DISPLAYNAME="Reference temperature" KEY="WallReferenceTemperature">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" UNIT="temperature" VALUE="0 C"/>
    </ITEM>
    <ITEM DISPLAYNAME="Turbulence wall type" KEY="Turbulence wall type">
     <COLUMN LIST="Wall Function" INDEX="2" TYPE="COMBOBOX" DATATYPE="INDEX" VALUE="Wall Function"/>
    </ITEM>
    <ITEM DISPLAYNAME="Roughness height" KEY="Roughness height">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" UNIT="length" VALUE="0 mm"/>
    </ITEM>
    <ITEM DISPLAYNAME="Wall function heat flux factor" KEY="Wall function heat flux factor">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" VALUE="1"/>
    </ITEM>
    <ITEM DISPLAYNAME="Gap" KEY="WallSlidingGap">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" UNIT="length" VALUE="0 mm"/>
    </ITEM>
    <ITEM DISPLAYNAME="Gap factor" KEY="WallGapFactor">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" VALUE="1"/>
    </ITEM>
    <ITEM DISPLAYNAME="Crease angle" KEY="WallCreaseAngle">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" UNIT="angle" VALUE="90 deg"/>
    </ITEM>
    <ITEM DISPLAYNAME="" KEY="Split internal surfaces">
     <COLUMN TYPE="CHECKBOX" CHECK="true" DATATYPE="BOOL" VALUE=""/>
    </ITEM>
   </CATEGORY>
  </AnalysisType>
 </SolutionParamOption>''';
simlab.execute(SolutionParameterOptions);

DeleteSolution=''' <DeleteSolution UUID="2a50db17-49c3-493c-ad2c-b2478aef96ea">
  <LoadsName AllSolution="0" Value=""/>
  <SolverOptions SolutionName="Flow" OptionType="SOLUTION_PARAM"/>
 </DeleteSolution>''';
simlab.execute(DeleteSolution);

SolutionParameterOptions=''' <SolutionParamOption pixmap="solution" UUID="0768c58f-4f3f-4e62-9efd-1ab017375c43">
  <tag Value="-1"/>
  <Name Value=""/>
  <SolverName Value="ACUSOLVE"/>
  <FileName Value=""/>
  <WriteMode Value=""/>
  <Renumber Value=""/>
  <RunSolver Value=""/>
  <RemoveOrphanNodes Value=""/>
  <Version Value="15"/>
  <SolverSetingType Value=""/>
  <Solution Value="Flow"/>
  <AnalysisType Index="0" Value="STEADYSTATE">
   <CATEGORY NAME="Offsets">
    <ITEM DISPLAYNAME="" KEY="Absolute pressure offset">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" UNIT="pressure" VALUE="0 MPa"/>
    </ITEM>
    <ITEM DISPLAYNAME="" KEY="Absolute temperature offset">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" UNIT="temperature" VALUE="-273.15 C"/>
    </ITEM>
   </CATEGORY>
   <CATEGORY NAME="Auto Solution Strategy">
    <ITEM DISPLAYNAME="" KEY="Maximun no. of time steps">
     <COLUMN TYPE="EDITBOX" DATATYPE="INT" VALUE="1000"/>
    </ITEM>
    <ITEM DISPLAYNAME="" KEY="Initial time increment">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" UNIT="time" VALUE="1E+10 s"/>
    </ITEM>
    <ITEM DISPLAYNAME="" KEY="Convergence tolerance">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" VALUE="1e-6"/>
    </ITEM>
    <ITEM DISPLAYNAME="" KEY="Number of krylov vectors">
     <COLUMN TYPE="EDITBOX" DATATYPE="INT" VALUE="10"/>
    </ITEM>
    <ITEM DISPLAYNAME="" KEY="Relaxation factor">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" VALUE="0.3"/>
    </ITEM>
    <ITEM DISPLAYNAME="Flow" KEY="Solve flow equation">
     <COLUMN TYPE="CHECKBOX" CHECK="true" DATATYPE="BOOL" VALUE=""/>
    </ITEM>
    <ITEM DISPLAYNAME="Turbulence" KEY="Solve turbulence equation">
     <COLUMN TYPE="CHECKBOX" CHECK="false" DATATYPE="BOOL" VALUE=""/>
    </ITEM>
    <ITEM DISPLAYNAME="Multiphase" KEY="Field">
     <COLUMN TYPE="CHECKBOX" CHECK="true" DATATYPE="BOOL" VALUE=""/>
    </ITEM>
    <ITEM DISPLAYNAME="Temperature" KEY="Solve temperature equation">
     <COLUMN TYPE="CHECKBOX" CHECK="true" DATATYPE="BOOL" VALUE=""/>
    </ITEM>
    <ITEM DISPLAYNAME="Temperature flow" KEY="Solve thermal flow">
     <COLUMN TYPE="CHECKBOX" CHECK="true" DATATYPE="BOOL" VALUE=""/>
    </ITEM>
    <ITEM DISPLAYNAME="Electrical potential" KEY="Electrical potential">
     <COLUMN TYPE="CHECKBOX" CHECK="true" DATATYPE="BOOL" VALUE=""/>
    </ITEM>
    <ITEM DISPLAYNAME="" KEY="Radiation">
     <COLUMN TYPE="CHECKBOX" CHECK="true" DATATYPE="BOOL" VALUE=""/>
    </ITEM>
    <ITEM DISPLAYNAME="Mesh" KEY="Mesh Displacement">
     <COLUMN TYPE="CHECKBOX" CHECK="true" DATATYPE="BOOL" VALUE=""/>
    </ITEM>
   </CATEGORY>
   <CATEGORY NAME="Advanced Solution Strategy">
    <CATEGORY NAME="Flow Stagger">
     <ITEM DISPLAYNAME="" KEY="Modify flow stagger settings">
      <COLUMN TYPE="CHECKBOX" CHECK="false" DATATYPE="BOOL" VALUE=""/>
     </ITEM>
     <ITEM DISPLAYNAME="Minimum stagger iterations" KEY="Flow Minimum stagger iterations">
      <COLUMN TYPE="EDITBOX" DATATYPE="INT" VALUE="1"/>
     </ITEM>
     <ITEM DISPLAYNAME="Maximum stagger iterations" KEY="Flow Maximum stagger iterations">
      <COLUMN TYPE="EDITBOX" DATATYPE="INT" VALUE="1"/>
     </ITEM>
     <ITEM DISPLAYNAME="Minimum linear solve iterations" KEY="Flow Minimum linear solve iterations">
      <COLUMN TYPE="EDITBOX" DATATYPE="INT" VALUE="10"/>
     </ITEM>
     <ITEM DISPLAYNAME="Maximum linear solve iterations" KEY="Flow Maximum linear solve iterations">
      <COLUMN TYPE="EDITBOX" DATATYPE="INT" VALUE="1000"/>
     </ITEM>
    </CATEGORY>
    <CATEGORY NAME="Temperature Stagger">
     <ITEM DISPLAYNAME="" KEY="Modify temperature stagger settings">
      <COLUMN TYPE="CHECKBOX" CHECK="false" DATATYPE="BOOL" VALUE=""/>
     </ITEM>
     <ITEM DISPLAYNAME="Minimum stagger iterations" KEY="Temperature Minimum stagger iterations">
      <COLUMN TYPE="EDITBOX" DATATYPE="INT" VALUE="1"/>
     </ITEM>
     <ITEM DISPLAYNAME="Maximum stagger iterations" KEY="Temperature Maximum stagger iterations">
      <COLUMN TYPE="EDITBOX" DATATYPE="INT" VALUE="1"/>
     </ITEM>
     <ITEM DISPLAYNAME="Minimum linear solve iterations" KEY="Temperature Minimum linear solve iterations">
      <COLUMN TYPE="EDITBOX" DATATYPE="INT" VALUE="10"/>
     </ITEM>
     <ITEM DISPLAYNAME="Maximum linear solve iterations" KEY="Temperature Maximum linear solve iterations">
      <COLUMN TYPE="EDITBOX" DATATYPE="INT" VALUE="1000"/>
     </ITEM>
    </CATEGORY>
   </CATEGORY>
   <CATEGORY NAME="Restart Parameters">
    <ITEM DISPLAYNAME="Restart from" KEY="Restart from">
     <COLUMN LIST="None" INDEX="0" TYPE="COMBOBOX" DATATYPE="INDEX" VALUE="None"/>
    </ITEM>
    <ITEM DISPLAYNAME="Restart from solution" KEY="Flow Solution Name List">
     <COLUMN LIST="None" INDEX="0" TYPE="COMBOBOX" DATATYPE="USER" VALUE="None"/>
    </ITEM>
    <ITEM DISPLAYNAME="From time step" KEY="Restart Time Step">
     <COLUMN TYPE="EDITBOX" DATATYPE="INT" VALUE="0"/>
    </ITEM>
    <ITEM DISPLAYNAME="" KEY="Reset time step">
     <COLUMN TYPE="CHECKBOX" CHECK="false" DATATYPE="BOOL" VALUE=""/>
    </ITEM>
   </CATEGORY>
   <CATEGORY NAME="Default Wall Parameters">
    <ITEM DISPLAYNAME="Wall velocity type" KEY="Wall velocity type">
     <COLUMN LIST="Match Mesh Velocity" INDEX="1" TYPE="COMBOBOX" DATATYPE="INDEX" VALUE="Match Mesh Velocity"/>
    </ITEM>
    <ITEM DISPLAYNAME="Thermal condition" KEY="WallThermaltype">
     <COLUMN LIST="Applied Flux" INDEX="1" TYPE="COMBOBOX" DATATYPE="INDEX" VALUE="Applied Flux"/>
    </ITEM>
    <ITEM DISPLAYNAME="Temperature" KEY="WallTemperature">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" UNIT="temperature" VALUE="0 C"/>
    </ITEM>
    <ITEM DISPLAYNAME="Heat flux" KEY="WallHeatFlux">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" UNIT="heat flux" VALUE="0 mlW/mm2"/>
    </ITEM>
    <ITEM DISPLAYNAME="Heat transfer coefficient" KEY="WallHeatTransferCoefficient">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" UNIT="heat transfer coefficient" VALUE="0 mlW/(mm2*C)"/>
    </ITEM>
    <ITEM DISPLAYNAME="Reference temperature" KEY="WallReferenceTemperature">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" UNIT="temperature" VALUE="0 C"/>
    </ITEM>
    <ITEM DISPLAYNAME="Turbulence wall type" KEY="Turbulence wall type">
     <COLUMN LIST="Wall Function" INDEX="2" TYPE="COMBOBOX" DATATYPE="INDEX" VALUE="Wall Function"/>
    </ITEM>
    <ITEM DISPLAYNAME="Roughness height" KEY="Roughness height">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" UNIT="length" VALUE="0 mm"/>
    </ITEM>
    <ITEM DISPLAYNAME="Wall function heat flux factor" KEY="Wall function heat flux factor">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" VALUE="1"/>
    </ITEM>
    <ITEM DISPLAYNAME="Gap" KEY="WallSlidingGap">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" UNIT="length" VALUE="0 mm"/>
    </ITEM>
    <ITEM DISPLAYNAME="Gap factor" KEY="WallGapFactor">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" VALUE="1"/>
    </ITEM>
    <ITEM DISPLAYNAME="Crease angle" KEY="WallCreaseAngle">
     <COLUMN TYPE="EDITBOX" DATATYPE="DOUBLE" UNIT="angle" VALUE="90 deg"/>
    </ITEM>
    <ITEM DISPLAYNAME="" KEY="Split internal surfaces">
     <COLUMN TYPE="CHECKBOX" CHECK="true" DATATYPE="BOOL" VALUE=""/>
    </ITEM>
   </CATEGORY>
  </AnalysisType>
 </SolutionParamOption>''';
simlab.execute(SolutionParameterOptions);

CreateResponseNew=''' <CreateResponseNew UUID="a7326802-d869-41d4-a46d-d4d5c159d938">
  <tag Value="-1"/>
  <Name Value="Pressure"/>
  <Response LoadCase="" Type="Pressure" ModeIndex="" Component=""/>
  <AllBodies Value="0"/>
  <Points Value="0"/>
  <SupportEntities>
   <Entities>
    <Model>flex_plate1_SM.gda</Model>
    <Face>1642,</Face>
   </Entities>
  </SupportEntities>
  <Regions/>
  <Sets Value=""/>
  <Interested_Regions/>
  <Ignore_Regions/>
  <ValueType Value="Maximum"/>
  <Sets Value=""/>
  <SurfaceOutputs Check="0" Value=""/>
  <ComputationType Value="0"/>
  <NormalModeNumber Value=""/>
  <SolutionName Value="Flow"/>
 </CreateResponseNew>''';
simlab.execute(CreateResponseNew);

CreateResponseNew=''' <CreateResponseNew UUID="a7326802-d869-41d4-a46d-d4d5c159d938">
  <tag Value="-1"/>
  <Name Value="Temperature"/>
  <Response LoadCase="" Type="Temperature" ModeIndex="" Component=""/>
  <AllBodies Value="0"/>
  <Points Value="0"/>
  <SupportEntities>
   <Entities>
    <Model>flex_plate1_SM.gda</Model>
    <Face>56,</Face>
   </Entities>
  </SupportEntities>
  <Regions/>
  <Sets Value=""/>
  <Interested_Regions/>
  <Ignore_Regions/>
  <ValueType Value="Maximum"/>
  <Sets Value=""/>
  <SurfaceOutputs Check="0" Value=""/>
  <ComputationType Value="0"/>
  <NormalModeNumber Value=""/>
  <SolutionName Value="Flow"/>
 </CreateResponseNew>''';
simlab.execute(CreateResponseNew);

CreateResponseNew=''' <CreateResponseNew UUID="a7326802-d869-41d4-a46d-d4d5c159d938">
  <tag Value="-1"/>
  <Name Value="Temperature_1"/>
  <Response LoadCase="" Type="Temperature" ModeIndex="" Component=""/>
  <AllBodies Value="0"/>
  <Points Value="0"/>
  <SupportEntities>
   <Entities>
    <Model>flex_plate1_SM.gda</Model>
    <Face>56,</Face>
   </Entities>
  </SupportEntities>
  <Regions/>
  <Sets Value=""/>
  <Interested_Regions/>
  <Ignore_Regions/>
  <ValueType Value="Minimum"/>
  <Sets Value=""/>
  <SurfaceOutputs Check="0" Value=""/>
  <ComputationType Value="0"/>
  <NormalModeNumber Value=""/>
  <SolutionName Value="Flow"/>
 </CreateResponseNew>''';
simlab.execute(CreateResponseNew);

CreateResponseNew=''' <CreateResponseNew UUID="a7326802-d869-41d4-a46d-d4d5c159d938">
  <tag Value="-1"/>
  <Name Value="Temperature_2"/>
  <Response LoadCase="" Type="Temperature" ModeIndex="" Component=""/>
  <AllBodies Value="0"/>
  <Points Value="0"/>
  <SupportEntities>
   <Entities>
    <Model>flex_plate1_SM.gda</Model>
    <Face>56,</Face>
   </Entities>
  </SupportEntities>
  <Regions/>
  <Sets Value=""/>
  <Interested_Regions/>
  <Ignore_Regions/>
  <ValueType Value="Average"/>
  <Sets Value=""/>
  <SurfaceOutputs Check="0" Value=""/>
  <ComputationType Value="0"/>
  <NormalModeNumber Value=""/>
  <SolutionName Value="Flow"/>
 </CreateResponseNew>''';
simlab.execute(CreateResponseNew);

ExportandSolve=''' <ExportStaticSolverInput pixmap="solution" UUID="f009bc99-991f-43b7-8c87-cc606ef9c443">
  <tag Value="-1"/>
  <Name Value=""/>
  <SolverName Value=""/>
  <FileName Value=""/>
  <Solution Value="Flow"/>
  <WriteMode ValueText="Default" Value="0"/>
  <LoadCase Value=""/>
  <Renumber Value="0"/>
  <RunSolver Value="1"/>
  <DataCheck Value="0"/>
  <RemoveOrphanNodes Value="1"/>
  <AnalysisType Index="" Value=""/>
  <Version Value="15"/>
  <ExportOptionsVersion Value="1"/>
  <RemoteSolve Value="0"/>
  <CopyIncludeFiles Value="1"/>
  <SupportEntities ModelIds="" EntityTypes="" Value=""/>
 </ExportStaticSolverInput>''';
simlab.execute(ExportandSolve);

PostDisplayMode=''' <PostDisplayMode UUID="95e3bea8-a2f3-4557-9482-d66ece623634">
  <SimLabDisplay Value="1"/>
  <PostMessage Value="0"/>
 </PostDisplayMode>''';
simlab.execute(PostDisplayMode);
