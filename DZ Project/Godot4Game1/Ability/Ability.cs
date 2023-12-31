using Godot;
using System;
using System.Data.Common;
using System.Runtime.CompilerServices;
public unsafe partial class Ability : Node2D, ICloneable
{
	public float CD;
	public float use_time;
	public float cost;
	protected Timer useTimer;
	protected Timer CDTimer;
	protected Node ParentalAbilityNode; //Connects parent ability node to inheriting children classes and nodes.
	protected entity passive_application; //from
	protected entity active_application; //to
	protected string input_key; //input_key to enable kbm input in order to call the function. Otherwise cast on CD

	public void perform(entity obj){
		if (get_state() & !is_oneshot()){
			Use(passive_application);
		}
		else{
			if (Input.IsActionJustPressed(input_key)){
				UseAbility(obj);
				passive_application = obj;
			}
		}
	}
	public void perform(entity from, entity to){
		if (get_state() & !is_oneshot()){
			Use(passive_application, active_application);
		}
		else{
			if (Input.IsActionJustPressed(input_key) || (input_key == null)){
				UseAbility(from, to);
				passive_application = from;
				active_application = to;
			}
		} 
	}
	public bool get_state(){
		return (bool)ParentalAbilityNode.GetMeta("is_using");
	}
	public void set_state(bool x){
		ParentalAbilityNode.SetMeta("is_using",x);
		return;
	}
	public void set_canuse(bool x){
		ParentalAbilityNode.SetMeta("CanUse",x);
		return;
	}
	public bool get_canuse_state(){
		return (bool)ParentalAbilityNode.GetMeta("CanUse");
	}
	public void set_oneshot(bool x){
		ParentalAbilityNode.SetMeta("OneShot",x);
		return;
	}
	public bool is_oneshot(){
		return (bool)ParentalAbilityNode.GetMeta("OneShot");
	}
	public object Clone()
	{
		return this.MemberwiseClone();
	}
	protected virtual void Use(entity obj){}
	protected virtual void Use(entity from, entity to){}
	public void UseAbility(entity obj)
	{
		if (get_canuse_state() == true){
			Use(obj);
			passive_application = obj;
			set_state(true);
			set_canuse(false);
			useTimer.Start();
		}
	}
	public void UseAbility(entity from, entity to)
	{
		GD.Print(get_canuse_state());
		if (get_canuse_state() == true){
			Use(from, to);
			passive_application = from;
			active_application = to;
			set_state(true);
			set_canuse(false);
			useTimer.Start();
		}
	}
	void _on_ready()
	{
		useTimer = GetNode<Timer>("useTimer");
		CDTimer = GetNode<Timer>("CDTimer");
		useTimer.WaitTime = use_time;
		CDTimer.WaitTime = CD;
		ParentalAbilityNode = GetNode(this.GetPath());
		set_state(false);
		set_oneshot(true);
	}
	
	protected Ability(Ability Obj){
		if (this != Obj){
			this.CD = Obj.CD;
			this.use_time = Obj.use_time;
			this.cost = Obj.cost;
		}
	}
	protected Ability(float cd, float uset, float ct, string input_key){
		CD = cd;
		use_time = uset;
		cost = ct;
		this.input_key = input_key;
	}
	protected void _on_use_timer_timeout()
	{
		set_state(false);
		CDTimer.Start();
	}

	protected void _on_cd_timer_timeout()
	{
		set_canuse(true);
	}
	public Ability()
	{
		CD=1.0f;
		use_time=0.5f;
		cost = 0;
	}
}